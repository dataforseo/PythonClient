from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class KeywordsDataBingSearchVolumeHistoryLiveRequestInfo(BaseModel):
    """
    KeywordsDataBingSearchVolumeHistoryLiveRequestInfo
    """ # noqa: E501
    keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="keywords. required field. The maximum number of keywords you can specify: 1000. The maximum number of characters for each keyword: 100. the specified keywords will be converted to lowercase, data will be provided in a separate array. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location. required field if you don’t specify location_code or location_coordinate. if you use this field, you don’t need to specify location_code or location_coordinate. you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/search_volume_history/locations_and_languages. example:. London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code. required field if you don’t specify location_name or location_coordinate. if you use this field, you don’t need to specify location_name or location_coordinate. you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/search_volume_history/locations_and_languages. example:. 2840")
    location_coordinate: Optional[StrictStr] = Field(default=None, description="GPS coordinates of a location. required field if you don’t specify location_name or location_code. if you use this field, you don’t need to specify location_name or location_code. location_coordinate parameter should be specified in the “latitude,longitude” format. the data will be provided for the country the specified coordinates belong to. example:. 52.6178549,-155.352142")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language. required field if you don’t specify language_code. if you use this field, you don’t need to specify language_code. you can receive the list of available languages of the search engines with their language_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/search_volume_history/locations_and_languages")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code. required field if you don’t specify language_name. if you use this field, you don’t need to specify language_name. you can receive the list of available languages of the search engines with their language_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/search_volume_history/locations_and_languages")
    device: Optional[List[Optional[StrictStr]]] = Field(default=None, description="device types. optional field. specify this field if you want to get the data for a particular device types. possible values: mobile, desktop, tablet, non_smartphones. default value:  ['mobile', 'desktop', 'tablet', 'non_smartphones']")
    period: Optional[StrictStr] = Field(default=None, description="aggregates the returned data to a certain time period. optional field. specify this field if you want to get the data in monthly, weekly or daily format. possible values: monthly, weekly, daily. monthly – returns data up to past 24 months. weekly – returns data up to past 15 weeks. daily – returns data up to past 45 days. default value:  monthly")
    date_from: Optional[StrictStr] = Field(default=None, description="starting date of the time range. optional field. minimum value: two years back from today’s date. maximum value: one day from today’s date. date format: 'yyyy-mm-dd'. example:. '2020-01-01'. Note: we do not recommend using a custom time range. Note 2: if date_from and date_to parameters are not specified, the data will be returned for the past 24 months. if you specify the period parameter:. with value weekly, you will get results for the past 15 weeks. with value daily, you will get results for the past 45 days")
    date_to: Optional[StrictStr] = Field(default=None, description="ending date of the time range. optional field. minimum value: two years back from today’s date;. maximum value: one day from today’s date;. date format: 'yyyy-mm-dd'. example:. '2020-03-15'. Note: we do not recommend using a custom time range. Note 2: if date_from and date_to parameters are not specified, the data will be returned for the past 24 months. if you specify the period parameter:. with value weekly, you will get results for the past 15 weeks. with value daily, you will get results for the past 45 days")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "keywords", 
        "location_name", 
        "location_code", 
        "location_coordinate", 
        "language_name", 
        "language_code", 
        "device", 
        "period", 
        "date_from", 
        "date_to", 
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
        _dict['location_coordinate'] = self.location_coordinate
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['device'] = self.device
        _dict['period'] = self.period
        _dict['date_from'] = self.date_from
        _dict['date_to'] = self.date_to
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
            "location_coordinate": obj.get("location_coordinate"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "device": obj.get("device"),
            "period": obj.get("period"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj