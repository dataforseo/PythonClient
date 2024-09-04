# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.base_merchant_serp_element_item import BaseMerchantSerpElementItem
from dataforseo_client.models.rating_element import RatingElement
from typing import Optional, Set
from typing_extensions import Self

class BuyOnGoogleMerchantSerpElementItem(BaseMerchantSerpElementItem):
    """
    BuyOnGoogleMerchantSerpElementItem
    """ # noqa: E501
    xpath: Optional[StrictStr] = Field(default=None, description="XPath of the element")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    title: Optional[StrictStr] = Field(default=None, description="product title")
    url: Optional[StrictStr] = Field(default=None, description="Google Shopping URL forwarding to the product page")
    details: Optional[StrictStr] = Field(default=None, description="details and special offers if there are no details, the value will be null")
    base_price: Optional[StrictInt] = Field(default=None, description="product price without tax and shipping")
    tax: Optional[StrictInt] = Field(default=None, description="the amount of tax tax is specified as the actual amount of money, not as the percentage")
    shipping_price: Optional[StrictInt] = Field(default=None, description="product shipping price")
    total_price: Optional[StrictInt] = Field(default=None, description="product price including tax and shipping")
    currency: Optional[StrictStr] = Field(default=None, description="currency in the ISO format example: USD")
    seller_name: Optional[StrictStr] = Field(default=None, description="name of the seller the name of the company that placed a corresponding product on Google Shopping")
    rating: Optional[RatingElement] = None
    shop_ad_aclk: Optional[StrictStr] = Field(default=None, description="unique ad click referral parameter using this parameter you can get a URL of the advertisement in Google Shopping Sellers Ad URL in this case, the value equals null")
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "position", "xpath", "domain", "title", "url", "details", "base_price", "tax", "shipping_price", "total_price", "currency", "seller_name", "rating", "shop_ad_aclk"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BuyOnGoogleMerchantSerpElementItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of rating
        if self.rating:
            _dict['rating'] = self.rating.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if rank_group (nullable) is None
        # and model_fields_set contains the field
        if self.rank_group is None and "rank_group" in self.model_fields_set:
            _dict['rank_group'] = None

        # set to None if rank_absolute (nullable) is None
        # and model_fields_set contains the field
        if self.rank_absolute is None and "rank_absolute" in self.model_fields_set:
            _dict['rank_absolute'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if xpath (nullable) is None
        # and model_fields_set contains the field
        if self.xpath is None and "xpath" in self.model_fields_set:
            _dict['xpath'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if details (nullable) is None
        # and model_fields_set contains the field
        if self.details is None and "details" in self.model_fields_set:
            _dict['details'] = None

        # set to None if base_price (nullable) is None
        # and model_fields_set contains the field
        if self.base_price is None and "base_price" in self.model_fields_set:
            _dict['base_price'] = None

        # set to None if tax (nullable) is None
        # and model_fields_set contains the field
        if self.tax is None and "tax" in self.model_fields_set:
            _dict['tax'] = None

        # set to None if shipping_price (nullable) is None
        # and model_fields_set contains the field
        if self.shipping_price is None and "shipping_price" in self.model_fields_set:
            _dict['shipping_price'] = None

        # set to None if total_price (nullable) is None
        # and model_fields_set contains the field
        if self.total_price is None and "total_price" in self.model_fields_set:
            _dict['total_price'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if seller_name (nullable) is None
        # and model_fields_set contains the field
        if self.seller_name is None and "seller_name" in self.model_fields_set:
            _dict['seller_name'] = None

        # set to None if shop_ad_aclk (nullable) is None
        # and model_fields_set contains the field
        if self.shop_ad_aclk is None and "shop_ad_aclk" in self.model_fields_set:
            _dict['shop_ad_aclk'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BuyOnGoogleMerchantSerpElementItem from a dict"""
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
            "shop_ad_aclk": obj.get("shop_ad_aclk")
        })
        return _obj


