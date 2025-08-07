from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class TrendsMapDataInfo(BaseModel):
    """
    TrendsMapDataInfo
    """ # noqa: E501
    geo_id: Optional[StrictStr] = Field(default=None, description="Google Trends location identifier. you can use this field for matching obtained results with location parameters specified in the request. example:. US-NY")
    geo_name: Optional[StrictStr] = Field(default=None, description="Google Trends location name. you can use this field for matching obtained results with location parameters specified in the request")
    values: Optional[List[Optional[StrictFloat]]] = Field(default=None, description="relative keyword popularity rate in a given location. represents the location-specific keyword popularity rate over the given time range. if you specify more than one keyword, the values will be averaged to the highest value across all specified keywords. a value of 100 is the peak popularity for the term. a value of 50 means that the term is half as popular. a value of 0 means there was not enough data for this term")
    max_value_index: Optional[StrictInt] = Field(default=None, description="max value among comparable terms. represents the maximum value if you specified more than two keywords in a POST array. if you specified only one keyword, the value will be null")
    __properties: ClassVar[List[str]] = [
        "geo_id", 
        "geo_name", 
        "values", 
        "max_value_index", 
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
        _dict['values'] = self.values
        _dict['max_value_index'] = self.max_value_index
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
            "values": obj.get("values"),
            "max_value_index": obj.get("max_value_index"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj