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
from pydantic import BaseModel, Field, StrictStr, constr


class AlarmTriggeredInfo(BaseModel):
    """
    AlarmTriggeredInfo
    """

    id: Optional[StrictStr] = None
    label: Optional[constr(strict=True, max_length=128)] = Field(
        None, description="Label for an alarm"
    )
    __properties = ["id", "label"]

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
    def from_json(cls, json_str: str) -> AlarmTriggeredInfo:
        """Create an instance of AlarmTriggeredInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AlarmTriggeredInfo:
        """Create an instance of AlarmTriggeredInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AlarmTriggeredInfo.parse_obj(obj)

        _obj = AlarmTriggeredInfo.parse_obj(
            {"id": obj.get("id"), "label": obj.get("label")}
        )
        return _obj