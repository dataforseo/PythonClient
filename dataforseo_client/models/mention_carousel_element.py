from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.price_info import PriceInfo
from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.link_element import LinkElement



class MentionCarouselElement(BaseModel):
    """
    MentionCarouselElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="title of a given link element")
    price: Optional[PriceInfo] = Field(default=None, description="price indicated in the element")
    rating: Optional[RatingElement] = Field(default=None, description="the item’s rating . the popularity rate based on reviews and displayed in SERP")
    mentioned_in: Optional[List[Optional[LinkElement]]] = Field(default=None, description="additional elements in the mention_carousel item")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "price", 
        "rating", 
        "mentioned_in", 
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
        _dict['price'] = self.price.to_dict() if self.price else None
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        mentioned_in_items = []
        if self.mentioned_in:
            for _item in self.mentioned_in:
                if _item:
                    mentioned_in_items.append(_item.to_dict())
            _dict['mentioned_in'] = mentioned_in_items
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
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "mentioned_in": [LinkElement.from_dict(_item) for _item in obj["mentioned_in"]] if obj.get("mentioned_in") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj