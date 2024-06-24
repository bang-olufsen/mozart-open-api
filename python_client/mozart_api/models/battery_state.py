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
    from pydantic.v1 import BaseModel, Field, StrictBool, StrictInt
except ImportError:
    from pydantic import BaseModel, Field, StrictBool, StrictInt


class BatteryState(BaseModel):
    """
    BatteryState
    """

    battery_level: Optional[StrictInt] = Field(
        default=None, alias="batteryLevel", description="Batterylevel in percent "
    )
    is_charging: Optional[StrictBool] = Field(default=None, alias="isCharging")
    remaining_charging_time_minutes: Optional[StrictInt] = Field(
        default=None,
        alias="remainingChargingTimeMinutes",
        description="Remaining charging time in minutes",
    )
    remaining_playing_time_minutes: Optional[StrictInt] = Field(
        default=None,
        alias="remainingPlayingTimeMinutes",
        description="Remaining playing time in minutes",
    )
    __properties = [
        "batteryLevel",
        "isCharging",
        "remainingChargingTimeMinutes",
        "remainingPlayingTimeMinutes",
    ]

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
    def from_json(cls, json_str: str) -> BatteryState:
        """Create an instance of BatteryState from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BatteryState:
        """Create an instance of BatteryState from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BatteryState.parse_obj(obj)

        _obj = BatteryState.parse_obj(
            {
                "battery_level": obj.get("batteryLevel"),
                "is_charging": obj.get("isCharging"),
                "remaining_charging_time_minutes": obj.get(
                    "remainingChargingTimeMinutes"
                ),
                "remaining_playing_time_minutes": obj.get(
                    "remainingPlayingTimeMinutes"
                ),
            }
        )
        return _obj
