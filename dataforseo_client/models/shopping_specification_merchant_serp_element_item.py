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

from pydantic import Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.base_merchant_serp_element_item import BaseMerchantSerpElementItem
from typing import Optional, Set
from typing_extensions import Self

class ShoppingSpecificationMerchantSerpElementItem(BaseMerchantSerpElementItem):
    """
    ShoppingSpecificationMerchantSerpElementItem
    """ # noqa: E501
    xpath: Optional[StrictStr] = Field(default=None, description="XPath of the element")
    block_name: Optional[StrictStr] = Field(default=None, description="name of the block of product attributes indicates the name of the product specification section in which the related element is listed")
    specification_name: Optional[StrictStr] = Field(default=None, description="product attribute attribute name of the product data specification")
    specification_value: Optional[StrictStr] = Field(default=None, description="content of the specification")
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "position", "xpath", "block_name", "specification_name", "specification_value"]

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
        """Create an instance of ShoppingSpecificationMerchantSerpElementItem from a JSON string"""
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

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if xpath (nullable) is None
        # and model_fields_set contains the field
        if self.xpath is None and "xpath" in self.model_fields_set:
            _dict['xpath'] = None

        # set to None if block_name (nullable) is None
        # and model_fields_set contains the field
        if self.block_name is None and "block_name" in self.model_fields_set:
            _dict['block_name'] = None

        # set to None if specification_name (nullable) is None
        # and model_fields_set contains the field
        if self.specification_name is None and "specification_name" in self.model_fields_set:
            _dict['specification_name'] = None

        # set to None if specification_value (nullable) is None
        # and model_fields_set contains the field
        if self.specification_value is None and "specification_value" in self.model_fields_set:
            _dict['specification_value'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ShoppingSpecificationMerchantSerpElementItem from a dict"""
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
            "block_name": obj.get("block_name"),
            "specification_name": obj.get("specification_name"),
            "specification_value": obj.get("specification_value")
        })
        return _obj


