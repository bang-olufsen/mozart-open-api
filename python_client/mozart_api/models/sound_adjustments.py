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


from typing import Optional, Union

try:
    from pydantic.v1 import (
        BaseModel,
        Field,
        StrictBool,
        StrictFloat,
        StrictInt,
        StrictStr,
    )
except ImportError:
    from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr


class SoundAdjustments(BaseModel):
    """
    SoundAdjustments
    """

    ambience: Optional[Union[StrictFloat, StrictInt]] = None
    bass: Optional[StrictInt] = None
    directivity: Optional[StrictStr] = None
    eco_mode: Optional[StrictBool] = Field(None, alias="ecoMode")
    fadein: Optional[StrictBool] = None
    loudness: Optional[StrictBool] = None
    treble: Optional[StrictInt] = None
    __properties = [
        "ambience",
        "bass",
        "directivity",
        "ecoMode",
        "fadein",
        "loudness",
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
    def from_json(cls, json_str: str) -> SoundAdjustments:
        """Create an instance of SoundAdjustments from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SoundAdjustments:
        """Create an instance of SoundAdjustments from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SoundAdjustments.parse_obj(obj)

        _obj = SoundAdjustments.parse_obj(
            {
                "ambience": obj.get("ambience"),
                "bass": obj.get("bass"),
                "directivity": obj.get("directivity"),
                "eco_mode": obj.get("ecoMode"),
                "fadein": obj.get("fadein"),
                "loudness": obj.get("loudness"),
                "treble": obj.get("treble"),
            }
        )
        return _obj
