from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.price_info import PriceInfo



class BusinessDataServiceInfo(BaseModel):
    """
    BusinessDataServiceInfo
    """ # noqa: E501
    category: Optional[StrictStr] = Field(default=None, description=r"business category. Google My Business general category that best describes the services provided by the business entity")
    title: Optional[StrictStr] = Field(default=None, description=r"title of the element in SERP. the name of the business entity for which the results are collected")
    snippet: Optional[StrictStr] = Field(default=None, description=r"additional information on the business entity")
    price: Optional[PriceInfo] = Field(default=None, description=r"")
    __properties: ClassVar[List[str]] = [
        "category", 
        "title", 
        "snippet", 
        "price", 
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

        _dict['category'] = self.category
        _dict['title'] = self.title
        _dict['snippet'] = self.snippet
        _dict['price'] = self.price.to_dict() if self.price else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "category": obj.get("category"),
            "title": obj.get("title"),
            "snippet": obj.get("snippet"),
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj