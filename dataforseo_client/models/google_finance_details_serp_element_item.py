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
from dataforseo_client.models.base_google_finance_serp_element_item import BaseGoogleFinanceSerpElementItem
from typing import Optional, Set
from typing_extensions import Self

class GoogleFinanceDetailsSerpElementItem(BaseGoogleFinanceSerpElementItem):
    """
    GoogleFinanceDetailsSerpElementItem
    """ # noqa: E501
    rank_group: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="absolute rank in SERP absolute position among all the elements in SERP")
    badges: Optional[List[Optional[StrictStr]]] = Field(default=None, description="google finance badges relevant to the element example: Futures Contract")
    previous_close: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="value of the previous close")
    start_day_range: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="value of the start day range")
    end_day_range: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="value of the end day range")
    start_year_range: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="value of the start year range")
    end_year_range: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="value of the end year range")
    market_cap: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="market cap value")
    volume: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="total volume value")
    avg_volume: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="average volume value")
    pe_ratio: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="price-earnings ratio")
    dividend_yield: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="dividend yield value")
    primary_exchange: Optional[StrictStr] = Field(default=None, description="primary exchange value")
    ytd_return: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="year-to-date return value")
    expense_ratio: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="expense ratio value")
    category: Optional[StrictStr] = Field(default=None, description="category name")
    net_assets: Optional[Union[StrictFloat, StrictInt]] = None
    var_yield: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="yield value", alias="yield")
    front_load: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="front load value")
    market_segment: Optional[StrictStr] = Field(default=None, description="name of the relevant market segment")
    open_interest: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="open interest value")
    settlement_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="settlement price value")
    cdp_climate_change_score: Optional[StrictStr] = Field(default=None, description="climate change score by carbon disclosure project methodology")
    metrics_currency: Optional[StrictStr] = Field(default=None, description="currency of the metrics")
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "badges", "previous_close", "start_day_range", "end_day_range", "start_year_range", "end_year_range", "market_cap", "volume", "avg_volume", "pe_ratio", "dividend_yield", "primary_exchange", "ytd_return", "expense_ratio", "category", "net_assets", "yield", "front_load", "market_segment", "open_interest", "settlement_price", "cdp_climate_change_score", "metrics_currency"]

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
        """Create an instance of GoogleFinanceDetailsSerpElementItem from a JSON string"""
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

        # set to None if badges (nullable) is None
        # and model_fields_set contains the field
        if self.badges is None and "badges" in self.model_fields_set:
            _dict['badges'] = None

        # set to None if previous_close (nullable) is None
        # and model_fields_set contains the field
        if self.previous_close is None and "previous_close" in self.model_fields_set:
            _dict['previous_close'] = None

        # set to None if start_day_range (nullable) is None
        # and model_fields_set contains the field
        if self.start_day_range is None and "start_day_range" in self.model_fields_set:
            _dict['start_day_range'] = None

        # set to None if end_day_range (nullable) is None
        # and model_fields_set contains the field
        if self.end_day_range is None and "end_day_range" in self.model_fields_set:
            _dict['end_day_range'] = None

        # set to None if start_year_range (nullable) is None
        # and model_fields_set contains the field
        if self.start_year_range is None and "start_year_range" in self.model_fields_set:
            _dict['start_year_range'] = None

        # set to None if end_year_range (nullable) is None
        # and model_fields_set contains the field
        if self.end_year_range is None and "end_year_range" in self.model_fields_set:
            _dict['end_year_range'] = None

        # set to None if market_cap (nullable) is None
        # and model_fields_set contains the field
        if self.market_cap is None and "market_cap" in self.model_fields_set:
            _dict['market_cap'] = None

        # set to None if volume (nullable) is None
        # and model_fields_set contains the field
        if self.volume is None and "volume" in self.model_fields_set:
            _dict['volume'] = None

        # set to None if avg_volume (nullable) is None
        # and model_fields_set contains the field
        if self.avg_volume is None and "avg_volume" in self.model_fields_set:
            _dict['avg_volume'] = None

        # set to None if pe_ratio (nullable) is None
        # and model_fields_set contains the field
        if self.pe_ratio is None and "pe_ratio" in self.model_fields_set:
            _dict['pe_ratio'] = None

        # set to None if dividend_yield (nullable) is None
        # and model_fields_set contains the field
        if self.dividend_yield is None and "dividend_yield" in self.model_fields_set:
            _dict['dividend_yield'] = None

        # set to None if primary_exchange (nullable) is None
        # and model_fields_set contains the field
        if self.primary_exchange is None and "primary_exchange" in self.model_fields_set:
            _dict['primary_exchange'] = None

        # set to None if ytd_return (nullable) is None
        # and model_fields_set contains the field
        if self.ytd_return is None and "ytd_return" in self.model_fields_set:
            _dict['ytd_return'] = None

        # set to None if expense_ratio (nullable) is None
        # and model_fields_set contains the field
        if self.expense_ratio is None and "expense_ratio" in self.model_fields_set:
            _dict['expense_ratio'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if net_assets (nullable) is None
        # and model_fields_set contains the field
        if self.net_assets is None and "net_assets" in self.model_fields_set:
            _dict['net_assets'] = None

        # set to None if var_yield (nullable) is None
        # and model_fields_set contains the field
        if self.var_yield is None and "var_yield" in self.model_fields_set:
            _dict['yield'] = None

        # set to None if front_load (nullable) is None
        # and model_fields_set contains the field
        if self.front_load is None and "front_load" in self.model_fields_set:
            _dict['front_load'] = None

        # set to None if market_segment (nullable) is None
        # and model_fields_set contains the field
        if self.market_segment is None and "market_segment" in self.model_fields_set:
            _dict['market_segment'] = None

        # set to None if open_interest (nullable) is None
        # and model_fields_set contains the field
        if self.open_interest is None and "open_interest" in self.model_fields_set:
            _dict['open_interest'] = None

        # set to None if settlement_price (nullable) is None
        # and model_fields_set contains the field
        if self.settlement_price is None and "settlement_price" in self.model_fields_set:
            _dict['settlement_price'] = None

        # set to None if cdp_climate_change_score (nullable) is None
        # and model_fields_set contains the field
        if self.cdp_climate_change_score is None and "cdp_climate_change_score" in self.model_fields_set:
            _dict['cdp_climate_change_score'] = None

        # set to None if metrics_currency (nullable) is None
        # and model_fields_set contains the field
        if self.metrics_currency is None and "metrics_currency" in self.model_fields_set:
            _dict['metrics_currency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GoogleFinanceDetailsSerpElementItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "badges": obj.get("badges"),
            "previous_close": obj.get("previous_close"),
            "start_day_range": obj.get("start_day_range"),
            "end_day_range": obj.get("end_day_range"),
            "start_year_range": obj.get("start_year_range"),
            "end_year_range": obj.get("end_year_range"),
            "market_cap": obj.get("market_cap"),
            "volume": obj.get("volume"),
            "avg_volume": obj.get("avg_volume"),
            "pe_ratio": obj.get("pe_ratio"),
            "dividend_yield": obj.get("dividend_yield"),
            "primary_exchange": obj.get("primary_exchange"),
            "ytd_return": obj.get("ytd_return"),
            "expense_ratio": obj.get("expense_ratio"),
            "category": obj.get("category"),
            "net_assets": obj.get("net_assets"),
            "yield": obj.get("yield"),
            "front_load": obj.get("front_load"),
            "market_segment": obj.get("market_segment"),
            "open_interest": obj.get("open_interest"),
            "settlement_price": obj.get("settlement_price"),
            "cdp_climate_change_score": obj.get("cdp_climate_change_score"),
            "metrics_currency": obj.get("metrics_currency")
        })
        return _obj


