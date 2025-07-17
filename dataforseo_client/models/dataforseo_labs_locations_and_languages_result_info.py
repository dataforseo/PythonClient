from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.available_languages import AvailableLanguages



class DataforseoLabsLocationsAndLanguagesResultInfo(BaseModel):
    """
    DataforseoLabsLocationsAndLanguagesResultInfo
    """ # noqa: E501
    location_code: Optional[StrictInt] = Field(default=None, description="location code")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location")
    location_code_parent: Optional[StrictInt] = Field(default=None, description="the code of the superordinate location. the value will be null as Country is the only supported location_type for this API")
    country_iso_code: Optional[StrictStr] = Field(default=None, description="ISO country code of the location")
    location_type: Optional[StrictStr] = Field(default=None, description="location type. possible values:. Country")
    available_languages: Optional[List[Optional[AvailableLanguages]]] = Field(default=None, description="supported languages. contains the languages which are supported for a specific location")
    __properties: ClassVar[List[str]] = [
        "location_code", 
        "location_name", 
        "location_code_parent", 
        "country_iso_code", 
        "location_type", 
        "available_languages", 
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

        _dict['location_code'] = self.location_code
        _dict['location_name'] = self.location_name
        _dict['location_code_parent'] = self.location_code_parent
        _dict['country_iso_code'] = self.country_iso_code
        _dict['location_type'] = self.location_type
        available_languages_items = []
        if self.available_languages:
            for _item in self.available_languages:
                if _item:
                    available_languages_items.append(_item.to_dict())
            _dict['available_languages'] = available_languages_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "location_code": obj.get("location_code"),
            "location_name": obj.get("location_name"),
            "location_code_parent": obj.get("location_code_parent"),
            "country_iso_code": obj.get("country_iso_code"),
            "location_type": obj.get("location_type"),
            "available_languages": [AvailableLanguages.from_dict(_item) for _item in obj["available_languages"]] if obj.get("available_languages") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj