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

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class PriceInfo(BaseModel):
    """
    PriceInfo
    """ # noqa: E501
    current: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="current price indicates the current price of the product or service featured in the result")
    regular: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="regular price indicates the regular price of the product or service with no discounts applied")
    max_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="the maximum price the maximum price of the product or service as indicated in the result")
    currency: Optional[StrictStr] = Field(default=None, description="currency of the listed price ISO code of the currency applied to the price")
    is_price_range: Optional[StrictBool] = Field(default=None, description="price is provided as a range indicates whether a price is provided in a range")
    displayed_price: Optional[StrictStr] = Field(default=None, description="price string in the result raw price string as provided in the result")
    __properties: ClassVar[List[str]] = ["current", "regular", "max_value", "currency", "is_price_range", "displayed_price"]

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
        """Create an instance of PriceInfo from a JSON string"""
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
        # set to None if current (nullable) is None
        # and model_fields_set contains the field
        if self.current is None and "current" in self.model_fields_set:
            _dict['current'] = None

        # set to None if regular (nullable) is None
        # and model_fields_set contains the field
        if self.regular is None and "regular" in self.model_fields_set:
            _dict['regular'] = None

        # set to None if max_value (nullable) is None
        # and model_fields_set contains the field
        if self.max_value is None and "max_value" in self.model_fields_set:
            _dict['max_value'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if is_price_range (nullable) is None
        # and model_fields_set contains the field
        if self.is_price_range is None and "is_price_range" in self.model_fields_set:
            _dict['is_price_range'] = None

        # set to None if displayed_price (nullable) is None
        # and model_fields_set contains the field
        if self.displayed_price is None and "displayed_price" in self.model_fields_set:
            _dict['displayed_price'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PriceInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "current": obj.get("current"),
            "regular": obj.get("regular"),
            "max_value": obj.get("max_value"),
            "currency": obj.get("currency"),
            "is_price_range": obj.get("is_price_range"),
            "displayed_price": obj.get("displayed_price")
        })
        return _obj


