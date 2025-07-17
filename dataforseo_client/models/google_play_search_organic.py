from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.price_info import PriceInfo



class GooglePlaySearchOrganic(BaseModel):
    """
    GooglePlaySearchOrganic
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    app_id: Optional[StrictStr] = Field(default=None, description="id of the app")
    title: Optional[StrictStr] = Field(default=None, description="title of the app")
    url: Optional[StrictStr] = Field(default=None, description="URL to the app page on Google Play")
    icon: Optional[StrictStr] = Field(default=None, description="URL to the app icon")
    reviews_count: Optional[StrictInt] = Field(default=None, description="the total number of reviews of the app")
    rating: Optional[RatingElement] = Field(default=None, description="average rating of the app")
    is_free: Optional[StrictBool] = Field(default=None, description="indicates whether the app is free")
    price: Optional[PriceInfo] = Field(default=None, description="price of the app")
    developer: Optional[StrictStr] = Field(default=None, description="name of the app developer")
    developer_url: Optional[StrictStr] = Field(default=None, description="URL to the developer page on Google Play")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "app_id", 
        "title", 
        "url", 
        "icon", 
        "reviews_count", 
        "rating", 
        "is_free", 
        "price", 
        "developer", 
        "developer_url", 
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
        _dict['position'] = self.position
        _dict['app_id'] = self.app_id
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['icon'] = self.icon
        _dict['reviews_count'] = self.reviews_count
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['is_free'] = self.is_free
        _dict['price'] = self.price.to_dict() if self.price else None
        _dict['developer'] = self.developer
        _dict['developer_url'] = self.developer_url
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
            "position": obj.get("position"),
            "app_id": obj.get("app_id"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "icon": obj.get("icon"),
            "reviews_count": obj.get("reviews_count"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "is_free": obj.get("is_free"),
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "developer": obj.get("developer"),
            "developer_url": obj.get("developer_url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj