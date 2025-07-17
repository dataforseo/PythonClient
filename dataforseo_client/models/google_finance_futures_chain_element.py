from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class GoogleFinanceFuturesChainElement(BaseModel):
    """
    GoogleFinanceFuturesChainElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    expiration_timestamp: Optional[StrictStr] = Field(default=None, description="futures’ date and time of expiration. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2025-02-10 09:40:00 +00:00")
    symbol: Optional[StrictStr] = Field(default=None, description="futures’ symbol")
    price: Optional[StrictFloat] = Field(default=None, description="price of the market instrument. price of the market instrument at a given timestamp")
    price_currency: Optional[StrictStr] = Field(default=None, description="currency of the price value")
    price_delta: Optional[StrictFloat] = Field(default=None, description="change in price of the market instrument. change in price at a given timestamp")
    percentage_delta: Optional[StrictFloat] = Field(default=None, description="percentage of change in value of the market index")
    trend: Optional[StrictStr] = Field(default=None, description="growth trend of the market index. possible values: up, down, stable")
    __properties: ClassVar[List[str]] = [
        "type", 
        "expiration_timestamp", 
        "symbol", 
        "price", 
        "price_currency", 
        "price_delta", 
        "percentage_delta", 
        "trend", 
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
        _dict['expiration_timestamp'] = self.expiration_timestamp
        _dict['symbol'] = self.symbol
        _dict['price'] = self.price
        _dict['price_currency'] = self.price_currency
        _dict['price_delta'] = self.price_delta
        _dict['percentage_delta'] = self.percentage_delta
        _dict['trend'] = self.trend
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "expiration_timestamp": obj.get("expiration_timestamp"),
            "symbol": obj.get("symbol"),
            "price": obj.get("price"),
            "price_currency": obj.get("price_currency"),
            "price_delta": obj.get("price_delta"),
            "percentage_delta": obj.get("percentage_delta"),
            "trend": obj.get("trend"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj