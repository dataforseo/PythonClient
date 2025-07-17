from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_merchant_amazon_sellers_element_item import BaseMerchantAmazonSellersElementItem
from dataforseo_client.models.price_info import PriceInfo
from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.amazon_delivery_info import AmazonDeliveryInfo



class MerchantAmazonSellerMainItemSerpElementItem(BaseMerchantAmazonSellersElementItem):
    """
    MerchantAmazonSellerMainItemSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements found in Amazon Sellers SERP")
    position: Optional[StrictStr] = Field(default=None, description="alignment of the element in SERP. possible values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="XPath of the element")
    seller_name: Optional[StrictStr] = Field(default=None, description="business name of the seller")
    seller_url: Optional[StrictStr] = Field(default=None, description="url forwarding to the seller’s page on Amazon")
    ships_from: Optional[StrictStr] = Field(default=None, description="sender company name")
    price: Optional[PriceInfo] = Field(default=None, description="product pricing details. if there are no details, the value will be null")
    rating: Optional[RatingElement] = Field(default=None, description="seller rating details. seller popularity rate based on customer reviews")
    condition: Optional[StrictStr] = Field(default=None, description="product condition. condition of the product offered by the seller")
    condition_description: Optional[StrictStr] = Field(default=None, description="product condition details. expanded details on the condition of the product offered by the seller")
    delivery_info: Optional[AmazonDeliveryInfo] = Field(default=None, description="delivery information. delivery information including free and fast delivery date ranges")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "seller_name", 
        "seller_url", 
        "ships_from", 
        "price", 
        "rating", 
        "condition", 
        "condition_description", 
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
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
        _dict['seller_name'] = self.seller_name
        _dict['seller_url'] = self.seller_url
        _dict['ships_from'] = self.ships_from
        _dict['price'] = self.price.to_dict() if self.price else None
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['condition'] = self.condition
        _dict['condition_description'] = self.condition_description
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
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "seller_name": obj.get("seller_name"),
            "seller_url": obj.get("seller_url"),
            "ships_from": obj.get("ships_from"),
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "condition": obj.get("condition"),
            "condition_description": obj.get("condition_description"),
            "delivery_info": AmazonDeliveryInfo.from_dict(obj["delivery_info"]) if obj.get("delivery_info") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj