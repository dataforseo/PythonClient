from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.fetch_timing import FetchTiming
from dataforseo_client.models.page_meta_info import PageMetaInfo
from dataforseo_client.models.base_on_page_resource_item import BaseOnPageResourceItem
from dataforseo_client.models.on_page_resource_issue_info import OnPageResourceIssueInfo
from dataforseo_client.models.cache_control import CacheControl
from dataforseo_client.models.last_modified import LastModified



class OnPageBrokenResourceItem(BaseOnPageResourceItem):
    """
    OnPageBrokenResourceItem
    """ # noqa: E501
    resource_type: Optional[StrictStr] = Field(default=None, description="type of element")
    status_code: Optional[StrictInt] = Field(default=None, description="status code of the page")
    location: Optional[StrictStr] = Field(default=None, description="location header. indicates the URL to redirect a page to")
    url: Optional[StrictStr] = Field(default=None, description="page URL")
    resource_errors: Optional[OnPageResourceIssueInfo] = Field(default=None, description="resource errors and warnings")
    size: Optional[StrictInt] = Field(default=None, description="resource size. indicates the size of a given page measured in bytes")
    encoded_size: Optional[StrictInt] = Field(default=None, description="page size after encoding. indicates the size of the encoded page measured in bytes")
    total_transfer_size: Optional[StrictInt] = Field(default=None, description="compressed page size. indicates the compressed size of a given page")
    fetch_time: Optional[StrictStr] = Field(default=None, description="date and time when a resource was fetched. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    cache_control: Optional[CacheControl] = Field(default=None, description="instructions for caching")
    checks: Optional[Dict[str, Optional[StrictBool]]] = Field(default=None, description="website checks. on-page check-ups related to the page")
    content_encoding: Optional[StrictStr] = Field(default=None, description="type of encoding")
    media_type: Optional[StrictStr] = Field(default=None, description="types of media used to display a page")
    server: Optional[StrictStr] = Field(default=None, description="server version")
    last_modified: Optional[LastModified] = Field(default=None, description="contains data on changes related to the resource. if there is no data, the value will be null")
    fetch_timing: Optional[FetchTiming] = Field(default=None, description="time range within which a result was fetched")
    is_resource: Optional[StrictBool] = Field(default=None, description="indicates whether a page is a single resource")
    meta: Optional[PageMetaInfo] = Field(default=None, description="resource properties. the value depends on the resource_type. note that if you do not indicate a url when setting a task, resource’s meta is returned based on the data from the page where our crawler first saw the resource;. to obtain resource’s meta from a particular url, specify that URL when setting a task")
    accept_type: Optional[StrictStr] = Field(default=None, description="indicates the expected type of resource. for example, if 'resource_type': 'broken', accept_type will indicate the type of the broken resource. possible values:. any, none, image, sitemap, robots, script, stylesheet, redirect, html, text, other, font")
    __properties: ClassVar[List[str]] = [
        "resource_type", 
        "status_code", 
        "location", 
        "url", 
        "resource_errors", 
        "size", 
        "encoded_size", 
        "total_transfer_size", 
        "fetch_time", 
        "cache_control", 
        "checks", 
        "content_encoding", 
        "media_type", 
        "server", 
        "last_modified", 
        "fetch_timing", 
        "is_resource", 
        "meta", 
        "accept_type", 
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

        _dict['resource_type'] = self.resource_type
        _dict['status_code'] = self.status_code
        _dict['location'] = self.location
        _dict['url'] = self.url
        _dict['resource_errors'] = self.resource_errors.to_dict() if self.resource_errors else None
        _dict['size'] = self.size
        _dict['encoded_size'] = self.encoded_size
        _dict['total_transfer_size'] = self.total_transfer_size
        _dict['fetch_time'] = self.fetch_time
        _dict['cache_control'] = self.cache_control.to_dict() if self.cache_control else None
        _dict['checks'] = self.checks
        _dict['content_encoding'] = self.content_encoding
        _dict['media_type'] = self.media_type
        _dict['server'] = self.server
        _dict['last_modified'] = self.last_modified.to_dict() if self.last_modified else None
        _dict['fetch_timing'] = self.fetch_timing.to_dict() if self.fetch_timing else None
        _dict['is_resource'] = self.is_resource
        _dict['meta'] = self.meta.to_dict() if self.meta else None
        _dict['accept_type'] = self.accept_type
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "resource_type": obj.get("resource_type"),
            "status_code": obj.get("status_code"),
            "location": obj.get("location"),
            "url": obj.get("url"),
            "resource_errors": OnPageResourceIssueInfo.from_dict(obj["resource_errors"]) if obj.get("resource_errors") is not None else None,
            "size": obj.get("size"),
            "encoded_size": obj.get("encoded_size"),
            "total_transfer_size": obj.get("total_transfer_size"),
            "fetch_time": obj.get("fetch_time"),
            "cache_control": CacheControl.from_dict(obj["cache_control"]) if obj.get("cache_control") is not None else None,
            "checks": obj.get("checks"),
            "content_encoding": obj.get("content_encoding"),
            "media_type": obj.get("media_type"),
            "server": obj.get("server"),
            "last_modified": LastModified.from_dict(obj["last_modified"]) if obj.get("last_modified") is not None else None,
            "fetch_timing": FetchTiming.from_dict(obj["fetch_timing"]) if obj.get("fetch_timing") is not None else None,
            "is_resource": obj.get("is_resource"),
            "meta": PageMetaInfo.from_dict(obj["meta"]) if obj.get("meta") is not None else None,
            "accept_type": obj.get("accept_type"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj