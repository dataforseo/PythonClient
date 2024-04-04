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

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.delivery_info import DeliveryInfo
from dataforseo_client.models.price_info import PriceInfo
from dataforseo_client.models.rating_element import RatingElement
from typing import Optional, Set
from typing_extensions import Self

class ProductSeller(BaseModel):
    """
    ProductSeller
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="product title")
    url: Optional[StrictStr] = Field(default=None, description="seller url url of the page where the product is sold")
    seller_rating: Optional[RatingElement] = None
    seller_review_count: Optional[StrictInt] = Field(default=None, description="number of seller reviews number of reviews on the product seller’s account")
    price: Optional[PriceInfo] = None
    delivery_info: Optional[DeliveryInfo] = None
    __properties: ClassVar[List[str]] = ["type", "title", "url", "seller_rating", "seller_review_count", "price", "delivery_info"]

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
        """Create an instance of ProductSeller from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of seller_rating
        if self.seller_rating:
            _dict['seller_rating'] = self.seller_rating.to_dict()
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of delivery_info
        if self.delivery_info:
            _dict['delivery_info'] = self.delivery_info.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if seller_review_count (nullable) is None
        # and model_fields_set contains the field
        if self.seller_review_count is None and "seller_review_count" in self.model_fields_set:
            _dict['seller_review_count'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProductSeller from a dict"""
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
            "delivery_info": DeliveryInfo.from_dict(obj["delivery_info"]) if obj.get("delivery_info") is not None else None
        })
        return _obj


