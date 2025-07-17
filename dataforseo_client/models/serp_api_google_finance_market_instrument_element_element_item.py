from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_serp_api_google_finance_element_item import BaseSerpApiGoogleFinanceElementItem



class SerpApiGoogleFinanceMarketInstrumentElementElementItem(BaseSerpApiGoogleFinanceElementItem):
    """
    SerpApiGoogleFinanceMarketInstrumentElementElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    ticker: Optional[StrictStr] = Field(default=None, description="ticker of the market index. example: DAX")
    price: Optional[StrictFloat] = Field(default=None, description="value of the base asset compared to the quote asset")
    price_delta: Optional[StrictFloat] = Field(default=None, description="change in price. change in price at a given timestamp")
    price_currency: Optional[StrictStr] = Field(default=None, description="price currency. example: USD")
    identifier: Optional[StrictStr] = Field(default=None, description="identifier of the element. full identifier of the element that consists from ticker and market_identifier. example: PX1:INDEXDB")
    displayed_name: Optional[StrictStr] = Field(default=None, description="name of the market index as displayed on Google Finance. example: CAC 40")
    url: Optional[StrictStr] = Field(default=None, description="URL to the page of the market index on Google Finance")
    location: Optional[StrictStr] = Field(default=None, description="location of the market index. example: Europe/Paris")
    trend: Optional[StrictStr] = Field(default=None, description="growth trend of the market index. possible values: up, down, stable")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time of the value readout. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2025-02-10 09:40:00 +00:00")
    percentage_delta: Optional[StrictFloat] = Field(default=None, description="percentage of change in value of the market index")
    __properties: ClassVar[List[str]] = [
        "type", 
        "ticker", 
        "price", 
        "price_delta", 
        "price_currency", 
        "identifier", 
        "displayed_name", 
        "url", 
        "location", 
        "trend", 
        "timestamp", 
        "percentage_delta", 
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
        _dict['ticker'] = self.ticker
        _dict['price'] = self.price
        _dict['price_delta'] = self.price_delta
        _dict['price_currency'] = self.price_currency
        _dict['identifier'] = self.identifier
        _dict['displayed_name'] = self.displayed_name
        _dict['url'] = self.url
        _dict['location'] = self.location
        _dict['trend'] = self.trend
        _dict['timestamp'] = self.timestamp
        _dict['percentage_delta'] = self.percentage_delta
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "ticker": obj.get("ticker"),
            "price": obj.get("price"),
            "price_delta": obj.get("price_delta"),
            "price_currency": obj.get("price_currency"),
            "identifier": obj.get("identifier"),
            "displayed_name": obj.get("displayed_name"),
            "url": obj.get("url"),
            "location": obj.get("location"),
            "trend": obj.get("trend"),
            "timestamp": obj.get("timestamp"),
            "percentage_delta": obj.get("percentage_delta"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj