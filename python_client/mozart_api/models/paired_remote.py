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

from datetime import datetime
from typing import List, Optional

try:
    from pydantic.v1 import (
        BaseModel,
        Field,
        StrictBool,
        StrictStr,
        conint,
        conlist,
        validator,
    )
except ImportError:
    from pydantic import (
        BaseModel,
        Field,
        StrictBool,
        StrictStr,
        conint,
        conlist,
        validator,
    )


class PairedRemote(BaseModel):
    """
    PairedRemote
    """

    address: StrictStr = Field(...)
    app_version: Optional[StrictStr] = Field(default=None, alias="appVersion")
    battery_level: Optional[conint(strict=True, le=100, ge=0)] = Field(
        default=None, alias="batteryLevel"
    )
    connected: Optional[StrictBool] = None
    db_version: Optional[StrictStr] = Field(default=None, alias="dbVersion")
    last_seen: Optional[datetime] = Field(default=None, alias="lastSeen")
    name: StrictStr = Field(...)
    serial_number: Optional[StrictStr] = Field(default=None, alias="serialNumber")
    updated: Optional[conlist(StrictStr)] = None
    __properties = [
        "address",
        "appVersion",
        "batteryLevel",
        "connected",
        "dbVersion",
        "lastSeen",
        "name",
        "serialNumber",
        "updated",
    ]

    @validator("updated")
    def updated_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in ("app", "db"):
                raise ValueError("each list item must be one of ('app', 'db')")
        return value

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
    def from_json(cls, json_str: str) -> PairedRemote:
        """Create an instance of PairedRemote from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PairedRemote:
        """Create an instance of PairedRemote from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PairedRemote.parse_obj(obj)

        _obj = PairedRemote.parse_obj(
            {
                "address": obj.get("address"),
                "app_version": obj.get("appVersion"),
                "battery_level": obj.get("batteryLevel"),
                "connected": obj.get("connected"),
                "db_version": obj.get("dbVersion"),
                "last_seen": obj.get("lastSeen"),
                "name": obj.get("name"),
                "serial_number": obj.get("serialNumber"),
                "updated": obj.get("updated"),
            }
        )
        return _obj
