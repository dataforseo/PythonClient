from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_merchant_google_shopping_sellers_element_item import BaseMerchantGoogleShoppingSellersElementItem
from dataforseo_client.models.rating_element import RatingElement



class GoogleShoppingSellersShopsListElementItem(BaseMerchantGoogleShoppingSellersElementItem):
    """
    GoogleShoppingSellersShopsListElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements found in Google Shopping SERP")
    position: Optional[StrictStr] = Field(default=None, description="alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="XPath of the element")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    title: Optional[StrictStr] = Field(default=None, description="product title")
    url: Optional[StrictStr] = Field(default=None, description="Google Shopping URL forwarding to the product page on the seller’s website. if you want to obtain a URL of the advertisement forwarding to the product page on the seller’s website, please refer to the Google Shopping Sellers Ad URL endpoint")
    details: Optional[StrictStr] = Field(default=None, description="details and special offers. if there are no details, the value will be null")
    base_price: Optional[StrictFloat] = Field(default=None, description="product price without tax and shipping")
    tax: Optional[StrictFloat] = Field(default=None, description="the amount of tax. tax is specified as the actual amount of money, not as the percentage")
    shipping_price: Optional[StrictFloat] = Field(default=None, description="product shipping price")
    total_price: Optional[StrictFloat] = Field(default=None, description="product price including tax and shipping")
    currency: Optional[StrictStr] = Field(default=None, description="currency in the ISO format. example:. USD")
    seller_name: Optional[StrictStr] = Field(default=None, description="name of the seller. the name of the company that placed a corresponding product on Google Shopping")
    rating: Optional[RatingElement] = Field(default=None, description="shop rating. the shop popularity rate based on product reviews")
    shop_ad_aclk: Optional[StrictStr] = Field(default=None, description="unique ad click referral parameter. using this parameter you can get a URL of the advertisement in Google Shopping Sellers Ad URL")
    price_multiplier: Optional[StrictInt] = Field(default=None, description="monthly price multiplier. indicates the number of months covered by the monthly payment for the product")
    product_condition: Optional[StrictStr] = Field(default=None, description="indicated condition of the product. possible values: Used, Refurbished, New, null")
    product_annotation: Optional[StrictStr] = Field(default=None, description="data from annotations and badges with special offers. if there is no annotation for this product, the value will be null. examples: LOW PRICE, SPECIAL OFFER, SALE, PRICE DROP")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "domain", 
        "title", 
        "url", 
        "details", 
        "base_price", 
        "tax", 
        "shipping_price", 
        "total_price", 
        "currency", 
        "seller_name", 
        "rating", 
        "shop_ad_aclk", 
        "price_multiplier", 
        "product_condition", 
        "product_annotation", 
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
        _dict['domain'] = self.domain
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['details'] = self.details
        _dict['base_price'] = self.base_price
        _dict['tax'] = self.tax
        _dict['shipping_price'] = self.shipping_price
        _dict['total_price'] = self.total_price
        _dict['currency'] = self.currency
        _dict['seller_name'] = self.seller_name
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['shop_ad_aclk'] = self.shop_ad_aclk
        _dict['price_multiplier'] = self.price_multiplier
        _dict['product_condition'] = self.product_condition
        _dict['product_annotation'] = self.product_annotation
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
            "domain": obj.get("domain"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "details": obj.get("details"),
            "base_price": obj.get("base_price"),
            "tax": obj.get("tax"),
            "shipping_price": obj.get("shipping_price"),
            "total_price": obj.get("total_price"),
            "currency": obj.get("currency"),
            "seller_name": obj.get("seller_name"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "shop_ad_aclk": obj.get("shop_ad_aclk"),
            "price_multiplier": obj.get("price_multiplier"),
            "product_condition": obj.get("product_condition"),
            "product_annotation": obj.get("product_annotation"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj