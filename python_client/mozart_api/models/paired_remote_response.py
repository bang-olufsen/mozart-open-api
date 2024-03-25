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
from pydantic import BaseModel, conlist
from mozart_api.models.paired_remote import PairedRemote


class PairedRemoteResponse(BaseModel):
    """
    PairedRemoteResponse
    """

    items: Optional[conlist(PairedRemote)] = None
    __properties = ["items"]

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
    def from_json(cls, json_str: str) -> PairedRemoteResponse:
        """Create an instance of PairedRemoteResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict["items"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PairedRemoteResponse:
        """Create an instance of PairedRemoteResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PairedRemoteResponse.parse_obj(obj)

        _obj = PairedRemoteResponse.parse_obj(
            {
                "items": (
                    [PairedRemote.from_dict(_item) for _item in obj.get("items")]
                    if obj.get("items") is not None
                    else None
                )
            }
        )
        return _obj
