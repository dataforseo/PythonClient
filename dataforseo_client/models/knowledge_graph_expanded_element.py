from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_mode_images_element_info import AiModeImagesElementInfo
from dataforseo_client.models.table import Table



class KnowledgeGraphExpandedElement(BaseModel):
    """
    KnowledgeGraphExpandedElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    featured_title: Optional[StrictStr] = Field(default=None, description="title of a given element")
    url: Optional[StrictStr] = Field(default=None, description="relevant URL")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    title: Optional[StrictStr] = Field(default=None, description="title of the result in SERP")
    snippet: Optional[StrictStr] = Field(default=None, description="text alongside the link title")
    images: Optional[List[Optional[AiModeImagesElementInfo]]] = Field(default=None, description="images of the element")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the result was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    table: Optional[Table] = Field(default=None, description="table present in the element. the header and content of the table present in the element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "featured_title", 
        "url", 
        "domain", 
        "title", 
        "snippet", 
        "images", 
        "timestamp", 
        "table", 
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
        _dict['featured_title'] = self.featured_title
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        _dict['title'] = self.title
        _dict['snippet'] = self.snippet
        images_items = []
        if self.images:
            for _item in self.images:
                if _item:
                    images_items.append(_item.to_dict())
            _dict['images'] = images_items
        _dict['timestamp'] = self.timestamp
        _dict['table'] = self.table.to_dict() if self.table else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "featured_title": obj.get("featured_title"),
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "title": obj.get("title"),
            "snippet": obj.get("snippet"),
            "images": [AiModeImagesElementInfo.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "timestamp": obj.get("timestamp"),
            "table": Table.from_dict(obj["table"]) if obj.get("table") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj