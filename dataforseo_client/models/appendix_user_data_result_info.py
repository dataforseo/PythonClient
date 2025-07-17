from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_rates_data import AppendixRatesData
from dataforseo_client.models.appendix_money_data import AppendixMoneyData
from dataforseo_client.models.appendix_price_data import AppendixPriceData



class AppendixUserDataResultInfo(BaseModel):
    """
    AppendixUserDataResultInfo
    """ # noqa: E501
    login: Optional[StrictStr] = Field(default=None, description="your login")
    timezone: Optional[StrictStr] = Field(default=None, description="your time zone. can be set in your profile settings")
    rates: Optional[AppendixRatesData] = Field(default=None, description="your API rates")
    money: Optional[AppendixMoneyData] = Field(default=None, description="section of your spending, USD")
    price: Optional[AppendixPriceData] = Field(default=None, description="pricing")
    backlinks_subscription_expiry_date: Optional[StrictStr] = Field(default=None, description="expiry date of the backlinks api subscription. date and time when the current subscription to Backlinks API expires;. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2025-06-15 12:57:46 +00:00. Note: if there is no active subscription to Backlinks API, the value equals null")
    __properties: ClassVar[List[str]] = [
        "login", 
        "timezone", 
        "rates", 
        "money", 
        "price", 
        "backlinks_subscription_expiry_date", 
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

        _dict['login'] = self.login
        _dict['timezone'] = self.timezone
        _dict['rates'] = self.rates.to_dict() if self.rates else None
        _dict['money'] = self.money.to_dict() if self.money else None
        _dict['price'] = self.price.to_dict() if self.price else None
        _dict['backlinks_subscription_expiry_date'] = self.backlinks_subscription_expiry_date
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "login": obj.get("login"),
            "timezone": obj.get("timezone"),
            "rates": AppendixRatesData.from_dict(obj["rates"]) if obj.get("rates") is not None else None,
            "money": AppendixMoneyData.from_dict(obj["money"]) if obj.get("money") is not None else None,
            "price": AppendixPriceData.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "backlinks_subscription_expiry_date": obj.get("backlinks_subscription_expiry_date"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj