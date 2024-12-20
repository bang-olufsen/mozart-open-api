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
from typing import List, Optional

try:
    from pydantic.v1 import BaseModel, Field, StrictStr, conlist
except ImportError:
    from pydantic import BaseModel, Field, StrictStr, conlist


class SceneMatch(BaseModel):
    """
    SceneMatch
    """

    label: Optional[StrictStr] = None
    tags: Optional[conlist(StrictStr)] = Field(
        default=None,
        description="A list of user defined tags. This allows a client to create virtual lists",
    )
    __properties = ["label", "tags"]

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
    def from_json(cls, json_str: str) -> SceneMatch:
        """Create an instance of SceneMatch from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if label (nullable) is None
        # and __fields_set__ contains the field
        if self.label is None and "label" in self.__fields_set__:
            _dict["label"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SceneMatch:
        """Create an instance of SceneMatch from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SceneMatch.parse_obj(obj)

        _obj = SceneMatch.parse_obj(
            {"label": obj.get("label"), "tags": obj.get("tags")}
        )
        return _obj
