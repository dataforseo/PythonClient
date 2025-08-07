from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.price_info import PriceInfo
from dataforseo_client.models.rating_element import RatingElement



class HotelsPackElement(BaseModel):
    """
    HotelsPackElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    price: Optional[PriceInfo] = Field(default=None, description="price indicated in the element")
    title: Optional[StrictStr] = Field(default=None, description="title of a given link element")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    hotel_identifier: Optional[StrictStr] = Field(default=None, description="unique hotel identifier. unique hotel identifier assigned by Google;. example: 'CgoIjaeSlI6CnNpVEAE'")
    domain: Optional[StrictStr] = Field(default=None, description="website domain")
    url: Optional[StrictStr] = Field(default=None, description="URL")
    is_paid: Optional[StrictBool] = Field(default=None, description="indicates whether the element is an ad")
    rating: Optional[RatingElement] = Field(default=None, description="the item’s rating . the popularity rate based on reviews and displayed in SERP")
    __properties: ClassVar[List[str]] = [
        "type", 
        "price", 
        "title", 
        "description", 
        "hotel_identifier", 
        "domain", 
        "url", 
        "is_paid", 
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
        _dict['price'] = self.price.to_dict() if self.price else None
        _dict['title'] = self.title
        _dict['description'] = self.description
        _dict['hotel_identifier'] = self.hotel_identifier
        _dict['domain'] = self.domain
        _dict['url'] = self.url
        _dict['is_paid'] = self.is_paid
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
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "title": obj.get("title"),
            "description": obj.get("description"),
            "hotel_identifier": obj.get("hotel_identifier"),
            "domain": obj.get("domain"),
            "url": obj.get("url"),
            "is_paid": obj.get("is_paid"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj