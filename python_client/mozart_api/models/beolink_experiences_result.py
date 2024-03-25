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


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from mozart_api.models.beolink_experience import BeolinkExperience


class BeolinkExperiencesResult(BaseModel):
    """
    BeolinkExperiencesResult
    """

    experiences: conlist(BeolinkExperience) = Field(...)
    request_id: StrictStr = Field(
        ..., alias="requestID", description="Beolink request ID"
    )
    status: StrictStr = Field(
        ...,
        description="Current scan status. * busy: there is another scan in progress * timeout: the scan timed out. The results will be partial ",
    )
    __properties = ["experiences", "requestID", "status"]

    @validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ("ok", "busy", "timeout"):
            raise ValueError("must be one of enum values ('ok', 'busy', 'timeout')")
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
    def from_json(cls, json_str: str) -> BeolinkExperiencesResult:
        """Create an instance of BeolinkExperiencesResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in experiences (list)
        _items = []
        if self.experiences:
            for _item in self.experiences:
                if _item:
                    _items.append(_item.to_dict())
            _dict["experiences"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BeolinkExperiencesResult:
        """Create an instance of BeolinkExperiencesResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BeolinkExperiencesResult.parse_obj(obj)

        _obj = BeolinkExperiencesResult.parse_obj(
            {
                "experiences": (
                    [
                        BeolinkExperience.from_dict(_item)
                        for _item in obj.get("experiences")
                    ]
                    if obj.get("experiences") is not None
                    else None
                ),
                "request_id": obj.get("requestID"),
                "status": obj.get("status"),
            }
        )
        return _obj
