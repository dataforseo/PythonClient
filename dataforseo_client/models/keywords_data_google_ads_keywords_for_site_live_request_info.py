from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class KeywordsDataGoogleAdsKeywordsForSiteLiveRequestInfo(BaseModel):
    """
    KeywordsDataGoogleAdsKeywordsForSiteLiveRequestInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="domain or page. required field. the domain name of the target website or the url of the target page;. note: to obtain keywords for the target website, use the target_type parameter")
    target_type: Optional[StrictStr] = Field(default=None, description="search keywords for site or for url. optional field. possible values: site, page;. default value: page;. if set to site, keywords will be provided for the entire site;. if set to page, keywords will be provided for the specified webpage")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location. optional field. if you do not indicate the location, you will receive worldwide results, i.e., for all available locations;. if you use this field, you don’t need to specify location_code or location_coordinate. you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/locations. example:. London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code. optional field. if you do not indicate the location, you will receive worldwide results, i.e., for all available locations;. if you use this field, you don’t need to specify location_name or location_coordinate;. you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/locations. example:. 2840")
    location_coordinate: Optional[StrictStr] = Field(default=None, description="GPS coordinates of a location. optional field. if you do not indicate the location, you will receive worldwide results, i.e., for all available locations;. if you use this field, you don’t need to specify location_name or location_code;. location_coordinate parameter should be specified in the “latitude,longitude” format;. the data will be provided for the country the specified coordinates belong to;. example:. 52.6178549,-155.352142")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language. optional field. you can receive the list of available languages of the search engine with their language_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code. optional field. you can receive the list of available languages of the search engine with their language_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/languages. example:. en")
    search_partners: Optional[StrictBool] = Field(default=None, description="include Google search partners. optional field. if you specify true, the results will be delivered for owned, operated, and syndicated networks across Google and partner sites that host Google search;. default value: false – results are returned for Google search sites")
    date_from: Optional[StrictStr] = Field(default=None, description="starting date of the time range. optional field. date format: 'yyyy-mm-dd'. minimal value: 4 years from the current date. by default, data is returned for the past 12 months;. Note: the indicated date cannot be greater than that specified in date_to and/or yesterday’s date;if Status endpoint returns false in the actual_data field, date_from can be set to the month before last and prior;. if Status endpoint returns true in the actual_data field, date_from can be set to the last month and prior")
    date_to: Optional[StrictStr] = Field(default=None, description="ending date of the time range. optional field. Note: the indicated date cannot be greater than yesterday’s date;. if you don’t specify this field, yesterday’s date will be used by default. date format: 'yyyy-mm-dd'. example:. '2022-11-30'")
    include_adult_keywords: Optional[StrictBool] = Field(default=None, description="include keywords associated with adult content. optional field. if set to true, adult keywords will be included in the response. default value: false. note that the API may return no data for such keywords due to Google Ads restrictions")
    sort_by: Optional[StrictStr] = Field(default=None, description="results sorting parameters. optional field. Use these parameters to sort the results by relevance, search_volume, competition_index, low_top_of_page_bid, or high_top_of_page_bid in descending order. default value: relevance")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "target", 
        "target_type", 
        "location_name", 
        "location_code", 
        "location_coordinate", 
        "language_name", 
        "language_code", 
        "search_partners", 
        "date_from", 
        "date_to", 
        "include_adult_keywords", 
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

        _dict['target'] = self.target
        _dict['target_type'] = self.target_type
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['location_coordinate'] = self.location_coordinate
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['search_partners'] = self.search_partners
        _dict['date_from'] = self.date_from
        _dict['date_to'] = self.date_to
        _dict['include_adult_keywords'] = self.include_adult_keywords
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
            "target": obj.get("target"),
            "target_type": obj.get("target_type"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "location_coordinate": obj.get("location_coordinate"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "search_partners": obj.get("search_partners"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "include_adult_keywords": obj.get("include_adult_keywords"),
            "sort_by": obj.get("sort_by"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj