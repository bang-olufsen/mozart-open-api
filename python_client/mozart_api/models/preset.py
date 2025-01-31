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

from mozart_api.models.action import Action
from mozart_api.models.content_item import ContentItem
from mozart_api.models.source_type_enum import SourceTypeEnum


class Preset(BaseModel):
    """
    Preset
    """

    action_list: Optional[conlist(Action)] = Field(
        default=None,
        alias="actionList",
        description="An ordered list of Actions to run on the product",
    )
    scene_list: Optional[conlist(StrictStr)] = Field(
        default=None, alias="sceneList", description="A list of scenes"
    )
    content: Optional[ContentItem] = None
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    source: Optional[SourceTypeEnum] = None
    title: Optional[StrictStr] = None
    __properties = [
        "actionList",
        "sceneList",
        "content",
        "id",
        "name",
        "source",
        "title",
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
    def from_json(cls, json_str: str) -> Preset:
        """Create an instance of Preset from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in action_list (list)
        _items = []
        if self.action_list:
            for _item in self.action_list:
                if _item:
                    _items.append(_item.to_dict())
            _dict["actionList"] = _items
        # override the default output from pydantic by calling `to_dict()` of content
        if self.content:
            _dict["content"] = self.content.to_dict()
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict["source"] = self.source.to_dict()
        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict["name"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Preset:
        """Create an instance of Preset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Preset.parse_obj(obj)

        _obj = Preset.parse_obj(
            {
                "action_list": [
                    Action.from_dict(_item) for _item in obj.get("actionList")
                ]
                if obj.get("actionList") is not None
                else None,
                "scene_list": obj.get("sceneList"),
                "content": ContentItem.from_dict(obj.get("content"))
                if obj.get("content") is not None
                else None,
                "id": obj.get("id"),
                "name": obj.get("name"),
                "source": SourceTypeEnum.from_dict(obj.get("source"))
                if obj.get("source") is not None
                else None,
                "title": obj.get("title"),
            }
        )
        return _obj
