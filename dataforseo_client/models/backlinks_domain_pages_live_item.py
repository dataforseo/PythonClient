from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.backlinks_page_meta import BacklinksPageMeta
from dataforseo_client.models.page_summary import PageSummary



class BacklinksDomainPagesLiveItem(BaseModel):
    """
    BacklinksDomainPagesLiveItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    main_domain: Optional[StrictStr] = Field(default=None, description="main website domain. main website domain does not include subdomains")
    domain: Optional[StrictStr] = Field(default=None, description="domain. domain where the page was found")
    tld: Optional[StrictStr] = Field(default=None, description="top-level domain. top-level domain in the DNS root zone")
    page: Optional[StrictStr] = Field(default=None, description="page URL. relevant page URL")
    ip: Optional[StrictStr] = Field(default=None, description="Internet Protocol address")
    first_visited: Optional[StrictStr] = Field(default=None, description="date and time of the first page visit. date and time when our crawler visited this page for the first time. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2017-01-24 13:20:59 +00:00")
    prev_visited: Optional[StrictStr] = Field(default=None, description="previous to the most recent date when our crawler visited the page. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2017-01-24 13:20:59 +00:00")
    fetch_time: Optional[StrictStr] = Field(default=None, description="most recent date and time when our crawler visited the page. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2017-01-24 13:20:59 +00:00")
    status_code: Optional[StrictInt] = Field(default=None, description="HTTP status code of the page")
    location: Optional[StrictStr] = Field(default=None, description="location header. indicates the URL to redirect a page to if exists")
    size: Optional[StrictInt] = Field(default=None, description="indicates the page size, in bytes")
    encoded_size: Optional[StrictInt] = Field(default=None, description="page size after encoding. indicates the size of the encoded page, in bytes")
    content_encoding: Optional[StrictStr] = Field(default=None, description="type of encoding")
    media_type: Optional[StrictStr] = Field(default=None, description="types of media used to display a page")
    server: Optional[StrictStr] = Field(default=None, description="server version")
    meta: Optional[BacklinksPageMeta] = Field(default=None, description="page meta data")
    page_summary: Optional[PageSummary] = Field(default=None, description="contains backlink data for this page")
    __properties: ClassVar[List[str]] = [
        "type", 
        "main_domain", 
        "domain", 
        "tld", 
        "page", 
        "ip", 
        "first_visited", 
        "prev_visited", 
        "fetch_time", 
        "status_code", 
        "location", 
        "size", 
        "encoded_size", 
        "content_encoding", 
        "media_type", 
        "server", 
        "meta", 
        "page_summary", 
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

        _dict['type'] = self.type
        _dict['main_domain'] = self.main_domain
        _dict['domain'] = self.domain
        _dict['tld'] = self.tld
        _dict['page'] = self.page
        _dict['ip'] = self.ip
        _dict['first_visited'] = self.first_visited
        _dict['prev_visited'] = self.prev_visited
        _dict['fetch_time'] = self.fetch_time
        _dict['status_code'] = self.status_code
        _dict['location'] = self.location
        _dict['size'] = self.size
        _dict['encoded_size'] = self.encoded_size
        _dict['content_encoding'] = self.content_encoding
        _dict['media_type'] = self.media_type
        _dict['server'] = self.server
        _dict['meta'] = self.meta.to_dict() if self.meta else None
        _dict['page_summary'] = self.page_summary.to_dict() if self.page_summary else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "main_domain": obj.get("main_domain"),
            "domain": obj.get("domain"),
            "tld": obj.get("tld"),
            "page": obj.get("page"),
            "ip": obj.get("ip"),
            "first_visited": obj.get("first_visited"),
            "prev_visited": obj.get("prev_visited"),
            "fetch_time": obj.get("fetch_time"),
            "status_code": obj.get("status_code"),
            "location": obj.get("location"),
            "size": obj.get("size"),
            "encoded_size": obj.get("encoded_size"),
            "content_encoding": obj.get("content_encoding"),
            "media_type": obj.get("media_type"),
            "server": obj.get("server"),
            "meta": BacklinksPageMeta.from_dict(obj["meta"]) if obj.get("meta") is not None else None,
            "page_summary": PageSummary.from_dict(obj["page_summary"]) if obj.get("page_summary") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj