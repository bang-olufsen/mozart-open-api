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
    from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, validator
except ImportError:
    from pydantic import BaseModel, Field, StrictBool, StrictStr, validator


class BeolinkExperience(BaseModel):
    """
    BeolinkExperience
    """

    category: StrictStr = Field(default=..., description="Source category")
    id: StrictStr = Field(
        default=..., description='experience id, e.g. "RADIO" or "toslink"'
    )
    linkable: StrictBool = Field(
        default=...,
        description='Linkable means "Does pressing play on this source make sense"',
    )
    name: StrictStr = Field(
        default=..., description='Experience name, e.g. "Bluetooth" or "B&O Radio"'
    )
    product_friendly_name: Optional[StrictStr] = Field(
        default=None,
        alias="productFriendlyName",
        description="Optional product friendly name",
    )
    source_friendly_name: Optional[StrictStr] = Field(
        default=None,
        alias="sourceFriendlyName",
        description="Optional friendly name for source",
    )
    type: StrictStr = Field(
        default=...,
        description="Source type. This corresponds to the exhaustive list or sources provided by the control layer",
    )
    unique_source_id: StrictStr = Field(
        default=...,
        alias="uniqueSourceId",
        description="The actual device jabber id that the experience comes from",
    )
    __properties = [
        "category",
        "id",
        "linkable",
        "name",
        "productFriendlyName",
        "sourceFriendlyName",
        "type",
        "uniqueSourceId",
    ]

    @validator("category")
    def category_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ("TV", "RADIO", "MUSIC", "MEDIA", "UNKNOWN"):
            raise ValueError(
                "must be one of enum values ('TV', 'RADIO', 'MUSIC', 'MEDIA', 'UNKNOWN')"
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
    def from_json(cls, json_str: str) -> BeolinkExperience:
        """Create an instance of BeolinkExperience from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BeolinkExperience:
        """Create an instance of BeolinkExperience from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BeolinkExperience.parse_obj(obj)

        _obj = BeolinkExperience.parse_obj(
            {
                "category": obj.get("category"),
                "id": obj.get("id"),
                "linkable": obj.get("linkable"),
                "name": obj.get("name"),
                "product_friendly_name": obj.get("productFriendlyName"),
                "source_friendly_name": obj.get("sourceFriendlyName"),
                "type": obj.get("type"),
                "unique_source_id": obj.get("uniqueSourceId"),
            }
        )
        return _obj
