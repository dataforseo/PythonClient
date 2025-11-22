from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.serp_api_stop_crawl_on_match_info import SerpApiStopCrawlOnMatchInfo



class SerpBingOrganicLiveRegularRequestInfo(BaseModel):
    """
    SerpBingOrganicLiveRegularRequestInfo
    """ # noqa: E501
    url: Optional[StrictStr] = Field(default=None, description=r"direct URL of the search query. optional field. you can specify a direct URL and we will sort it out to the necessary fields. Note that this method is the most difficult for our API to process and also requires you to specify the exact language and location in the URL. In most cases, we wouldn’t recommend using this method.. example:. https://www.bing.com/search?q=rank%20checker&count=50&first=1&setlang=en&cc=US&safesearch=Moderate&FORM=SEPAGE")
    keyword: Optional[StrictStr] = Field(default=None, description=r"keyword. required field. you can specify up to 700 characters in the keyword field. all %## will be decoded (plus character ‘+’ will be decoded to a space character). if you need to use the “%” character for your keyword, please specify it as “%25”;. if you need to use the “+” character for your keyword, please specify it as “%2B”;. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine location. required field if you don’t specify location_code or location_coordinate. if you use this field, you don’t need to specify location_code or location_coordinate. you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/bing/locations. example:. London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description=r"search engine location code. required field if you don’t specify location_name or location_coordinate. if you use this field, you don’t need to specify location_name or location_coordinate. you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/bing/locations. example:. 2840")
    location_coordinate: Optional[StrictStr] = Field(default=None, description=r"GPS coordinates of a location. required field if you don’t specify location_name or location_code. if you use this field, you don’t need to specify location_name or location_code. location_coordinate parameter should be specified in the “latitude,longitude” format. the maximum number of decimal digits for “latitude” and “longitude”: 7. example:. 53.476225,-2.243572")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine language. required field if you don’t specify language_code. if you use this field, you don’t need to specify language_code. you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/bing/languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search engine language code. required field if you don’t specify language_name. if you use this field, you don’t need to specify language_name. you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/bing/languages. example:. en")
    device: Optional[StrictStr] = Field(default=None, description=r"device type. optional field. can take the values:desktop, mobile. default value: desktop")
    os: Optional[StrictStr] = Field(default=None, description=r"device operating system. optional field. if you specify desktop in the device field, choose from the following values: windows, macos. default value: windows. if you specify mobile in the device field, choose from the following values: android, ios. default value: android")
    depth: Optional[StrictInt] = Field(default=None, description=r"parsing depth. optional field. number of results in SERP. default value: 10. max value: 200. Your account will be billed per each SERP containing up to 10 results;. Setting depth above 10 may result in additional charges if the search engine returns more than 10 results;. The cost can be calculated on the Pricing page.")
    max_crawl_pages: Optional[StrictInt] = Field(default=None, description=r"page crawl limit. optional field. number of search results pages to crawl. default value: 1. max value: 100. Note: the max_crawl_pages and depth parameters complement each other;. learn more at our help center")
    target: Optional[StrictStr] = Field(default=None, description=r"target domain, subdomain, or webpage to get results for. optional field. a domain or a subdomain should be specified without https:// and www.. note that the results of target-specific tasks will only include SERP elements that contain a url string;. you can also use a wildcard (‘*’) character to specify the search pattern in SERP and narrow down the results;. examples:. example.com – returns results for the website’s home page with URLs, such as https://example.com, or https://www.example.com/, or https://example.com/;. example.com* – returns results for the domain, including all its pages;. *example.com* – returns results for the entire domain, including all its pages and subdomains;. *example.com  – returns results for the home page regardless of the subdomain, such as https://en.example.com;. example.com/example-page – returns results for the exact URL;. example.com/example-page* – returns results for all domain’s URLs that start with the specified string")
    stop_crawl_on_match: Optional[List[Optional[SerpApiStopCrawlOnMatchInfo]]] = Field(default=None, description=r"array of targets to stop crawling. optional field. if specified, the response will contain SERP results up to and including the specified match_value;. you can specify up to 10 target values in this array. example:. 'stop_crawl_on_match':[{'match_value':'dataforseo.com','match_type':'with_subdomains'}]. learn more about this parameter on our Help Center - https://dataforseo.com/help-center/using-the-stop_crawl_on_match-parameter-in-serp-api. Your account will be billed per each SERP crawled through the specified targets")
    match_value: Optional[StrictStr] = Field(default=None, description=r"target domain or wildcard value. required field if stop_crawl_on_match is specified;. specify a target domain or wildcard value;. Note: domain name must be specified without a request protocol;. example: dataforseo.com")
    match_type: Optional[StrictStr] = Field(default=None, description=r"target match type. required field if stop_crawl_on_match is specified;. type of match for the match_value. possible values: domain, with_subdomains, wildcard")
    search_param: Optional[StrictStr] = Field(default=None, description=r"additional parameters of the search query. optional field. get the list of available parameters and additional details here")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "url", 
        "keyword", 
        "location_name", 
        "location_code", 
        "location_coordinate", 
        "language_name", 
        "language_code", 
        "device", 
        "os", 
        "depth", 
        "max_crawl_pages", 
        "target", 
        "stop_crawl_on_match", 
        "match_value", 
        "match_type", 
        "search_param", 
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

        _dict['url'] = self.url
        _dict['keyword'] = self.keyword
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['location_coordinate'] = self.location_coordinate
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['device'] = self.device
        _dict['os'] = self.os
        _dict['depth'] = self.depth
        _dict['max_crawl_pages'] = self.max_crawl_pages
        _dict['target'] = self.target
        stop_crawl_on_match_items = []
        if self.stop_crawl_on_match:
            for _item in self.stop_crawl_on_match:
                if _item:
                    stop_crawl_on_match_items.append(_item.to_dict())
            _dict['stop_crawl_on_match'] = stop_crawl_on_match_items
        _dict['match_value'] = self.match_value
        _dict['match_type'] = self.match_type
        _dict['search_param'] = self.search_param
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "keyword": obj.get("keyword"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "location_coordinate": obj.get("location_coordinate"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "device": obj.get("device"),
            "os": obj.get("os"),
            "depth": obj.get("depth"),
            "max_crawl_pages": obj.get("max_crawl_pages"),
            "target": obj.get("target"),
            "stop_crawl_on_match": [SerpApiStopCrawlOnMatchInfo.from_dict(_item) for _item in obj["stop_crawl_on_match"]] if obj.get("stop_crawl_on_match") is not None else None,
            "match_value": obj.get("match_value"),
            "match_type": obj.get("match_type"),
            "search_param": obj.get("search_param"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj