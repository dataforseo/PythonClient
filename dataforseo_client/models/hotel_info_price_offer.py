from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class HotelInfoPriceOffer(BaseModel):
    """
    HotelInfoPriceOffer
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="title of the hotel")
    price: Optional[StrictFloat] = Field(default=None, description="price per night")
    currency: Optional[StrictStr] = Field(default=None, description="price currency. USD is applied by default, unless specified in the POST array")
    url: Optional[StrictStr] = Field(default=None, description="url of the price offer. URL to the page of the website where price offer appears")
    max_visitors: Optional[StrictInt] = Field(default=None, description="the maximal number of visitors. the maximum number of visitors for which the price offer is valid")
    offer_images: Optional[List[Optional[StrictStr]]] = Field(default=None, description="price offer images. URLs of the images featured in the price offer")
    free_cancellation_until: Optional[StrictStr] = Field(default=None, description="date until free cancellation is available. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. equals null if free cancellation is not available for the selected dates")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "price", 
        "currency", 
        "url", 
        "max_visitors", 
        "offer_images", 
        "free_cancellation_until", 
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
        _dict['max_visitors'] = self.max_visitors
        _dict['offer_images'] = self.offer_images
        _dict['free_cancellation_until'] = self.free_cancellation_until
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
            "max_visitors": obj.get("max_visitors"),
            "offer_images": obj.get("offer_images"),
            "free_cancellation_until": obj.get("free_cancellation_until"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj