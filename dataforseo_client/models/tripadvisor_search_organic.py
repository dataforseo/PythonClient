from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement



class TripadvisorSearchOrganic(BaseModel):
    """
    TripadvisorSearchOrganic
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank among all the listed results. absolute position among all reviews on the list")
    title: Optional[StrictStr] = Field(default=None, description="name of the business entity")
    url_path: Optional[StrictStr] = Field(default=None, description="URL path of the business entity. URL path to the Tripadvisor page of the business entity. you can use this identifier to collect reviews for the business entity using Tripadvisor Reviews")
    is_sponsored: Optional[StrictBool] = Field(default=None, description="indicates a sponsored placement. if true, related tripadvisor_search_organic item is a paid advertising on Tripadvisor")
    reviews_count: Optional[StrictInt] = Field(default=None, description="the total number of reviews")
    category: Optional[StrictStr] = Field(default=None, description="place category")
    price_rate: Optional[StrictStr] = Field(default=None, description="average price rate")
    rating: Optional[RatingElement] = Field(default=None, description="the rating score of the establishment submitted by the reviewers")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "title", 
        "url_path", 
        "is_sponsored", 
        "reviews_count", 
        "category", 
        "price_rate", 
        "rating", 
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
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['title'] = self.title
        _dict['url_path'] = self.url_path
        _dict['is_sponsored'] = self.is_sponsored
        _dict['reviews_count'] = self.reviews_count
        _dict['category'] = self.category
        _dict['price_rate'] = self.price_rate
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "title": obj.get("title"),
            "url_path": obj.get("url_path"),
            "is_sponsored": obj.get("is_sponsored"),
            "reviews_count": obj.get("reviews_count"),
            "category": obj.get("category"),
            "price_rate": obj.get("price_rate"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj