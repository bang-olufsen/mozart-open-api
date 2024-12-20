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
    from pydantic.v1 import BaseModel
except ImportError:
    from pydantic import BaseModel

from mozart_api.models.volume_level import VolumeLevel
from mozart_api.models.volume_mute import VolumeMute


class VolumeState(BaseModel):
    """
    VolumeState
    """

    default: Optional[VolumeLevel] = None
    level: Optional[VolumeLevel] = None
    maximum: Optional[VolumeLevel] = None
    muted: Optional[VolumeMute] = None
    __properties = ["default", "level", "maximum", "muted"]

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
    def from_json(cls, json_str: str) -> VolumeState:
        """Create an instance of VolumeState from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of default
        if self.default:
            _dict["default"] = self.default.to_dict()
        # override the default output from pydantic by calling `to_dict()` of level
        if self.level:
            _dict["level"] = self.level.to_dict()
        # override the default output from pydantic by calling `to_dict()` of maximum
        if self.maximum:
            _dict["maximum"] = self.maximum.to_dict()
        # override the default output from pydantic by calling `to_dict()` of muted
        if self.muted:
            _dict["muted"] = self.muted.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VolumeState:
        """Create an instance of VolumeState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VolumeState.parse_obj(obj)

        _obj = VolumeState.parse_obj(
            {
                "default": VolumeLevel.from_dict(obj.get("default"))
                if obj.get("default") is not None
                else None,
                "level": VolumeLevel.from_dict(obj.get("level"))
                if obj.get("level") is not None
                else None,
                "maximum": VolumeLevel.from_dict(obj.get("maximum"))
                if obj.get("maximum") is not None
                else None,
                "muted": VolumeMute.from_dict(obj.get("muted"))
                if obj.get("muted") is not None
                else None,
            }
        )
        return _obj
