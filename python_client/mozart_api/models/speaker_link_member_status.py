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
from datetime import datetime
from typing import Optional

try:
    from pydantic.v1 import BaseModel, Field, StrictStr, constr, validator
except ImportError:
    from pydantic import BaseModel, Field, StrictStr, constr, validator


class SpeakerLinkMemberStatus(BaseModel):
    """
    SpeakerLinkMemberStatus
    """

    base_url: Optional[StrictStr] = Field(
        default=None,
        alias="baseUrl",
        description="API prefix to use when talking to the secondary",
    )
    health: StrictStr = Field(...)
    ip_address: Optional[StrictStr] = Field(
        default=None, alias="ipAddress", description="IP address"
    )
    network_type: StrictStr = Field(default=..., alias="networkType")
    product_type: Optional[StrictStr] = Field(default=None, alias="productType")
    serial_number: constr(strict=True) = Field(
        default=..., alias="serialNumber", description="Speaker serial number"
    )
    updated_at: datetime = Field(
        default=..., alias="updatedAt", description="Timestamp in RFC3393 format"
    )
    __properties = [
        "baseUrl",
        "health",
        "ipAddress",
        "networkType",
        "productType",
        "serialNumber",
        "updatedAt",
    ]

    @validator("health")
    def health_validate_enum(cls, value):
        """Validates the enum"""
        if value not in (
            "unknown",
            "good",
            "warning",
            "bad",
        ):
            raise ValueError(
                "must be one of enum values ('unknown', 'good', 'warning', 'bad')"
            )
        return value

    @validator("network_type")
    def network_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in (
            "none",
            "wired",
            "wireless",
        ):
            raise ValueError("must be one of enum values ('none', 'wired', 'wireless')")
        return value

    @validator("serial_number")
    def serial_number_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^\d{8}", value):
            raise ValueError(r"must validate the regular expression /^\d{8}/")
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
    def from_json(cls, json_str: str) -> SpeakerLinkMemberStatus:
        """Create an instance of SpeakerLinkMemberStatus from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # set to None if base_url (nullable) is None
        # and __fields_set__ contains the field
        if self.base_url is None and "base_url" in self.__fields_set__:
            _dict["baseUrl"] = None

        # set to None if ip_address (nullable) is None
        # and __fields_set__ contains the field
        if self.ip_address is None and "ip_address" in self.__fields_set__:
            _dict["ipAddress"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SpeakerLinkMemberStatus:
        """Create an instance of SpeakerLinkMemberStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SpeakerLinkMemberStatus.parse_obj(obj)

        _obj = SpeakerLinkMemberStatus.parse_obj(
            {
                "base_url": obj.get("baseUrl"),
                "health": obj.get("health"),
                "ip_address": obj.get("ipAddress"),
                "network_type": obj.get("networkType"),
                "product_type": obj.get("productType"),
                "serial_number": obj.get("serialNumber"),
                "updated_at": obj.get("updatedAt"),
            }
        )
        return _obj
