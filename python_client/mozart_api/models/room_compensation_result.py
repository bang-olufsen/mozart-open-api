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
from datetime import datetime
from typing import List, Optional

try:
    from pydantic.v1 import BaseModel, Field, StrictStr, conlist, validator
except ImportError:
    from pydantic import BaseModel, Field, StrictStr, conlist, validator

from mozart_api.models.room_compensation_response import RoomCompensationResponse
from mozart_api.models.speaker_group import SpeakerGroup


class RoomCompensationResult(BaseModel):
    """
    RoomCompensationResult
    """

    compensation: Optional[conlist(RoomCompensationResponse)] = None
    measured_response: Optional[conlist(RoomCompensationResponse)] = Field(
        default=None, alias="measuredResponse"
    )
    placement: Optional[StrictStr] = None
    reference_response: Optional[conlist(RoomCompensationResponse)] = Field(
        default=None, alias="referenceResponse"
    )
    speaker_group_suggestion: Optional[SpeakerGroup] = Field(
        default=None, alias="speakerGroupSuggestion"
    )
    time_stamp: Optional[datetime] = Field(default=None, alias="timeStamp")
    __properties = [
        "compensation",
        "measuredResponse",
        "placement",
        "referenceResponse",
        "speakerGroupSuggestion",
        "timeStamp",
    ]

    @validator("placement")
    def placement_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (
            "free",
            "nearWall",
            "unknown",
        ):
            raise ValueError(
                "must be one of enum values ('free', 'nearWall', 'unknown')"
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
    def from_json(cls, json_str: str) -> RoomCompensationResult:
        """Create an instance of RoomCompensationResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in compensation (list)
        _items = []
        if self.compensation:
            for _item in self.compensation:
                if _item:
                    _items.append(_item.to_dict())
            _dict["compensation"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in measured_response (list)
        _items = []
        if self.measured_response:
            for _item in self.measured_response:
                if _item:
                    _items.append(_item.to_dict())
            _dict["measuredResponse"] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in reference_response (list)
        _items = []
        if self.reference_response:
            for _item in self.reference_response:
                if _item:
                    _items.append(_item.to_dict())
            _dict["referenceResponse"] = _items
        # override the default output from pydantic by calling `to_dict()` of speaker_group_suggestion
        if self.speaker_group_suggestion:
            _dict["speakerGroupSuggestion"] = self.speaker_group_suggestion.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoomCompensationResult:
        """Create an instance of RoomCompensationResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoomCompensationResult.parse_obj(obj)

        _obj = RoomCompensationResult.parse_obj(
            {
                "compensation": [
                    RoomCompensationResponse.from_dict(_item)
                    for _item in obj.get("compensation")
                ]
                if obj.get("compensation") is not None
                else None,
                "measured_response": [
                    RoomCompensationResponse.from_dict(_item)
                    for _item in obj.get("measuredResponse")
                ]
                if obj.get("measuredResponse") is not None
                else None,
                "placement": obj.get("placement"),
                "reference_response": [
                    RoomCompensationResponse.from_dict(_item)
                    for _item in obj.get("referenceResponse")
                ]
                if obj.get("referenceResponse") is not None
                else None,
                "speaker_group_suggestion": SpeakerGroup.from_dict(
                    obj.get("speakerGroupSuggestion")
                )
                if obj.get("speakerGroupSuggestion") is not None
                else None,
                "time_stamp": obj.get("timeStamp"),
            }
        )
        return _obj
