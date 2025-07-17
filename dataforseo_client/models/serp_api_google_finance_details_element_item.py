from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_serp_api_google_finance_element_item import BaseSerpApiGoogleFinanceElementItem



class SerpApiGoogleFinanceDetailsElementItem(BaseSerpApiGoogleFinanceElementItem):
    """
    SerpApiGoogleFinanceDetailsElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    badges: Optional[List[Optional[StrictStr]]] = Field(default=None, description="google finance badges relevant to the element. example: Futures Contract")
    previous_close: Optional[StrictFloat] = Field(default=None, description="value of the previous close")
    start_day_range: Optional[StrictFloat] = Field(default=None, description="value of the start day range")
    end_day_range: Optional[StrictFloat] = Field(default=None, description="value of the end day range")
    start_year_range: Optional[StrictFloat] = Field(default=None, description="value of the start year range")
    end_year_range: Optional[StrictFloat] = Field(default=None, description="value of the end year range")
    market_cap: Optional[StrictFloat] = Field(default=None, description="market cap value")
    volume: Optional[StrictFloat] = Field(default=None, description="total volume value")
    avg_volume: Optional[StrictFloat] = Field(default=None, description="average volume value")
    pe_ratio: Optional[StrictFloat] = Field(default=None, description="price-earnings ratio")
    dividend_yield: Optional[StrictFloat] = Field(default=None, description="dividend yield value")
    primary_exchange: Optional[StrictStr] = Field(default=None, description="primary exchange value")
    ytd_return: Optional[StrictFloat] = Field(default=None, description="year-to-date return value")
    expense_ratio: Optional[StrictFloat] = Field(default=None, description="expense ratio value")
    category: Optional[StrictStr] = Field(default=None, description="category name")
    net_assets: Optional[StrictFloat] = Field(default=None, description="")
    yield_: Optional[StrictFloat] = Field(default=None, description="yield value")
    front_load: Optional[StrictFloat] = Field(default=None, description="front load value")
    market_segment: Optional[StrictStr] = Field(default=None, description="name of the relevant market segment")
    open_interest: Optional[StrictFloat] = Field(default=None, description="open interest value")
    settlement_price: Optional[StrictFloat] = Field(default=None, description="settlement price value")
    cdp_climate_change_score: Optional[StrictStr] = Field(default=None, description="climate change score by carbon disclosure project methodology")
    metrics_currency: Optional[StrictStr] = Field(default=None, description="currency of the metrics")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "badges", 
        "previous_close", 
        "start_day_range", 
        "end_day_range", 
        "start_year_range", 
        "end_year_range", 
        "market_cap", 
        "volume", 
        "avg_volume", 
        "pe_ratio", 
        "dividend_yield", 
        "primary_exchange", 
        "ytd_return", 
        "expense_ratio", 
        "category", 
        "net_assets", 
        "yield", 
        "front_load", 
        "market_segment", 
        "open_interest", 
        "settlement_price", 
        "cdp_climate_change_score", 
        "metrics_currency", 
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
        _dict['badges'] = self.badges
        _dict['previous_close'] = self.previous_close
        _dict['start_day_range'] = self.start_day_range
        _dict['end_day_range'] = self.end_day_range
        _dict['start_year_range'] = self.start_year_range
        _dict['end_year_range'] = self.end_year_range
        _dict['market_cap'] = self.market_cap
        _dict['volume'] = self.volume
        _dict['avg_volume'] = self.avg_volume
        _dict['pe_ratio'] = self.pe_ratio
        _dict['dividend_yield'] = self.dividend_yield
        _dict['primary_exchange'] = self.primary_exchange
        _dict['ytd_return'] = self.ytd_return
        _dict['expense_ratio'] = self.expense_ratio
        _dict['category'] = self.category
        _dict['net_assets'] = self.net_assets
        _dict['yield'] = self.yield_
        _dict['front_load'] = self.front_load
        _dict['market_segment'] = self.market_segment
        _dict['open_interest'] = self.open_interest
        _dict['settlement_price'] = self.settlement_price
        _dict['cdp_climate_change_score'] = self.cdp_climate_change_score
        _dict['metrics_currency'] = self.metrics_currency
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
            "yield_": obj.get("yield"),
            "front_load": obj.get("front_load"),
            "market_segment": obj.get("market_segment"),
            "open_interest": obj.get("open_interest"),
            "settlement_price": obj.get("settlement_price"),
            "cdp_climate_change_score": obj.get("cdp_climate_change_score"),
            "metrics_currency": obj.get("metrics_currency"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj