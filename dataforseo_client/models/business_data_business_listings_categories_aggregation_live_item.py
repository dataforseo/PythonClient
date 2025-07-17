from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.business_listing_aggregation_info import BusinessListingAggregationInfo



class BusinessDataBusinessListingsCategoriesAggregationLiveItem(BaseModel):
    """
    BusinessDataBusinessListingsCategoriesAggregationLiveItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    categories: Optional[List[Optional[StrictStr]]] = Field(default=None, description="business categories. Google My Business general category that best describes the cluster of related categories")
    aggregation: Optional[BusinessListingAggregationInfo] = Field(default=None, description="aggregation of the category")
    __properties: ClassVar[List[str]] = [
        "type", 
        "categories", 
        "aggregation", 
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
        _dict['categories'] = self.categories
        _dict['aggregation'] = self.aggregation.to_dict() if self.aggregation else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "categories": obj.get("categories"),
            "aggregation": BusinessListingAggregationInfo.from_dict(obj["aggregation"]) if obj.get("aggregation") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj