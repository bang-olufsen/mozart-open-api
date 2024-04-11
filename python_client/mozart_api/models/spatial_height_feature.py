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


from typing import List, Union

try:
    from pydantic.v1 import BaseModel, Field, StrictFloat, StrictInt, conlist
except ImportError:
    from pydantic import BaseModel, Field, StrictFloat, StrictInt, conlist

from mozart_api.models.spatial_height import SpatialHeight


class SpatialHeightFeature(BaseModel):
    """
    SpatialHeightFeature
    """

    value: Union[StrictFloat, StrictInt] = Field(
        ..., description="Selected spatial-height value"
    )
    default: SpatialHeight = Field(...)
    range: conlist(SpatialHeight, unique_items=True) = Field(
        ..., description="spatial-height range"
    )
    __properties = ["value", "default", "range"]

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
    def from_json(cls, json_str: str) -> SpatialHeightFeature:
        """Create an instance of SpatialHeightFeature from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of default
        if self.default:
            _dict["default"] = self.default.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in range (list)
        _items = []
        if self.range:
            for _item in self.range:
                if _item:
                    _items.append(_item.to_dict())
            _dict["range"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SpatialHeightFeature:
        """Create an instance of SpatialHeightFeature from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SpatialHeightFeature.parse_obj(obj)

        _obj = SpatialHeightFeature.parse_obj(
            {
                "value": obj.get("value"),
                "default": (
                    SpatialHeight.from_dict(obj.get("default"))
                    if obj.get("default") is not None
                    else None
                ),
                "range": (
                    [SpatialHeight.from_dict(_item) for _item in obj.get("range")]
                    if obj.get("range") is not None
                    else None
                ),
            }
        )
        return _obj
