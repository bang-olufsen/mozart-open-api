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
from typing import Optional, Union

try:
    from pydantic.v1 import BaseModel, Field, StrictStr, confloat, conint
except ImportError:
    from pydantic import BaseModel, Field, StrictStr, confloat, conint

from mozart_api.models.speaker_group_member_location import SpeakerGroupMemberLocation


class SpeakerGroupMember(BaseModel):
    """
    SpeakerGroupMember
    """

    distance: Optional[conint(strict=True, le=1500, ge=0)] = Field(
        default=None, description="Distance from listening position in cm"
    )
    friendly_name: Optional[StrictStr] = Field(default=None, alias="friendlyName")
    gain: Optional[
        Union[confloat(le=6, ge=-24, strict=True), conint(le=6, ge=-24, strict=True)]
    ] = Field(default=None, description="Level in dB")
    id: StrictStr = Field(...)
    location: Optional[SpeakerGroupMemberLocation] = None
    redirection_level: Optional[conint(strict=True, le=6, ge=-100)] = Field(
        default=None,
        alias="redirectionLevel",
        description="Redirection level for bass management in dB",
    )
    role: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    __properties = [
        "distance",
        "friendlyName",
        "gain",
        "id",
        "location",
        "redirectionLevel",
        "role",
        "type",
    ]

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
    def from_json(cls, json_str: str) -> SpeakerGroupMember:
        """Create an instance of SpeakerGroupMember from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict["location"] = self.location.to_dict()
        # set to None if distance (nullable) is None
        # and __fields_set__ contains the field
        if self.distance is None and "distance" in self.__fields_set__:
            _dict["distance"] = None

        # set to None if friendly_name (nullable) is None
        # and __fields_set__ contains the field
        if self.friendly_name is None and "friendly_name" in self.__fields_set__:
            _dict["friendlyName"] = None

        # set to None if gain (nullable) is None
        # and __fields_set__ contains the field
        if self.gain is None and "gain" in self.__fields_set__:
            _dict["gain"] = None

        # set to None if location (nullable) is None
        # and __fields_set__ contains the field
        if self.location is None and "location" in self.__fields_set__:
            _dict["location"] = None

        # set to None if redirection_level (nullable) is None
        # and __fields_set__ contains the field
        if (
            self.redirection_level is None
            and "redirection_level" in self.__fields_set__
        ):
            _dict["redirectionLevel"] = None

        # set to None if role (nullable) is None
        # and __fields_set__ contains the field
        if self.role is None and "role" in self.__fields_set__:
            _dict["role"] = None

        # set to None if type (nullable) is None
        # and __fields_set__ contains the field
        if self.type is None and "type" in self.__fields_set__:
            _dict["type"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SpeakerGroupMember:
        """Create an instance of SpeakerGroupMember from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SpeakerGroupMember.parse_obj(obj)

        _obj = SpeakerGroupMember.parse_obj(
            {
                "distance": obj.get("distance"),
                "friendly_name": obj.get("friendlyName"),
                "gain": obj.get("gain"),
                "id": obj.get("id"),
                "location": SpeakerGroupMemberLocation.from_dict(obj.get("location"))
                if obj.get("location") is not None
                else None,
                "redirection_level": obj.get("redirectionLevel"),
                "role": obj.get("role"),
                "type": obj.get("type"),
            }
        )
        return _obj
