from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.delivery_info import DeliveryInfo
from dataforseo_client.models.special_offer_info import SpecialOfferInfo



class GoogleShoppingSponsoredCarouselElement(BaseModel):
    """
    GoogleShoppingSponsoredCarouselElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    xpath: Optional[StrictStr] = Field(default=None, description="XPath of the element")
    title: Optional[StrictStr] = Field(default=None, description="product title")
    tags: Optional[List[Optional[StrictStr]]] = Field(default=None, description="tags assigned to the product")
    seller: Optional[StrictStr] = Field(default=None, description="name of the seller. the name of the company that placed a corresponding product on Google Shopping")
    price: Optional[StrictFloat] = Field(default=None, description="product price. example:. 384.99")
    currency: Optional[StrictStr] = Field(default=None, description="currency in the ISO format. example:. USD")
    product_rating: Optional[RatingElement] = Field(default=None, description="product rating. the product popularity rate based on product reviews")
    product_images: Optional[List[Optional[StrictStr]]] = Field(default=None, description="URLs to the images of the product. the first URL in the array is the featured image of the product")
    shop_ad_aclk: Optional[StrictStr] = Field(default=None, description="unique ad click referral parameter. using this parameter you can get a URL of the advertisement in Google Shopping Sellers Ad URL")
    delivery_info: Optional[DeliveryInfo] = Field(default=None, description="delivery information. delivery information including free and fast delivery date ranges")
    special_offer_info: Optional[SpecialOfferInfo] = Field(default=None, description="special offer from the seller. information on the special offer from the seller, including discount and coupon info")
    __properties: ClassVar[List[str]] = [
        "type", 
        "xpath", 
        "title", 
        "tags", 
        "seller", 
        "price", 
        "currency", 
        "product_rating", 
        "product_images", 
        "shop_ad_aclk", 
        "delivery_info", 
        "special_offer_info", 
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
        _dict['xpath'] = self.xpath
        _dict['title'] = self.title
        _dict['tags'] = self.tags
        _dict['seller'] = self.seller
        _dict['price'] = self.price
        _dict['currency'] = self.currency
        _dict['product_rating'] = self.product_rating.to_dict() if self.product_rating else None
        _dict['product_images'] = self.product_images
        _dict['shop_ad_aclk'] = self.shop_ad_aclk
        _dict['delivery_info'] = self.delivery_info.to_dict() if self.delivery_info else None
        _dict['special_offer_info'] = self.special_offer_info.to_dict() if self.special_offer_info else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "xpath": obj.get("xpath"),
            "title": obj.get("title"),
            "tags": obj.get("tags"),
            "seller": obj.get("seller"),
            "price": obj.get("price"),
            "currency": obj.get("currency"),
            "product_rating": RatingElement.from_dict(obj["product_rating"]) if obj.get("product_rating") is not None else None,
            "product_images": obj.get("product_images"),
            "shop_ad_aclk": obj.get("shop_ad_aclk"),
            "delivery_info": DeliveryInfo.from_dict(obj["delivery_info"]) if obj.get("delivery_info") is not None else None,
            "special_offer_info": SpecialOfferInfo.from_dict(obj["special_offer_info"]) if obj.get("special_offer_info") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj