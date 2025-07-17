from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.backlinks_referring_networks_live_item import BacklinksReferringNetworksLiveItem



class BacklinksReferringNetworksLiveResultInfo(BaseModel):
    """
    BacklinksReferringNetworksLiveResultInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="target in a POST array")
    total_count: Optional[StrictInt] = Field(default=None, description="total number of relevant items in the database")
    items_count: Optional[StrictInt] = Field(default=None, description="number of items in the items array")
    items: Optional[List[Optional[BacklinksReferringNetworksLiveItem]]] = Field(default=None, description="items array")
    __properties: ClassVar[List[str]] = [
        "target", 
        "total_count", 
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

        _dict['target'] = self.target
        _dict['total_count'] = self.total_count
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
            "target": obj.get("target"),
            "total_count": obj.get("total_count"),
            "items_count": obj.get("items_count"),
            "items": [BacklinksReferringNetworksLiveItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj