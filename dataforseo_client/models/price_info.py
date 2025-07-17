from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class PriceInfo(BaseModel):
    """
    PriceInfo
    """ # noqa: E501
    current: Optional[StrictFloat] = Field(default=None, description="current price. indicates the current price of the product or service featured in the result")
    regular: Optional[StrictFloat] = Field(default=None, description="regular price. indicates the regular price of the product or service with no discounts applied")
    max_value: Optional[StrictFloat] = Field(default=None, description="the maximum price. the maximum price of the product or service as indicated in the result")
    currency: Optional[StrictStr] = Field(default=None, description="currency of the listed price. ISO code of the currency applied to the price")
    is_price_range: Optional[StrictBool] = Field(default=None, description="price is provided as a range. indicates whether a price is provided in a range")
    displayed_price: Optional[StrictStr] = Field(default=None, description="price string in the result. raw price string as provided in the result")
    __properties: ClassVar[List[str]] = [
        "current", 
        "regular", 
        "max_value", 
        "currency", 
        "is_price_range", 
        "displayed_price", 
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

        _dict['current'] = self.current
        _dict['regular'] = self.regular
        _dict['max_value'] = self.max_value
        _dict['currency'] = self.currency
        _dict['is_price_range'] = self.is_price_range
        _dict['displayed_price'] = self.displayed_price
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "current": obj.get("current"),
            "regular": obj.get("regular"),
            "max_value": obj.get("max_value"),
            "currency": obj.get("currency"),
            "is_price_range": obj.get("is_price_range"),
            "displayed_price": obj.get("displayed_price"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj