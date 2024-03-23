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
from pydantic import BaseModel, Field
from mozart_api.models.ambience import Ambience
from mozart_api.models.balance import Balance
from mozart_api.models.bass_management import BassManagement
from mozart_api.models.compression import Compression
from mozart_api.models.directivity import Directivity
from mozart_api.models.fader import Fader
from mozart_api.models.room_compensation import RoomCompensation
from mozart_api.models.spatial_envelopment import SpatialEnvelopment
from mozart_api.models.spatial_height import SpatialHeight
from mozart_api.models.spatial_processing import SpatialProcessing
from mozart_api.models.spatial_surround import SpatialSurround
from mozart_api.models.spatial_width import SpatialWidth
from mozart_api.models.speech_enhance import SpeechEnhance
from mozart_api.models.tone_touch import ToneTouch


class ListeningModeFeatures(BaseModel):
    """
    Sound features to apply  # noqa: E501
    """

    ambience: Optional[Ambience] = None
    balance: Optional[Balance] = None
    bass_management: Optional[BassManagement] = Field(None, alias="bassManagement")
    compression: Optional[Compression] = None
    directivity: Optional[Directivity] = None
    fader: Optional[Fader] = None
    room_compensation: Optional[RoomCompensation] = Field(
        None, alias="roomCompensation"
    )
    spatial_envelopment: Optional[SpatialEnvelopment] = Field(
        None, alias="spatialEnvelopment"
    )
    spatial_height: Optional[SpatialHeight] = Field(None, alias="spatialHeight")
    spatial_processing: Optional[SpatialProcessing] = Field(
        None, alias="spatialProcessing"
    )
    spatial_surround: Optional[SpatialSurround] = Field(None, alias="spatialSurround")
    spatial_width: Optional[SpatialWidth] = Field(None, alias="spatialWidth")
    speech_enhance: Optional[SpeechEnhance] = Field(None, alias="speechEnhance")
    tone_touch: Optional[ToneTouch] = Field(None, alias="toneTouch")
    __properties = [
        "ambience",
        "balance",
        "bassManagement",
        "compression",
        "directivity",
        "fader",
        "roomCompensation",
        "spatialEnvelopment",
        "spatialHeight",
        "spatialProcessing",
        "spatialSurround",
        "spatialWidth",
        "speechEnhance",
        "toneTouch",
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
    def from_json(cls, json_str: str) -> ListeningModeFeatures:
        """Create an instance of ListeningModeFeatures from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of ambience
        if self.ambience:
            _dict["ambience"] = self.ambience.to_dict()
        # override the default output from pydantic by calling `to_dict()` of balance
        if self.balance:
            _dict["balance"] = self.balance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bass_management
        if self.bass_management:
            _dict["bassManagement"] = self.bass_management.to_dict()
        # override the default output from pydantic by calling `to_dict()` of compression
        if self.compression:
            _dict["compression"] = self.compression.to_dict()
        # override the default output from pydantic by calling `to_dict()` of directivity
        if self.directivity:
            _dict["directivity"] = self.directivity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fader
        if self.fader:
            _dict["fader"] = self.fader.to_dict()
        # override the default output from pydantic by calling `to_dict()` of room_compensation
        if self.room_compensation:
            _dict["roomCompensation"] = self.room_compensation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spatial_envelopment
        if self.spatial_envelopment:
            _dict["spatialEnvelopment"] = self.spatial_envelopment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spatial_height
        if self.spatial_height:
            _dict["spatialHeight"] = self.spatial_height.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spatial_processing
        if self.spatial_processing:
            _dict["spatialProcessing"] = self.spatial_processing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spatial_surround
        if self.spatial_surround:
            _dict["spatialSurround"] = self.spatial_surround.to_dict()
        # override the default output from pydantic by calling `to_dict()` of spatial_width
        if self.spatial_width:
            _dict["spatialWidth"] = self.spatial_width.to_dict()
        # override the default output from pydantic by calling `to_dict()` of speech_enhance
        if self.speech_enhance:
            _dict["speechEnhance"] = self.speech_enhance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tone_touch
        if self.tone_touch:
            _dict["toneTouch"] = self.tone_touch.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ListeningModeFeatures:
        """Create an instance of ListeningModeFeatures from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ListeningModeFeatures.parse_obj(obj)

        _obj = ListeningModeFeatures.parse_obj(
            {
                "ambience": Ambience.from_dict(obj.get("ambience"))
                if obj.get("ambience") is not None
                else None,
                "balance": Balance.from_dict(obj.get("balance"))
                if obj.get("balance") is not None
                else None,
                "bass_management": BassManagement.from_dict(obj.get("bassManagement"))
                if obj.get("bassManagement") is not None
                else None,
                "compression": Compression.from_dict(obj.get("compression"))
                if obj.get("compression") is not None
                else None,
                "directivity": Directivity.from_dict(obj.get("directivity"))
                if obj.get("directivity") is not None
                else None,
                "fader": Fader.from_dict(obj.get("fader"))
                if obj.get("fader") is not None
                else None,
                "room_compensation": RoomCompensation.from_dict(
                    obj.get("roomCompensation")
                )
                if obj.get("roomCompensation") is not None
                else None,
                "spatial_envelopment": SpatialEnvelopment.from_dict(
                    obj.get("spatialEnvelopment")
                )
                if obj.get("spatialEnvelopment") is not None
                else None,
                "spatial_height": SpatialHeight.from_dict(obj.get("spatialHeight"))
                if obj.get("spatialHeight") is not None
                else None,
                "spatial_processing": SpatialProcessing.from_dict(
                    obj.get("spatialProcessing")
                )
                if obj.get("spatialProcessing") is not None
                else None,
                "spatial_surround": SpatialSurround.from_dict(
                    obj.get("spatialSurround")
                )
                if obj.get("spatialSurround") is not None
                else None,
                "spatial_width": SpatialWidth.from_dict(obj.get("spatialWidth"))
                if obj.get("spatialWidth") is not None
                else None,
                "speech_enhance": SpeechEnhance.from_dict(obj.get("speechEnhance"))
                if obj.get("speechEnhance") is not None
                else None,
                "tone_touch": ToneTouch.from_dict(obj.get("toneTouch"))
                if obj.get("toneTouch") is not None
                else None,
            }
        )
        return _obj
