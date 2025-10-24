from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_info import RatingInfo
from dataforseo_client.models.price_info import PriceInfo



class AiModeAiOverviewShoppingElementInfo(BaseModel):
    """
    AiModeAiOverviewShoppingElementInfo
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    product_id: Optional[StrictStr] = Field(default=None, description=r"")
    title: Optional[StrictStr] = Field(default=None, description=r"title of the element")
    url: Optional[StrictStr] = Field(default=None, description=r"reference page URL")
    domain: Optional[StrictStr] = Field(default=None, description=r"domain in link")
    rating: Optional[RatingInfo] = Field(default=None, description=r"the item’s rating . the popularity rate based on reviews and displayed in SERP")
    price: Optional[PriceInfo] = Field(default=None, description=r"pricing details. contains the pricing details of the product or service featured in the result")
    seller: Optional[StrictStr] = Field(default=None, description=r"seller of the product")
    snippet: Optional[StrictStr] = Field(default=None, description=r"text alongside the link title")
    marketplace: Optional[StrictStr] = Field(default=None, description=r"merchant account provider. commerce site that hosts products or websites of individual sellers under the same merchant account. example:. by Google")
    marketplace_url: Optional[StrictStr] = Field(default=None, description=r"relevant marketplace URL. URL of the page on the marketplace website where the product is hosted")
    image_url: Optional[StrictStr] = Field(default=None, description=r"URL of the image. the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available)")
    __properties: ClassVar[List[str]] = [
        "type", 
        "product_id", 
        "title", 
        "url", 
        "domain", 
        "rating", 
        "price", 
        "seller", 
        "snippet", 
        "marketplace", 
        "marketplace_url", 
        "image_url", 
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
        _dict['product_id'] = self.product_id
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['price'] = self.price.to_dict() if self.price else None
        _dict['seller'] = self.seller
        _dict['snippet'] = self.snippet
        _dict['marketplace'] = self.marketplace
        _dict['marketplace_url'] = self.marketplace_url
        _dict['image_url'] = self.image_url
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "product_id": obj.get("product_id"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "rating": RatingInfo.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "seller": obj.get("seller"),
            "snippet": obj.get("snippet"),
            "marketplace": obj.get("marketplace"),
            "marketplace_url": obj.get("marketplace_url"),
            "image_url": obj.get("image_url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj