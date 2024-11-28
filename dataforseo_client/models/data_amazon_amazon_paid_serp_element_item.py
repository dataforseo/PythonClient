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

from pydantic import ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.amazon_delivery_info import AmazonDeliveryInfo
from dataforseo_client.models.base_amazon_serp_element_item import BaseAmazonSerpElementItem
from dataforseo_client.models.rating_element import RatingElement
from typing import Optional, Set
from typing_extensions import Self

class DataAmazonAmazonPaidSerpElementItem(BaseAmazonSerpElementItem):
    """
    DataAmazonAmazonPaidSerpElementItem
    """ # noqa: E501
    domain: Optional[StrictStr] = Field(default=None, description="Amazon domain")
    title: Optional[StrictStr] = Field(default=None, description="product title")
    url: Optional[StrictStr] = Field(default=None, description="the URL of the product page")
    image_url: Optional[StrictStr] = Field(default=None, description="URL of the product image featured in the results")
    bought_past_month: Optional[StrictInt] = Field(default=None, description="number of product purchases in the past month")
    price_from: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="the regular price of a product example: 49.98")
    price_to: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="the upper limit of the product price range example: 384.99")
    currency: Optional[StrictStr] = Field(default=None, description="currency in the ISO format example: USD")
    special_offers: Optional[List[Optional[StrictStr]]] = Field(default=None, description="special offer details contains special offer details, including coupon and Subscribe & Save discounts")
    data_asin: Optional[StrictStr] = Field(default=None, description="unique product identifier on Amazon note that there is no full list of possible values as the data_asin is a dynamic value assigned by Amazon example: B07G82D89J")
    rating: Optional[RatingElement] = None
    is_amazon_choice: Optional[StrictBool] = Field(default=None, description="“Amazon’s choice” label if the value is true, the product is marked with the “Amazon’s choice” label")
    is_best_seller: Optional[StrictBool] = Field(default=None, description="“Best Seller” label if the value is true, the product is marked with the “Best Seller” label")
    delivery_info: Optional[AmazonDeliveryInfo] = None
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "xpath", "domain", "title", "url", "image_url", "bought_past_month", "price_from", "price_to", "currency", "special_offers", "data_asin", "rating", "is_amazon_choice", "is_best_seller", "delivery_info"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DataAmazonAmazonPaidSerpElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of delivery_info
        if self.delivery_info:
            _dict['delivery_info'] = self.delivery_info.to_dict()
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

        # set to None if image_url (nullable) is None
        # and model_fields_set contains the field
        if self.image_url is None and "image_url" in self.model_fields_set:
            _dict['image_url'] = None

        # set to None if bought_past_month (nullable) is None
        # and model_fields_set contains the field
        if self.bought_past_month is None and "bought_past_month" in self.model_fields_set:
            _dict['bought_past_month'] = None

        # set to None if price_from (nullable) is None
        # and model_fields_set contains the field
        if self.price_from is None and "price_from" in self.model_fields_set:
            _dict['price_from'] = None

        # set to None if price_to (nullable) is None
        # and model_fields_set contains the field
        if self.price_to is None and "price_to" in self.model_fields_set:
            _dict['price_to'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if special_offers (nullable) is None
        # and model_fields_set contains the field
        if self.special_offers is None and "special_offers" in self.model_fields_set:
            _dict['special_offers'] = None

        # set to None if data_asin (nullable) is None
        # and model_fields_set contains the field
        if self.data_asin is None and "data_asin" in self.model_fields_set:
            _dict['data_asin'] = None

        # set to None if is_amazon_choice (nullable) is None
        # and model_fields_set contains the field
        if self.is_amazon_choice is None and "is_amazon_choice" in self.model_fields_set:
            _dict['is_amazon_choice'] = None

        # set to None if is_best_seller (nullable) is None
        # and model_fields_set contains the field
        if self.is_best_seller is None and "is_best_seller" in self.model_fields_set:
            _dict['is_best_seller'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataAmazonAmazonPaidSerpElementItem from a dict"""
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
            "delivery_info": AmazonDeliveryInfo.from_dict(obj["delivery_info"]) if obj.get("delivery_info") is not None else None
        })
        return _obj


