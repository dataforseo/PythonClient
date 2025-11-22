from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.serp_api_stop_crawl_on_match_info import SerpApiStopCrawlOnMatchInfo



class SerpNaverOrganicTaskPostRequestInfo(BaseModel):
    """
    SerpNaverOrganicTaskPostRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description=r"keyword. required field. you can specify up to 700 characters in the keyword field. all %## will be decoded (plus character ‘+’ will be decoded to a space character). if you need to use the “%” character for your keyword, please specify it as “%25”;. if you need to use the “+” character for your keyword, please specify it as “%2B”. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    url: Optional[StrictStr] = Field(default=None, description=r"direct URL of the search query. optional field. you can specify a direct URL and we will sort it out to the necessary fields. in most cases, we wouldn’t recommend using this method;. example:. https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=iphone")
    priority: Optional[StrictInt] = Field(default=None, description=r"task priority. optional field. can take the following values:. 1 – normal execution priority (set by default). 2 – high execution priority. You will be additionally charged for the tasks with high execution priority.. The cost can be calculated on the Pricing page.")
    depth: Optional[StrictInt] = Field(default=None, description=r"parsing depth. optional field. number of results in SERP. default value: 15. max value: 700. Your account will be billed per each SERP containing up to 15 results;. Setting depth above 15 may result in additional charges if the search engine returns more than 15 results;. The cost can be calculated on the Pricing page.")
    max_crawl_pages: Optional[StrictInt] = Field(default=None, description=r"page crawl limit. optional field. number of search results pages to crawl. default value: 1. max value: 100. Note: the max_crawl_pages and depth parameters complement each other;. learn more at our help center")
    device: Optional[StrictStr] = Field(default=None, description=r"device type. optional field. can take the values:desktop, mobile. default value: desktop")
    os: Optional[StrictStr] = Field(default=None, description=r"device operating system. optional field. if you specify desktop in the device field, choose from the following values: windows, macos. default value: windows. if you specify mobile in the device field, choose from the following values: android, ios. default value: android")
    se_domain: Optional[StrictStr] = Field(default=None, description=r"search engine domain. optional field. we choose the relevant search engine domain automatically. however, you can set a custom search engine domain in this field. example:. search.naver.com")
    search_param: Optional[StrictStr] = Field(default=None, description=r"additional parameters of the search query. optional field. get the list of available parameters and additional details here")
    stop_crawl_on_match: Optional[List[Optional[SerpApiStopCrawlOnMatchInfo]]] = Field(default=None, description=r"array of targets to stop crawling. optional field. if specified, the response will contain SERP results up to and including the specified match_value;. you can specify up to 10 target values in this array. example:. 'stop_crawl_on_match':[{'match_value':'dataforseo.com','match_type':'with_subdomains'}]. learn more about this parameter on our Help Center - https://dataforseo.com/help-center/using-the-stop_crawl_on_match-parameter-in-serp-api. Your account will be billed per each SERP crawled through the specified targets")
    match_value: Optional[StrictStr] = Field(default=None, description=r"target domain or wildcard value. required field if stop_crawl_on_match is specified;. specify a target domain or wildcard value;. Note: domain name must be specified without a request protocol;. example: dataforseo.com")
    match_type: Optional[StrictStr] = Field(default=None, description=r"target match type. required field if stop_crawl_on_match is specified;. type of match for the match_value. possible values: domain, with_subdomains, wildcard")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    postback_url: Optional[StrictStr] = Field(default=None, description=r"return URL for sending task results. optional field. once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.. example:. http://your-server.com/postbackscript?id=$id. http://your-server.com/postbackscript?id=$id&tag=$tag. Note: special characters in postback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    postback_data: Optional[StrictStr] = Field(default=None, description=r"postback_url datatype. required field if you specify postback_url. corresponds to the function you used for setting a task. possible values:. regular, advanced, html")
    pingback_url: Optional[StrictStr] = Field(default=None, description=r"notification URL of a completed task. optional field. when a task is completed we will notify you by GET request sent to the URL you have specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.. example:. http://your-server.com/pingscript?id=$id. http://your-server.com/pingscript?id=$id&tag=$tag. Note: special characters in pingback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "url", 
        "priority", 
        "depth", 
        "max_crawl_pages", 
        "device", 
        "os", 
        "se_domain", 
        "search_param", 
        "stop_crawl_on_match", 
        "match_value", 
        "match_type", 
        "tag", 
        "postback_url", 
        "postback_data", 
        "pingback_url", 
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

        _dict['keyword'] = self.keyword
        _dict['url'] = self.url
        _dict['priority'] = self.priority
        _dict['depth'] = self.depth
        _dict['max_crawl_pages'] = self.max_crawl_pages
        _dict['device'] = self.device
        _dict['os'] = self.os
        _dict['se_domain'] = self.se_domain
        _dict['search_param'] = self.search_param
        stop_crawl_on_match_items = []
        if self.stop_crawl_on_match:
            for _item in self.stop_crawl_on_match:
                if _item:
                    stop_crawl_on_match_items.append(_item.to_dict())
            _dict['stop_crawl_on_match'] = stop_crawl_on_match_items
        _dict['match_value'] = self.match_value
        _dict['match_type'] = self.match_type
        _dict['tag'] = self.tag
        _dict['postback_url'] = self.postback_url
        _dict['postback_data'] = self.postback_data
        _dict['pingback_url'] = self.pingback_url
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "url": obj.get("url"),
            "priority": obj.get("priority"),
            "depth": obj.get("depth"),
            "max_crawl_pages": obj.get("max_crawl_pages"),
            "device": obj.get("device"),
            "os": obj.get("os"),
            "se_domain": obj.get("se_domain"),
            "search_param": obj.get("search_param"),
            "stop_crawl_on_match": [SerpApiStopCrawlOnMatchInfo.from_dict(_item) for _item in obj["stop_crawl_on_match"]] if obj.get("stop_crawl_on_match") is not None else None,
            "match_value": obj.get("match_value"),
            "match_type": obj.get("match_type"),
            "tag": obj.get("tag"),
            "postback_url": obj.get("postback_url"),
            "postback_data": obj.get("postback_data"),
            "pingback_url": obj.get("pingback_url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj