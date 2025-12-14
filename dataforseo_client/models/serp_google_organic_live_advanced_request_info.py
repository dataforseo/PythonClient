from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.serp_api_stop_crawl_on_match_info import SerpApiStopCrawlOnMatchInfo



class SerpGoogleOrganicLiveAdvancedRequestInfo(BaseModel):
    """
    SerpGoogleOrganicLiveAdvancedRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description=r"keyword. required field. you can specify up to 700 characters in the keyword field. all %## will be decoded (plus character ‘+’ will be decoded to a space character). if you need to use the “%” character for your keyword, please specify it as “%25”;. if you need to use the “+” character for your keyword, please specify it as “%2B”;. if this field contains such parameters as ‘allinanchor:’, ‘allintext:’, ‘allintitle:’, ‘allinurl:’, ‘define:’, ‘definition:’, ‘filetype:’, ‘id:’, ‘inanchor:’, ‘info:’, ‘intext:’, ‘intitle:’, ‘inurl:’, ‘link:’, ‘site:’, the charge per task will be multiplied by 5. Note: queries containing the ‘cache:’ parameter are not supported and will return a validation errorlearn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_code: Optional[StrictInt] = Field(default=None, description=r"search engine location code. required field if you don't specify location_name or location_coordinate. if you use this field, you don't need to specify location_name or location_coordinate. you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/{{low_se_name}}/locations. example:. 2840")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search engine language code. optional field if you specify language_name. if you use this field, you don't need to specify language_name. you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/{{low_se_name}}/languages. example:. en")
    depth: Optional[StrictInt] = Field(default=None, description=r"parsing depth. optional field. number of results in SERP. default value: 10. max value: 200. Your account will be billed per each SERP containing up to 10 results;. Setting depth above 10 may result in additional charges if the search engine returns more than 10 results;. The cost can be calculated on the Pricing page.")
    device: Optional[StrictStr] = Field(default=None, description=r"device type. optional field. can take the values:desktop, mobile. default value: desktop")
    load_async_ai_overview: Optional[StrictBool] = Field(default=None, description=r"load asynchronous ai overview. optional field. set to true to obtain ai_overview items is SERPs even if they are loaded asynchronously;. if set to false, you will only obtain ai_overview items from cache;. default value: false. Note: you will be charged extra $0.002 for using this parameter;. if the element is absent or contains 'asynchronous_ai_overview': false, all extra charges will be returned to your account balance")
    location_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine location. required field if you don't specify location_code or location_coordinate. if you use this field, you don't need to specify location_code or location_coordinate. you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/{{low_se_name}}/locations. example:. London,England,United Kingdom")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine language. optional field if you specify language_code. if you use this field, you don't need to specify language_code. you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/{{low_se_name}}/languages. example:. English")
    os: Optional[StrictStr] = Field(default=None, description=r"device operating system. optional field. if you specify desktop in the device field, choose from the following values: windows, macos. default value: windows. if you specify mobile in the device field, choose from the following values: android, ios. default value: android")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    stop_crawl_on_match: Optional[List[Optional[SerpApiStopCrawlOnMatchInfo]]] = Field(default=None, description=r"array of targets to stop crawling. optional field. if specified, the response will contain SERP results up to and including the specified match_value;. you can specify up to 10 target values in this array. example:. 'stop_crawl_on_match':[{'match_value':'dataforseo.com','match_type':'with_subdomains'}]. learn more about this parameter on our Help Center - https://dataforseo.com/help-center/using-the-stop_crawl_on_match-parameter-in-serp-api. Your account will be billed per each SERP crawled through the specified targets")
    match_type: Optional[StrictStr] = Field(default=None, description=r"target match type. optional field. type of match for the match_value. possible values: domain, with_subdomains, wildcard")
    match_value: Optional[StrictStr] = Field(default=None, description=r"target domain or wildcard value. optional field. specify a target domain or wildcard value;. Note: domain name must be specified without a request protocol;. example: dataforseo.com")
    max_crawl_pages: Optional[StrictInt] = Field(default=None, description=r"page crawl limit. optional field. number of search results pages to crawl. max value: 100. Note: you will be charged for each page crawled (10 organic results per page);. learn more about pricing on our Pricing page;. Note#2: the max_crawl_pages and depth parameters complement each other;. learn more at our help center")
    search_param: Optional[StrictStr] = Field(default=None, description=r"additional parameters of the search query. optional field. get the list of available parameters and additional details here")
    remove_from_url: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"remove specific parameters from URLs. optional field. using this field, you can specify up to 10 parameters to remove from URLs in the result. example:. 'remove_from_url': ['srsltid']. Note: if the target field is specified, the specified URL parameters will be removed before the search")
    people_also_ask_click_depth: Optional[StrictInt] = Field(default=None, description=r"clicks on the corresponding element. optional field. specify the click depth on the people_also_ask element to get additional people_also_ask_element items;. Note your account will be billed $0.00015 extra for each click;. if the element is absent or we perform fewer clicks than you specified, all extra charges will be returned to your account balance. possible values: from 1 to 4")
    group_organic_results: Optional[StrictBool] = Field(default=None, description=r"display related results. optional field. if set to true, the related_result element in the response will be provided as a snippet of its parent organic result;. if set to false, the related_result element will be provided as a separate organic result;. default value: true")
    calculate_rectangles: Optional[StrictBool] = Field(default=None, description=r"calcualte pixel rankings for SERP elements in advanced results. optional field. pixel ranking refers to the distance between the result snippet and top left corner of the screen;. Visit Help Center to learn more>>. by default, the parameter is set to false;. Note: you will be charged extra $0.002 for using this parameter")
    browser_screen_width: Optional[StrictInt] = Field(default=None, description=r"browser screen width. optional field. you can set a custom browser screen width to calculate pixel rankings for a particular device;. by default, the parameter is set to:. 1920 for desktop;. 360 for mobile on android;. 375 for mobile on iOS;. Note: to use this parameter, set calculate_rectangles to true")
    browser_screen_height: Optional[StrictInt] = Field(default=None, description=r"browser screen height. optional field. you can set a custom browser screen height to calculate pixel rankings for a particular device;. by default, the parameter is set to:. 1080 for desktop;. 640 for mobile on android;. 812 for mobile on iOS;. Note: to use this parameter, set calculate_rectangles to true")
    browser_screen_resolution_ratio: Optional[StrictInt] = Field(default=None, description=r"browser screen resolution ratio. optional field. you can set a custom browser screen resolution ratio to calculate pixel rankings for a particular device;. possible values: from 1 to 3;. by default, the parameter is set to:. 1 for desktop;. 3 for mobile on android;. 3 for mobile on iOS;. Note: to use this parameter, set calculate_rectangles to true")
    url: Optional[StrictStr] = Field(default=None, description=r"direct URL of the search query. optional field. you can specify a direct URL and we will sort it out to the necessary fields. Note that this method is the most difficult for our API to process and also requires you to specify the exact language and location in the URL. In most cases, we wouldn’t recommend using this method.. example:. https://www.google.co.uk/search?q=%20rank%20tracker%20api&hl=en&gl=GB&uule=w+CAIQIFISCXXeIa8LoNhHEZkq1d1aOpZS")
    location_coordinate: Optional[StrictStr] = Field(default=None, description=r"GPS coordinates of a location. optional field if you specify location_name or location_code. if you use this field, you don't need to specify location_name or location_code. location_coordinate parameter should be specified in the 'latitude,longitude,radius' format. the maximum number of decimal digits for 'latitude' and 'longitude': 7. the minimum value for 'radius': 199.9 (mm). the maximum value for 'radius': 199999 (mm). example:. 53.476225,-2.243572,200")
    se_domain: Optional[StrictStr] = Field(default=None, description=r"search engine domain. optional field. we choose the relevant search engine domain automatically according to the location and language you specify. however, you can set a custom search engine domain in this field. example:. google.co.uk, google.com.au, google.de, etc.")
    target: Optional[StrictStr] = Field(default=None, description=r"target domain, subdomain, or webpage to get results for. optional field. a domain or a subdomain should be specified without https:// and www.. note that the results of target-specific tasks will only include SERP elements that contain a url string;. you can also use a wildcard (‘*’) character to specify the search pattern in SERP and narrow down the results;. examples:. example.com - returns results for the website's home page with URLs, such as https://example.com, or https://www.example.com/, or https://example.com/;. example.com* - returns results for the domain, including all its pages;. *example.com* - returns results for the entire domain, including all its pages and subdomains;. *example.com - returns results for the home page regardless of the subdomain, such as https://en.example.com;. example.com/example-page - returns results for the exact URL;. example.com/example-page* - returns results for all domain's URLs that start with the specified string")
    target_search_mode: Optional[StrictStr] = Field(default=None, description=r"target matching mode. optional field. to enable this parameter, stop_crawl_on_match must also be enabled. defines how the crawl should stop when multiple targets are specified in stop_crawl_on_match. possible values: all, any. all – the crawl stops only when all specified targets are found. any – the crawl stops when any single target is found. default value: any. learn more about this parameter on our Help Center")
    find_targets_in: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"SERP element types to check for targets. optional field. to enable this parameter, stop_crawl_on_match must also be enabled. specifies which SERP element types should be checked for target matches. if not specified, all first-level elements with url and domain fields are checked for targets. possible values: organic, paid, local_pack, featured_snippet, events, google_flights, images, jobs, knowledge_graph, local_service, map, scholarly_articles, third_party_reviews, twitter. Note: cannot contain the same element types as ignore_targets_in. example:. 'find_targets_in': ['organic', 'featured_snippet']. learn more about this parameter on our Help Center")
    ignore_targets_in: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"SERP element types to exclude from target search. optional field. to enable this parameter, stop_crawl_on_match must also be enabled. specifies which SERP element types should be excluded when searching for target matches. possible values: organic, paid, local_pack, featured_snippet, events, google_flights, images, jobs, knowledge_graph, local_service, map, scholarly_articles, third_party_reviews, twitter. Note: cannot contain the same element types as find_targets_in. example:. 'ignore_targets_in': ['paid', 'images']. learn more about this parameter on our Help Center")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_code", 
        "language_code", 
        "depth", 
        "device", 
        "load_async_ai_overview", 
        "location_name", 
        "language_name", 
        "os", 
        "tag", 
        "stop_crawl_on_match", 
        "match_type", 
        "match_value", 
        "max_crawl_pages", 
        "search_param", 
        "remove_from_url", 
        "people_also_ask_click_depth", 
        "group_organic_results", 
        "calculate_rectangles", 
        "browser_screen_width", 
        "browser_screen_height", 
        "browser_screen_resolution_ratio", 
        "url", 
        "location_coordinate", 
        "se_domain", 
        "target", 
        "target_search_mode", 
        "find_targets_in", 
        "ignore_targets_in", 
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
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['depth'] = self.depth
        _dict['device'] = self.device
        _dict['load_async_ai_overview'] = self.load_async_ai_overview
        _dict['location_name'] = self.location_name
        _dict['language_name'] = self.language_name
        _dict['os'] = self.os
        _dict['tag'] = self.tag
        stop_crawl_on_match_items = []
        if self.stop_crawl_on_match:
            for _item in self.stop_crawl_on_match:
                if _item:
                    stop_crawl_on_match_items.append(_item.to_dict())
            _dict['stop_crawl_on_match'] = stop_crawl_on_match_items
        _dict['match_type'] = self.match_type
        _dict['match_value'] = self.match_value
        _dict['max_crawl_pages'] = self.max_crawl_pages
        _dict['search_param'] = self.search_param
        _dict['remove_from_url'] = self.remove_from_url
        _dict['people_also_ask_click_depth'] = self.people_also_ask_click_depth
        _dict['group_organic_results'] = self.group_organic_results
        _dict['calculate_rectangles'] = self.calculate_rectangles
        _dict['browser_screen_width'] = self.browser_screen_width
        _dict['browser_screen_height'] = self.browser_screen_height
        _dict['browser_screen_resolution_ratio'] = self.browser_screen_resolution_ratio
        _dict['url'] = self.url
        _dict['location_coordinate'] = self.location_coordinate
        _dict['se_domain'] = self.se_domain
        _dict['target'] = self.target
        _dict['target_search_mode'] = self.target_search_mode
        _dict['find_targets_in'] = self.find_targets_in
        _dict['ignore_targets_in'] = self.ignore_targets_in
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "depth": obj.get("depth"),
            "device": obj.get("device"),
            "load_async_ai_overview": obj.get("load_async_ai_overview"),
            "location_name": obj.get("location_name"),
            "language_name": obj.get("language_name"),
            "os": obj.get("os"),
            "tag": obj.get("tag"),
            "stop_crawl_on_match": [SerpApiStopCrawlOnMatchInfo.from_dict(_item) for _item in obj["stop_crawl_on_match"]] if obj.get("stop_crawl_on_match") is not None else None,
            "match_type": obj.get("match_type"),
            "match_value": obj.get("match_value"),
            "max_crawl_pages": obj.get("max_crawl_pages"),
            "search_param": obj.get("search_param"),
            "remove_from_url": obj.get("remove_from_url"),
            "people_also_ask_click_depth": obj.get("people_also_ask_click_depth"),
            "group_organic_results": obj.get("group_organic_results"),
            "calculate_rectangles": obj.get("calculate_rectangles"),
            "browser_screen_width": obj.get("browser_screen_width"),
            "browser_screen_height": obj.get("browser_screen_height"),
            "browser_screen_resolution_ratio": obj.get("browser_screen_resolution_ratio"),
            "url": obj.get("url"),
            "location_coordinate": obj.get("location_coordinate"),
            "se_domain": obj.get("se_domain"),
            "target": obj.get("target"),
            "target_search_mode": obj.get("target_search_mode"),
            "find_targets_in": obj.get("find_targets_in"),
            "ignore_targets_in": obj.get("ignore_targets_in"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj