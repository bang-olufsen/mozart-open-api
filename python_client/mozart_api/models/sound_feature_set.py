# coding: utf-8

"""
Mozart platform API

API for interacting with the Mozart platform.

The version of the OpenAPI document: 0.2.0
Contact: support@bang-olufsen.dk
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from __future__ import annotations

import json
import pprint
import re  # noqa: F401
from typing import Optional

try:
    from pydantic.v1 import BaseModel, Field
except ImportError:
    from pydantic import BaseModel, Field

from mozart_api.models.ambience_feature import AmbienceFeature
from mozart_api.models.balance_feature import BalanceFeature
from mozart_api.models.bass_feature import BassFeature
from mozart_api.models.bass_management_feature import BassManagementFeature
from mozart_api.models.compression_feature import CompressionFeature
from mozart_api.models.directivity_feature import DirectivityFeature
from mozart_api.models.fader_feature import FaderFeature
from mozart_api.models.room_compensation_feature import RoomCompensationFeature
from mozart_api.models.spatial_envelopment_feature import SpatialEnvelopmentFeature
from mozart_api.models.spatial_height_feature import SpatialHeightFeature
from mozart_api.models.spatial_processing_feature import SpatialProcessingFeature
from mozart_api.models.spatial_surround_feature import SpatialSurroundFeature
from mozart_api.models.spatial_width_feature import SpatialWidthFeature
from mozart_api.models.speech_enhance_feature import SpeechEnhanceFeature
from mozart_api.models.tone_touch_x_feature import ToneTouchXFeature
from mozart_api.models.tone_touch_y_feature import ToneTouchYFeature
from mozart_api.models.treble_feature import TrebleFeature


class SoundFeatureSet(BaseModel):
    """
    SoundFeatureSet
    """

    ambience: Optional[AmbienceFeature] = None
    balance: Optional[BalanceFeature] = None
    bass: Optional[BassFeature] = None
    bass_management: Optional[BassManagementFeature] = Field(
        default=None, alias="bass-management"
    )
    compression: Optional[CompressionFeature] = None
    directivity: Optional[DirectivityFeature] = None
    fader: Optional[FaderFeature] = None
    room_compensation: Optional[RoomCompensationFeature] = Field(
        default=None, alias="roomCompensation"
    )
    spatial_envelopment: Optional[SpatialEnvelopmentFeature] = Field(
        default=None, alias="spatial-envelopment"
    )
    spatial_height: Optional[SpatialHeightFeature] = Field(
        default=None, alias="spatial-height"
    )
    spatial_processing: Optional[SpatialProcessingFeature] = Field(
        default=None, alias="spatial-processing"
    )
    spatial_surround: Optional[SpatialSurroundFeature] = Field(
        default=None, alias="spatial-surround"
    )
    spatial_width: Optional[SpatialWidthFeature] = Field(
        default=None, alias="spatial-width"
    )
    speech_enhance: Optional[SpeechEnhanceFeature] = Field(
        default=None, alias="speech-enhance"
    )
    tone_touch_x: Optional[ToneTouchXFeature] = Field(default=None, alias="toneTouchX")
    tone_touch_y: Optional[ToneTouchYFeature] = Field(default=None, alias="toneTouchY")
    treble: Optional[TrebleFeature] = None
    __properties = [
        "ambience",
        "balance",
        "bass",
        "bass-management",
        "compression",
        "directivity",
        "fader",
        "roomCompensation",
        "spatial-envelopment",
        "spatial-height",
        "spatial-processing",
        "spatial-surround",
        "spatial-width",
        "speech-enhance",
        "toneTouchX",
        "toneTouchY",
        "treble",
    ]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SoundFeatureSet:
        """Create an instance of SoundFeatureSet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of ambience
        if self.ambience:
            _dict["ambience"] = self.ambience.to_dict()
        # override the default output from pydantic by calling `to_dict()` of balance
        if self.balance:
            _dict["balance"] = self.balance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bass
        if self.bass:
            _dict["bass"] = self.bass.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bass_management
        if self.bass_management:
            _dict["bass-management"] = self.bass_management.to_dict()
        # override the default output from pydantic by calling `to_dict()` of compression
        if self.compression:
            _dict["compression"] = self.compression.to_dict()
        # override the default output from pydantic by calling `to_dict()` of directivity
        if self.directivity:
            _dict["directivity"] = self.directivity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fader
        if self.fader:
            _dict["fader"] = self.fader.to_dict()
        # override the default output from pydantic by calling `to_dict()` of room_compensation
        if self.room_compensation:
            _dict["roomCompensation"] = self.room_compensation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spatial_envelopment
        if self.spatial_envelopment:
            _dict["spatial-envelopment"] = self.spatial_envelopment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spatial_height
        if self.spatial_height:
            _dict["spatial-height"] = self.spatial_height.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spatial_processing
        if self.spatial_processing:
            _dict["spatial-processing"] = self.spatial_processing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spatial_surround
        if self.spatial_surround:
            _dict["spatial-surround"] = self.spatial_surround.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spatial_width
        if self.spatial_width:
            _dict["spatial-width"] = self.spatial_width.to_dict()
        # override the default output from pydantic by calling `to_dict()` of speech_enhance
        if self.speech_enhance:
            _dict["speech-enhance"] = self.speech_enhance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tone_touch_x
        if self.tone_touch_x:
            _dict["toneTouchX"] = self.tone_touch_x.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tone_touch_y
        if self.tone_touch_y:
            _dict["toneTouchY"] = self.tone_touch_y.to_dict()
        # override the default output from pydantic by calling `to_dict()` of treble
        if self.treble:
            _dict["treble"] = self.treble.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SoundFeatureSet:
        """Create an instance of SoundFeatureSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SoundFeatureSet.parse_obj(obj)

        _obj = SoundFeatureSet.parse_obj(
            {
                "ambience": AmbienceFeature.from_dict(obj.get("ambience"))
                if obj.get("ambience") is not None
                else None,
                "balance": BalanceFeature.from_dict(obj.get("balance"))
                if obj.get("balance") is not None
                else None,
                "bass": BassFeature.from_dict(obj.get("bass"))
                if obj.get("bass") is not None
                else None,
                "bass_management": BassManagementFeature.from_dict(
                    obj.get("bass-management")
                )
                if obj.get("bass-management") is not None
                else None,
                "compression": CompressionFeature.from_dict(obj.get("compression"))
                if obj.get("compression") is not None
                else None,
                "directivity": DirectivityFeature.from_dict(obj.get("directivity"))
                if obj.get("directivity") is not None
                else None,
                "fader": FaderFeature.from_dict(obj.get("fader"))
                if obj.get("fader") is not None
                else None,
                "room_compensation": RoomCompensationFeature.from_dict(
                    obj.get("roomCompensation")
                )
                if obj.get("roomCompensation") is not None
                else None,
                "spatial_envelopment": SpatialEnvelopmentFeature.from_dict(
                    obj.get("spatial-envelopment")
                )
                if obj.get("spatial-envelopment") is not None
                else None,
                "spatial_height": SpatialHeightFeature.from_dict(
                    obj.get("spatial-height")
                )
                if obj.get("spatial-height") is not None
                else None,
                "spatial_processing": SpatialProcessingFeature.from_dict(
                    obj.get("spatial-processing")
                )
                if obj.get("spatial-processing") is not None
                else None,
                "spatial_surround": SpatialSurroundFeature.from_dict(
                    obj.get("spatial-surround")
                )
                if obj.get("spatial-surround") is not None
                else None,
                "spatial_width": SpatialWidthFeature.from_dict(obj.get("spatial-width"))
                if obj.get("spatial-width") is not None
                else None,
                "speech_enhance": SpeechEnhanceFeature.from_dict(
                    obj.get("speech-enhance")
                )
                if obj.get("speech-enhance") is not None
                else None,
                "tone_touch_x": ToneTouchXFeature.from_dict(obj.get("toneTouchX"))
                if obj.get("toneTouchX") is not None
                else None,
                "tone_touch_y": ToneTouchYFeature.from_dict(obj.get("toneTouchY"))
                if obj.get("toneTouchY") is not None
                else None,
                "treble": TrebleFeature.from_dict(obj.get("treble"))
                if obj.get("treble") is not None
                else None,
            }
        )
        return _obj
