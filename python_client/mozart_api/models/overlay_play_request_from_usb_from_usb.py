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


try:
    from pydantic.v1 import BaseModel, Field, constr
except ImportError:
    from pydantic import BaseModel, Field, constr


class OverlayPlayRequestFromUsbFromUsb(BaseModel):
    """
    OverlayPlayRequestFromUsbFromUsb
    """

    file_location: constr(strict=True, max_length=1024) = Field(
        default=...,
        alias="fileLocation",
        description="Required field containing the relative path (i.e. from the USB drive root) and file name with extension (if one exists) that will be played. A maximum length of 1024 characters is allowed. ",
    )
    __properties = ["fileLocation"]

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
    def from_json(cls, json_str: str) -> OverlayPlayRequestFromUsbFromUsb:
        """Create an instance of OverlayPlayRequestFromUsbFromUsb from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OverlayPlayRequestFromUsbFromUsb:
        """Create an instance of OverlayPlayRequestFromUsbFromUsb from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OverlayPlayRequestFromUsbFromUsb.parse_obj(obj)

        _obj = OverlayPlayRequestFromUsbFromUsb.parse_obj(
            {"file_location": obj.get("fileLocation")}
        )
        return _obj
