from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_info import RatingInfo



class ChatGptProductsElement(BaseModel):
    """
    ChatGptProductsElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    product_id: Optional[StrictStr] = Field(default=None, description=r"product id")
    title: Optional[StrictStr] = Field(default=None, description=r"title of the element")
    rating: Optional[RatingInfo] = Field(default=None, description=r"rating of the corresponding local businesses. popularity rate based on reviews as displayed in the results")
    price: Optional[StrictFloat] = Field(default=None, description=r"product price")
    currency: Optional[StrictStr] = Field(default=None, description=r"currency of the listed price. ISO code of the currency applied to the price")
    tag: Optional[StrictStr] = Field(default=None, description=r"tag text")
    url: Optional[StrictStr] = Field(default=None, description=r"URL")
    domain: Optional[StrictStr] = Field(default=None, description=r"domain")
    images: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"image URLs of the element. contains URLs leading to the images on the original resource or DataForSEO storage (in case the original source is not available)")
    __properties: ClassVar[List[str]] = [
        "type", 
        "product_id", 
        "title", 
        "rating", 
        "price", 
        "currency", 
        "tag", 
        "url", 
        "domain", 
        "images", 
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
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['price'] = self.price
        _dict['currency'] = self.currency
        _dict['tag'] = self.tag
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        _dict['images'] = self.images
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
            "rating": RatingInfo.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "price": obj.get("price"),
            "currency": obj.get("currency"),
            "tag": obj.get("tag"),
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "images": obj.get("images"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj