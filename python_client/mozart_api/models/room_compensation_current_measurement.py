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


class RoomCompensationCurrentMeasurement(BaseModel):
    """
    State and speaker ID of the currently running measurement. Is only relevant for advanced room compensation.   # noqa: E501
    """

    speaker_id: Optional[StrictStr] = Field(None, alias="speakerId")
    state: Optional[StrictStr] = Field(
        None,
        description="State of the measurement for the speaker. started:   The measurement has started. done:   The measurement has ended successfully. lastDone:   The last measurement in the run has ended successfully. error:   An error occurred during measurement. ",
    )
    __properties = ["speakerId", "state"]

    @validator("state")
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("started", "done", "lastDone", "error"):
            raise ValueError(
                "must be one of enum values ('started', 'done', 'lastDone', 'error')"
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
    def from_json(cls, json_str: str) -> RoomCompensationCurrentMeasurement:
        """Create an instance of RoomCompensationCurrentMeasurement from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoomCompensationCurrentMeasurement:
        """Create an instance of RoomCompensationCurrentMeasurement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoomCompensationCurrentMeasurement.parse_obj(obj)

        _obj = RoomCompensationCurrentMeasurement.parse_obj(
            {"speaker_id": obj.get("speakerId"), "state": obj.get("state")}
        )
        return _obj