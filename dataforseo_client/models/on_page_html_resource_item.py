from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.page_meta_info import PageMetaInfo
from dataforseo_client.models.page_timing import PageTiming
from dataforseo_client.models.base_on_page_resource_item import BaseOnPageResourceItem
from dataforseo_client.models.on_page_resource_issue_info import OnPageResourceIssueInfo
from dataforseo_client.models.cache_control import CacheControl
from dataforseo_client.models.last_modified import LastModified



class OnPageHtmlResourceItem(BaseOnPageResourceItem):
    """
    OnPageHtmlResourceItem
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
    meta: Optional[PageMetaInfo] = Field(default=None, description="page properties. the value depends on the resource_type")
    page_timing: Optional[PageTiming] = Field(default=None, description="object of page load metrics")
    onpage_score: Optional[StrictFloat] = Field(default=None, description="shows how page is optimized on a 100-point scale. this field shows how page is optimized considering critical on-page issues and warnings detected;. 100 is the highest possible score that means the page does not have any critical on-page issues and important warnings;. learn more about how the metric is calculated in this help center article")
    total_dom_size: Optional[StrictInt] = Field(default=None, description="total DOM size of a page")
    custom_js_response: Optional[Any] = Field(default=None, description="the result of executing a specified JS script. note that you should specify a custom_js field when setting a task to receive this data and the field type and its value will totally depend on the script you specified;. you can also filter the results by this value specifying filters in the following way:. ['custom_js_response.url', 'like', 'pixel']")
    custom_js_client_exception: Optional[StrictStr] = Field(default=None, description="error when executing a custom js. if the error occurred when executing the script you specified in the custom_js field, the error message would be displayed here")
    broken_resources: Optional[StrictBool] = Field(default=None, description="indicates whether a page contains broken resources")
    broken_links: Optional[StrictBool] = Field(default=None, description="indicates whether a page contains broken links")
    duplicate_title: Optional[StrictBool] = Field(default=None, description="indicates whether a page has duplicate title tags")
    duplicate_description: Optional[StrictBool] = Field(default=None, description="indicates whether a page has a duplicate description")
    duplicate_content: Optional[StrictBool] = Field(default=None, description="indicates whether a page has duplicate content")
    click_depth: Optional[StrictInt] = Field(default=None, description="number of clicks it takes to get to the page. indicates the number of clicks from the homepage needed before landing at the target page")
    is_resource: Optional[StrictBool] = Field(default=None, description="indicates whether a page is a single resource")
    url_length: Optional[StrictInt] = Field(default=None, description="page URL length in characters")
    relative_url_length: Optional[StrictInt] = Field(default=None, description="relative URL length in characters")
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
        "meta", 
        "page_timing", 
        "onpage_score", 
        "total_dom_size", 
        "custom_js_response", 
        "custom_js_client_exception", 
        "broken_resources", 
        "broken_links", 
        "duplicate_title", 
        "duplicate_description", 
        "duplicate_content", 
        "click_depth", 
        "is_resource", 
        "url_length", 
        "relative_url_length", 
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
        _dict['meta'] = self.meta.to_dict() if self.meta else None
        _dict['page_timing'] = self.page_timing.to_dict() if self.page_timing else None
        _dict['onpage_score'] = self.onpage_score
        _dict['total_dom_size'] = self.total_dom_size
        _dict['custom_js_response'] = self.custom_js_response
        _dict['custom_js_client_exception'] = self.custom_js_client_exception
        _dict['broken_resources'] = self.broken_resources
        _dict['broken_links'] = self.broken_links
        _dict['duplicate_title'] = self.duplicate_title
        _dict['duplicate_description'] = self.duplicate_description
        _dict['duplicate_content'] = self.duplicate_content
        _dict['click_depth'] = self.click_depth
        _dict['is_resource'] = self.is_resource
        _dict['url_length'] = self.url_length
        _dict['relative_url_length'] = self.relative_url_length
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
            "meta": PageMetaInfo.from_dict(obj["meta"]) if obj.get("meta") is not None else None,
            "page_timing": PageTiming.from_dict(obj["page_timing"]) if obj.get("page_timing") is not None else None,
            "onpage_score": obj.get("onpage_score"),
            "total_dom_size": obj.get("total_dom_size"),
            "custom_js_response": obj.get("custom_js_response"),
            "custom_js_client_exception": obj.get("custom_js_client_exception"),
            "broken_resources": obj.get("broken_resources"),
            "broken_links": obj.get("broken_links"),
            "duplicate_title": obj.get("duplicate_title"),
            "duplicate_description": obj.get("duplicate_description"),
            "duplicate_content": obj.get("duplicate_content"),
            "click_depth": obj.get("click_depth"),
            "is_resource": obj.get("is_resource"),
            "url_length": obj.get("url_length"),
            "relative_url_length": obj.get("relative_url_length"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj