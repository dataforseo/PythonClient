from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class PricesByDates(BaseModel):
    """
    PricesByDates
    """ # noqa: E501
    price: Optional[StrictFloat] = Field(default=None, description="price per night")
    currency: Optional[StrictStr] = Field(default=None, description="price currency. USD is applied by default, unless specified in the POST array")
    check_in_date: Optional[StrictStr] = Field(default=None, description="")
    check_out_date: Optional[StrictStr] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "price", 
        "currency", 
        "check_in_date", 
        "check_out_date", 
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
        _dict['currency'] = self.currency
        _dict['check_in_date'] = self.check_in_date
        _dict['check_out_date'] = self.check_out_date
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "price": obj.get("price"),
            "currency": obj.get("currency"),
            "check_in_date": obj.get("check_in_date"),
            "check_out_date": obj.get("check_out_date"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj