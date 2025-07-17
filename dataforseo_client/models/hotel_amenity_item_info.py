from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class HotelAmenityItemInfo(BaseModel):
    """
    HotelAmenityItemInfo
    """ # noqa: E501
    amenity: Optional[StrictStr] = Field(default=None, description="standardised amenity name")
    amenity_label: Optional[StrictStr] = Field(default=None, description="displayed amenity name")
    hint: Optional[StrictStr] = Field(default=None, description="standardised details about the amenity")
    hint_label: Optional[StrictStr] = Field(default=None, description="displayed details about the amenity")
    is_available: Optional[StrictBool] = Field(default=None, description="indicates whether the amenity is available in the hotel")
    __properties: ClassVar[List[str]] = [
        "amenity", 
        "amenity_label", 
        "hint", 
        "hint_label", 
        "is_available", 
        ]

    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        excluded_fields: Set[str] = set([
        ])

        _dict = {}

        _dict['amenity'] = self.amenity
        _dict['amenity_label'] = self.amenity_label
        _dict['hint'] = self.hint
        _dict['hint_label'] = self.hint_label
        _dict['is_available'] = self.is_available
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amenity": obj.get("amenity"),
            "amenity_label": obj.get("amenity_label"),
            "hint": obj.get("hint"),
            "hint_label": obj.get("hint_label"),
            "is_available": obj.get("is_available"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj