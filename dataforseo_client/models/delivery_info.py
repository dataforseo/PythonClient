from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.price_info import PriceInfo



class DeliveryInfo(BaseModel):
    """
    DeliveryInfo
    """ # noqa: E501
    delivery_message: Optional[StrictStr] = Field(default=None, description="delivery information. message accompanying the delivery information as posted by the seller")
    delivery_price: Optional[PriceInfo] = Field(default=None, description="price for the delivery. price of the delivery based on the location you specified in the POST request;. if free delivery is available, the value is null")
    __properties: ClassVar[List[str]] = [
        "delivery_message", 
        "delivery_price", 
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

        _dict['delivery_message'] = self.delivery_message
        _dict['delivery_price'] = self.delivery_price.to_dict() if self.delivery_price else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "delivery_message": obj.get("delivery_message"),
            "delivery_price": PriceInfo.from_dict(obj["delivery_price"]) if obj.get("delivery_price") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj