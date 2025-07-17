from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BusinessListingAggregationInfo(BaseModel):
    """
    BusinessListingAggregationInfo
    """ # noqa: E501
    top_categories: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="the most mentioned related categories. top categories displayed with the number of businesses in each category")
    top_countries: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="the most mentioned counties. country codes with the biggest number of businesses in the category")
    websites_count: Optional[StrictInt] = Field(default=None, description="number of unique websites")
    count: Optional[StrictInt] = Field(default=None, description="number of unique entities")
    top_attributes: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="the most mentioned service details. service details of a business entity displayed in a form of checks and the number of entities mentioning each attribute")
    top_place_topics: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="top keywords mentioned in customer reviews. contains most popular keywords related to products/services mentioned in customer reviews of a business entity and the number of reviews mentioning each keyword")
    __properties: ClassVar[List[str]] = [
        "top_categories", 
        "top_countries", 
        "websites_count", 
        "count", 
        "top_attributes", 
        "top_place_topics", 
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

        _dict['top_categories'] = self.top_categories
        _dict['top_countries'] = self.top_countries
        _dict['websites_count'] = self.websites_count
        _dict['count'] = self.count
        _dict['top_attributes'] = self.top_attributes
        _dict['top_place_topics'] = self.top_place_topics
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "top_categories": obj.get("top_categories"),
            "top_countries": obj.get("top_countries"),
            "websites_count": obj.get("websites_count"),
            "count": obj.get("count"),
            "top_attributes": obj.get("top_attributes"),
            "top_place_topics": obj.get("top_place_topics"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj