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


from typing import List, Optional

try:
    from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, validator
except ImportError:
    from pydantic import BaseModel, Field, StrictBool, StrictStr, conlist, validator

from mozart_api.models.action import Action
from mozart_api.models.content_item import ContentItem


class RemoteMenuItem(BaseModel):
    """
    RemoteMenuItem
    """

    action_list: Optional[conlist(Action)] = Field(
        None,
        alias="actionList",
        description="An ordered list of Actions to run on the product",
    )
    scene_list: Optional[conlist(StrictStr)] = Field(
        None, alias="sceneList", description="A list of scenes"
    )
    disabled: Optional[StrictBool] = None
    dynamic_list: Optional[StrictStr] = Field(
        None,
        alias="dynamicList",
        description="Let mozart create a dynamic list. This list will be attached as children to the menu item. If dynamicList is set it's not possible to change or manipulate any of the children because mozart can alter them at any given time ",
    )
    first_child_menu_item_id: Optional[StrictStr] = Field(
        None,
        alias="firstChildMenuItemId",
        description="ID of the first child menu item",
    )
    label: Optional[StrictStr] = Field(
        None, description="Alternative label, if omitted mozart will try its best"
    )
    next_sibling_menu_item_id: Optional[StrictStr] = Field(
        None,
        alias="nextSiblingMenuItemId",
        description="ID of the next sibling menu item",
    )
    parent_menu_item_id: Optional[StrictStr] = Field(
        None, alias="parentMenuItemId", description="ID of the parent menu item"
    )
    available: Optional[StrictBool] = None
    content: Optional[ContentItem] = None
    fixed: StrictBool = Field(
        ...,
        description="True if this is a fixed menu item. A fixed item can't be deleted or moved",
    )
    id: StrictStr = Field(..., description="Unique ID for this menu item")
    __properties = [
        "actionList",
        "sceneList",
        "disabled",
        "dynamicList",
        "firstChildMenuItemId",
        "label",
        "nextSiblingMenuItemId",
        "parentMenuItemId",
        "available",
        "content",
        "fixed",
        "id",
    ]

    @validator("dynamic_list")
    def dynamic_list_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("none", "radioFavorites"):
            raise ValueError("must be one of enum values ('none', 'radioFavorites')")
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
    def from_json(cls, json_str: str) -> RemoteMenuItem:
        """Create an instance of RemoteMenuItem from a JSON string"""
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
        # set to None if disabled (nullable) is None
        # and __fields_set__ contains the field
        if self.disabled is None and "disabled" in self.__fields_set__:
            _dict["disabled"] = None

        # set to None if dynamic_list (nullable) is None
        # and __fields_set__ contains the field
        if self.dynamic_list is None and "dynamic_list" in self.__fields_set__:
            _dict["dynamicList"] = None

        # set to None if first_child_menu_item_id (nullable) is None
        # and __fields_set__ contains the field
        if (
            self.first_child_menu_item_id is None
            and "first_child_menu_item_id" in self.__fields_set__
        ):
            _dict["firstChildMenuItemId"] = None

        # set to None if label (nullable) is None
        # and __fields_set__ contains the field
        if self.label is None and "label" in self.__fields_set__:
            _dict["label"] = None

        # set to None if next_sibling_menu_item_id (nullable) is None
        # and __fields_set__ contains the field
        if (
            self.next_sibling_menu_item_id is None
            and "next_sibling_menu_item_id" in self.__fields_set__
        ):
            _dict["nextSiblingMenuItemId"] = None

        # set to None if parent_menu_item_id (nullable) is None
        # and __fields_set__ contains the field
        if (
            self.parent_menu_item_id is None
            and "parent_menu_item_id" in self.__fields_set__
        ):
            _dict["parentMenuItemId"] = None

        # set to None if available (nullable) is None
        # and __fields_set__ contains the field
        if self.available is None and "available" in self.__fields_set__:
            _dict["available"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RemoteMenuItem:
        """Create an instance of RemoteMenuItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RemoteMenuItem.parse_obj(obj)

        _obj = RemoteMenuItem.parse_obj(
            {
                "action_list": (
                    [Action.from_dict(_item) for _item in obj.get("actionList")]
                    if obj.get("actionList") is not None
                    else None
                ),
                "scene_list": obj.get("sceneList"),
                "disabled": obj.get("disabled"),
                "dynamic_list": obj.get("dynamicList"),
                "first_child_menu_item_id": obj.get("firstChildMenuItemId"),
                "label": obj.get("label"),
                "next_sibling_menu_item_id": obj.get("nextSiblingMenuItemId"),
                "parent_menu_item_id": obj.get("parentMenuItemId"),
                "available": obj.get("available"),
                "content": (
                    ContentItem.from_dict(obj.get("content"))
                    if obj.get("content") is not None
                    else None
                ),
                "fixed": obj.get("fixed"),
                "id": obj.get("id"),
            }
        )
        return _obj
