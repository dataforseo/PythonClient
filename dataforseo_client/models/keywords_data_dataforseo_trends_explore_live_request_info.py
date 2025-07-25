from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class KeywordsDataDataforseoTrendsExploreLiveRequestInfo(BaseModel):
    """
    KeywordsDataDataforseoTrendsExploreLiveRequestInfo
    """ # noqa: E501
    keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="keywords. required field. the maximum number of keywords you can specify: 5. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location. optional field. if you don’t use this field, you will recieve global results. if you use this field, you don’t need to specify location_code. you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations. note that the data will be provided for the country the specified location_name belongs to;. example:. United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code. optional field. if you don’t use this field, you will recieve global results. if you use this field, you don’t need to specify location_name. you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/dataforseo_trends/locations. note that the data will be provided for the country the specified location_code belongs to;. example:. 2840")
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    date_from: Optional[StrictStr] = Field(default=None, description="starting date of the time range. optional field. if you don’t specify this field, the current day and month of the preceding year will be used by default. minimal value for the web type: 2004-01-01. minimal value for other types: 2008-01-01. date format: 'yyyy-mm-dd'. example:. '2019-01-15'")
    date_to: Optional[StrictStr] = Field(default=None, description="ending date of the time range. optional field. if you don’t specify this field, the today’s date will be used by default. date format: 'yyyy-mm-dd'. example:. '2019-01-15'")
    time_range: Optional[StrictStr] = Field(default=None, description="preset time ranges. optional field. if you specify date_from or date_to parameters, this field will be ignored when setting a task. possible values for all type parameters:. past_4_hours, past_day, past_7_days, past_30_days, past_90_days, past_12_months, past_5_years")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "keywords", 
        "location_name", 
        "location_code", 
        "type", 
        "date_from", 
        "date_to", 
        "time_range", 
        "tag", 
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

        _dict['keywords'] = self.keywords
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['type'] = self.type
        _dict['date_from'] = self.date_from
        _dict['date_to'] = self.date_to
        _dict['time_range'] = self.time_range
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keywords": obj.get("keywords"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "type": obj.get("type"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "time_range": obj.get("time_range"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj