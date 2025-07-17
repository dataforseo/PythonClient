from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.price_info import PriceInfo



class KnowledgeGraphShoppingElement(BaseModel):
    """
    KnowledgeGraphShoppingElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="title of the result in SERP")
    url: Optional[StrictStr] = Field(default=None, description="relevant URL")
    domain: Optional[StrictStr] = Field(default=None, description="website domain")
    price: Optional[PriceInfo] = Field(default=None, description="pricing details. contains the pricing details of the product or service featured in the result")
    source: Optional[StrictStr] = Field(default=None, description="source of additional information about the result")
    snippet: Optional[StrictStr] = Field(default=None, description="text alongside the link title")
    marketplace: Optional[StrictStr] = Field(default=None, description="merchant account provider. ecommerce site that hosts products or websites of individual sellers under the same merchant account. example:. by Google")
    marketplace_url: Optional[StrictStr] = Field(default=None, description="URL to the merchant account provider. ecommerce site that hosts products or websites of individual sellers under the same merchant account")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "url", 
        "domain", 
        "price", 
        "source", 
        "snippet", 
        "marketplace", 
        "marketplace_url", 
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
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        _dict['price'] = self.price.to_dict() if self.price else None
        _dict['source'] = self.source
        _dict['snippet'] = self.snippet
        _dict['marketplace'] = self.marketplace
        _dict['marketplace_url'] = self.marketplace_url
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
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "source": obj.get("source"),
            "snippet": obj.get("snippet"),
            "marketplace": obj.get("marketplace"),
            "marketplace_url": obj.get("marketplace_url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj