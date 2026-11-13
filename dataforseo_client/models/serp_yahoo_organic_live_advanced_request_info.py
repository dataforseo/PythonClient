from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpYahooOrganicLiveAdvancedRequestInfo(BaseModel):
    """
    SerpYahooOrganicLiveAdvancedRequestInfo
    """ # noqa: E501
    url: Optional[StrictStr] = Field(default=None, description=r"direct URL of the search queryoptional fieldyou can specify a direct URL and we will sort it out to the necessary fields. Note that this method is the most difficult for our API to process and also requires you to specify the exact language and location in the URL. In most cases, we wouldn’t recommend using this method.example:https://search.yahoo.com/search?p=rank+checker&n=100&vl=lang_en&vc=us&ei=UTF-8")
    keyword: Optional[StrictStr] = Field(default=None, description=r"keywordrequired fieldyou can specify up to 700 characters in the keyword fieldall %## will be decoded (plus character '+' will be decoded to a space character)if you need to use the '%' character for your keyword, please specify it as '%25';if you need to use the “+” character for your keyword, please specify it as “%2B”learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine locationrequired field if you don't specify location_code or location_coordinateif you use this field, you don't need to specify location_code or location_coordinateyou can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/yahoo/locationsexample:London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description=r"search engine location coderequired field if you don't specify location_name_or location_coordinateif you use this field, you don't need to specify location_name or location_coordinateyou can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/yahoo/locationsexample:2840n")
    location_coordinate: Optional[StrictStr] = Field(default=None, description=r"GPS coordinates of a locationrequired field if you don't specify location_name_or location_codeif you use this field, you don't need to specify location_name or location_codelocation_coordinate parameter should be specified in the 'latitude,longitude,radius' formatthe maximum number of decimal digits for 'latitude' and 'longitude': 7the minimum value for 'radius': 199.9 (mm)the maximum value for 'radius': 199999 (mm)example:53.476225,-2.243572,200n")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine languagerequired field if you don't specify language_codeif you use this field, you don't need to specify language_codeyou can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/yahoo/languagesexample:English")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search engine language coderequired field if you don't specify language_nameif you use this field, you don't need to specify language_nameyou can receive the list of available languages of the search engine with their language_code_by making a separate request to the https://api.dataforseo.com/v3/serp/yahoo/languagesexample:enn")
    device: Optional[StrictStr] = Field(default=None, description=r"device typeoptional fieldreturn results for a specific device typecan take the values:desktop, mobiledefault value: desktop")
    os: Optional[StrictStr] = Field(default=None, description=r"device operating systemoptional fieldif you specify desktop in the device field, choose from the following values: windows, macosdefault value: windowsif you specify mobile in the device field, choose from the following values: android, iosdefault value: android")
    se_domain: Optional[StrictStr] = Field(default=None, description=r"search engine domainoptional fieldwe choose the relevant search engine domain automatically according to the location and language you specifyhowever, you can set a custom search engine domain in this fieldexample:au.search.yahoo.com, uk.search.yahoo.com, ca.search.yahoo.com, etc.")
    depth: Optional[StrictInt] = Field(default=None, description=r"parsing depthoptional fieldnumber of results in SERPdefault value: 6max value: 200Your account will be billed per each SERP; Each Yahoo SERP can contain fewer than 10 results, so setting depth above the default value may result in additional charges ;The cost can be calculated on the Pricing page.")
    max_crawl_pages: Optional[StrictInt] = Field(default=None, description=r"page crawl limitoptional fieldnumber of search results pages to crawldefault value: 1max value: 100Note: the max_crawl_pages and depth parameters complement each other;learn more at our help center")
    target: Optional[StrictStr] = Field(default=None, description=r"target domain, subdomain, or webpage to get results foroptional fielda domain or a subdomain should be specified without https:// and www.note that the results of target-specific tasks will only include SERP elements that contain a url string;you can also use a wildcard (‘’) character to specify the search pattern in SERP and narrow down the results;examples:example.com  - returns results for the website's home page with URLs, such as https://example.com, or https://www.example.com/, or https://example.com/;example.com - returns results for the domain, including all its pages;example.com - returns results for the entire domain, including all its pages and subdomains;example.com  - returns results for the home page regardless of the subdomain, such as https://en.example.com; example.com/example-page  - returns results for the exact URL;example.com/example-page  - returns results for all domain's URLs that start with the specified string")
    search_param: Optional[StrictStr] = Field(default=None, description=r"additional parameters of the search queryoptional fieldget the list of available parameters and additional details here")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response")
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
        "se_domain", 
        "depth", 
        "max_crawl_pages", 
        "target", 
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
        _dict['se_domain'] = self.se_domain
        _dict['depth'] = self.depth
        _dict['max_crawl_pages'] = self.max_crawl_pages
        _dict['target'] = self.target
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
            "se_domain": obj.get("se_domain"),
            "depth": obj.get("depth"),
            "max_crawl_pages": obj.get("max_crawl_pages"),
            "target": obj.get("target"),
            "search_param": obj.get("search_param"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj