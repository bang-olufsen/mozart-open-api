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
    from pydantic.v1 import BaseModel, Field, StrictStr, constr
except ImportError:
    from pydantic import BaseModel, Field, StrictStr, constr


class OverlayPlayRequestTextToSpeechTextToSpeech(BaseModel):
    """
    Object used for performing a text-to-speech operation on the product.   # noqa: E501
    """

    lang: Optional[StrictStr] = Field(
        default=None,
        description="An optional specification of the language to use. The default value is ultimately decided by the BeoCloud API, but currently it defaults to `en-us`. ",
    )
    text: constr(strict=True, max_length=2048) = Field(
        default=...,
        description="Required field containing the actual text that will be converted to speech (audio). A maximum length of 2048 characters is allowed. ",
    )
    __properties = ["lang", "text"]

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
    def from_json(cls, json_str: str) -> OverlayPlayRequestTextToSpeechTextToSpeech:
        """Create an instance of OverlayPlayRequestTextToSpeechTextToSpeech from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if lang (nullable) is None
        # and __fields_set__ contains the field
        if self.lang is None and "lang" in self.__fields_set__:
            _dict["lang"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OverlayPlayRequestTextToSpeechTextToSpeech:
        """Create an instance of OverlayPlayRequestTextToSpeechTextToSpeech from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OverlayPlayRequestTextToSpeechTextToSpeech.parse_obj(obj)

        _obj = OverlayPlayRequestTextToSpeechTextToSpeech.parse_obj(
            {"lang": obj.get("lang"), "text": obj.get("text")}
        )
        return _obj
