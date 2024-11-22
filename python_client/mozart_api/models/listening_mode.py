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
    from pydantic.v1 import (
        BaseModel,
        Field,
        StrictStr,
        conint,
        conlist,
        constr,
        validator,
    )
except ImportError:
    from pydantic import BaseModel, Field, StrictStr, conint, conlist, constr, validator

from mozart_api.models.listening_mode_features import ListeningModeFeatures
from mozart_api.models.listening_mode_trigger import ListeningModeTrigger


class ListeningMode(BaseModel):
    """
    ListeningMode
    """

    client_ctx: Optional[constr(strict=True, max_length=4096)] = Field(
        default=None,
        alias="clientCtx",
        description="An optional generic string property supplied from the client. If provided, it will be stored without changes. If not supplied, any current clientCtx will remain unchanged. ",
    )
    features: ListeningModeFeatures = Field(...)
    id: conint(strict=True, ge=0) = Field(...)
    name: StrictStr = Field(default=..., description="Friendly name")
    origin: Optional[StrictStr] = Field(
        default=None,
        description="User created, default or an edited default listening mode",
    )
    role: Optional[StrictStr] = Field(
        default=None, description="Role a listening mode applies to"
    )
    triggers: conlist(ListeningModeTrigger) = Field(...)
    __properties = ["clientCtx", "features", "id", "name", "origin", "role", "triggers"]

    @validator("origin")
    def origin_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (
            "user",
            "default",
            "edited",
        ):
            raise ValueError("must be one of enum values ('user', 'default', 'edited')")
        return value

    @validator("role")
    def role_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (
            "standalone",
            "multichannel",
            "all",
        ):
            raise ValueError(
                "must be one of enum values ('standalone', 'multichannel', 'all')"
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
    def from_json(cls, json_str: str) -> ListeningMode:
        """Create an instance of ListeningMode from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of features
        if self.features:
            _dict["features"] = self.features.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in triggers (list)
        _items = []
        if self.triggers:
            for _item in self.triggers:
                if _item:
                    _items.append(_item.to_dict())
            _dict["triggers"] = _items
        # set to None if client_ctx (nullable) is None
        # and __fields_set__ contains the field
        if self.client_ctx is None and "client_ctx" in self.__fields_set__:
            _dict["clientCtx"] = None

        # set to None if role (nullable) is None
        # and __fields_set__ contains the field
        if self.role is None and "role" in self.__fields_set__:
            _dict["role"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListeningMode:
        """Create an instance of ListeningMode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListeningMode.parse_obj(obj)

        _obj = ListeningMode.parse_obj(
            {
                "client_ctx": obj.get("clientCtx"),
                "features": ListeningModeFeatures.from_dict(obj.get("features"))
                if obj.get("features") is not None
                else None,
                "id": obj.get("id"),
                "name": obj.get("name"),
                "origin": obj.get("origin"),
                "role": obj.get("role"),
                "triggers": [
                    ListeningModeTrigger.from_dict(_item)
                    for _item in obj.get("triggers")
                ]
                if obj.get("triggers") is not None
                else None,
            }
        )
        return _obj
