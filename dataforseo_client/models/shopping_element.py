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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.business_data_rating_info import BusinessDataRatingInfo
from dataforseo_client.models.price_info import PriceInfo
from typing import Optional, Set
from typing_extensions import Self

class ShoppingElement(BaseModel):
    """
    ShoppingElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="title of a given link element")
    price: Optional[PriceInfo] = None
    source: Optional[StrictStr] = Field(default=None, description="source of the element indicates the source of information included in the top_stories_element")
    description: Optional[StrictStr] = Field(default=None, description="description")
    marketplace: Optional[StrictStr] = Field(default=None, description="merchant account provider commerce site that hosts products or websites of individual sellers under the same merchant account example: by Google")
    marketplace_url: Optional[StrictStr] = Field(default=None, description="relevant marketplace URL URL of the page on the marketplace website where the product is hosted")
    url: Optional[StrictStr] = Field(default=None, description="URL")
    rating: Optional[BusinessDataRatingInfo] = None
    __properties: ClassVar[List[str]] = ["type", "title", "price", "source", "description", "marketplace", "marketplace_url", "url", "rating"]

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
        """Create an instance of ShoppingElement from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rating
        if self.rating:
            _dict['rating'] = self.rating.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict['source'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if marketplace (nullable) is None
        # and model_fields_set contains the field
        if self.marketplace is None and "marketplace" in self.model_fields_set:
            _dict['marketplace'] = None

        # set to None if marketplace_url (nullable) is None
        # and model_fields_set contains the field
        if self.marketplace_url is None and "marketplace_url" in self.model_fields_set:
            _dict['marketplace_url'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShoppingElement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "source": obj.get("source"),
            "description": obj.get("description"),
            "marketplace": obj.get("marketplace"),
            "marketplace_url": obj.get("marketplace_url"),
            "url": obj.get("url"),
            "rating": BusinessDataRatingInfo.from_dict(obj["rating"]) if obj.get("rating") is not None else None
        })
        return _obj


