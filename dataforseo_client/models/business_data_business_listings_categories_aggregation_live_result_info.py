from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.business_data_business_listings_categories_aggregation_live_item import BusinessDataBusinessListingsCategoriesAggregationLiveItem



class BusinessDataBusinessListingsCategoriesAggregationLiveResultInfo(BaseModel):
    """
    BusinessDataBusinessListingsCategoriesAggregationLiveResultInfo
    """ # noqa: E501
    total_count: Optional[StrictInt] = Field(default=None, description="total number of results in our database relevant to your request")
    count: Optional[StrictInt] = Field(default=None, description="item types. the number of items in the items array")
    offset: Optional[StrictStr] = Field(default=None, description="offset in the results array of returned categories")
    offset_token: Optional[StrictStr] = Field(default=None, description="token for subsequent requests. by specifying the unique offset_token when setting a new task, you will get the subsequent results of the initial task;. offset_token values are unique for each subsequent task")
    items: Optional[List[Optional[BusinessDataBusinessListingsCategoriesAggregationLiveItem]]] = Field(default=None, description="encountered item types. types of search engine results encountered in the items array;. possible item types: business_category")
    __properties: ClassVar[List[str]] = [
        "total_count", 
        "count", 
        "offset", 
        "offset_token", 
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
        _dict['count'] = self.count
        _dict['offset'] = self.offset
        _dict['offset_token'] = self.offset_token
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
            "count": obj.get("count"),
            "offset": obj.get("offset"),
            "offset_token": obj.get("offset_token"),
            "items": [BusinessDataBusinessListingsCategoriesAggregationLiveItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj