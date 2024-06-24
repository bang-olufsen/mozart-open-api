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
    from pydantic.v1 import BaseModel, Field, StrictInt, StrictStr
except ImportError:
    from pydantic import BaseModel, Field, StrictInt, StrictStr


class PlaybackProgress(BaseModel):
    """
    PlaybackProgress
    """

    id: Optional[StrictStr] = None
    progress: Optional[StrictInt] = None
    total_duration: Optional[StrictInt] = Field(default=None, alias="totalDuration")
    __properties = ["id", "progress", "totalDuration"]

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
    def from_json(cls, json_str: str) -> PlaybackProgress:
        """Create an instance of PlaybackProgress from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if total_duration (nullable) is None
        # and __fields_set__ contains the field
        if self.total_duration is None and "total_duration" in self.__fields_set__:
            _dict["totalDuration"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PlaybackProgress:
        """Create an instance of PlaybackProgress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PlaybackProgress.parse_obj(obj)

        _obj = PlaybackProgress.parse_obj(
            {
                "id": obj.get("id"),
                "progress": obj.get("progress"),
                "total_duration": obj.get("totalDuration"),
            }
        )
        return _obj
