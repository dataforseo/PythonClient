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

from pydantic import ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.base_google_finance_ticker_search_serp_element_item import BaseGoogleFinanceTickerSearchSerpElementItem
from typing import Optional, Set
from typing_extensions import Self

class GoogleFinanceAssetPairSerpElementItem(BaseGoogleFinanceTickerSearchSerpElementItem):
    """
    GoogleFinanceAssetPairSerpElementItem
    """ # noqa: E501
    base_symbol: Optional[StrictStr] = Field(default=None, description="identifier of the base asset in a pair example: EUR")
    quote_symbol: Optional[StrictStr] = Field(default=None, description="identifier of the quote asset in a pair example: USD")
    base_display_name: Optional[StrictStr] = Field(default=None, description="full name of the base asset in a pair example: Euro")
    quote_display_name: Optional[StrictStr] = Field(default=None, description="full name of the base asset in a pair example: Euro")
    price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="value of the base asset compared to the quote asset")
    price_delta: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="change in price change in price at a given timestamp")
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "identifier", "displayed_name", "url", "location", "trend", "timestamp", "percentage_delta", "base_symbol", "quote_symbol", "base_display_name", "quote_display_name", "price", "price_delta"]

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
        """Create an instance of GoogleFinanceAssetPairSerpElementItem from a JSON string"""
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

        # set to None if identifier (nullable) is None
        # and model_fields_set contains the field
        if self.identifier is None and "identifier" in self.model_fields_set:
            _dict['identifier'] = None

        # set to None if displayed_name (nullable) is None
        # and model_fields_set contains the field
        if self.displayed_name is None and "displayed_name" in self.model_fields_set:
            _dict['displayed_name'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if location (nullable) is None
        # and model_fields_set contains the field
        if self.location is None and "location" in self.model_fields_set:
            _dict['location'] = None

        # set to None if trend (nullable) is None
        # and model_fields_set contains the field
        if self.trend is None and "trend" in self.model_fields_set:
            _dict['trend'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        # set to None if percentage_delta (nullable) is None
        # and model_fields_set contains the field
        if self.percentage_delta is None and "percentage_delta" in self.model_fields_set:
            _dict['percentage_delta'] = None

        # set to None if base_symbol (nullable) is None
        # and model_fields_set contains the field
        if self.base_symbol is None and "base_symbol" in self.model_fields_set:
            _dict['base_symbol'] = None

        # set to None if quote_symbol (nullable) is None
        # and model_fields_set contains the field
        if self.quote_symbol is None and "quote_symbol" in self.model_fields_set:
            _dict['quote_symbol'] = None

        # set to None if base_display_name (nullable) is None
        # and model_fields_set contains the field
        if self.base_display_name is None and "base_display_name" in self.model_fields_set:
            _dict['base_display_name'] = None

        # set to None if quote_display_name (nullable) is None
        # and model_fields_set contains the field
        if self.quote_display_name is None and "quote_display_name" in self.model_fields_set:
            _dict['quote_display_name'] = None

        # set to None if price (nullable) is None
        # and model_fields_set contains the field
        if self.price is None and "price" in self.model_fields_set:
            _dict['price'] = None

        # set to None if price_delta (nullable) is None
        # and model_fields_set contains the field
        if self.price_delta is None and "price_delta" in self.model_fields_set:
            _dict['price_delta'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GoogleFinanceAssetPairSerpElementItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "identifier": obj.get("identifier"),
            "displayed_name": obj.get("displayed_name"),
            "url": obj.get("url"),
            "location": obj.get("location"),
            "trend": obj.get("trend"),
            "timestamp": obj.get("timestamp"),
            "percentage_delta": obj.get("percentage_delta"),
            "base_symbol": obj.get("base_symbol"),
            "quote_symbol": obj.get("quote_symbol"),
            "base_display_name": obj.get("base_display_name"),
            "quote_display_name": obj.get("quote_display_name"),
            "price": obj.get("price"),
            "price_delta": obj.get("price_delta")
        })
        return _obj


