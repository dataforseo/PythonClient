from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AppDataGoogleLocationsCountryResultInfo(BaseModel):
    """
    AppDataGoogleLocationsCountryResultInfo
    """ # noqa: E501
    location_code: Optional[StrictInt] = Field(default=None, description="location code")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location")
    location_name_parent: Optional[StrictStr] = Field(default=None, description="the name of the superordinate location. example:. 'location_code': 1006473,. 'location_name': 'Altrincham,England,United Kingdom',. 'location_name_parent': 'England,United Kingdom', where location_name_parent corresponds to:. 'location_code': 20339,. 'location_name': 'England,United Kingdom'")
    country_iso_code: Optional[StrictStr] = Field(default=None, description="ISO country code of the location")
    location_type: Optional[StrictStr] = Field(default=None, description="location type")
    __properties: ClassVar[List[str]] = [
        "location_code", 
        "location_name", 
        "location_name_parent", 
        "country_iso_code", 
        "location_type", 
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
        _dict['location_name_parent'] = self.location_name_parent
        _dict['country_iso_code'] = self.country_iso_code
        _dict['location_type'] = self.location_type
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
            "location_name_parent": obj.get("location_name_parent"),
            "country_iso_code": obj.get("country_iso_code"),
            "location_type": obj.get("location_type"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj