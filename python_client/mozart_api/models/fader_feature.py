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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Union
from mozart_api.models.fader import Fader
from typing import Optional, Set
from typing_extensions import Self


class FaderFeature(BaseModel):
    """
    FaderFeature
    """  # noqa: E501

    value: Union[StrictFloat, StrictInt] = Field(description="Selected fader value")
    default: Fader
    range: List[Fader] = Field(description="fader range")
    __properties: ClassVar[List[str]] = ["value", "default", "range"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of FaderFeature from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
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
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FaderFeature from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "value": obj.get("value"),
                "default": (
                    Fader.from_dict(obj["default"])
                    if obj.get("default") is not None
                    else None
                ),
                "range": (
                    [Fader.from_dict(_item) for _item in obj["range"]]
                    if obj.get("range") is not None
                    else None
                ),
            }
        )
        return _obj
