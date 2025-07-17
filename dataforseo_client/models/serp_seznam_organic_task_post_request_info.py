from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpSeznamOrganicTaskPostRequestInfo(BaseModel):
    """
    SerpSeznamOrganicTaskPostRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword. required field. you can specify up to 700 characters in the keyword field. all %## will be decoded (plus character ‘+’ will be decoded to a space character). if you need to use the “%” character for your keyword, please specify it as “%25”;. if you need to use the “+” character for your keyword, please specify it as “%2B”. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location. required field if you don’t specify location_code. if you use this field, you don’t need to specify location_code. you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/seznam/locations. example:. London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code. required field if you don’t specify location_name. if you use this field, you don’t need to specify location_name. you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/seznam/locations. example:. 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language. required field if you don’t specify language_code. if you use this field, you don’t need to specify language_code. you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/seznam/languages. example:. Czech")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code. required field if you don’t specify language_name. if you use this field, you don’t need to specify language_name. you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/seznam/languages. example:. cs")
    url: Optional[StrictStr] = Field(default=None, description="direct URL of the search query. optional field. you can specify a direct URL and we will sort it out to the necessary fields;. note that this method is the most difficult for our API to process and also requires you to specify the exact language and location in the URL;. in most cases, we wouldn’t recommend using this method.")
    priority: Optional[StrictInt] = Field(default=None, description="task priority. optional field. can take the following values:. 1 – normal execution priority (set by default). 2 – high execution priority. You will be additionally charged for the tasks with high execution priority.. The cost can be calculated on the Pricing page.")
    depth: Optional[StrictInt] = Field(default=None, description="parsing depth. optional field. number of results in SERP. default value: 10;. maximum value: 500;. Note: your account will be billed per each SERP containing up to 10 results;. thus, setting a depth above 10 may result in additional charges if the search engine returns more than 10 results;. if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance")
    max_crawl_pages: Optional[StrictInt] = Field(default=None, description="page crawl limit. optional field. number of search results pages to crawl. max value: 10. Note: the max_crawl_pages and depth parameters complement each other;. learn more at our help center")
    device: Optional[StrictStr] = Field(default=None, description="device type. optional field. can take the values:desktop, mobile. default value: desktop")
    os: Optional[StrictStr] = Field(default=None, description="device operating system. optional field. if you specify desktop in the device field, choose from the following values: windows, macos. default value: windows. if you specify mobile in the device field, choose from the following values: android, ios. default value: android")
    se_domain: Optional[StrictStr] = Field(default=None, description="search engine domain. optional field. we choose the relevant search engine domain automatically. however, you can set a custom search engine domain in this field. example:. search.seznam.cz")
    search_param: Optional[StrictStr] = Field(default=None, description="additional parameters of the search query. optional field")
    calculate_rectangles: Optional[StrictBool] = Field(default=None, description="calcualte pixel rankings for SERP elements in advanced results. optional field. pixel ranking refers to the distance between the result snippet and top left corner of the screen;. Visit Help Center to learn more>>. by default, the parameter is set to false. Note: if set to true, the charge per task will be multiplied by 2")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    postback_url: Optional[StrictStr] = Field(default=None, description="return URL for sending task results. optional field. once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.. example:. http://your-server.com/postbackscript?id=$id. http://your-server.com/postbackscript?id=$id&tag=$tag. Note: special characters in postback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    postback_data: Optional[StrictStr] = Field(default=None, description="postback_url datatype. required field if you specify postback_url. corresponds to the function you used for setting a task. possible values:. regular, advanced, html")
    pingback_url: Optional[StrictStr] = Field(default=None, description="notification URL of a completed task. optional field. when a task is completed we will notify you by GET request sent to the URL you have specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.. example:. http://your-server.com/pingscript?id=$id. http://your-server.com/pingscript?id=$id&tag=$tag. Note: special characters in pingback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "url", 
        "priority", 
        "depth", 
        "max_crawl_pages", 
        "device", 
        "os", 
        "se_domain", 
        "search_param", 
        "calculate_rectangles", 
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
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['url'] = self.url
        _dict['priority'] = self.priority
        _dict['depth'] = self.depth
        _dict['max_crawl_pages'] = self.max_crawl_pages
        _dict['device'] = self.device
        _dict['os'] = self.os
        _dict['se_domain'] = self.se_domain
        _dict['search_param'] = self.search_param
        _dict['calculate_rectangles'] = self.calculate_rectangles
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
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "url": obj.get("url"),
            "priority": obj.get("priority"),
            "depth": obj.get("depth"),
            "max_crawl_pages": obj.get("max_crawl_pages"),
            "device": obj.get("device"),
            "os": obj.get("os"),
            "se_domain": obj.get("se_domain"),
            "search_param": obj.get("search_param"),
            "calculate_rectangles": obj.get("calculate_rectangles"),
            "tag": obj.get("tag"),
            "postback_url": obj.get("postback_url"),
            "postback_data": obj.get("postback_data"),
            "pingback_url": obj.get("pingback_url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj