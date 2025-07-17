from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.app_store_reviews_search import AppStoreReviewsSearch



class AppDataAppleAppReviewsTaskGetAdvancedResultInfo(BaseModel):
    """
    AppDataAppleAppReviewsTaskGetAdvancedResultInfo
    """ # noqa: E501
    app_id: Optional[StrictStr] = Field(default=None, description="application id received in a POST array")
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    se_domain: Optional[StrictStr] = Field(default=None, description="search engine domain in a POST array")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to search engine results. you can use it to make sure that we provided accurate results")
    datetime: Optional[StrictStr] = Field(default=None, description="date and time when the result was received. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    title: Optional[StrictStr] = Field(default=None, description="title of the app. title of the application for which the reviews are collected")
    rating: Optional[RatingElement] = Field(default=None, description="rating of the app. rating of the application for which the reviews are collected")
    reviews_count: Optional[StrictInt] = Field(default=None, description="the total number of reviews. in this case, the value will be null as App Store does not indicate the total number of app reviews")
    items_count: Optional[StrictInt] = Field(default=None, description="the number of reviews items in the results array. you can get more results by using the depth parameter when setting a task")
    items: Optional[List[Optional[AppStoreReviewsSearch]]] = Field(default=None, description="found reviews")
    __properties: ClassVar[List[str]] = [
        "app_id", 
        "type", 
        "se_domain", 
        "location_code", 
        "language_code", 
        "check_url", 
        "datetime", 
        "title", 
        "rating", 
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

        _dict['app_id'] = self.app_id
        _dict['type'] = self.type
        _dict['se_domain'] = self.se_domain
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['check_url'] = self.check_url
        _dict['datetime'] = self.datetime
        _dict['title'] = self.title
        _dict['rating'] = self.rating.to_dict() if self.rating else None
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
            "app_id": obj.get("app_id"),
            "type": obj.get("type"),
            "se_domain": obj.get("se_domain"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "check_url": obj.get("check_url"),
            "datetime": obj.get("datetime"),
            "title": obj.get("title"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "reviews_count": obj.get("reviews_count"),
            "items_count": obj.get("items_count"),
            "items": [AppStoreReviewsSearch.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj