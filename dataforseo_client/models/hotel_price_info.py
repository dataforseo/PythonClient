from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.hotel_price_item_info import HotelPriceItemInfo
from dataforseo_client.models.prices_by_dates import PricesByDates



class HotelPriceInfo(BaseModel):
    """
    HotelPriceInfo
    """ # noqa: E501
    price: Optional[StrictFloat] = Field(default=None, description="price per night")
    price_without_discount: Optional[StrictFloat] = Field(default=None, description="full price per night without a discount applied")
    currency: Optional[StrictStr] = Field(default=None, description="price currency. USD is applied by default, unless specified in the POST array")
    discount_text: Optional[StrictStr] = Field(default=None, description="text about a discount applied")
    check_in: Optional[StrictStr] = Field(default=None, description="check-in date and time. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    check_out: Optional[StrictStr] = Field(default=None, description="check-out date and time. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    visitors: Optional[StrictInt] = Field(default=None, description="number of hotel visitors for this price")
    items: Optional[List[Optional[HotelPriceItemInfo]]] = Field(default=None, description="encountered item types. types of search engine results encountered in the items array;. possible item types: hotel_search_item")
    prices_by_dates: Optional[List[Optional[PricesByDates]]] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "price", 
        "price_without_discount", 
        "currency", 
        "discount_text", 
        "check_in", 
        "check_out", 
        "visitors", 
        "items", 
        "prices_by_dates", 
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

        _dict['price'] = self.price
        _dict['price_without_discount'] = self.price_without_discount
        _dict['currency'] = self.currency
        _dict['discount_text'] = self.discount_text
        _dict['check_in'] = self.check_in
        _dict['check_out'] = self.check_out
        _dict['visitors'] = self.visitors
        items_items = []
        if self.items:
            for _item in self.items:
                if _item:
                    items_items.append(_item.to_dict())
            _dict['items'] = items_items
        prices_by_dates_items = []
        if self.prices_by_dates:
            for _item in self.prices_by_dates:
                if _item:
                    prices_by_dates_items.append(_item.to_dict())
            _dict['prices_by_dates'] = prices_by_dates_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "price": obj.get("price"),
            "price_without_discount": obj.get("price_without_discount"),
            "currency": obj.get("currency"),
            "discount_text": obj.get("discount_text"),
            "check_in": obj.get("check_in"),
            "check_out": obj.get("check_out"),
            "visitors": obj.get("visitors"),
            "items": [HotelPriceItemInfo.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "prices_by_dates": [PricesByDates.from_dict(_item) for _item in obj["prices_by_dates"]] if obj.get("prices_by_dates") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj