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
from dataforseo_client.models.ssl_info import SslInfo
from typing import Optional, Set
from typing_extensions import Self

class DomainInfo(BaseModel):
    """
    DomainInfo
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="domain name")
    cms: Optional[StrictStr] = Field(default=None, description="content management system content management system identified on a website the content of the generator meta tag the data is taken from the first random page that returns the 200 response code if our crawler was unable to identify the cms, the value would be null")
    ip: Optional[StrictStr] = Field(default=None, description="domain ip address")
    server: Optional[StrictStr] = Field(default=None, description="website server the version of the server detected on a website the content of the server header the information is taken from the first page which response code is 200")
    crawl_start: Optional[StrictStr] = Field(default=None, description="time when the crawling start date and time when the website was sent for crawling in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    crawl_end: Optional[StrictStr] = Field(default=None, description="time when the crawling ended date and time when the crawling was finished in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00note: informative only if \"crawl_progress\" is \"finished\" if \"crawl_progress\" is in_progress, the value will be null")
    extended_crawl_status: Optional[StrictStr] = Field(default=None, description="crawl status and errors indicates the reason why a website was not crawled; can take the following values: no_errors – no crawling errors were detected; site_unreachable – our crawler could not reach a website and thus was not able to obtain a status code; invalid_page_status_code – status code of the first crawled page >= 400; forbidden_meta_tag – the first crawled page contains the <meta robots=”noindex”> tag; forbidden_robots – robots.txt forbids crawling the page; forbidden_http_header – HTTP header of the page contains “X-Robots-Tag: noindex” ; too_many_redirects – the first crawled page has more than 10 redirects; unknown – the reason is unknown")
    ssl_info: Optional[SslInfo] = None
    checks: Optional[Dict[str, Optional[StrictBool]]] = Field(default=None, description="website checks other on-page check-ups related to the website")
    total_pages: Optional[StrictInt] = Field(default=None, description="total crawled pages the total number of crawled pages")
    page_not_found_status_code: Optional[StrictInt] = Field(default=None, description="status code returned by a non-existent page in most cases, it is recommended a server returns a 404 response code")
    canonicalization_status_code: Optional[StrictInt] = Field(default=None, description="status code returned by a canonicalized page the checkup of the server behavior when our crawler tries to access the website via IP; in most cases, it is recommended that canonicalized pages respond with a 301 or 302 status code")
    directory_browsing_status_code: Optional[StrictInt] = Field(default=None, description="status code returned by a directory the status code returned by a directory page on a target website in most cases, it is recommended that directories respond with a 403 or 401 status code")
    www_redirect_status_code: Optional[StrictInt] = Field(default=None, description="redirect status code the status code of the www to non-www redirect in most cases, it is recommended that redirect returns a 301 status code")
    main_domain: Optional[StrictStr] = Field(default=None, description="root domain name")
    __properties: ClassVar[List[str]] = ["name", "cms", "ip", "server", "crawl_start", "crawl_end", "extended_crawl_status", "ssl_info", "checks", "total_pages", "page_not_found_status_code", "canonicalization_status_code", "directory_browsing_status_code", "www_redirect_status_code", "main_domain"]

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
        """Create an instance of DomainInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ssl_info
        if self.ssl_info:
            _dict['ssl_info'] = self.ssl_info.to_dict()
        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if cms (nullable) is None
        # and model_fields_set contains the field
        if self.cms is None and "cms" in self.model_fields_set:
            _dict['cms'] = None

        # set to None if ip (nullable) is None
        # and model_fields_set contains the field
        if self.ip is None and "ip" in self.model_fields_set:
            _dict['ip'] = None

        # set to None if server (nullable) is None
        # and model_fields_set contains the field
        if self.server is None and "server" in self.model_fields_set:
            _dict['server'] = None

        # set to None if crawl_start (nullable) is None
        # and model_fields_set contains the field
        if self.crawl_start is None and "crawl_start" in self.model_fields_set:
            _dict['crawl_start'] = None

        # set to None if crawl_end (nullable) is None
        # and model_fields_set contains the field
        if self.crawl_end is None and "crawl_end" in self.model_fields_set:
            _dict['crawl_end'] = None

        # set to None if extended_crawl_status (nullable) is None
        # and model_fields_set contains the field
        if self.extended_crawl_status is None and "extended_crawl_status" in self.model_fields_set:
            _dict['extended_crawl_status'] = None

        # set to None if checks (nullable) is None
        # and model_fields_set contains the field
        if self.checks is None and "checks" in self.model_fields_set:
            _dict['checks'] = None

        # set to None if total_pages (nullable) is None
        # and model_fields_set contains the field
        if self.total_pages is None and "total_pages" in self.model_fields_set:
            _dict['total_pages'] = None

        # set to None if page_not_found_status_code (nullable) is None
        # and model_fields_set contains the field
        if self.page_not_found_status_code is None and "page_not_found_status_code" in self.model_fields_set:
            _dict['page_not_found_status_code'] = None

        # set to None if canonicalization_status_code (nullable) is None
        # and model_fields_set contains the field
        if self.canonicalization_status_code is None and "canonicalization_status_code" in self.model_fields_set:
            _dict['canonicalization_status_code'] = None

        # set to None if directory_browsing_status_code (nullable) is None
        # and model_fields_set contains the field
        if self.directory_browsing_status_code is None and "directory_browsing_status_code" in self.model_fields_set:
            _dict['directory_browsing_status_code'] = None

        # set to None if www_redirect_status_code (nullable) is None
        # and model_fields_set contains the field
        if self.www_redirect_status_code is None and "www_redirect_status_code" in self.model_fields_set:
            _dict['www_redirect_status_code'] = None

        # set to None if main_domain (nullable) is None
        # and model_fields_set contains the field
        if self.main_domain is None and "main_domain" in self.model_fields_set:
            _dict['main_domain'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DomainInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "cms": obj.get("cms"),
            "ip": obj.get("ip"),
            "server": obj.get("server"),
            "crawl_start": obj.get("crawl_start"),
            "crawl_end": obj.get("crawl_end"),
            "extended_crawl_status": obj.get("extended_crawl_status"),
            "ssl_info": SslInfo.from_dict(obj["ssl_info"]) if obj.get("ssl_info") is not None else None,
            "checks": obj.get("checks"),
            "total_pages": obj.get("total_pages"),
            "page_not_found_status_code": obj.get("page_not_found_status_code"),
            "canonicalization_status_code": obj.get("canonicalization_status_code"),
            "directory_browsing_status_code": obj.get("directory_browsing_status_code"),
            "www_redirect_status_code": obj.get("www_redirect_status_code"),
            "main_domain": obj.get("main_domain")
        })
        return _obj


