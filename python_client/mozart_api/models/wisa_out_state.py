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
from pydantic import BaseModel, StrictStr, validator


class WisaOutState(BaseModel):
    """
    WisaOutState
    """

    state: Optional[StrictStr] = None
    __properties = ["state"]

    @validator("state")
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("idle", "discovering", "deleting", "updatingSpeakerFirmware"):
            raise ValueError(
                "must be one of enum values ('idle', 'discovering', 'deleting', 'updatingSpeakerFirmware')"
            )
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
    def from_json(cls, json_str: str) -> WisaOutState:
        """Create an instance of WisaOutState from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WisaOutState:
        """Create an instance of WisaOutState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return WisaOutState.parse_obj(obj)

        _obj = WisaOutState.parse_obj({"state": obj.get("state")})
        return _obj
