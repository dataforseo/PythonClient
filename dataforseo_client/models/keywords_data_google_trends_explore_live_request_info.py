from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class KeywordsDataGoogleTrendsExploreLiveRequestInfo(BaseModel):
    """
    KeywordsDataGoogleTrendsExploreLiveRequestInfo
    """ # noqa: E501
    keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="keywords. required field. the maximum number of keywords you can specify: 5. the maximum number of characters you can specify in a keyword: 100. the minimum number of characters must be greater than 1. comma characters (,) in the specified keywords will be unset and ignored. Note: keywords cannot consist of a combination of the following characters: < > | \ ' - + = ~ ! : * ( ) [ ] { }. Note: to obtain google_trends_topics_list and google_trends_queries_list items, specify no more than 1 keyword. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location. optional field. if you don’t use this field, you will recieve global results. if you use this field, you don’t need to specify location_code. you can use this field as an array to set several locations, each corresponding to a specific keyword – learn more;. you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_trends/locations. example:. United Kingdom")
    location_code: Optional[StrictStr] = Field(default=None, description="search engine location code. optional field. if you don’t use this field, you will recieve global results. if you use this field, you don’t need to specify location_name. you can use this field as an array to set several locations, each corresponding to a specific keyword – learn more;. you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_trends/locations. example:. 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language. optional field. default value: English. if you use this field, you don’t need to specify language_code. you can receive the list of available languages of the search engine with their language_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_trends/languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code. optional field. default value: en. if you use this field, you don’t need to specify language_name. you can receive the list of available languages of the search engine with their language_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_trends/languages. example:. en")
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    category_code: Optional[StrictInt] = Field(default=None, description="google trends search category. optional field. if you don’t specify this field, the 0 value will be applied by default and the search will be carried out across all available categories. you can receive the list of available categories with their category_code by making a separate request to the https://api.dataforseo.com/v3/keywords_data/google_trends/categories")
    date_from: Optional[StrictStr] = Field(default=None, description="starting date of the time range. optional field. if you don’t specify this field, the current day and month of the preceding year will be used by default. minimal value for the web type: 2004-01-01. minimal value for other types: 2008-01-01. date format: 'yyyy-mm-dd'. example:. '2019-01-15'")
    date_to: Optional[StrictStr] = Field(default=None, description="ending date of the time range. optional field. if you don’t specify this field, the today’s date will be used by default. date format: 'yyyy-mm-dd'. example:. '2019-01-15'")
    time_range: Optional[StrictStr] = Field(default=None, description="preset time ranges. optional field. if you specify date_from or date_to parameters, this field will be ignored when setting a task. possible values for all type parameters:. past_hour, past_4_hours, past_day, past_7_days, past_30_days, past_90_days, past_12_months, past_5_years. possible values for web only:. 2004_present. possible values for news, youtube, images, froogle:. 2008_present")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="types of items returned. optional field. to speed up the execution of the request, specify one item at a time;. possible values:. 'google_trends_graph', 'google_trends_map', 'google_trends_topics_list','google_trends_queries_list'. default value:. 'google_trends_graph'. Note: to obtain google_trends_topics_list and google_trends_queries_list items, specify no more than 1 keyword in the keywords field")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "keywords", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "type", 
        "category_code", 
        "date_from", 
        "date_to", 
        "time_range", 
        "item_types", 
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
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['type'] = self.type
        _dict['category_code'] = self.category_code
        _dict['date_from'] = self.date_from
        _dict['date_to'] = self.date_to
        _dict['time_range'] = self.time_range
        _dict['item_types'] = self.item_types
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
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "type": obj.get("type"),
            "category_code": obj.get("category_code"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "time_range": obj.get("time_range"),
            "item_types": obj.get("item_types"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj