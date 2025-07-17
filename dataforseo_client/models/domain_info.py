from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ssl_info import SslInfo



class DomainInfo(BaseModel):
    """
    DomainInfo
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="domain name")
    cms: Optional[StrictStr] = Field(default=None, description="content management system. content management system identified on a website. the content of the generator meta tag. the data is taken from the first random page that returns the 200 response code. if our crawler was unable to identify the cms, the value would be null")
    ip: Optional[StrictStr] = Field(default=None, description="domain ip address")
    server: Optional[StrictStr] = Field(default=None, description="website server. the version of the server detected on a website. the content of the server header. the information is taken from the first page which response code is 200")
    crawl_start: Optional[StrictStr] = Field(default=None, description="time when the crawling start. date and time when the website was sent for crawling. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    crawl_end: Optional[StrictStr] = Field(default=None, description="time when the crawling ended. date and time when the crawling was finished. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00. Note: informative only if 'crawl_progress' is 'finished'. if 'crawl_progress' is in_progress, the value will be null")
    extended_crawl_status: Optional[StrictStr] = Field(default=None, description="crawl status and errors. indicates the reason why a website was not crawled;. can take the following values:. no_errors – no crawling errors were detected;. site_unreachable – our crawler could not reach a website and thus was not able to obtain a status code;. invalid_page_status_code – status code of the first crawled page >= 400;. forbidden_meta_tag – the first crawled page contains the <meta robots=”noindex”> tag;. forbidden_robots – robots.txt forbids crawling the page;. forbidden_http_header – HTTP header of the page contains “X-Robots-Tag: noindex” ;. too_many_redirects – the first crawled page has more than 10 redirects;. unknown – the reason is unknown")
    ssl_info: Optional[SslInfo] = Field(default=None, description="ssl certificate info. information about the Secure Sockets Layer protocol detected on a website")
    checks: Optional[Dict[str, Optional[StrictBool]]] = Field(default=None, description="website checks. other on-page check-ups related to the website")
    total_pages: Optional[StrictInt] = Field(default=None, description="total crawled pages. the total number of crawled pages")
    page_not_found_status_code: Optional[StrictInt] = Field(default=None, description="status code returned by a non-existent page. in most cases, it is recommended a server returns a 404 response code")
    canonicalization_status_code: Optional[StrictInt] = Field(default=None, description="status code returned by a canonicalized page. the checkup of the server behavior when our crawler tries to access the website via IP;. in most cases, it is recommended that canonicalized pages respond with a 301 or 302 status code")
    directory_browsing_status_code: Optional[StrictInt] = Field(default=None, description="status code returned by a directory. the status code returned by a directory page on a target website. in most cases, it is recommended that directories respond with a 403 or 401 status code")
    www_redirect_status_code: Optional[StrictInt] = Field(default=None, description="redirect status code. the status code of the www to non-www redirect. in most cases, it is recommended that redirect returns a 301 status code")
    main_domain: Optional[StrictStr] = Field(default=None, description="root domain name")
    __properties: ClassVar[List[str]] = [
        "name", 
        "cms", 
        "ip", 
        "server", 
        "crawl_start", 
        "crawl_end", 
        "extended_crawl_status", 
        "ssl_info", 
        "checks", 
        "total_pages", 
        "page_not_found_status_code", 
        "canonicalization_status_code", 
        "directory_browsing_status_code", 
        "www_redirect_status_code", 
        "main_domain", 
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

        _dict['name'] = self.name
        _dict['cms'] = self.cms
        _dict['ip'] = self.ip
        _dict['server'] = self.server
        _dict['crawl_start'] = self.crawl_start
        _dict['crawl_end'] = self.crawl_end
        _dict['extended_crawl_status'] = self.extended_crawl_status
        _dict['ssl_info'] = self.ssl_info.to_dict() if self.ssl_info else None
        _dict['checks'] = self.checks
        _dict['total_pages'] = self.total_pages
        _dict['page_not_found_status_code'] = self.page_not_found_status_code
        _dict['canonicalization_status_code'] = self.canonicalization_status_code
        _dict['directory_browsing_status_code'] = self.directory_browsing_status_code
        _dict['www_redirect_status_code'] = self.www_redirect_status_code
        _dict['main_domain'] = self.main_domain
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
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
            "main_domain": obj.get("main_domain"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj