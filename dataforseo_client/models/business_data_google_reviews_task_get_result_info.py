from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.google_reviews_search import GoogleReviewsSearch



class BusinessDataGoogleReviewsTaskGetResultInfo(BaseModel):
    """
    BusinessDataGoogleReviewsTaskGetResultInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword received in a POST array. keyword is returned with decoded %## (plus character ‘+’ will be decoded to a space character)")
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    se_domain: Optional[StrictStr] = Field(default=None, description="search engine domain in a POST array")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to search engine results. you can use it to make sure that we provided accurate results")
    datetime: Optional[StrictStr] = Field(default=None, description="date and time when the result was received. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    title: Optional[StrictStr] = Field(default=None, description="title of the ‘reviews’ element in SERP. the name of the local establishment for which the reviews are collected")
    sub_title: Optional[StrictStr] = Field(default=None, description="subtitle of the ‘reviews’ element in SERP. additional information (e.g., address) on the ‘reviews’ element for which the reviews are collected")
    rating: Optional[RatingElement] = Field(default=None, description="rating of the corresponding local establishment. popularity rate based on reviews and displayed in SERP")
    feature_id: Optional[StrictStr] = Field(default=None, description="the unique identifier of the ‘reviews’ element in SERP. learn more about the identifier in this help center article")
    place_id: Optional[StrictStr] = Field(default=None, description="unique identifier of a business location assigned by Google. learn more about the identifier in this help center article")
    cid: Optional[StrictStr] = Field(default=None, description="google-defined client id. unique id of a local establishment. learn more about the identifier in this help center article")
    reviews_count: Optional[StrictInt] = Field(default=None, description="the total number of reviews")
    items_count: Optional[StrictInt] = Field(default=None, description="the number of reviews items in the results array. you can get more results by using the depth parameter when setting a task")
    items: Optional[List[Optional[GoogleReviewsSearch]]] = Field(default=None, description="found reviews. you can get more results by using the depth parameter when setting a task")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "type", 
        "se_domain", 
        "location_code", 
        "language_code", 
        "check_url", 
        "datetime", 
        "title", 
        "sub_title", 
        "rating", 
        "feature_id", 
        "place_id", 
        "cid", 
        "reviews_count", 
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

        _dict['keyword'] = self.keyword
        _dict['type'] = self.type
        _dict['se_domain'] = self.se_domain
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['check_url'] = self.check_url
        _dict['datetime'] = self.datetime
        _dict['title'] = self.title
        _dict['sub_title'] = self.sub_title
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['feature_id'] = self.feature_id
        _dict['place_id'] = self.place_id
        _dict['cid'] = self.cid
        _dict['reviews_count'] = self.reviews_count
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
            "keyword": obj.get("keyword"),
            "type": obj.get("type"),
            "se_domain": obj.get("se_domain"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "check_url": obj.get("check_url"),
            "datetime": obj.get("datetime"),
            "title": obj.get("title"),
            "sub_title": obj.get("sub_title"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "feature_id": obj.get("feature_id"),
            "place_id": obj.get("place_id"),
            "cid": obj.get("cid"),
            "reviews_count": obj.get("reviews_count"),
            "items_count": obj.get("items_count"),
            "items": [GoogleReviewsSearch.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj