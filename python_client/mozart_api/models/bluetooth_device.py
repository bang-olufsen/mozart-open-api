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
    from pydantic.v1 import BaseModel, StrictBool, StrictStr
except ImportError:
    from pydantic import BaseModel, StrictBool, StrictStr


class BluetoothDevice(BaseModel):
    """
    BluetoothDevice
    """

    address: Optional[StrictStr] = None
    connected: Optional[StrictBool] = None
    name: Optional[StrictStr] = None
    __properties = ["address", "connected", "name"]

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
    def from_json(cls, json_str: str) -> BluetoothDevice:
        """Create an instance of BluetoothDevice from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BluetoothDevice:
        """Create an instance of BluetoothDevice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BluetoothDevice.parse_obj(obj)

        _obj = BluetoothDevice.parse_obj(
            {
                "address": obj.get("address"),
                "connected": obj.get("connected"),
                "name": obj.get("name"),
            }
        )
        return _obj
