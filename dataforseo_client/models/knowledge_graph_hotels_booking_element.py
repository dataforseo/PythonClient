from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.price_info import PriceInfo



class KnowledgeGraphHotelsBookingElement(BaseModel):
    """
    KnowledgeGraphHotelsBookingElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    source: Optional[StrictStr] = Field(default=None, description="source of additional information about the result")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    url: Optional[StrictStr] = Field(default=None, description="relevant URL")
    domain: Optional[StrictStr] = Field(default=None, description="domain where a link points")
    price: Optional[PriceInfo] = Field(default=None, description="pricing details. contains the pricing details of the product or service featured in the result")
    is_paid: Optional[StrictBool] = Field(default=None, description="indicates whether the element is an ad")
    __properties: ClassVar[List[str]] = [
        "type", 
        "source", 
        "description", 
        "url", 
        "domain", 
        "price", 
        "is_paid", 
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
        _dict['source'] = self.source
        _dict['description'] = self.description
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        _dict['price'] = self.price.to_dict() if self.price else None
        _dict['is_paid'] = self.is_paid
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "source": obj.get("source"),
            "description": obj.get("description"),
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "is_paid": obj.get("is_paid"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj