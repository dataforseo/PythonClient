from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.hotel_info_price_offer import HotelInfoPriceOffer



class HotelPriceItemInfo(BaseModel):
    """
    HotelPriceItemInfo
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="title of the hotel")
    price: Optional[StrictFloat] = Field(default=None, description="price per night")
    currency: Optional[StrictStr] = Field(default=None, description="price currency. USD is applied by default, unless specified in the POST array")
    url: Optional[StrictStr] = Field(default=None, description="third-party page url. URL to the third-party website page with pricing information")
    domain: Optional[StrictStr] = Field(default=None, description="third-party domain. domain of the third-party website page with pricing information")
    is_paid: Optional[StrictBool] = Field(default=None, description="indicates a paid hotel listing. if true, related hotel_search_item is a paid ad. if false, related hotel_search_item is an organic hotel listing")
    free_cancellation_until: Optional[StrictStr] = Field(default=None, description="date until which free cancellation is available. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. equals null if free cancellation is not available for the selected dates")
    offers: Optional[List[Optional[HotelInfoPriceOffer]]] = Field(default=None, description="featured price offers")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "price", 
        "currency", 
        "url", 
        "domain", 
        "is_paid", 
        "free_cancellation_until", 
        "offers", 
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
        _dict['title'] = self.title
        _dict['price'] = self.price
        _dict['currency'] = self.currency
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        _dict['is_paid'] = self.is_paid
        _dict['free_cancellation_until'] = self.free_cancellation_until
        offers_items = []
        if self.offers:
            for _item in self.offers:
                if _item:
                    offers_items.append(_item.to_dict())
            _dict['offers'] = offers_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "price": obj.get("price"),
            "currency": obj.get("currency"),
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "is_paid": obj.get("is_paid"),
            "free_cancellation_until": obj.get("free_cancellation_until"),
            "offers": [HotelInfoPriceOffer.from_dict(_item) for _item in obj["offers"]] if obj.get("offers") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj