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
from pydantic import BaseModel, Field, StrictStr, validator


class RoomCompensationType(BaseModel):
    """
    RoomCompensationType
    """

    value: Optional[StrictStr] = Field(
        None,
        description="The type of roomcompensation used / to use. simple:   For speakers without external speakers. advanced:   For products with external speakers or other advanced multichannel capabilities.   This requires that at least action in the other properties of RoomCompensationProperties is set. ",
    )
    __properties = ["value"]

    @validator("value")
    def value_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("simple", "advanced"):
            raise ValueError("must be one of enum values ('simple', 'advanced')")
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
    def from_json(cls, json_str: str) -> RoomCompensationType:
        """Create an instance of RoomCompensationType from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoomCompensationType:
        """Create an instance of RoomCompensationType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoomCompensationType.parse_obj(obj)

        _obj = RoomCompensationType.parse_obj({"value": obj.get("value")})
        return _obj
