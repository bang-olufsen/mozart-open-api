# coding: utf-8

# flake8: noqa

"""
    Mozart platform API

    API for interacting with the Mozart platform.

    The version of the OpenAPI document: 0.2.0
    Contact: support@bang-olufsen.dk
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "3.4.1.8.4"

# import apis into sdk package
from mozart_api.api.beolink_api import BeolinkApi
from mozart_api.api.bluetooth_api import BluetoothApi
from mozart_api.api.content_api import ContentApi
from mozart_api.api.deezer_api import DeezerApi
from mozart_api.api.overlay_api import OverlayApi
from mozart_api.api.playback_api import PlaybackApi
from mozart_api.api.power_api import PowerApi
from mozart_api.api.product_api import ProductApi
from mozart_api.api.remote_api import RemoteApi
from mozart_api.api.scenes_api import ScenesApi
from mozart_api.api.settings_api import SettingsApi
from mozart_api.api.software_update_api import SoftwareUpdateApi
from mozart_api.api.sound_api import SoundApi
from mozart_api.api.speaker_group_api import SpeakerGroupApi
from mozart_api.api.stand_api import StandApi
from mozart_api.api.mozart_api import MozartApi

# import ApiClient
from mozart_api.api_response import ApiResponse
from mozart_api.api_client import ApiClient
from mozart_api.configuration import Configuration
from mozart_api.exceptions import OpenApiException
from mozart_api.exceptions import ApiTypeError
from mozart_api.exceptions import ApiValueError
from mozart_api.exceptions import ApiKeyError
from mozart_api.exceptions import ApiAttributeError
from mozart_api.exceptions import ApiException

# import models into sdk package
from mozart_api.models.action import Action
from mozart_api.models.alarm_timer_event_data import AlarmTimerEventData
from mozart_api.models.alarm_triggered_info import AlarmTriggeredInfo
from mozart_api.models.ambience import Ambience
from mozart_api.models.ambience_feature import AmbienceFeature
from mozart_api.models.ambience_range import AmbienceRange
from mozart_api.models.art import Art
from mozart_api.models.balance import Balance
from mozart_api.models.balance_feature import BalanceFeature
from mozart_api.models.balance_range import BalanceRange
from mozart_api.models.bass import Bass
from mozart_api.models.bass_feature import BassFeature
from mozart_api.models.bass_management import BassManagement
from mozart_api.models.bass_management_feature import BassManagementFeature
from mozart_api.models.bass_management_range import BassManagementRange
from mozart_api.models.bass_range import BassRange
from mozart_api.models.battery_state import BatteryState
from mozart_api.models.beo_remote_button import BeoRemoteButton
from mozart_api.models.beolink_available_listener import BeolinkAvailableListener
from mozart_api.models.beolink_experience import BeolinkExperience
from mozart_api.models.beolink_experiences_result import BeolinkExperiencesResult
from mozart_api.models.beolink_join_request import BeolinkJoinRequest
from mozart_api.models.beolink_join_result import BeolinkJoinResult
from mozart_api.models.beolink_leader import BeolinkLeader
from mozart_api.models.beolink_listener import BeolinkListener
from mozart_api.models.beolink_peer import BeolinkPeer
from mozart_api.models.bluetooth_device import BluetoothDevice
from mozart_api.models.bluetooth_device_list import BluetoothDeviceList
from mozart_api.models.button_event import ButtonEvent
from mozart_api.models.compression import Compression
from mozart_api.models.compression_feature import CompressionFeature
from mozart_api.models.compression_range import CompressionRange
from mozart_api.models.content_item import ContentItem
from mozart_api.models.directivity import Directivity
from mozart_api.models.directivity_feature import DirectivityFeature
from mozart_api.models.directivity_range import DirectivityRange
from mozart_api.models.error_model import ErrorModel
from mozart_api.models.fader import Fader
from mozart_api.models.fader_feature import FaderFeature
from mozart_api.models.fader_range import FaderRange
from mozart_api.models.hdmi_input import HdmiInput
from mozart_api.models.hdmi_video_format import HdmiVideoFormat
from mozart_api.models.home_control_ixp import HomeControlIxp
from mozart_api.models.home_control_uri import HomeControlUri
from mozart_api.models.install_record_id_state import InstallRecordIdState
from mozart_api.models.latency_profile import LatencyProfile
from mozart_api.models.lge_tv_sound_settings import LgeTvSoundSettings
from mozart_api.models.listening_mode import ListeningMode
from mozart_api.models.listening_mode_features import ListeningModeFeatures
from mozart_api.models.listening_mode_props import ListeningModeProps
from mozart_api.models.listening_mode_ref import ListeningModeRef
from mozart_api.models.listening_mode_trigger import ListeningModeTrigger
from mozart_api.models.loudness import Loudness
from mozart_api.models.microphone_state import MicrophoneState
from mozart_api.models.microphones_state import MicrophonesState
from mozart_api.models.overlay_play_request import OverlayPlayRequest
from mozart_api.models.overlay_play_request_common import OverlayPlayRequestCommon
from mozart_api.models.overlay_play_request_from_usb import OverlayPlayRequestFromUsb
from mozart_api.models.overlay_play_request_from_usb_from_usb import (
    OverlayPlayRequestFromUsbFromUsb,
)
from mozart_api.models.overlay_play_request_text_to_speech import (
    OverlayPlayRequestTextToSpeech,
)
from mozart_api.models.overlay_play_request_text_to_speech_text_to_speech import (
    OverlayPlayRequestTextToSpeechTextToSpeech,
)
from mozart_api.models.overlay_play_request_uri import OverlayPlayRequestUri
from mozart_api.models.paired_remote import PairedRemote
from mozart_api.models.paired_remote_response import PairedRemoteResponse
from mozart_api.models.play_queue_item import PlayQueueItem
from mozart_api.models.play_queue_item_type import PlayQueueItemType
from mozart_api.models.play_queue_settings import PlayQueueSettings
from mozart_api.models.playback_content_metadata import PlaybackContentMetadata
from mozart_api.models.playback_error import PlaybackError
from mozart_api.models.playback_progress import PlaybackProgress
from mozart_api.models.playback_state import PlaybackState
from mozart_api.models.power_link_trigger import PowerLinkTrigger
from mozart_api.models.power_state_enum import PowerStateEnum
from mozart_api.models.preset import Preset
from mozart_api.models.product_curtain_status import ProductCurtainStatus
from mozart_api.models.product_friendly_name import ProductFriendlyName
from mozart_api.models.product_state import ProductState
from mozart_api.models.remote_menu_item import RemoteMenuItem
from mozart_api.models.remote_menu_item_properties import RemoteMenuItemProperties
from mozart_api.models.remote_ui_key_state import RemoteUIKeyState
from mozart_api.models.rendering_state import RenderingState
from mozart_api.models.room_compensation import RoomCompensation
from mozart_api.models.room_compensation_current_measurement import (
    RoomCompensationCurrentMeasurement,
)
from mozart_api.models.room_compensation_debug import RoomCompensationDebug
from mozart_api.models.room_compensation_enabled import RoomCompensationEnabled
from mozart_api.models.room_compensation_error_details import (
    RoomCompensationErrorDetails,
)
from mozart_api.models.room_compensation_feature import RoomCompensationFeature
from mozart_api.models.room_compensation_info import RoomCompensationInfo
from mozart_api.models.room_compensation_measurement_error import (
    RoomCompensationMeasurementError,
)
from mozart_api.models.room_compensation_properties import RoomCompensationProperties
from mozart_api.models.room_compensation_range import RoomCompensationRange
from mozart_api.models.room_compensation_response import RoomCompensationResponse
from mozart_api.models.room_compensation_result import RoomCompensationResult
from mozart_api.models.room_compensation_state import RoomCompensationState
from mozart_api.models.room_compensation_state_value import RoomCompensationStateValue
from mozart_api.models.room_compensation_type import RoomCompensationType
from mozart_api.models.room_compensation_version import RoomCompensationVersion
from mozart_api.models.scene import Scene
from mozart_api.models.scene_classification import SceneClassification
from mozart_api.models.scene_match import SceneMatch
from mozart_api.models.scene_properties import SceneProperties
from mozart_api.models.scene_trigger_base_properties import SceneTriggerBaseProperties
from mozart_api.models.software_update_state import SoftwareUpdateState
from mozart_api.models.software_update_status import SoftwareUpdateStatus
from mozart_api.models.sound_adjustments import SoundAdjustments
from mozart_api.models.sound_feature_set import SoundFeatureSet
from mozart_api.models.sound_settings import SoundSettings
from mozart_api.models.sound_tone_touch import SoundToneTouch
from mozart_api.models.source import Source
from mozart_api.models.source_array import SourceArray
from mozart_api.models.source_type_enum import SourceTypeEnum
from mozart_api.models.spatial_envelopment import SpatialEnvelopment
from mozart_api.models.spatial_envelopment_feature import SpatialEnvelopmentFeature
from mozart_api.models.spatial_envelopment_range import SpatialEnvelopmentRange
from mozart_api.models.spatial_height import SpatialHeight
from mozart_api.models.spatial_height_feature import SpatialHeightFeature
from mozart_api.models.spatial_height_range import SpatialHeightRange
from mozart_api.models.spatial_processing import SpatialProcessing
from mozart_api.models.spatial_processing_feature import SpatialProcessingFeature
from mozart_api.models.spatial_processing_range import SpatialProcessingRange
from mozart_api.models.spatial_surround import SpatialSurround
from mozart_api.models.spatial_surround_feature import SpatialSurroundFeature
from mozart_api.models.spatial_surround_range import SpatialSurroundRange
from mozart_api.models.spatial_width import SpatialWidth
from mozart_api.models.spatial_width_feature import SpatialWidthFeature
from mozart_api.models.spatial_width_range import SpatialWidthRange
from mozart_api.models.speaker_group import SpeakerGroup
from mozart_api.models.speaker_group_member import SpeakerGroupMember
from mozart_api.models.speaker_group_member_location import SpeakerGroupMemberLocation
from mozart_api.models.speaker_group_overview import SpeakerGroupOverview
from mozart_api.models.speaker_link_member_status import SpeakerLinkMemberStatus
from mozart_api.models.speaker_link_status import SpeakerLinkStatus
from mozart_api.models.speaker_role_enum import SpeakerRoleEnum
from mozart_api.models.speech_enhance import SpeechEnhance
from mozart_api.models.speech_enhance_feature import SpeechEnhanceFeature
from mozart_api.models.speech_enhance_range import SpeechEnhanceRange
from mozart_api.models.stand_connected import StandConnected
from mozart_api.models.stand_movement import StandMovement
from mozart_api.models.stand_position import StandPosition
from mozart_api.models.tone_touch import ToneTouch
from mozart_api.models.tone_touch_type import ToneTouchType
from mozart_api.models.tone_touch_type_range import ToneTouchTypeRange
from mozart_api.models.tone_touch_x_feature import ToneTouchXFeature
from mozart_api.models.tone_touch_y_feature import ToneTouchYFeature
from mozart_api.models.treble import Treble
from mozart_api.models.treble_feature import TrebleFeature
from mozart_api.models.treble_range import TrebleRange
from mozart_api.models.tv_info_event_data import TvInfoEventData
from mozart_api.models.tv_integration_types import TvIntegrationTypes
from mozart_api.models.tv_properties import TvProperties
from mozart_api.models.tv_sound_settings import TvSoundSettings
from mozart_api.models.tv_state import TvState
from mozart_api.models.uri import Uri
from mozart_api.models.user_flow import UserFlow
from mozart_api.models.video_pixel_format import VideoPixelFormat
from mozart_api.models.video_timings import VideoTimings
from mozart_api.models.volume_level import VolumeLevel
from mozart_api.models.volume_mute import VolumeMute
from mozart_api.models.volume_settings import VolumeSettings
from mozart_api.models.volume_state import VolumeState
from mozart_api.models.web_socket_event_active_hdmi_input_signal import (
    WebSocketEventActiveHdmiInputSignal,
)
from mozart_api.models.web_socket_event_active_listening_mode import (
    WebSocketEventActiveListeningMode,
)
from mozart_api.models.web_socket_event_active_speaker_group import (
    WebSocketEventActiveSpeakerGroup,
)
from mozart_api.models.web_socket_event_alarm_timer import WebSocketEventAlarmTimer
from mozart_api.models.web_socket_event_alarm_triggered import (
    WebSocketEventAlarmTriggered,
)
from mozart_api.models.web_socket_event_battery import WebSocketEventBattery
from mozart_api.models.web_socket_event_beo_remote_button import (
    WebSocketEventBeoRemoteButton,
)
from mozart_api.models.web_socket_event_beolink_experiences_result import (
    WebSocketEventBeolinkExperiencesResult,
)
from mozart_api.models.web_socket_event_beolink_join_result import (
    WebSocketEventBeolinkJoinResult,
)
from mozart_api.models.web_socket_event_button import WebSocketEventButton
from mozart_api.models.web_socket_event_curtains import WebSocketEventCurtains
from mozart_api.models.web_socket_event_hdmi_video_format_signal import (
    WebSocketEventHdmiVideoFormatSignal,
)
from mozart_api.models.web_socket_event_notification import WebSocketEventNotification
from mozart_api.models.web_socket_event_playback_error import (
    WebSocketEventPlaybackError,
)
from mozart_api.models.web_socket_event_playback_metadata import (
    WebSocketEventPlaybackMetadata,
)
from mozart_api.models.web_socket_event_playback_progress import (
    WebSocketEventPlaybackProgress,
)
from mozart_api.models.web_socket_event_playback_source import (
    WebSocketEventPlaybackSource,
)
from mozart_api.models.web_socket_event_playback_state import (
    WebSocketEventPlaybackState,
)
from mozart_api.models.web_socket_event_power_state import WebSocketEventPowerState
from mozart_api.models.web_socket_event_puc_install_remote_id_status import (
    WebSocketEventPucInstallRemoteIdStatus,
)
from mozart_api.models.web_socket_event_role import WebSocketEventRole
from mozart_api.models.web_socket_event_room_compensation_current_measurement_event import (
    WebSocketEventRoomCompensationCurrentMeasurementEvent,
)
from mozart_api.models.web_socket_event_room_compensation_state import (
    WebSocketEventRoomCompensationState,
)
from mozart_api.models.web_socket_event_software_update_state import (
    WebSocketEventSoftwareUpdateState,
)
from mozart_api.models.web_socket_event_sound_settings import (
    WebSocketEventSoundSettings,
)
from mozart_api.models.web_socket_event_source_change import WebSocketEventSourceChange
from mozart_api.models.web_socket_event_speaker_group_changed import (
    WebSocketEventSpeakerGroupChanged,
)
from mozart_api.models.web_socket_event_speaker_link_status_changed import (
    WebSocketEventSpeakerLinkStatusChanged,
)
from mozart_api.models.web_socket_event_stand_connected import (
    WebSocketEventStandConnected,
)
from mozart_api.models.web_socket_event_stand_position import (
    WebSocketEventStandPosition,
)
from mozart_api.models.web_socket_event_tv_info import WebSocketEventTvInfo
from mozart_api.models.web_socket_event_volume import WebSocketEventVolume
from mozart_api.models.web_socket_event_wisa_out_state import WebSocketEventWisaOutState
from mozart_api.models.websocket_notification_tag import WebsocketNotificationTag
from mozart_api.models.wisa_out_state import WisaOutState
