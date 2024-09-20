"""Helper classes for using auto-generated API."""

# pylint: disable=line-too-long too-many-instance-attributes too-many-public-methods

import asyncio
import contextlib
import json
import logging
import re
from collections import defaultdict
from dataclasses import dataclass
from datetime import time
from ssl import SSLContext
from typing import Callable, Literal

from aiohttp import ClientSession
from aiohttp.client_exceptions import (
    ClientConnectorError,
    ClientOSError,
    ServerTimeoutError,
)
from inflection import underscore
from mozart_api.api.mozart_api import MozartApi
from mozart_api.api_client import ApiClient
from mozart_api.rest import RESTClientObject
from mozart_api.configuration import Configuration
from mozart_api.exceptions import ApiException
from mozart_api.models import Art, PlaybackContentMetadata

WEBSOCKET_TIMEOUT = 5.0

# Generated section start

NOTIFICATION_TYPES = {
    "active_hdmi_input_signal",
    "active_listening_mode",
    "active_speaker_group",
    "alarm_timer",
    "alarm_triggered",
    "battery",
    "beo_remote_button",
    "beolink_experiences_result",
    "beolink_join_result",
    "button",
    "curtains",
    "hdmi_video_format_signal",
    "notification",
    "playback_error",
    "playback_metadata",
    "playback_progress",
    "playback_source",
    "playback_state",
    "power_state",
    "puc_install_remote_id_status",
    "role",
    "room_compensation_current_measurement_event",
    "room_compensation_state",
    "software_update_state",
    "sound_settings",
    "source_change",
    "speaker_group_changed",
    "speaker_link_status_changed",
    "stand_connected",
    "stand_position",
    "tv_info",
    "volume",
    "wisa_out_state",
}

# Generated section end

logger = logging.getLogger(__name__)


def refactor_name(notification_type: str) -> str:
    """Remove WebSocketEvent prefix from string and convert to snake_case."""
    return underscore(notification_type.removeprefix("WebSocketEvent"))


def time_to_seconds(time_object: time) -> int:
    """Convert time object to number of seconds."""
    return (time_object.hour * 60 * 60) + (time_object.minute * 60) + time_object.second


def check_valid_jid(jid: str) -> bool:
    """Check if a JID is valid."""
    pattern = re.compile(r"(^\d{4})[.](\d{7})[.](\d{8})(@products\.bang-olufsen\.com)$")

    if pattern.fullmatch(jid) is not None:
        return True

    return False


def check_valid_serial_number(serial_number: str) -> bool:
    """Check if a serial_number is valid."""
    return bool(re.fullmatch(r"\d{8}", serial_number))


def get_highest_resolution_artwork(metadata: PlaybackContentMetadata) -> Art:
    """Get the highest resolution Art from provided PlaybackContentMetadata."""

    # Return an empty Art if no artwork is in metadata to ensure no stale artwork
    if not metadata.art:
        return Art()  # type: ignore

    # Dict for sorting images that have size defined by a string
    art_size = {"small": 1, "medium": 2, "large": 3}

    images = []

    # Images either have a key for specifying resolution or a "size" for the image.
    for image in metadata.art:
        # Skip any invalid artwork
        if not image.url:
            continue
        # Netradio.
        if image.key:
            images.append(int(image.key.split("x")[0]))
        # Everything else.
        elif image.size:
            images.append(art_size[image.size])

    # Check if only invalid images were provided
    if not images:
        return Art()  # type: ignore

    # Choose the largest image.
    return metadata.art[images.index(max(images))]


class MozartClient(MozartApi):
    """User friendly Mozart REST API and WebSocket client."""

    def __init__(self, host: str, ssl_context: SSLContext | None = None) -> None:
        """Initialize Mozart client."""
        self.host = host
        self.websocket_connected = False
        self.websocket_reconnect = False

        self._websocket_listener_active = False
        self._websocket_listener_remote_listener_active = False
        self._websocket_listeners_active = False
        self._websocket_tasks: set[asyncio.Task] = set()

        self._on_connection_lost = None
        self._on_connection = None

        self._on_all_notifications = None
        self._on_all_notifications_raw = None

        self._notification_callbacks: dict[str, Callable | None] = defaultdict()
        self._notification_callbacks.default_factory = lambda: None

        # Configure MozartApi object.
        self.configuration = Configuration(host=f"http://{self.host}")
        self.configuration.verify_ssl = False

        if ssl_context is None:
            super().__init__(ApiClient(self.configuration))
        elif ssl_context:
            super().__init__(
                ApiClient(
                    self.configuration,
                    rest_client=RESTClientObject(
                        configuration=self.configuration, ssl_context=ssl_context
                    ),
                )
            )

    async def close_api_client(self) -> None:
        """Close the API ClientSession."""
        await self.api_client.close()

    async def __aenter__(self):
        """Context entry"""
        if self.api_client.rest_client.pool_manager.closed:
            self.api_client = ApiClient(self.configuration)
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        """Context exit."""
        await self.close_api_client()

    async def _check_websocket_connection(
        self,
    ) -> Literal[True] | ClientConnectorError | ClientOSError | ServerTimeoutError:
        """Check if a connection can be made to the device's WebSocket notification channel."""
        try:
            async with ClientSession(conn_timeout=WEBSOCKET_TIMEOUT) as session:
                async with session.ws_connect(
                    f"ws://{self.host}:9339/",
                    timeout=WEBSOCKET_TIMEOUT,
                    receive_timeout=WEBSOCKET_TIMEOUT,
                ) as websocket:
                    if await websocket.receive():
                        return True

        except (ClientConnectorError, ClientOSError, ServerTimeoutError) as error:
            return error

    async def _check_api_connection(
        self,
    ) -> Literal[True] | ApiException | ClientConnectorError | TimeoutError:
        """Check if a connection can be made to the device's REST API."""
        try:
            await self.get_battery_state(_request_timeout=3)
        except (ApiException, ClientConnectorError, TimeoutError) as error:
            return error

        return True

    async def check_device_connection(self, raise_error=False) -> bool:
        """Check API and WebSocket connection."""
        # Don't use a taskgroup as both tasks should always be checked
        tasks: tuple[
            asyncio.Task[
                Literal[True]
                | ClientConnectorError
                | ClientOSError
                | ServerTimeoutError
            ],
            asyncio.Task[
                Literal[True] | ApiException | ClientConnectorError | TimeoutError
            ],
        ] = (
            asyncio.create_task(self._check_websocket_connection(), name="websocket"),
            asyncio.create_task(self._check_api_connection(), name="REST API"),
        )

        # Wait for tasks to complete
        for task in tasks:
            while not task.done():
                await asyncio.sleep(0)

        errors: list[
            ClientConnectorError
            | ClientOSError
            | ServerTimeoutError
            | ApiException
            | TimeoutError
        ] = []

        # Check status
        for task in tasks:
            if (result := task.result()) is not True:
                errors.append(result)

        connection_available = bool(len(errors) == 0)

        # Raise any exceptions
        if not connection_available and raise_error:
            raise ExceptionGroup(f"Can't connect to {self.host}", tuple(errors))

        return connection_available

    async def connect_notifications(
        self, remote_control=False, reconnect=False
    ) -> None:
        """Start the WebSocket listener task(s)."""
        self.websocket_reconnect = reconnect

        # Always add main WebSocket listener
        if not self._websocket_listener_active:
            self._websocket_tasks.add(
                asyncio.create_task(
                    coro=self._websocket_listener(f"ws://{self.host}:9339/"),
                    name=f"{self.host} - listener task",
                )
            )

            self._websocket_listener_active = True

        # Add WebSocket listener for remote control events if defined.
        if not self._websocket_listener_remote_listener_active and remote_control:
            self._websocket_tasks.add(
                asyncio.create_task(
                    coro=self._websocket_listener(
                        f"ws://{self.host}:9339/remoteControl"
                    ),
                    name=f"{self.host} - remote listener task",
                )
            )
            self._websocket_listener_remote_listener_active = True

        self._websocket_listeners_active = True

    def disconnect_notifications(self) -> None:
        """Stop the WebSocket listener tasks."""
        self._websocket_listener_active = False
        self._websocket_listener_remote_listener_active = False
        self._websocket_listeners_active = False

        for task in self._websocket_tasks:
            task.cancel()

        self._websocket_tasks.clear()

    async def _websocket_listener(self, host: str) -> None:
        """WebSocket listener."""
        while True:
            try:
                async with ClientSession(conn_timeout=WEBSOCKET_TIMEOUT) as session:
                    async with session.ws_connect(
                        url=host, heartbeat=WEBSOCKET_TIMEOUT
                    ) as websocket:
                        self.websocket_connected = True

                        if self._on_connection:
                            await self._trigger_callback(self._on_connection)

                        while self._websocket_listeners_active:
                            with contextlib.suppress(asyncio.TimeoutError):
                                # Receive JSON in order to get the Websocket notification name for deserialization
                                notification = await asyncio.wait_for(
                                    websocket.receive_json(),
                                    timeout=WEBSOCKET_TIMEOUT,
                                )

                                # Ensure that any notifications received after the disconnect command has been executed are not processed
                                if not self._websocket_listeners_active:
                                    break

                                await self._on_message(notification)

                        # Disconnect
                        self.websocket_connected = False
                        await websocket.close()
                        return

            except (
                ClientConnectorError,
                ClientOSError,
                TypeError,
                ServerTimeoutError,
            ) as error:
                if self.websocket_connected:
                    logger.debug("%s : %s - %s", host, type(error), error)
                    self.websocket_connected = False

                    if self._on_connection_lost:
                        await self._trigger_callback(self._on_connection_lost)

                if not self.websocket_reconnect:
                    logger.error("%s : %s - %s", host, type(error), error)
                    self.disconnect_notifications()
                    return

                await asyncio.sleep(WEBSOCKET_TIMEOUT)

    @dataclass
    class _ResponseWrapper:
        """Wrapper class for deserializing WebSocket response."""

        data: str

    async def _on_message(self, notification) -> None:
        """Handle WebSocket notifications."""

        # Get the object type and deserialized object.
        try:
            notification_type = notification["eventType"]

            deserialized_data = self.api_client.deserialize(
                self._ResponseWrapper(json.dumps(notification)), notification_type
            ).event_data

        except (ValueError, AttributeError) as error:
            logger.error(
                "%s unable to deserialize WebSocket notification: (%s : %s) with error: (%s : %s)",
                self.host,
                notification_type,
                notification,
                type(error),
                error,
            )
            return

        # Ensure that only valid notifications trigger callbacks
        if deserialized_data is None:
            return

        # Handle all notifications if defined
        if self._on_all_notifications:
            await self._trigger_callback(
                self._on_all_notifications,
                notification,
                refactor_name(notification_type),
            )

        if self._on_all_notifications_raw:
            await self._trigger_callback(self._on_all_notifications_raw, notification)

        # Handle specific notifications if defined
        triggered_notification = self._notification_callbacks[notification_type]

        if triggered_notification:
            await self._trigger_callback(triggered_notification, deserialized_data)

    async def _trigger_callback(self, callback, *args):
        """Trigger async or sync callback correctly."""
        if asyncio.iscoroutinefunction(callback):
            await callback(*args)
        else:
            callback(*args)

    def get_on_connection_lost(self, on_connection_lost) -> None:
        """Callback for WebSocket connection lost."""
        self._on_connection_lost = on_connection_lost

    def get_on_connection(self, on_connection) -> None:
        """Callback for WebSocket connection."""
        self._on_connection = on_connection

    def get_all_notifications(self, on_all_notifications) -> None:
        """Callback for all notifications."""
        self._on_all_notifications = on_all_notifications

    def get_all_notifications_raw(self, on_all_notifications_raw) -> None:
        """Callback for all notifications as dict."""
        self._on_all_notifications_raw = on_all_notifications_raw

    # Generated section start

    def get_active_hdmi_input_signal_notifications(
        self, on_active_hdmi_input_signal_notification
    ) -> None:
        """Callback for WebSocketEventActiveHdmiInputSignal notifications."""
        self._notification_callbacks["WebSocketEventActiveHdmiInputSignal"] = (
            on_active_hdmi_input_signal_notification
        )

    def get_active_listening_mode_notifications(
        self, on_active_listening_mode_notification
    ) -> None:
        """Callback for WebSocketEventActiveListeningMode notifications."""
        self._notification_callbacks["WebSocketEventActiveListeningMode"] = (
            on_active_listening_mode_notification
        )

    def get_active_speaker_group_notifications(
        self, on_active_speaker_group_notification
    ) -> None:
        """Callback for WebSocketEventActiveSpeakerGroup notifications."""
        self._notification_callbacks["WebSocketEventActiveSpeakerGroup"] = (
            on_active_speaker_group_notification
        )

    def get_alarm_timer_notifications(self, on_alarm_timer_notification) -> None:
        """Callback for WebSocketEventAlarmTimer notifications."""
        self._notification_callbacks["WebSocketEventAlarmTimer"] = (
            on_alarm_timer_notification
        )

    def get_alarm_triggered_notifications(
        self, on_alarm_triggered_notification
    ) -> None:
        """Callback for WebSocketEventAlarmTriggered notifications."""
        self._notification_callbacks["WebSocketEventAlarmTriggered"] = (
            on_alarm_triggered_notification
        )

    def get_battery_notifications(self, on_battery_notification) -> None:
        """Callback for WebSocketEventBattery notifications."""
        self._notification_callbacks["WebSocketEventBattery"] = on_battery_notification

    def get_beo_remote_button_notifications(
        self, on_beo_remote_button_notification
    ) -> None:
        """Callback for WebSocketEventBeoRemoteButton notifications."""
        self._notification_callbacks["WebSocketEventBeoRemoteButton"] = (
            on_beo_remote_button_notification
        )

    def get_beolink_experiences_result_notifications(
        self, on_beolink_experiences_result_notification
    ) -> None:
        """Callback for WebSocketEventBeolinkExperiencesResult notifications."""
        self._notification_callbacks["WebSocketEventBeolinkExperiencesResult"] = (
            on_beolink_experiences_result_notification
        )

    def get_beolink_join_result_notifications(
        self, on_beolink_join_result_notification
    ) -> None:
        """Callback for WebSocketEventBeolinkJoinResult notifications."""
        self._notification_callbacks["WebSocketEventBeolinkJoinResult"] = (
            on_beolink_join_result_notification
        )

    def get_button_notifications(self, on_button_notification) -> None:
        """Callback for WebSocketEventButton notifications."""
        self._notification_callbacks["WebSocketEventButton"] = on_button_notification

    def get_curtains_notifications(self, on_curtains_notification) -> None:
        """Callback for WebSocketEventCurtains notifications."""
        self._notification_callbacks["WebSocketEventCurtains"] = (
            on_curtains_notification
        )

    def get_hdmi_video_format_signal_notifications(
        self, on_hdmi_video_format_signal_notification
    ) -> None:
        """Callback for WebSocketEventHdmiVideoFormatSignal notifications."""
        self._notification_callbacks["WebSocketEventHdmiVideoFormatSignal"] = (
            on_hdmi_video_format_signal_notification
        )

    def get_notification_notifications(self, on_notification_notification) -> None:
        """Callback for WebSocketEventNotification notifications."""
        self._notification_callbacks["WebSocketEventNotification"] = (
            on_notification_notification
        )

    def get_playback_error_notifications(self, on_playback_error_notification) -> None:
        """Callback for WebSocketEventPlaybackError notifications."""
        self._notification_callbacks["WebSocketEventPlaybackError"] = (
            on_playback_error_notification
        )

    def get_playback_metadata_notifications(
        self, on_playback_metadata_notification
    ) -> None:
        """Callback for WebSocketEventPlaybackMetadata notifications."""
        self._notification_callbacks["WebSocketEventPlaybackMetadata"] = (
            on_playback_metadata_notification
        )

    def get_playback_progress_notifications(
        self, on_playback_progress_notification
    ) -> None:
        """Callback for WebSocketEventPlaybackProgress notifications."""
        self._notification_callbacks["WebSocketEventPlaybackProgress"] = (
            on_playback_progress_notification
        )

    def get_playback_source_notifications(
        self, on_playback_source_notification
    ) -> None:
        """Callback for WebSocketEventPlaybackSource notifications."""
        self._notification_callbacks["WebSocketEventPlaybackSource"] = (
            on_playback_source_notification
        )

    def get_playback_state_notifications(self, on_playback_state_notification) -> None:
        """Callback for WebSocketEventPlaybackState notifications."""
        self._notification_callbacks["WebSocketEventPlaybackState"] = (
            on_playback_state_notification
        )

    def get_power_state_notifications(self, on_power_state_notification) -> None:
        """Callback for WebSocketEventPowerState notifications."""
        self._notification_callbacks["WebSocketEventPowerState"] = (
            on_power_state_notification
        )

    def get_puc_install_remote_id_status_notifications(
        self, on_puc_install_remote_id_status_notification
    ) -> None:
        """Callback for WebSocketEventPucInstallRemoteIdStatus notifications."""
        self._notification_callbacks["WebSocketEventPucInstallRemoteIdStatus"] = (
            on_puc_install_remote_id_status_notification
        )

    def get_role_notifications(self, on_role_notification) -> None:
        """Callback for WebSocketEventRole notifications."""
        self._notification_callbacks["WebSocketEventRole"] = on_role_notification

    def get_room_compensation_current_measurement_event_notifications(
        self, on_room_compensation_current_measurement_event_notification
    ) -> None:
        """Callback for WebSocketEventRoomCompensationCurrentMeasurementEvent notifications."""
        self._notification_callbacks[
            "WebSocketEventRoomCompensationCurrentMeasurementEvent"
        ] = on_room_compensation_current_measurement_event_notification

    def get_room_compensation_state_notifications(
        self, on_room_compensation_state_notification
    ) -> None:
        """Callback for WebSocketEventRoomCompensationState notifications."""
        self._notification_callbacks["WebSocketEventRoomCompensationState"] = (
            on_room_compensation_state_notification
        )

    def get_software_update_state_notifications(
        self, on_software_update_state_notification
    ) -> None:
        """Callback for WebSocketEventSoftwareUpdateState notifications."""
        self._notification_callbacks["WebSocketEventSoftwareUpdateState"] = (
            on_software_update_state_notification
        )

    def get_sound_settings_notifications(self, on_sound_settings_notification) -> None:
        """Callback for WebSocketEventSoundSettings notifications."""
        self._notification_callbacks["WebSocketEventSoundSettings"] = (
            on_sound_settings_notification
        )

    def get_source_change_notifications(self, on_source_change_notification) -> None:
        """Callback for WebSocketEventSourceChange notifications."""
        self._notification_callbacks["WebSocketEventSourceChange"] = (
            on_source_change_notification
        )

    def get_speaker_group_changed_notifications(
        self, on_speaker_group_changed_notification
    ) -> None:
        """Callback for WebSocketEventSpeakerGroupChanged notifications."""
        self._notification_callbacks["WebSocketEventSpeakerGroupChanged"] = (
            on_speaker_group_changed_notification
        )

    def get_speaker_link_status_changed_notifications(
        self, on_speaker_link_status_changed_notification
    ) -> None:
        """Callback for WebSocketEventSpeakerLinkStatusChanged notifications."""
        self._notification_callbacks["WebSocketEventSpeakerLinkStatusChanged"] = (
            on_speaker_link_status_changed_notification
        )

    def get_stand_connected_notifications(
        self, on_stand_connected_notification
    ) -> None:
        """Callback for WebSocketEventStandConnected notifications."""
        self._notification_callbacks["WebSocketEventStandConnected"] = (
            on_stand_connected_notification
        )

    def get_stand_position_notifications(self, on_stand_position_notification) -> None:
        """Callback for WebSocketEventStandPosition notifications."""
        self._notification_callbacks["WebSocketEventStandPosition"] = (
            on_stand_position_notification
        )

    def get_tv_info_notifications(self, on_tv_info_notification) -> None:
        """Callback for WebSocketEventTvInfo notifications."""
        self._notification_callbacks["WebSocketEventTvInfo"] = on_tv_info_notification

    def get_volume_notifications(self, on_volume_notification) -> None:
        """Callback for WebSocketEventVolume notifications."""
        self._notification_callbacks["WebSocketEventVolume"] = on_volume_notification

    def get_wisa_out_state_notifications(self, on_wisa_out_state_notification) -> None:
        """Callback for WebSocketEventWisaOutState notifications."""
        self._notification_callbacks["WebSocketEventWisaOutState"] = (
            on_wisa_out_state_notification
        )

    # Generated section end
