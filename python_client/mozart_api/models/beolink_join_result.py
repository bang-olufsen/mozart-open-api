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
from pydantic import BaseModel, Field, StrictStr, validator


class BeolinkJoinResult(BaseModel):
    """
    BeolinkJoinResult
    """

    error: Optional[StrictStr] = Field(None, description="Join error")
    jid: StrictStr = Field(..., description="Beolink peer ID")
    request_id: StrictStr = Field(
        ..., alias="requestID", description="Beolink request ID"
    )
    status: StrictStr = Field(..., description="Overall join status")
    type: StrictStr = Field(
        ..., description="The type of join request this is a result of"
    )
    __properties = ["error", "jid", "requestID", "status", "type"]

    @validator("error")
    def error_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (
            "ok",
            "busy",
            "leaderless",
            "alone",
            "silent",
            "missing",
            "rejected",
            "timeout",
        ):
            raise ValueError(
                "must be one of enum values ('ok', 'busy', 'leaderless', 'alone', 'silent', 'missing', 'rejected', 'timeout')"
            )
        return value

    @validator("status")
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ("idle", "joined", "failed"):
            raise ValueError("must be one of enum values ('idle', 'joined', 'failed')")
        return value

    @validator("type")
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ("join", "joinRequested", "expand", "expandRequested"):
            raise ValueError(
                "must be one of enum values ('join', 'joinRequested', 'expand', 'expandRequested')"
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
    def from_json(cls, json_str: str) -> BeolinkJoinResult:
        """Create an instance of BeolinkJoinResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BeolinkJoinResult:
        """Create an instance of BeolinkJoinResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BeolinkJoinResult.parse_obj(obj)

        _obj = BeolinkJoinResult.parse_obj(
            {
                "error": obj.get("error"),
                "jid": obj.get("jid"),
                "request_id": obj.get("requestID"),
                "status": obj.get("status"),
                "type": obj.get("type"),
            }
        )
        return _obj
