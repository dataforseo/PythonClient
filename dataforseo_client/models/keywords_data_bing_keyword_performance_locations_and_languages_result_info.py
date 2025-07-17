from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.available_locations import AvailableLocations



class KeywordsDataBingKeywordPerformanceLocationsAndLanguagesResultInfo(BaseModel):
    """
    KeywordsDataBingKeywordPerformanceLocationsAndLanguagesResultInfo
    """ # noqa: E501
    language_name: Optional[StrictStr] = Field(default=None, description="language name")
    language_code: Optional[StrictStr] = Field(default=None, description="language code")
    available_locations: Optional[List[Optional[AvailableLocations]]] = Field(default=None, description="supported locations. contains locations supported in combination with a specific language")
    __properties: ClassVar[List[str]] = [
        "language_name", 
        "language_code", 
        "available_locations", 
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

        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        available_locations_items = []
        if self.available_locations:
            for _item in self.available_locations:
                if _item:
                    available_locations_items.append(_item.to_dict())
            _dict['available_locations'] = available_locations_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "available_locations": [AvailableLocations.from_dict(_item) for _item in obj["available_locations"]] if obj.get("available_locations") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj