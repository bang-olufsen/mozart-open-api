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

from mozart_api.models.room_compensation_info import RoomCompensationInfo
from mozart_api.models.sound_adjustments import SoundAdjustments
from mozart_api.models.sound_tone_touch import SoundToneTouch


class SoundSettings(BaseModel):
    """
    SoundSettings
    """

    adjustments: Optional[SoundAdjustments] = None
    room_compensation: Optional[RoomCompensationInfo] = Field(
        default=None, alias="roomCompensation"
    )
    tone_touch: Optional[SoundToneTouch] = Field(default=None, alias="toneTouch")
    __properties = ["adjustments", "roomCompensation", "toneTouch"]

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
    def from_json(cls, json_str: str) -> SoundSettings:
        """Create an instance of SoundSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of adjustments
        if self.adjustments:
            _dict["adjustments"] = self.adjustments.to_dict()
        # override the default output from pydantic by calling `to_dict()` of room_compensation
        if self.room_compensation:
            _dict["roomCompensation"] = self.room_compensation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tone_touch
        if self.tone_touch:
            _dict["toneTouch"] = self.tone_touch.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SoundSettings:
        """Create an instance of SoundSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SoundSettings.parse_obj(obj)

        _obj = SoundSettings.parse_obj(
            {
                "adjustments": SoundAdjustments.from_dict(obj.get("adjustments"))
                if obj.get("adjustments") is not None
                else None,
                "room_compensation": RoomCompensationInfo.from_dict(
                    obj.get("roomCompensation")
                )
                if obj.get("roomCompensation") is not None
                else None,
                "tone_touch": SoundToneTouch.from_dict(obj.get("toneTouch"))
                if obj.get("toneTouch") is not None
                else None,
            }
        )
        return _obj
