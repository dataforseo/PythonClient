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
from dataforseo_client.models.delivery_info import DeliveryInfo



class ProductSeller(BaseModel):
    """
    ProductSeller
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="product title")
    url: Optional[StrictStr] = Field(default=None, description="seller url. url of the page where the product is sold")
    seller_rating: Optional[RatingElement] = Field(default=None, description="rating of the seller")
    seller_review_count: Optional[StrictInt] = Field(default=None, description="number of seller reviews. number of reviews on the product seller’s account")
    price: Optional[PriceInfo] = Field(default=None, description="product price. product price details on the seller’s website")
    delivery_info: Optional[DeliveryInfo] = Field(default=None, description="delivery information. product delivery information")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "url", 
        "seller_rating", 
        "seller_review_count", 
        "price", 
        "delivery_info", 
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
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['seller_rating'] = self.seller_rating.to_dict() if self.seller_rating else None
        _dict['seller_review_count'] = self.seller_review_count
        _dict['price'] = self.price.to_dict() if self.price else None
        _dict['delivery_info'] = self.delivery_info.to_dict() if self.delivery_info else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "seller_rating": RatingElement.from_dict(obj["seller_rating"]) if obj.get("seller_rating") is not None else None,
            "seller_review_count": obj.get("seller_review_count"),
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "delivery_info": DeliveryInfo.from_dict(obj["delivery_info"]) if obj.get("delivery_info") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj