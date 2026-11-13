from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpGoogleOrganicLiveRegularRequestInfo(BaseModel):
    """
    SerpGoogleOrganicLiveRegularRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description=r"*keyword*. **required field**. you can specify **up to 700 characters** in the `keyword` field. all %## will be decoded (plus character '+' will be decoded to a space character). if you need to use the '%' character for your `keyword`, please specify it as '%25';. if you need to use the “+” character for your `keyword`, please specify it as “%2B”;. if this field contains such parameters as *'allinanchor:', 'allintext:', 'allintitle:', 'allinurl:', ‘cache:’, 'define:', 'filetype:', 'id:', 'inanchor:', 'info:', 'intext:', 'intitle:', 'inurl:', 'link:', 'site:'*, **the charge per task will be multiplied by 5**")
    location_code: Optional[StrictInt] = Field(default=None, description=r"*search engine location code*. **required field if you don't specify** `location_name` or `location_coordinate`. **if you use this field, you don't need to specify `location_name` or `location_coordinate`**. you can receive the list of available locations of the search engines with their `location_code` by making a separate request to the `https://api.dataforseo.com/v3/serp/google/locations`. example:. `2840`")
    language_code: Optional[StrictStr] = Field(default=None, description=r"*search engine language code*. **required field if you don't specify** `language_name`. **if you use this field, you don't need to specify `language_name`**. you can receive the list of available languages of the search engine with their `language_code` by making a separate request to the `https://api.dataforseo.com/v3/serp/google/languages`**example:**`en`")
    depth: Optional[StrictInt] = Field(default=None, description=r"*parsing depth*. optional field. number of results in SERP. **default value: `10`**. max value: `200`. **Your account will be billed per each SERP containing up to 10 results;**. Setting depth above 10 may result in additional charges [if the search engine returns more than 10 results](https://dataforseo.com/help-center/how-many-results-scraped);. The cost can be calculated on the [Pricing](https://dataforseo.com/pricing/serp/google-organic-serp-api) page.")
    resolve_goto_urls: Optional[StrictBool] = Field(default=None, description=r"*resolve goto redirect URLs*. optional field. set to `true` to resolve goto redirect URLs in SERPs. default value: `false`. **Note:** this parameter adds up to 40 seconds to the turnaround time, with a maximum turnaround time of 260 seconds")
    device: Optional[StrictStr] = Field(default=None, description=r"*device type*. optional field. return results for a specific device type. can take the values:`desktop`, `mobile`. default value: `desktop`")
    location_name: Optional[StrictStr] = Field(default=None, description=r"*full name of search engine location*. **required field if you don't specify** `location_code` or `location_coordinate`. **if you use this field, you don't need to specify `location_code` or `location_coordinate`**. you can receive the list of available locations of the search engine with their `location_name` by making a separate request to the `https://api.dataforseo.com/v3/serp/google/locations`. example:. `London,England,United Kingdom`")
    language_name: Optional[StrictStr] = Field(default=None, description=r"*full name of search engine language*. **required field if you don't specify** `language_code`. **if you use this field, you don't need to specify `language_code`**. you can receive the list of available languages of the search engine with their `language_name` by making a separate request to the `https://api.dataforseo.com/v3/serp/google/languages`. example:. `English`")
    os: Optional[StrictStr] = Field(default=None, description=r"*device operating system*. optional field. if you specify `desktop` in the `device` field, choose from the following values: `windows`, `macos`. default value: `windows`. if you specify `mobile` in the `device` field, choose from the following values: `android`, `ios`. default value: `android`")
    tag: Optional[StrictStr] = Field(default=None, description=r"*user-defined task identifier*. optional field. *the character limit is 255*. you can use this parameter to identify the task and match it with the result. you will find the specified `tag` value in the `data` object of the response")
    max_crawl_pages: Optional[StrictInt] = Field(default=None, description=r"*page crawl limit*. optional field. number of search results pages to crawl. max value: `100`. **Note:** you will be charged for each page crawled (10 organic results per page);. learn more about pricing on our [Pricing](https://dataforseo.com/pricing/serp/google-organic-serp-api) page;. **Note#2:** the `max_crawl_pages` and `depth` parameters complement each other;. learn more at [our help center](https://dataforseo.com/help-center/what-is-max-crawl-pages-and-how-does-it-work)")
    search_param: Optional[StrictStr] = Field(default=None, description=r"*additional parameters of the search query*. optional field. [get the list of available parameters and additional details here](https://dataforseo.com/what-are-google-search-parameters-and-how-to-use-them-with-serp-api.html). **Note:** the following search engine parameters are not supported and will be automatically unset if specified: `lr`, `cr`, `as_qdr`, `as_sitesearch`, `as_occt`, `as_filetype`.")
    group_organic_results: Optional[StrictBool] = Field(default=None, description=r"*display related results*. optional field. if set to `true`, the `related_result` element in the response will be provided as a snippet of its parent organic result;. if set to `false`, the `related_result` element will be provided as a separate organic result;. default value: `true`")
    url: Optional[StrictStr] = Field(default=None, description=r"*direct URL of the search query*. optional field. you can specify a direct URL and we will sort it out to the necessary fields. Note that this method is the most difficult for our API to process and also requires you to specify the exact language and location in the URL. In most cases, we wouldn’t recommend using this method.. example:. `https://www.google.co.uk/search?q=%20rank%20tracker%20api&hl=en&gl=GB&uule=w+CAIQIFISCXXeIa8LoNhHEZkq1d1aOpZS`. **Note:** the following search engine parameters are not supported and will be automatically unset if specified in the URL: `lr`, `cr`, `as_qdr`, `as_sitesearch`, `as_occt`, `as_filetype`.")
    location_coordinate: Optional[StrictStr] = Field(default=None, description=r"*GPS coordinates of a location*. **required field if you don't specify** `location_name` or `location_code`. **if you use this field, you don't need to specify `location_name` or `location_code`**. `location_coordinate` parameter should be specified in the *'latitude,longitude,radius'* format. the maximum number of decimal digits for *'latitude'* and *'longitude'*: 7. the minimum value for *'radius'*: 199 (mm). the maximum value for *'radius'*: 199999 (mm). example:. `53.476225,-2.243572,200`")
    se_domain: Optional[StrictStr] = Field(default=None, description=r"*search engine domain*. optional field. we choose the relevant search engine domain automatically according to the location and language you specify. however, you can set a custom search engine domain in this field. example:. `google.co.uk`, `google.com.au`, `google.de`, etc.")
    target: Optional[StrictStr] = Field(default=None, description=r"*target domain, subdomain, or webpage to get results for*. optional field. a domain or a subdomain should be specified without `https://` and `www.`. note that the results of `target`-specific tasks will only include SERP elements that contain a `url` string;. you can also use a wildcard (‘*’) character to specify the search pattern in SERP and narrow down the results;. examples:. **`example.com`**  - returns results for the website's home page with URLs, such as `https://example.com`, or `https://www.example.com/`, or `https://example.com/`;. **`example.com*`** - returns results for the domain, including all its pages;. **`*example.com*`** - returns results for the entire domain, including all its pages and subdomains;. **`*example.com`**  - returns results for the home page regardless of the subdomain, such as `https://en.example.com`;. **`example.com/example-page`**  - returns results for the exact URL;. **`example.com/example-page*`**  - returns results for all domain's URLs that start with the specified string")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_code", 
        "language_code", 
        "depth", 
        "resolve_goto_urls", 
        "device", 
        "location_name", 
        "language_name", 
        "os", 
        "tag", 
        "max_crawl_pages", 
        "search_param", 
        "group_organic_results", 
        "url", 
        "location_coordinate", 
        "se_domain", 
        "target", 
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
        _dict['resolve_goto_urls'] = self.resolve_goto_urls
        _dict['device'] = self.device
        _dict['location_name'] = self.location_name
        _dict['language_name'] = self.language_name
        _dict['os'] = self.os
        _dict['tag'] = self.tag
        _dict['max_crawl_pages'] = self.max_crawl_pages
        _dict['search_param'] = self.search_param
        _dict['group_organic_results'] = self.group_organic_results
        _dict['url'] = self.url
        _dict['location_coordinate'] = self.location_coordinate
        _dict['se_domain'] = self.se_domain
        _dict['target'] = self.target
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
            "resolve_goto_urls": obj.get("resolve_goto_urls"),
            "device": obj.get("device"),
            "location_name": obj.get("location_name"),
            "language_name": obj.get("language_name"),
            "os": obj.get("os"),
            "tag": obj.get("tag"),
            "max_crawl_pages": obj.get("max_crawl_pages"),
            "search_param": obj.get("search_param"),
            "group_organic_results": obj.get("group_organic_results"),
            "url": obj.get("url"),
            "location_coordinate": obj.get("location_coordinate"),
            "se_domain": obj.get("se_domain"),
            "target": obj.get("target"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj