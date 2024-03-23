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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator
from mozart_api.models.room_compensation_error_details import (
    RoomCompensationErrorDetails,
)
from mozart_api.models.room_compensation_properties import RoomCompensationProperties


class RoomCompensationState(BaseModel):
    """
    RoomCompensationState
    """

    state: Optional[StrictStr] = None
    error: Optional[StrictStr] = Field(
        None,
        description="microphoneMuted:   The microphone is muted (soft-off, using touch button). microphoneSwitchOff:   The microphone switch is set in its off position. microphoneSignalMissing:   No signal was detected. Is the microphone blocked? externalMicrophoneMissing:   The external microphone is not connected.   Is only relevant for advanced room compensation. externalMicrophoneInvalidPosition:   The external microphone is placed in an invalid position,   e.g. placed too close or in an extreme angle to the internal speakers.   Is only relevant for advanced room compensation. noisyEnvironment:   Too much environment noise to get a valid measurement. speakerMeasurementFailed:   A measurement failed, related to one of the individual speakers.   See the errorDetails property for details about the error and which speaker measurement failed.   Is only relevant for advanced room compensation. invalidSpeakerList:   The speaker list contains invalid speakers.   Valid speakers are: all external speakers and non-virtual internal speakers.   Is only relevant for advanced room compensation. invalidAction:   Could not start with given action.   Eg. can't run from last failed speaker if there isn't any failed run.   Is only relevant for advanced room compensation. internalError:   Internal product error. ",
    )
    error_details: Optional[RoomCompensationErrorDetails] = Field(
        None, alias="errorDetails"
    )
    last_run_available: Optional[StrictBool] = Field(
        None,
        alias="lastRunAvailable",
        description='When true, measurements have been cached due to manual interrupt or failure, making it possible to use the action "continue" where the system will continue from the speaker where interrupted. The cached measurements are only temporary and will be cleared after some time (default 15min), in which case lastRunAvailable becomes false. ',
    )
    properties: Optional[RoomCompensationProperties] = None
    time_stamp: Optional[datetime] = Field(None, alias="timeStamp")
    __properties = [
        "state",
        "error",
        "errorDetails",
        "lastRunAvailable",
        "properties",
        "timeStamp",
    ]

    @validator("state")
    def state_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ("notStarted", "running", "done", "error", "stopped"):
            raise ValueError(
                "must be one of enum values ('notStarted', 'running', 'done', 'error', 'stopped')"
            )
        return value

    @validator("error")
    def error_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in (
            "noError",
            "microphoneMuted",
            "microphoneSwitchOff",
            "microphoneSignalMissing",
            "externalMicrophoneMissing",
            "externalMicrophoneInvalidPosition",
            "noisyEnvironment",
            "speakerMeasurementFailed",
            "invalidSpeakerList",
            "invalidAction",
            "internalError",
        ):
            raise ValueError(
                "must be one of enum values ('noError', 'microphoneMuted', 'microphoneSwitchOff', 'microphoneSignalMissing', 'externalMicrophoneMissing', 'externalMicrophoneInvalidPosition', 'noisyEnvironment', 'speakerMeasurementFailed', 'invalidSpeakerList', 'invalidAction', 'internalError')"
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
    def from_json(cls, json_str: str) -> RoomCompensationState:
        """Create an instance of RoomCompensationState from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of error_details
        if self.error_details:
            _dict["errorDetails"] = self.error_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict["properties"] = self.properties.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoomCompensationState:
        """Create an instance of RoomCompensationState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoomCompensationState.parse_obj(obj)

        _obj = RoomCompensationState.parse_obj(
            {
                "state": obj.get("state"),
                "error": obj.get("error"),
                "error_details": RoomCompensationErrorDetails.from_dict(
                    obj.get("errorDetails")
                )
                if obj.get("errorDetails") is not None
                else None,
                "last_run_available": obj.get("lastRunAvailable"),
                "properties": RoomCompensationProperties.from_dict(
                    obj.get("properties")
                )
                if obj.get("properties") is not None
                else None,
                "time_stamp": obj.get("timeStamp"),
            }
        )
        return _obj
