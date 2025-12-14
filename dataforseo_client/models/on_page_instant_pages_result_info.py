from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_on_page_resource_item import BaseOnPageResourceItem



class OnPageInstantPagesResultInfo(BaseModel):
    """
    OnPageInstantPagesResultInfo
    """ # noqa: E501
    crawl_progress: Optional[StrictStr] = Field(default=None, description=r"status of the crawling session. possible values: in_progress, finished")
    crawl_status: Optional[Any] = Field(default=None, description=r"details of the crawling session. in this case the value will be null")
    crawl_gateway_address: Optional[StrictStr] = Field(default=None, description=r"crawler ip address. displays the IP address used by the crawler to initiate the current crawling session. you can find the full list of IPs used by our crawler in the Overview section")
    items_count: Optional[StrictInt] = Field(default=None, description=r"number of items in the results array")
    items: Optional[List[Optional[BaseOnPageResourceItem]]] = Field(default=None, description=r"items array")
    __properties: ClassVar[List[str]] = [
        "crawl_progress", 
        "crawl_status", 
        "crawl_gateway_address", 
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
        _dict['crawl_status'] = self.crawl_status
        _dict['crawl_gateway_address'] = self.crawl_gateway_address
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
            "crawl_status": obj.get("crawl_status"),
            "crawl_gateway_address": obj.get("crawl_gateway_address"),
            "items_count": obj.get("items_count"),
            "items": [BaseOnPageResourceItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj