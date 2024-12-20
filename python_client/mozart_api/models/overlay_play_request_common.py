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
    from pydantic.v1 import BaseModel, Field, conint
except ImportError:
    from pydantic import BaseModel, Field, conint


class OverlayPlayRequestCommon(BaseModel):
    """
    OverlayPlayRequestCommon
    """

    volume_absolute: Optional[conint(strict=True, le=100, ge=0)] = Field(
        default=None,
        alias="volumeAbsolute",
        description="An optional absolute volume level at which to play the URI. If not provided, the URI will play at the currently configured volume level on the product. The level should be provided in volume steps [0, 100] ",
    )
    __properties = ["volumeAbsolute"]

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
    def from_json(cls, json_str: str) -> OverlayPlayRequestCommon:
        """Create an instance of OverlayPlayRequestCommon from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if volume_absolute (nullable) is None
        # and __fields_set__ contains the field
        if self.volume_absolute is None and "volume_absolute" in self.__fields_set__:
            _dict["volumeAbsolute"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OverlayPlayRequestCommon:
        """Create an instance of OverlayPlayRequestCommon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OverlayPlayRequestCommon.parse_obj(obj)

        _obj = OverlayPlayRequestCommon.parse_obj(
            {"volume_absolute": obj.get("volumeAbsolute")}
        )
        return _obj
