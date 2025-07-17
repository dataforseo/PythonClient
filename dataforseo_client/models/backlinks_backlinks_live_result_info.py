from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.backlinks_backlinks_live_item import BacklinksBacklinksLiveItem



class BacklinksBacklinksLiveResultInfo(BaseModel):
    """
    BacklinksBacklinksLiveResultInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="target domain in a POST array")
    mode: Optional[StrictStr] = Field(default=None, description="mode specified in a POST array")
    custom_mode: Optional[Dict[str, Optional[Any]]] = Field(default=None, description="custom mode specified in a POST array")
    total_count: Optional[StrictInt] = Field(default=None, description="total amount of results relevant the request")
    items_count: Optional[StrictInt] = Field(default=None, description="the number of results returned in the items array")
    items: Optional[List[Optional[BacklinksBacklinksLiveItem]]] = Field(default=None, description="contains relevant backlinks and referring domains data")
    search_after_token: Optional[StrictStr] = Field(default=None, description="token for subsequent requests. by specifying the unique search_after_token when setting a new task, you will get the subsequent results of the initial task;. search_after_token values are unique for each subsequent task")
    __properties: ClassVar[List[str]] = [
        "target", 
        "mode", 
        "custom_mode", 
        "total_count", 
        "items_count", 
        "items", 
        "search_after_token", 
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

        _dict['target'] = self.target
        _dict['mode'] = self.mode
        _dict['custom_mode'] = self.custom_mode
        _dict['total_count'] = self.total_count
        _dict['items_count'] = self.items_count
        items_items = []
        if self.items:
            for _item in self.items:
                if _item:
                    items_items.append(_item.to_dict())
            _dict['items'] = items_items
        _dict['search_after_token'] = self.search_after_token
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "target": obj.get("target"),
            "mode": obj.get("mode"),
            "custom_mode": obj.get("custom_mode"),
            "total_count": obj.get("total_count"),
            "items_count": obj.get("items_count"),
            "items": [BacklinksBacklinksLiveItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "search_after_token": obj.get("search_after_token"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj