# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SerpGoogleOrganicTaskPostRequestInfo(BaseModel):
    """
    SerpGoogleOrganicTaskPostRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword required field you can specify up to 700 characters in the keyword field all %## will be decoded (plus character ‘+’ will be decoded to a space character) if you need to use the “%” character for your keyword, please specify it as “%25”; if you need to use the “+” character for your keyword, please specify it as “%2B”; if this field contains such parameters as ‘allinanchor:’, ‘allintext:’, ‘allintitle:’, ‘allinurl:’, ‘define:’, ‘filetype:’, ‘id:’, ‘inanchor:’, ‘info:’, ‘intext:’, ‘intitle:’, ‘inurl:’, ‘link:’, ‘site:’, the charge per task will be multiplied by 5 Note: queries containing the ‘cache:’ parameter are not supported and will return a validation error learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    url: Optional[StrictStr] = Field(default=None, description="direct URL of the search query optional field you can specify a direct URL and we will sort it out to the necessary fields. Note that this method is the most difficult for our API to process and also requires you to specify the exact language and location in the URL. In most cases, we wouldn’t recommend using this method. example: https://www.google.co.uk/search?q=%20rank%20tracker%20api&hl=en&gl=GB&uule=w+CAIQIFISCXXeIa8LoNhHEZkq1d1aOpZS")
    priority: Optional[StrictInt] = Field(default=None, description="task priority optional field can take the following values: 1 – normal execution priority (set by default); 2 – high execution priority You will be additionally charged for the tasks with high execution priority; The cost can be calculated on the Pricing page")
    depth: Optional[StrictInt] = Field(default=None, description="parsing depth optional field number of results in SERP default value: 100 max value: 700 Note: your account will be billed per each SERP containing up to 100 results; thus, setting a depth above 100 may result in additional charges if the search engine returns more than 100 results; if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance")
    max_crawl_pages: Optional[StrictInt] = Field(default=None, description="page crawl limit optional field number of search results pages to crawl max value: 100 Note: the max_crawl_pages and depth parameters complement each other; learn more at our help center")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/locations example: London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/locations example: 2840")
    location_coordinate: Optional[StrictStr] = Field(default=None, description="GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude,radius” format the maximum number of decimal digits for “latitude” and “longitude”: 7 the minimum value for “radius”: 199.9 (mm) the maximum value for “radius”: 199999 (mm) example: 53.476225,-2.243572,200")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages example: English")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages example: en")
    se_domain: Optional[StrictStr] = Field(default=None, description="search engine domain optional field we choose the relevant search engine domain automatically according to the location and language you specify however, you can set a custom search engine domain in this field example: google.co.uk, google.com.au, google.de, etc.")
    device: Optional[StrictStr] = Field(default=None, description="device type optional field can take the values:desktop, mobile default value: desktop")
    os: Optional[StrictStr] = Field(default=None, description="device operating system optional field if you specify desktop in the device field, choose from the following values: windows, macos default value: windows if you specify mobile in the device field, choose from the following values: android, ios default value: android")
    group_organic_results: Optional[StrictBool] = Field(default=None, description="display related results optional field if set to true, the related_result element in the response will be provided as a snippet of its parent organic result; if set to false, the related_result element will be provided as a separate organic result; default value: true")
    calculate_rectangles: Optional[StrictBool] = Field(default=None, description="calcualte pixel rankings for SERP elements in advanced results optional field pixel ranking refers to the distance between the result snippet and top left corner of the screen; Visit Help Center to learn more>> by default, the parameter is set to false Note: if set to true, the charge per task will be multiplied by 2")
    browser_screen_width: Optional[StrictInt] = Field(default=None, description="browser screen width optional field you can set a custom browser screen width to calculate pixel rankings for a particular device; by default, the parameter is set to: 1920 for desktop; 360 for mobile on android; 375 for mobile on iOS; Note: to use this parameter, set calculate_rectangles to true")
    browser_screen_height: Optional[StrictInt] = Field(default=None, description="browser screen height optional field you can set a custom browser screen height to calculate pixel rankings for a particular device; by default, the parameter is set to: 1080 for desktop; 640 for mobile on android; 812 for mobile on iOS; Note: to use this parameter, set calculate_rectangles to true")
    browser_screen_resolution_ratio: Optional[StrictInt] = Field(default=None, description="browser screen resolution ratio optional field you can set a custom browser screen resolution ratio to calculate pixel rankings for a particular device; by default, the parameter is set to: 1 for desktop; 3 for mobile on android; 3 for mobile on iOS; Note: to use this parameter, set calculate_rectangles to true")
    people_also_ask_click_depth: Optional[StrictInt] = Field(default=None, description="clicks on the corresponding element optional field specify the click depth on the people_also_ask element to get additional people_also_ask_element items; Note your account will be billed $0.00015 extra for each click regardless of task priority; if the element is absent or we perform fewer clicks than you specified, all extra charges will be returned to your account balance possible values: from 1 to 4")
    load_async_ai_overview: Optional[StrictBool] = Field(default=None, description="load asynchronous ai overview optional field set to true to obtain ai_overview items is SERPs even if they are loaded asynchronically; if set to false, you will only obtain ai_overview items from cache; default value: false Note your account will be billed $0.0006-$0.0012 extra for each request, depending on the priority; if the element is absent or contains \"asynchronous_ai_overview\": false, all extra charges will be returned to your account balance")
    expand_ai_overview: Optional[StrictBool] = Field(default=None, description="expand ai overview optional field set to true to expand the ai_overview item; default value: false; Note: this parameter applies only to HTML task results")
    search_param: Optional[StrictStr] = Field(default=None, description="additional parameters of the search query optional field get the list of available parameters and additional details here")
    remove_from_url: Optional[List[StrictStr]] = Field(default=None, description="remove specific parameters from URLs optional field using this field, you can specify up to 10 parameters to remove from URLs in the result example: \"remove_from_url\": [\"srsltid\"] Note: if the target field is specified, the specified URL parameters will be removed before the search")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response")
    postback_url: Optional[StrictStr] = Field(default=None, description="return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request example: http://your-server.com/postbackscript?id=$id http://your-server.com/postbackscript?id=$id&tag=$tag Note: special characters in postback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center")
    postback_data: Optional[StrictStr] = Field(default=None, description="postback_url datatype required field if you specify postback_url corresponds to the datatype that will be sent to your server possible values: regular, advanced, html")
    pingback_url: Optional[StrictStr] = Field(default=None, description="notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id=$id http://your-server.com/pingscript?id=$id&tag=$tag Note: special characters in pingback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center")
    __properties: ClassVar[List[str]] = ["keyword", "url", "priority", "depth", "max_crawl_pages", "location_name", "location_code", "location_coordinate", "language_name", "language_code", "se_domain", "device", "os", "group_organic_results", "calculate_rectangles", "browser_screen_width", "browser_screen_height", "browser_screen_resolution_ratio", "people_also_ask_click_depth", "load_async_ai_overview", "expand_ai_overview", "search_param", "remove_from_url", "tag", "postback_url", "postback_data", "pingback_url"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SerpGoogleOrganicTaskPostRequestInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if priority (nullable) is None
        # and model_fields_set contains the field
        if self.priority is None and "priority" in self.model_fields_set:
            _dict['priority'] = None

        # set to None if depth (nullable) is None
        # and model_fields_set contains the field
        if self.depth is None and "depth" in self.model_fields_set:
            _dict['depth'] = None

        # set to None if max_crawl_pages (nullable) is None
        # and model_fields_set contains the field
        if self.max_crawl_pages is None and "max_crawl_pages" in self.model_fields_set:
            _dict['max_crawl_pages'] = None

        # set to None if location_name (nullable) is None
        # and model_fields_set contains the field
        if self.location_name is None and "location_name" in self.model_fields_set:
            _dict['location_name'] = None

        # set to None if location_code (nullable) is None
        # and model_fields_set contains the field
        if self.location_code is None and "location_code" in self.model_fields_set:
            _dict['location_code'] = None

        # set to None if location_coordinate (nullable) is None
        # and model_fields_set contains the field
        if self.location_coordinate is None and "location_coordinate" in self.model_fields_set:
            _dict['location_coordinate'] = None

        # set to None if language_name (nullable) is None
        # and model_fields_set contains the field
        if self.language_name is None and "language_name" in self.model_fields_set:
            _dict['language_name'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if se_domain (nullable) is None
        # and model_fields_set contains the field
        if self.se_domain is None and "se_domain" in self.model_fields_set:
            _dict['se_domain'] = None

        # set to None if device (nullable) is None
        # and model_fields_set contains the field
        if self.device is None and "device" in self.model_fields_set:
            _dict['device'] = None

        # set to None if os (nullable) is None
        # and model_fields_set contains the field
        if self.os is None and "os" in self.model_fields_set:
            _dict['os'] = None

        # set to None if group_organic_results (nullable) is None
        # and model_fields_set contains the field
        if self.group_organic_results is None and "group_organic_results" in self.model_fields_set:
            _dict['group_organic_results'] = None

        # set to None if calculate_rectangles (nullable) is None
        # and model_fields_set contains the field
        if self.calculate_rectangles is None and "calculate_rectangles" in self.model_fields_set:
            _dict['calculate_rectangles'] = None

        # set to None if browser_screen_width (nullable) is None
        # and model_fields_set contains the field
        if self.browser_screen_width is None and "browser_screen_width" in self.model_fields_set:
            _dict['browser_screen_width'] = None

        # set to None if browser_screen_height (nullable) is None
        # and model_fields_set contains the field
        if self.browser_screen_height is None and "browser_screen_height" in self.model_fields_set:
            _dict['browser_screen_height'] = None

        # set to None if browser_screen_resolution_ratio (nullable) is None
        # and model_fields_set contains the field
        if self.browser_screen_resolution_ratio is None and "browser_screen_resolution_ratio" in self.model_fields_set:
            _dict['browser_screen_resolution_ratio'] = None

        # set to None if people_also_ask_click_depth (nullable) is None
        # and model_fields_set contains the field
        if self.people_also_ask_click_depth is None and "people_also_ask_click_depth" in self.model_fields_set:
            _dict['people_also_ask_click_depth'] = None

        # set to None if load_async_ai_overview (nullable) is None
        # and model_fields_set contains the field
        if self.load_async_ai_overview is None and "load_async_ai_overview" in self.model_fields_set:
            _dict['load_async_ai_overview'] = None

        # set to None if expand_ai_overview (nullable) is None
        # and model_fields_set contains the field
        if self.expand_ai_overview is None and "expand_ai_overview" in self.model_fields_set:
            _dict['expand_ai_overview'] = None

        # set to None if search_param (nullable) is None
        # and model_fields_set contains the field
        if self.search_param is None and "search_param" in self.model_fields_set:
            _dict['search_param'] = None

        # set to None if remove_from_url (nullable) is None
        # and model_fields_set contains the field
        if self.remove_from_url is None and "remove_from_url" in self.model_fields_set:
            _dict['remove_from_url'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        # set to None if postback_url (nullable) is None
        # and model_fields_set contains the field
        if self.postback_url is None and "postback_url" in self.model_fields_set:
            _dict['postback_url'] = None

        # set to None if postback_data (nullable) is None
        # and model_fields_set contains the field
        if self.postback_data is None and "postback_data" in self.model_fields_set:
            _dict['postback_data'] = None

        # set to None if pingback_url (nullable) is None
        # and model_fields_set contains the field
        if self.pingback_url is None and "pingback_url" in self.model_fields_set:
            _dict['pingback_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SerpGoogleOrganicTaskPostRequestInfo from a dict"""
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
            "pingback_url": obj.get("pingback_url")
        })
        return _obj


