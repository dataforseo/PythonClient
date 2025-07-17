from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.crawl_status_info import CrawlStatusInfo
from dataforseo_client.models.base_on_page_resource_item import BaseOnPageResourceItem



class OnPageResourcesResultInfo(BaseModel):
    """
    OnPageResourcesResultInfo
    """ # noqa: E501
    crawl_progress: Optional[StrictStr] = Field(default=None, description="status of the crawling session. possible values: in_progress, finished")
    crawl_status: Optional[CrawlStatusInfo] = Field(default=None, description="details of the crawling session")
    search_after_token: Optional[StrictStr] = Field(default=None, description="")
    current_offset: Optional[StrictInt] = Field(default=None, description="")
    total_items_count: Optional[StrictInt] = Field(default=None, description="total number of relevant items crawled")
    items_count: Optional[StrictInt] = Field(default=None, description="number of items in the results array")
    items: Optional[List[Optional[BaseOnPageResourceItem]]] = Field(default=None, description="items array")
    __properties: ClassVar[List[str]] = [
        "crawl_progress", 
        "crawl_status", 
        "search_after_token", 
        "current_offset", 
        "total_items_count", 
        "items_count", 
        "items", 
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

        _dict['crawl_progress'] = self.crawl_progress
        _dict['crawl_status'] = self.crawl_status.to_dict() if self.crawl_status else None
        _dict['search_after_token'] = self.search_after_token
        _dict['current_offset'] = self.current_offset
        _dict['total_items_count'] = self.total_items_count
        _dict['items_count'] = self.items_count
        items_items = []
        if self.items:
            for _item in self.items:
                if _item:
                    items_items.append(_item.to_dict())
            _dict['items'] = items_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "crawl_progress": obj.get("crawl_progress"),
            "crawl_status": CrawlStatusInfo.from_dict(obj["crawl_status"]) if obj.get("crawl_status") is not None else None,
            "search_after_token": obj.get("search_after_token"),
            "current_offset": obj.get("current_offset"),
            "total_items_count": obj.get("total_items_count"),
            "items_count": obj.get("items_count"),
            "items": [BaseOnPageResourceItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj