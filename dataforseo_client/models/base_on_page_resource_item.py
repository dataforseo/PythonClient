from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.on_page_resource_issue_info import OnPageResourceIssueInfo
from dataforseo_client.models.cache_control import CacheControl
from dataforseo_client.models.last_modified import LastModified

from importlib import import_module
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dataforseo_client.models.on_page_html_resource_item import OnPageHtmlResourceItem;
    from dataforseo_client.models.on_page_broken_resource_item import OnPageBrokenResourceItem;
    from dataforseo_client.models.on_page_redirect_resource_item import OnPageRedirectResourceItem;
    from dataforseo_client.models.on_page_script_resource_item import OnPageScriptResourceItem;
    from dataforseo_client.models.on_page_image_resource_item import OnPageImageResourceItem;
    from dataforseo_client.models.on_page_stylesheet_resource_item import OnPageStylesheetResourceItem;



class BaseOnPageResourceItem(BaseModel):
    """
    BaseOnPageResourceItem
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
        ]
    __discriminator_property_name: ClassVar[str] = 'resource_type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'html': 'OnPageHtmlResourceItem',
        'broken': 'OnPageBrokenResourceItem',
        'redirect': 'OnPageRedirectResourceItem',
        'script': 'OnPageScriptResourceItem',
        'image': 'OnPageImageResourceItem',
        'stylesheet': 'OnPageStylesheetResourceItem',
    }

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
        return _dict


    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None
    
    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[
        OnPageHtmlResourceItem, 
        OnPageBrokenResourceItem, 
        OnPageRedirectResourceItem, 
        OnPageScriptResourceItem, 
        OnPageImageResourceItem, 
        OnPageStylesheetResourceItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'OnPageHtmlResourceItem':
            return import_module("dataforseo_client.models.on_page_html_resource_item").OnPageHtmlResourceItem.from_dict(obj)
        if object_type == 'OnPageBrokenResourceItem':
            return import_module("dataforseo_client.models.on_page_broken_resource_item").OnPageBrokenResourceItem.from_dict(obj)
        if object_type == 'OnPageRedirectResourceItem':
            return import_module("dataforseo_client.models.on_page_redirect_resource_item").OnPageRedirectResourceItem.from_dict(obj)
        if object_type == 'OnPageScriptResourceItem':
            return import_module("dataforseo_client.models.on_page_script_resource_item").OnPageScriptResourceItem.from_dict(obj)
        if object_type == 'OnPageImageResourceItem':
            return import_module("dataforseo_client.models.on_page_image_resource_item").OnPageImageResourceItem.from_dict(obj)
        if object_type == 'OnPageStylesheetResourceItem':
            return import_module("dataforseo_client.models.on_page_stylesheet_resource_item").OnPageStylesheetResourceItem.from_dict(obj)

        return None