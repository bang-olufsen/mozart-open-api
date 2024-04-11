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

from mozart_api.models.uri import Uri


class OverlayPlayRequestUri(BaseModel):
    """
    OverlayPlayRequestUri
    """

    uri: Optional[Uri] = None
    __properties = ["uri"]

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
    def from_json(cls, json_str: str) -> OverlayPlayRequestUri:
        """Create an instance of OverlayPlayRequestUri from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of uri
        if self.uri:
            _dict["uri"] = self.uri.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OverlayPlayRequestUri:
        """Create an instance of OverlayPlayRequestUri from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OverlayPlayRequestUri.parse_obj(obj)

        _obj = OverlayPlayRequestUri.parse_obj(
            {
                "uri": (
                    Uri.from_dict(obj.get("uri"))
                    if obj.get("uri") is not None
                    else None
                )
            }
        )
        return _obj
