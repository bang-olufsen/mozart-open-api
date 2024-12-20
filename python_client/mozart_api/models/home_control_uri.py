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
    from pydantic.v1 import BaseModel, StrictStr
except ImportError:
    from pydantic import BaseModel, StrictStr


class HomeControlUri(BaseModel):
    """
    HomeControlUri
    """

    ixp: Optional[StrictStr] = None
    uri: Optional[StrictStr] = None
    __properties = ["ixp", "uri"]

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
    def from_json(cls, json_str: str) -> HomeControlUri:
        """Create an instance of HomeControlUri from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if ixp (nullable) is None
        # and __fields_set__ contains the field
        if self.ixp is None and "ixp" in self.__fields_set__:
            _dict["ixp"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HomeControlUri:
        """Create an instance of HomeControlUri from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HomeControlUri.parse_obj(obj)

        _obj = HomeControlUri.parse_obj({"ixp": obj.get("ixp"), "uri": obj.get("uri")})
        return _obj
