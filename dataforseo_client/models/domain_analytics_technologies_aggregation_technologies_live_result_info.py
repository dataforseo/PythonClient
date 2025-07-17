from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.domain_analytics_technologies_aggregation_technologies_live_item import DomainAnalyticsTechnologiesAggregationTechnologiesLiveItem



class DomainAnalyticsTechnologiesAggregationTechnologiesLiveResultInfo(BaseModel):
    """
    DomainAnalyticsTechnologiesAggregationTechnologiesLiveResultInfo
    """ # noqa: E501
    total_count: Optional[StrictInt] = Field(default=None, description="total amount of results in our database relevant to your request")
    items_count: Optional[StrictInt] = Field(default=None, description="the number of results returned in the items array")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned domains")
    items: Optional[List[Optional[DomainAnalyticsTechnologiesAggregationTechnologiesLiveItem]]] = Field(default=None, description="items array")
    __properties: ClassVar[List[str]] = [
        "total_count", 
        "items_count", 
        "offset", 
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

        _dict['total_count'] = self.total_count
        _dict['items_count'] = self.items_count
        _dict['offset'] = self.offset
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
            "total_count": obj.get("total_count"),
            "items_count": obj.get("items_count"),
            "offset": obj.get("offset"),
            "items": [DomainAnalyticsTechnologiesAggregationTechnologiesLiveItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj