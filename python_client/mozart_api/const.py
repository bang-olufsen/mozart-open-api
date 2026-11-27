"""Various constants useful for interacting with Mozart devices."""

from enum import StrEnum
from typing import Final, TypedDict

# Generated section start
from mozart_api.models import (
    WebSocketEventActiveHdmiInputSignal,
    WebSocketEventActiveListeningMode,
    WebSocketEventActiveSpeakerGroup,
    WebSocketEventAlarmTimer,
    WebSocketEventAlarmTriggered,
    WebSocketEventBattery,
    WebSocketEventBeolinkExperiencesResult,
    WebSocketEventBeolinkJoinResult,
    WebSocketEventBeoRemoteButton,
    WebSocketEventButton,
    WebSocketEventChannelSurveyStatus,
    WebSocketEventClassicsAdapterContent,
    WebSocketEventCurtains,
    WebSocketEventHdmiVideoFormatSignal,
    WebSocketEventNotification,
    WebSocketEventPlaybackError,
    WebSocketEventPlaybackMetadata,
    WebSocketEventPlaybackProgress,
    WebSocketEventPlaybackSource,
    WebSocketEventPlaybackState,
    WebSocketEventPowerlinkConnectionState,
    WebSocketEventPowerState,
    WebSocketEventPucInstallRemoteIdStatus,
    WebSocketEventRole,
    WebSocketEventRoomCompensationCurrentMeasurementEvent,
    WebSocketEventRoomCompensationState,
    WebSocketEventSoftwareUpdateState,
    WebSocketEventSoundSettings,
    WebSocketEventSourceChange,
    WebSocketEventSpeakerGroupChanged,
    WebSocketEventSpeakerLinkStatusChanged,
    WebSocketEventStandConnected,
    WebSocketEventStandPosition,
    WebSocketEventTvBnOMode,
    WebSocketEventTvInfo,
    WebSocketEventVolume,
    WebSocketEventWisaOutState,
)

# Generated section end

# MDNS helper constants
MDNS_SERVICE_TYPE: Final = "_bangolufsen._tcp.local."
MDNS_TYPE_NUMBER: Final = b"tn"
MDNS_ITEM_NUMBER: Final = b"in"
MDNS_SERIAL_NUMBER: Final = b"sn"
MDNS_FRIENDLY_NAME: Final = b"fn"
MDNS_SOFTWARE_VERSION: Final = b"fv"


class BaseWebSocketResponse(TypedDict):
    """Base class for serialized WebSocket notifications."""

    eventType: str
    eventData: dict | str


# Generated section start


class WebSocketEventTypes(StrEnum):
    """Available WebSocket notification event types."""

    ACTIVE_HDMI_INPUT_SIGNAL = "WebSocketEventActiveHdmiInputSignal"
    ACTIVE_LISTENING_MODE = "WebSocketEventActiveListeningMode"
    ACTIVE_SPEAKER_GROUP = "WebSocketEventActiveSpeakerGroup"
    ALARM_TIMER = "WebSocketEventAlarmTimer"
    ALARM_TRIGGERED = "WebSocketEventAlarmTriggered"
    BATTERY = "WebSocketEventBattery"
    BEO_REMOTE_BUTTON = "WebSocketEventBeoRemoteButton"
    BEOLINK_EXPERIENCES_RESULT = "WebSocketEventBeolinkExperiencesResult"
    BEOLINK_JOIN_RESULT = "WebSocketEventBeolinkJoinResult"
    BUTTON = "WebSocketEventButton"
    CHANNEL_SURVEY_STATUS = "WebSocketEventChannelSurveyStatus"
    CLASSICS_ADAPTER_CONTENT = "WebSocketEventClassicsAdapterContent"
    CURTAINS = "WebSocketEventCurtains"
    HDMI_VIDEO_FORMAT_SIGNAL = "WebSocketEventHdmiVideoFormatSignal"
    NOTIFICATION = "WebSocketEventNotification"
    PLAYBACK_ERROR = "WebSocketEventPlaybackError"
    PLAYBACK_METADATA = "WebSocketEventPlaybackMetadata"
    PLAYBACK_PROGRESS = "WebSocketEventPlaybackProgress"
    PLAYBACK_SOURCE = "WebSocketEventPlaybackSource"
    PLAYBACK_STATE = "WebSocketEventPlaybackState"
    POWER_STATE = "WebSocketEventPowerState"
    POWERLINK_CONNECTION_STATE = "WebSocketEventPowerlinkConnectionState"
    PUC_INSTALL_REMOTE_ID_STATUS = "WebSocketEventPucInstallRemoteIdStatus"
    ROLE = "WebSocketEventRole"
    ROOM_COMPENSATION_CURRENT_MEASUREMENT_EVENT = (
        "WebSocketEventRoomCompensationCurrentMeasurementEvent"
    )
    ROOM_COMPENSATION_STATE = "WebSocketEventRoomCompensationState"
    SOFTWARE_UPDATE_STATE = "WebSocketEventSoftwareUpdateState"
    SOUND_SETTINGS = "WebSocketEventSoundSettings"
    SOURCE_CHANGE = "WebSocketEventSourceChange"
    SPEAKER_GROUP_CHANGED = "WebSocketEventSpeakerGroupChanged"
    SPEAKER_LINK_STATUS_CHANGED = "WebSocketEventSpeakerLinkStatusChanged"
    STAND_CONNECTED = "WebSocketEventStandConnected"
    STAND_POSITION = "WebSocketEventStandPosition"
    TV_BN_O_MODE = "WebSocketEventTvBnOMode"
    TV_INFO = "WebSocketEventTvInfo"
    VOLUME = "WebSocketEventVolume"
    WISA_OUT_STATE = "WebSocketEventWisaOutState"


WebSocketEventType = type[
    WebSocketEventActiveHdmiInputSignal
    | WebSocketEventActiveListeningMode
    | WebSocketEventActiveSpeakerGroup
    | WebSocketEventAlarmTimer
    | WebSocketEventAlarmTriggered
    | WebSocketEventBattery
    | WebSocketEventBeoRemoteButton
    | WebSocketEventBeolinkExperiencesResult
    | WebSocketEventBeolinkJoinResult
    | WebSocketEventButton
    | WebSocketEventChannelSurveyStatus
    | WebSocketEventClassicsAdapterContent
    | WebSocketEventCurtains
    | WebSocketEventHdmiVideoFormatSignal
    | WebSocketEventNotification
    | WebSocketEventPlaybackError
    | WebSocketEventPlaybackMetadata
    | WebSocketEventPlaybackProgress
    | WebSocketEventPlaybackSource
    | WebSocketEventPlaybackState
    | WebSocketEventPowerState
    | WebSocketEventPowerlinkConnectionState
    | WebSocketEventPucInstallRemoteIdStatus
    | WebSocketEventRole
    | WebSocketEventRoomCompensationCurrentMeasurementEvent
    | WebSocketEventRoomCompensationState
    | WebSocketEventSoftwareUpdateState
    | WebSocketEventSoundSettings
    | WebSocketEventSourceChange
    | WebSocketEventSpeakerGroupChanged
    | WebSocketEventSpeakerLinkStatusChanged
    | WebSocketEventStandConnected
    | WebSocketEventStandPosition
    | WebSocketEventTvBnOMode
    | WebSocketEventTvInfo
    | WebSocketEventVolume
    | WebSocketEventWisaOutState
]

# Generated section end
