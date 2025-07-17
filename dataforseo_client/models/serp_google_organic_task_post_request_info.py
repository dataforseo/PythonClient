from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpGoogleOrganicTaskPostRequestInfo(BaseModel):
    """
    SerpGoogleOrganicTaskPostRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword. required field. you can specify up to 700 characters in the keyword field. all %## will be decoded (plus character ‘+’ will be decoded to a space character). if you need to use the “%” character for your keyword, please specify it as “%25”;. if you need to use the “+” character for your keyword, please specify it as “%2B”;. if this field contains such parameters as ‘allinanchor:’, ‘allintext:’, ‘allintitle:’, ‘allinurl:’, ‘define:’, ‘filetype:’, ‘id:’, ‘inanchor:’, ‘info:’, ‘intext:’, ‘intitle:’, ‘inurl:’, ‘link:’, ‘site:’, the charge per task will be multiplied by 5. Note: queries containing the ‘cache:’ parameter are not supported and will return a validation error. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    url: Optional[StrictStr] = Field(default=None, description="direct URL of the search query. optional field. you can specify a direct URL and we will sort it out to the necessary fields. Note that this method is the most difficult for our API to process and also requires you to specify the exact language and location in the URL. In most cases, we wouldn’t recommend using this method.. example:. https://www.google.co.uk/search?q=%20rank%20tracker%20api&hl=en&gl=GB&uule=w+CAIQIFISCXXeIa8LoNhHEZkq1d1aOpZS")
    priority: Optional[StrictInt] = Field(default=None, description="task priority. optional field. can take the following values:. 1 – normal execution priority (set by default);. 2 – high execution priority. You will be additionally charged for the tasks with high execution priority;. The cost can be calculated on the Pricing page")
    depth: Optional[StrictInt] = Field(default=None, description="parsing depth. optional field. number of results in SERP. default value: 100. max value: 700. Note: your account will be billed per each SERP containing up to 100 results;. thus, setting a depth above 100 may result in additional charges if the search engine returns more than 100 results;. if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance")
    max_crawl_pages: Optional[StrictInt] = Field(default=None, description="page crawl limit. optional field. number of search results pages to crawl. max value: 100. Note: the max_crawl_pages and depth parameters complement each other;. learn more at our help center")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location. required field if you don’t specify location_code or location_coordinate. if you use this field, you don’t need to specify location_code or location_coordinate. you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/locations. example:. London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code. required field if you don’t specify location_name or location_coordinate. if you use this field, you don’t need to specify location_name or location_coordinate. you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/locations. example:. 2840")
    location_coordinate: Optional[StrictStr] = Field(default=None, description="GPS coordinates of a location. required field if you don’t specify location_name or location_code. if you use this field, you don’t need to specify location_name or location_code. location_coordinate parameter should be specified in the “latitude,longitude,radius” format. the maximum number of decimal digits for “latitude” and “longitude”: 7. the minimum value for “radius”: 199.9 (mm). the maximum value for “radius”: 199999 (mm). example:. 53.476225,-2.243572,200")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language. required field if you don’t specify language_code. if you use this field, you don’t need to specify language_code. you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code. required field if you don’t specify language_name. if you use this field, you don’t need to specify language_name. you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages. example:. en")
    se_domain: Optional[StrictStr] = Field(default=None, description="search engine domain. optional field. we choose the relevant search engine domain automatically according to the location and language you specify. however, you can set a custom search engine domain in this field. example:. google.co.uk, google.com.au, google.de, etc.")
    device: Optional[StrictStr] = Field(default=None, description="device type. optional field. can take the values:desktop, mobile. default value: desktop")
    os: Optional[StrictStr] = Field(default=None, description="device operating system. optional field. if you specify desktop in the device field, choose from the following values: windows, macos. default value: windows. if you specify mobile in the device field, choose from the following values: android, ios. default value: android")
    group_organic_results: Optional[StrictBool] = Field(default=None, description="display related results. optional field. if set to true, the related_result element in the response will be provided as a snippet of its parent organic result;. if set to false, the related_result element will be provided as a separate organic result;. default value: true")
    calculate_rectangles: Optional[StrictBool] = Field(default=None, description="calcualte pixel rankings for SERP elements in advanced results. optional field. pixel ranking refers to the distance between the result snippet and top left corner of the screen;. Visit Help Center to learn more>>. by default, the parameter is set to false. Note: if set to true, the charge per task will be multiplied by 2")
    browser_screen_width: Optional[StrictInt] = Field(default=None, description="browser screen width. optional field. you can set a custom browser screen width to calculate pixel rankings for a particular device;. by default, the parameter is set to:. 1920 for desktop;. 360 for mobile on android;. 375 for mobile on iOS;. Note: to use this parameter, set calculate_rectangles to true")
    browser_screen_height: Optional[StrictInt] = Field(default=None, description="browser screen height. optional field. you can set a custom browser screen height to calculate pixel rankings for a particular device;. by default, the parameter is set to:. 1080 for desktop;. 640 for mobile on android;. 812 for mobile on iOS;. Note: to use this parameter, set calculate_rectangles to true")
    browser_screen_resolution_ratio: Optional[StrictInt] = Field(default=None, description="browser screen resolution ratio. optional field. you can set a custom browser screen resolution ratio to calculate pixel rankings for a particular device;. by default, the parameter is set to:. 1 for desktop;. 3 for mobile on android;. 3 for mobile on iOS;. Note: to use this parameter, set calculate_rectangles to true")
    people_also_ask_click_depth: Optional[StrictInt] = Field(default=None, description="clicks on the corresponding element. optional field. specify the click depth on the people_also_ask element to get additional people_also_ask_element items;. Note your account will be billed $0.00015 extra for each click regardless of task priority;. if the element is absent or we perform fewer clicks than you specified, all extra charges will be returned to your account balance. possible values: from 1 to 4")
    load_async_ai_overview: Optional[StrictBool] = Field(default=None, description="load asynchronous ai overview. optional field. set to true to obtain ai_overview items is SERPs even if they are loaded asynchronically;. if set to false, you will only obtain ai_overview items from cache;. default value: false. Note your account will be billed $0.0006-$0.0012 extra for each request, depending on the priority;. if the element is absent or contains 'asynchronous_ai_overview': false, all extra charges will be returned to your account balance")
    expand_ai_overview: Optional[StrictBool] = Field(default=None, description="expand ai overview. optional field. set to true to expand the ai_overview item;. default value: false;. Note: this parameter applies only to HTML task results")
    search_param: Optional[StrictStr] = Field(default=None, description="additional parameters of the search query. optional field. get the list of available parameters and additional details here")
    remove_from_url: Optional[List[Optional[StrictStr]]] = Field(default=None, description="remove specific parameters from URLs. optional field. using this field, you can specify up to 10 parameters to remove from URLs in the result. example:. 'remove_from_url': ['srsltid']. Note: if the target field is specified, the specified URL parameters will be removed before the search")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    postback_url: Optional[StrictStr] = Field(default=None, description="return URL for sending task results. optional field. once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example:. http://your-server.com/postbackscript?id=$id. http://your-server.com/postbackscript?id=$id&tag=$tag. Note: special characters in postback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    postback_data: Optional[StrictStr] = Field(default=None, description="postback_url datatype. required field if you specify postback_url. corresponds to the datatype that will be sent to your server. possible values:. regular, advanced, html")
    pingback_url: Optional[StrictStr] = Field(default=None, description="notification URL of a completed task. optional field. when a task is completed we will notify you by GET request sent to the URL you have specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.. example:. http://your-server.com/pingscript?id=$id. http://your-server.com/pingscript?id=$id&tag=$tag. Note: special characters in pingback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "url", 
        "priority", 
        "depth", 
        "max_crawl_pages", 
        "location_name", 
        "location_code", 
        "location_coordinate", 
        "language_name", 
        "language_code", 
        "se_domain", 
        "device", 
        "os", 
        "group_organic_results", 
        "calculate_rectangles", 
        "browser_screen_width", 
        "browser_screen_height", 
        "browser_screen_resolution_ratio", 
        "people_also_ask_click_depth", 
        "load_async_ai_overview", 
        "expand_ai_overview", 
        "search_param", 
        "remove_from_url", 
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
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['location_coordinate'] = self.location_coordinate
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['se_domain'] = self.se_domain
        _dict['device'] = self.device
        _dict['os'] = self.os
        _dict['group_organic_results'] = self.group_organic_results
        _dict['calculate_rectangles'] = self.calculate_rectangles
        _dict['browser_screen_width'] = self.browser_screen_width
        _dict['browser_screen_height'] = self.browser_screen_height
        _dict['browser_screen_resolution_ratio'] = self.browser_screen_resolution_ratio
        _dict['people_also_ask_click_depth'] = self.people_also_ask_click_depth
        _dict['load_async_ai_overview'] = self.load_async_ai_overview
        _dict['expand_ai_overview'] = self.expand_ai_overview
        _dict['search_param'] = self.search_param
        _dict['remove_from_url'] = self.remove_from_url
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
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "location_coordinate": obj.get("location_coordinate"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "se_domain": obj.get("se_domain"),
            "device": obj.get("device"),
            "os": obj.get("os"),
            "group_organic_results": obj.get("group_organic_results"),
            "calculate_rectangles": obj.get("calculate_rectangles"),
            "browser_screen_width": obj.get("browser_screen_width"),
            "browser_screen_height": obj.get("browser_screen_height"),
            "browser_screen_resolution_ratio": obj.get("browser_screen_resolution_ratio"),
            "people_also_ask_click_depth": obj.get("people_also_ask_click_depth"),
            "load_async_ai_overview": obj.get("load_async_ai_overview"),
            "expand_ai_overview": obj.get("expand_ai_overview"),
            "search_param": obj.get("search_param"),
            "remove_from_url": obj.get("remove_from_url"),
            "tag": obj.get("tag"),
            "postback_url": obj.get("postback_url"),
            "postback_data": obj.get("postback_data"),
            "pingback_url": obj.get("pingback_url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj