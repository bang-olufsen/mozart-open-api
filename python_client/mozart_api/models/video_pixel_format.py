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
    from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, validator
except ImportError:
    from pydantic import BaseModel, Field, StrictBool, StrictStr, validator


class VideoPixelFormat(BaseModel):
    """
    VideoPixelFormat
    """

    bitdepth: Optional[StrictStr] = None
    chroma_subsample: Optional[StrictStr] = Field(default=None, alias="chromaSubsample")
    colorimetry: Optional[StrictStr] = None
    full_range: Optional[StrictBool] = Field(default=None, alias="fullRange")
    __properties = ["bitdepth", "chromaSubsample", "colorimetry", "fullRange"]

    @validator("bitdepth")
    def bitdepth_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (
            "bit8",
            "bit10",
            "bit12",
        ):
            raise ValueError("must be one of enum values ('bit8', 'bit10', 'bit12')")
        return value

    @validator("chroma_subsample")
    def chroma_subsample_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (
            "yCbCr444RGB",
            "yCbCr422",
            "yCbCr420",
        ):
            raise ValueError(
                "must be one of enum values ('yCbCr444RGB', 'yCbCr422', 'yCbCr420')"
            )
        return value

    @validator("colorimetry")
    def colorimetry_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (
            "rGB",
            "opRGB",
            "rGBP3D65",
            "rGBP3DCI",
            "rGB2020",
            "yCC601",
            "yCC709",
            "xvYCC601",
            "xvYCC709",
            "sYCC601",
            "opYCC601",
            "yCC2020NCL",
            "yCC2020NL",
        ):
            raise ValueError(
                "must be one of enum values ('rGB', 'opRGB', 'rGBP3D65', 'rGBP3DCI', 'rGB2020', 'yCC601', 'yCC709', 'xvYCC601', 'xvYCC709', 'sYCC601', 'opYCC601', 'yCC2020NCL', 'yCC2020NL')"
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
    def from_json(cls, json_str: str) -> VideoPixelFormat:
        """Create an instance of VideoPixelFormat from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VideoPixelFormat:
        """Create an instance of VideoPixelFormat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VideoPixelFormat.parse_obj(obj)

        _obj = VideoPixelFormat.parse_obj(
            {
                "bitdepth": obj.get("bitdepth"),
                "chroma_subsample": obj.get("chromaSubsample"),
                "colorimetry": obj.get("colorimetry"),
                "full_range": obj.get("fullRange"),
            }
        )
        return _obj
