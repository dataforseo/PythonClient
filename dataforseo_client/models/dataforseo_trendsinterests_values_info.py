from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoTrendsinterestsValuesInfo(BaseModel):
    """
    DataforseoTrendsinterestsValuesInfo
    """ # noqa: E501
    geo_id: Optional[StrictStr] = Field(default=None, description="location identifier. you can use this field for matching obtained results with location parameters specified in the request. see the full list of available locations with their geo_id here or by making a separate request to https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations. example:. US-NY")
    geo_name: Optional[StrictStr] = Field(default=None, description="location name. you can use this field for matching obtained results with location parameters specified in the request. see the full list of available locations with their geo_name here or by making a separate request to https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations. example:. Andorra")
    value: Optional[StrictInt] = Field(default=None, description="relative keyword popularity rate in a given location. represents location-specific keyword popularity rate over the specified time range;. using this value you can understand how popular a keyword is in one location compared to another location;. calculation: we determine the highest popularity value for the relevant keyword across all locations, and then express all other values as a percentage of that highest value (100);. a value of 100 is the highest popularity for the term. a value of 50 means that the term is half as popular. a value of 0 means there was not enough data for this term")
    __properties: ClassVar[List[str]] = [
        "geo_id", 
        "geo_name", 
        "value", 
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

        _dict['geo_id'] = self.geo_id
        _dict['geo_name'] = self.geo_name
        _dict['value'] = self.value
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "geo_id": obj.get("geo_id"),
            "geo_name": obj.get("geo_name"),
            "value": obj.get("value"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj