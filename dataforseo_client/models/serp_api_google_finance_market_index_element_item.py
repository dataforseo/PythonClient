from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_serp_api_google_finance_ticker_search_element_item import BaseSerpApiGoogleFinanceTickerSearchElementItem



class SerpApiGoogleFinanceMarketIndexElementItem(BaseSerpApiGoogleFinanceTickerSearchElementItem):
    """
    SerpApiGoogleFinanceMarketIndexElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    identifier: Optional[StrictStr] = Field(default=None, description="identifier of the element. full identifier of the element that consists from ticker and market_identifier. example: PX1:INDEXDB")
    displayed_name: Optional[StrictStr] = Field(default=None, description="name of the market index as displayed on Google Finance. example: CAC 40")
    url: Optional[StrictStr] = Field(default=None, description="URL to the page of the market index on Google Finance")
    location: Optional[StrictStr] = Field(default=None, description="location of the market index. example: Europe/Paris")
    trend: Optional[StrictStr] = Field(default=None, description="growth trend of the market index. possible values: up, down, stable")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time of the value readout. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2025-02-10 09:40:00 +00:00")
    percentage_delta: Optional[StrictFloat] = Field(default=None, description="percentage of change in value of the market index")
    ticker: Optional[StrictStr] = Field(default=None, description="ticker of the market index. example: DAX")
    market_identifier: Optional[StrictStr] = Field(default=None, description="market identifier. example: INDEXDB")
    index_value: Optional[StrictFloat] = Field(default=None, description="value of the market index. numerical value of the index at a given timestamp")
    index_value_delta: Optional[StrictFloat] = Field(default=None, description="change in value of the market index. change in the index_value at a given timestamp")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "identifier", 
        "displayed_name", 
        "url", 
        "location", 
        "trend", 
        "timestamp", 
        "percentage_delta", 
        "ticker", 
        "market_identifier", 
        "index_value", 
        "index_value_delta", 
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
        _dict['identifier'] = self.identifier
        _dict['displayed_name'] = self.displayed_name
        _dict['url'] = self.url
        _dict['location'] = self.location
        _dict['trend'] = self.trend
        _dict['timestamp'] = self.timestamp
        _dict['percentage_delta'] = self.percentage_delta
        _dict['ticker'] = self.ticker
        _dict['market_identifier'] = self.market_identifier
        _dict['index_value'] = self.index_value
        _dict['index_value_delta'] = self.index_value_delta
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
            "identifier": obj.get("identifier"),
            "displayed_name": obj.get("displayed_name"),
            "url": obj.get("url"),
            "location": obj.get("location"),
            "trend": obj.get("trend"),
            "timestamp": obj.get("timestamp"),
            "percentage_delta": obj.get("percentage_delta"),
            "ticker": obj.get("ticker"),
            "market_identifier": obj.get("market_identifier"),
            "index_value": obj.get("index_value"),
            "index_value_delta": obj.get("index_value_delta"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj