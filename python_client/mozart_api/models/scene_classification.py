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
    from pydantic.v1 import BaseModel, Field, StrictStr, validator
except ImportError:
    from pydantic import BaseModel, Field, StrictStr, validator


class SceneClassification(BaseModel):
    """
    SceneClassification
    """

    classification: Optional[StrictStr] = Field(
        default=None, description="The classification of Scene"
    )
    __properties = ["classification"]

    @validator("classification")
    def classification_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (
            "system",
            "userDefined",
        ):
            raise ValueError("must be one of enum values ('system', 'userDefined')")
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
    def from_json(cls, json_str: str) -> SceneClassification:
        """Create an instance of SceneClassification from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if classification (nullable) is None
        # and __fields_set__ contains the field
        if self.classification is None and "classification" in self.__fields_set__:
            _dict["classification"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SceneClassification:
        """Create an instance of SceneClassification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SceneClassification.parse_obj(obj)

        _obj = SceneClassification.parse_obj(
            {"classification": obj.get("classification")}
        )
        return _obj
