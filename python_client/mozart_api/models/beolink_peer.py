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


try:
    from pydantic.v1 import BaseModel, Field, StrictStr
except ImportError:
    from pydantic import BaseModel, Field, StrictStr


class BeolinkPeer(BaseModel):
    """
    BeolinkPeer
    """

    friendly_name: StrictStr = Field(default=..., alias="friendlyName")
    ip_address: StrictStr = Field(
        default=..., alias="ipAddress", description="IP address"
    )
    jid: StrictStr = Field(default=..., description="Beolink peer ID")
    __properties = ["friendlyName", "ipAddress", "jid"]

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
    def from_json(cls, json_str: str) -> BeolinkPeer:
        """Create an instance of BeolinkPeer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BeolinkPeer:
        """Create an instance of BeolinkPeer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BeolinkPeer.parse_obj(obj)

        _obj = BeolinkPeer.parse_obj(
            {
                "friendly_name": obj.get("friendlyName"),
                "ip_address": obj.get("ipAddress"),
                "jid": obj.get("jid"),
            }
        )
        return _obj
