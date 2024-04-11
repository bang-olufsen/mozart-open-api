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
import pprint
import re  # noqa: F401
import json


from typing import Optional

try:
    from pydantic.v1 import BaseModel
except ImportError:
    from pydantic import BaseModel

from mozart_api.models.lge_tv_sound_settings import LgeTvSoundSettings


class TvSoundSettings(BaseModel):
    """
    TvSoundSettings
    """

    lge: Optional[LgeTvSoundSettings] = None
    __properties = ["lge"]

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
    def from_json(cls, json_str: str) -> TvSoundSettings:
        """Create an instance of TvSoundSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of lge
        if self.lge:
            _dict["lge"] = self.lge.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TvSoundSettings:
        """Create an instance of TvSoundSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TvSoundSettings.parse_obj(obj)

        _obj = TvSoundSettings.parse_obj(
            {
                "lge": (
                    LgeTvSoundSettings.from_dict(obj.get("lge"))
                    if obj.get("lge") is not None
                    else None
                )
            }
        )
        return _obj
