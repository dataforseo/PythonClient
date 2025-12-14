from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpGoogleNewsLiveHtmlRequestInfo(BaseModel):
    """
    SerpGoogleNewsLiveHtmlRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description=r"keyword. required field. you can specify up to 700 characters in the keyword field. all %## will be decoded (plus character '+' will be decoded to a space character). if you need to use the '%' character for your keyword, please specify it as '%25';. if you need to use the “+” character for your keyword, please specify it as “%2B”;. if this field contains such parameters as 'allinanchor:', 'allintext:', 'allintitle:', 'allinurl:', 'define:', 'filetype:', 'id:', 'inanchor:', 'info:', 'intext:', 'intitle:', 'inurl:', 'link:', 'related:', 'site:', the charge per task will be multiplied by 5. Note: queries containing the ‘cache:’ parameter are not supported and will return a validation error. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_code: Optional[StrictInt] = Field(default=None, description=r"search engine location code. required field if you don't specify location_name or location_coordinate. if you use this field, you don't need to specify location_name or location_coordinate. you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/{{low_se_name}}/locations. example:. 2840")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search engine language code. required field if you don't specify language_name. if you use this field, you don't need to specify language_name. you can receive the list of available locations of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/{{low_se_name}}/languages. example:. en")
    depth: Optional[StrictInt] = Field(default=None, description=r"parsing depth. optional field. number of results in SERP. default value: 10. max value: 200. Your account will be billed per each SERP containing up to 10 results;. Setting depth above 10 may result in additional charges if the search engine returns more than 10 results;. If the specified depth is higher than the number of results in the response, the difference will be refunded to your account balance automatically. The cost can be calculated on the Pricing page.")
    location_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine location. required field if you don't specify location_code or location_coordinate. if you use this field, you don't need to specify location_code or location_coordinate. you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/{{low_se_name}}/locations. example:. London,England,United Kingdom")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine language. required field if you don't specify language_code. if you use this field, you don't need to specify language_code. you can receive the list of available locations of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/{{low_se_name}}/languages. example:. English")
    os: Optional[StrictStr] = Field(default=None, description=r"device operating system. optional field. note that this API provides results for desktop only. choose from the following values: windows, macos. default value: windows")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    max_crawl_pages: Optional[StrictInt] = Field(default=None, description=r"page crawl limit. optional field. number of search results pages to crawl. max value: 100. Note: the max_crawl_pages and depth parameters complement each other;. learn more at our help center")
    search_param: Optional[StrictStr] = Field(default=None, description=r"additional parameters of the search query. optional field. get the list of available parameters and additional details here")
    url: Optional[StrictStr] = Field(default=None, description=r"direct URL of the search query. optional field. you can specify a direct URL and we will sort it out to the necessary fields. Note that this method is the most difficult for our API to process and also requires you to specify the exact language and location in the URL. In most cases, we wouldn’t recommend using this method.. example:. https://www.google.co.uk/search?q=%20rank%20tracker%20api&hl=en&gl=GB&uule=w+CAIQIFISCXXeIa8LoNhHEZkq1d1aOpZS")
    location_coordinate: Optional[StrictStr] = Field(default=None, description=r"GPS coordinates of a location. required field if you don't specify location_name or location_code. if you use this field, you don't need to specify location_name or location_code. location_coordinate parameter should be specified in the 'latitude,longitude,radius' format. the maximum number of decimal digits for 'latitude' and 'longitude': 7. the minimum value for 'radius': 199.9 (mm). the maximum value for 'radius': 199999 (mm). example:. 53.476225,-2.243572,200")
    se_domain: Optional[StrictStr] = Field(default=None, description=r"search engine domain. optional field. we choose the relevant search engine domain automatically according to the location and language you specify. however, you can set a custom search engine domain in this field. example:. google.co.uk, google.com.au, google.de, etc.")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_code", 
        "language_code", 
        "depth", 
        "location_name", 
        "language_name", 
        "os", 
        "tag", 
        "max_crawl_pages", 
        "search_param", 
        "url", 
        "location_coordinate", 
        "se_domain", 
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
        _dict['location_name'] = self.location_name
        _dict['language_name'] = self.language_name
        _dict['os'] = self.os
        _dict['tag'] = self.tag
        _dict['max_crawl_pages'] = self.max_crawl_pages
        _dict['search_param'] = self.search_param
        _dict['url'] = self.url
        _dict['location_coordinate'] = self.location_coordinate
        _dict['se_domain'] = self.se_domain
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
            "location_name": obj.get("location_name"),
            "language_name": obj.get("language_name"),
            "os": obj.get("os"),
            "tag": obj.get("tag"),
            "max_crawl_pages": obj.get("max_crawl_pages"),
            "search_param": obj.get("search_param"),
            "url": obj.get("url"),
            "location_coordinate": obj.get("location_coordinate"),
            "se_domain": obj.get("se_domain"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj