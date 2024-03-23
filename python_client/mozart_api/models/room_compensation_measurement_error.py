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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self


class RoomCompensationMeasurementError(BaseModel):
    """
    RoomCompensationMeasurementError
    """  # noqa: E501

    error: Optional[StrictStr] = Field(
        default=None,
        description="noError:   The measurement went OK. lowSignal:   When there is too low signal in the recording, e.g. due to a loudspeaker being placed at   too great a distance from the microphone. speakerSilent:   No signal could be measured.   Could be because:     - The speaker is powered off or not connected.     - The left/right switch on a wired powerlink speaker is set in the wrong position.     - The speaker is placed in another room behind closed doors. noisy<Left/Right/External>Microphone:   When the recording of the given microphone is too noisy.   Could be because:     - Something is blocking the microphone externalMicrophoneLocation:   When the location of the external microphone is invalid. externalMicrophoneMissing:   If the external microphone was missing/disconnected during a measurement. microphonesDisabled:   If the microphones are either muted or disabled. noisyMeasurement:   When too much background noise has been detected during the measurement internalError:   Something went wrong internally - can not be fixed by the user. Try again. ",
    )
    speaker_id: Optional[StrictStr] = Field(default=None, alias="speakerId")
    __properties: ClassVar[List[str]] = ["error", "speakerId"]

    @field_validator("error")
    def error_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(
            [
                "noError",
                "lowSignal",
                "speakerSilent",
                "noisyLeftMicrophone",
                "noisyRightMicrophone",
                "noisyExternalMicrophone",
                "externalMicrophoneLocation",
                "externalMicrophoneMissing",
                "microphonesDisabled",
                "noisyMeasurement",
                "internalError",
            ]
        ):
            raise ValueError(
                "must be one of enum values ('noError', 'lowSignal', 'speakerSilent', 'noisyLeftMicrophone', 'noisyRightMicrophone', 'noisyExternalMicrophone', 'externalMicrophoneLocation', 'externalMicrophoneMissing', 'microphonesDisabled', 'noisyMeasurement', 'internalError')"
            )
        return value

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
        """Create an instance of RoomCompensationMeasurementError from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RoomCompensationMeasurementError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {"error": obj.get("error"), "speakerId": obj.get("speakerId")}
        )
        return _obj
