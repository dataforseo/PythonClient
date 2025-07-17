from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.tripadvisor_review_search import TripadvisorReviewSearch



class BusinessDataTripadvisorReviewsTaskGetResultInfo(BaseModel):
    """
    BusinessDataTripadvisorReviewsTaskGetResultInfo
    """ # noqa: E501
    url_path: Optional[StrictStr] = Field(default=None, description="URL path received in a POST array")
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    se_domain: Optional[StrictStr] = Field(default=None, description="search engine domain in a POST array")
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to search engine results. you can use it to make sure that we provided accurate results")
    datetime: Optional[StrictStr] = Field(default=None, description="date and time when the result was received. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    title: Optional[StrictStr] = Field(default=None, description="title of the ‘reviews’ element in SERP. the name of the local establishment for which the reviews are collected")
    location: Optional[StrictStr] = Field(default=None, description="location of the local establishment. address of the local establishment for which the reviews are collected")
    reviews_count: Optional[StrictInt] = Field(default=None, description="the total number of reviews")
    rating: Optional[RatingElement] = Field(default=None, description="rating of the corresponding local establishment. popularity rate based on reviews and displayed in SERP")
    rating_distribution: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="rating distribution by votes. the distribution of votes across the rating in the range from 1 to 5")
    items_count: Optional[StrictInt] = Field(default=None, description="the number of reviews items in the results array. you can get more results by using the depth parameter when setting a task")
    items: Optional[List[Optional[TripadvisorReviewSearch]]] = Field(default=None, description="found reviews. you can get more results by using the depth parameter when setting a task")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    __properties: ClassVar[List[str]] = [
        "url_path", 
        "type", 
        "se_domain", 
        "check_url", 
        "datetime", 
        "title", 
        "location", 
        "reviews_count", 
        "rating", 
        "rating_distribution", 
        "items_count", 
        "items", 
        "language_code", 
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

        _dict['url_path'] = self.url_path
        _dict['type'] = self.type
        _dict['se_domain'] = self.se_domain
        _dict['check_url'] = self.check_url
        _dict['datetime'] = self.datetime
        _dict['title'] = self.title
        _dict['location'] = self.location
        _dict['reviews_count'] = self.reviews_count
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['rating_distribution'] = self.rating_distribution
        _dict['items_count'] = self.items_count
        items_items = []
        if self.items:
            for _item in self.items:
                if _item:
                    items_items.append(_item.to_dict())
            _dict['items'] = items_items
        _dict['language_code'] = self.language_code
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url_path": obj.get("url_path"),
            "type": obj.get("type"),
            "se_domain": obj.get("se_domain"),
            "check_url": obj.get("check_url"),
            "datetime": obj.get("datetime"),
            "title": obj.get("title"),
            "location": obj.get("location"),
            "reviews_count": obj.get("reviews_count"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "rating_distribution": obj.get("rating_distribution"),
            "items_count": obj.get("items_count"),
            "items": [TripadvisorReviewSearch.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "language_code": obj.get("language_code"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj