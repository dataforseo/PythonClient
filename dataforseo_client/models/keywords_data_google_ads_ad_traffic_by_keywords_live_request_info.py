from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class KeywordsDataGoogleAdsAdTrafficByKeywordsLiveRequestInfo(BaseModel):
    """
    KeywordsDataGoogleAdsAdTrafficByKeywordsLiveRequestInfo
    """ # noqa: E501
    keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="keywords. required field. The maximum number of keywords you can specify: 1000. The maximum number of characters for each keyword: 80. The maximum number of words for each keyword phrase: 10. the keywords you specify will be converted to a lowercase format. Note: Google Ads may return no data for certain groups of keywords. visit our Help Center to learn more. Also note that Google Ads doesn’t allow using certain symbols and characters (e.g., UTF symbols, emojis), so you can’t use them when setting a task;. to learn more about which symbols and characters can be used, please refer to this article. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    bid: Optional[StrictInt] = Field(default=None, description="the maximum custom bid. required field. the collected data will be based on this value. it stands for the price you are willing to pay for an ad; the higher value you specify here, the higher values you will get in the returned metrics. learn more in this help center article")
    match: Optional[StrictStr] = Field(default=None, description="keywords match-type. required field. can take the following values: exact, broad, phrase")
    search_partners: Optional[StrictBool] = Field(default=None, description="include Google search partners. optional field. if you specify true, the results will be delivered for owned, operated, and syndicated networks across Google and partner sites that host Google search;. default value: false – results are returned for Google search sites")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location. optional field. if you do not indicate the location, you will receive worldwide results, i.e., for all available locations;. if you use this field, you don’t need to specify location_code or location_coordinate. you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/locations. example:. London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code. optional field. if you do not indicate the location, you will receive worldwide results, i.e., for all available locations;. if you use this field, you don’t need to specify location_name or location_coordinate;. you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/locations. example:. 2840")
    location_coordinate: Optional[StrictStr] = Field(default=None, description="GPS coordinates of a location. optional field. if you do not indicate the location, you will receive worldwide results, i.e., for all available locations;. if you use this field, you don’t need to specify location_name or location_code;. location_coordinate parameter should be specified in the “latitude,longitude” format;. the data will be provided for the country the specified coordinates belong to;. example:. 52.6178549,-155.352142")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language. optional field. you can receive the list of available languages of the search engine with their language_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code. optional field. you can receive the list of available languages of the search engine with their language_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/languages. example:. en")
    date_from: Optional[StrictStr] = Field(default=None, description="starting date of the forecasting time range. required field if you specify date_to. if you indicate date_from and date_to, you don’t need to specify date_interval. minimum value is tomorrow’s date. the value you specify in date_from shouldn’t be further than date_to. date format: 'yyyy-mm-dd'. example:. '2021-10-30'if Status endpoint returns false in the actual_data field, date_from can be set to the month before last and prior;. if Status endpoint returns true in the actual_data field, date_from can be set to the last month and prior")
    date_to: Optional[StrictStr] = Field(default=None, description="ending date of the forecasting time range. required field if you specify date_from. if you indicate date_from and date_to, you don’t need to specify date_interval. minimum value is date_from +1 day. maximum value is current day and month of the next year. date format: 'yyyy-mm-dd'. example:. '2022-10-30'")
    date_interval: Optional[StrictStr] = Field(default=None, description="forecasting date interval. optional field. if you specify date_interval, you don’t need to indicate date_from and date_to. possible values: next_week, next_month, next_quarter. default value: next_month")
    sort_by: Optional[StrictStr] = Field(default=None, description="results sorting parameters. optional field. Use these parameters to sort the results by relevance, impressions, ctr, average_cpc, cost, or clicks in the descending order. default value: relevance")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "keywords", 
        "bid", 
        "match", 
        "search_partners", 
        "location_name", 
        "location_code", 
        "location_coordinate", 
        "language_name", 
        "language_code", 
        "date_from", 
        "date_to", 
        "date_interval", 
        "sort_by", 
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
        _dict['bid'] = self.bid
        _dict['match'] = self.match
        _dict['search_partners'] = self.search_partners
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['location_coordinate'] = self.location_coordinate
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['date_from'] = self.date_from
        _dict['date_to'] = self.date_to
        _dict['date_interval'] = self.date_interval
        _dict['sort_by'] = self.sort_by
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
            "bid": obj.get("bid"),
            "match": obj.get("match"),
            "search_partners": obj.get("search_partners"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "location_coordinate": obj.get("location_coordinate"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "date_interval": obj.get("date_interval"),
            "sort_by": obj.get("sort_by"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj