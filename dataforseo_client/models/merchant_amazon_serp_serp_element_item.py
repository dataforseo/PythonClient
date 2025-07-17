from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.amazon_delivery_info import AmazonDeliveryInfo
from dataforseo_client.models.base_merchant_amazon_element_item import BaseMerchantAmazonElementItem



class MerchantAmazonSerpSerpElementItem(BaseMerchantAmazonElementItem):
    """
    MerchantAmazonSerpSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements found in Amazon SERP")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    domain: Optional[StrictStr] = Field(default=None, description="Amazon domain")
    title: Optional[StrictStr] = Field(default=None, description="product title")
    url: Optional[StrictStr] = Field(default=None, description="the URL of the product page")
    image_url: Optional[StrictStr] = Field(default=None, description="URL of the product image featured in the results")
    bought_past_month: Optional[StrictInt] = Field(default=None, description="number of product purchases in the past month")
    price_from: Optional[StrictFloat] = Field(default=None, description="the regular price of a product. example:. 49.98")
    price_to: Optional[StrictFloat] = Field(default=None, description="the upper limit of the product price range. example:. 384.99")
    currency: Optional[StrictStr] = Field(default=None, description="currency in the ISO format. example:. USD")
    special_offers: Optional[List[Optional[StrictStr]]] = Field(default=None, description="special offer details. contains special offer details, including coupon and Subscribe & Save discounts")
    data_asin: Optional[StrictStr] = Field(default=None, description="unique product identifier on Amazon. note that there is no full list of possible values as the data_asin is a dynamic value assigned by Amazon. example:. B07G82D89J")
    rating: Optional[RatingElement] = Field(default=None, description="product rating info")
    is_amazon_choice: Optional[StrictBool] = Field(default=None, description="“Amazon’s choice” label. if the value is true, the product is marked with the “Amazon’s choice” label")
    is_best_seller: Optional[StrictBool] = Field(default=None, description="“Best Seller” label. if the value is true, the product is marked with the “Best Seller” label")
    delivery_info: Optional[AmazonDeliveryInfo] = Field(default=None, description="delivery information. delivery information including free and fast delivery date ranges")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "xpath", 
        "domain", 
        "title", 
        "url", 
        "image_url", 
        "bought_past_month", 
        "price_from", 
        "price_to", 
        "currency", 
        "special_offers", 
        "data_asin", 
        "rating", 
        "is_amazon_choice", 
        "is_best_seller", 
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
        _dict['xpath'] = self.xpath
        _dict['domain'] = self.domain
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['image_url'] = self.image_url
        _dict['bought_past_month'] = self.bought_past_month
        _dict['price_from'] = self.price_from
        _dict['price_to'] = self.price_to
        _dict['currency'] = self.currency
        _dict['special_offers'] = self.special_offers
        _dict['data_asin'] = self.data_asin
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['is_amazon_choice'] = self.is_amazon_choice
        _dict['is_best_seller'] = self.is_best_seller
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
            "xpath": obj.get("xpath"),
            "domain": obj.get("domain"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "image_url": obj.get("image_url"),
            "bought_past_month": obj.get("bought_past_month"),
            "price_from": obj.get("price_from"),
            "price_to": obj.get("price_to"),
            "currency": obj.get("currency"),
            "special_offers": obj.get("special_offers"),
            "data_asin": obj.get("data_asin"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "is_amazon_choice": obj.get("is_amazon_choice"),
            "is_best_seller": obj.get("is_best_seller"),
            "delivery_info": AmazonDeliveryInfo.from_dict(obj["delivery_info"]) if obj.get("delivery_info") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj