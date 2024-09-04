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

from pydantic import Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.base_serp_element_item import BaseSerpElementItem
from dataforseo_client.models.graph import Graph
from dataforseo_client.models.rectangle import Rectangle
from dataforseo_client.models.table import Table
from typing import Optional, Set
from typing_extensions import Self

class CurrencyBoxSerpElementItem(BaseSerpElementItem):
    """
    CurrencyBoxSerpElementItem
    """ # noqa: E501
    value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="the value of the rating")
    converted_value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="value converted to a requested currency indicates the exact value based on Google Fincance data at the time when our API pulled the results note that exchange rates displayed in the currency_box element may be delayed according to the Google Finance disclaimer")
    currency: Optional[StrictStr] = Field(default=None, description="currency of the listed price ISO code of the currency applied to the price")
    converted_currency: Optional[StrictStr] = Field(default=None, description="converted currency")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    table: Optional[Table] = None
    graph: Optional[Graph] = None
    rectangle: Optional[Rectangle] = None
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "position", "xpath", "value", "converted_value", "currency", "converted_currency", "timestamp", "table", "graph", "rectangle"]

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
        """Create an instance of CurrencyBoxSerpElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of table
        if self.table:
            _dict['table'] = self.table.to_dict()
        # override the default output from pydantic by calling `to_dict()` of graph
        if self.graph:
            _dict['graph'] = self.graph.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rectangle
        if self.rectangle:
            _dict['rectangle'] = self.rectangle.to_dict()
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

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        # set to None if converted_value (nullable) is None
        # and model_fields_set contains the field
        if self.converted_value is None and "converted_value" in self.model_fields_set:
            _dict['converted_value'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if converted_currency (nullable) is None
        # and model_fields_set contains the field
        if self.converted_currency is None and "converted_currency" in self.model_fields_set:
            _dict['converted_currency'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CurrencyBoxSerpElementItem from a dict"""
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
            "value": obj.get("value"),
            "converted_value": obj.get("converted_value"),
            "currency": obj.get("currency"),
            "converted_currency": obj.get("converted_currency"),
            "timestamp": obj.get("timestamp"),
            "table": Table.from_dict(obj["table"]) if obj.get("table") is not None else None,
            "graph": Graph.from_dict(obj["graph"]) if obj.get("graph") is not None else None,
            "rectangle": Rectangle.from_dict(obj["rectangle"]) if obj.get("rectangle") is not None else None
        })
        return _obj


