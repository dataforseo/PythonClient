from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ContentOfferInfo(BaseModel):
    """
    ContentOfferInfo
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="name of the product")
    price: Optional[StrictFloat] = Field(default=None, description="price of the product")
    price_currency: Optional[StrictStr] = Field(default=None, description="price currency")
    price_valid_until: Optional[StrictStr] = Field(default=None, description="displays the date and time until which the price is valid. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example: '2022-11-01 10:02:52 +00:00'")
    __properties: ClassVar[List[str]] = [
        "name", 
        "price", 
        "price_currency", 
        "price_valid_until", 
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

        _dict['name'] = self.name
        _dict['price'] = self.price
        _dict['price_currency'] = self.price_currency
        _dict['price_valid_until'] = self.price_valid_until
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "price": obj.get("price"),
            "price_currency": obj.get("price_currency"),
            "price_valid_until": obj.get("price_valid_until"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj