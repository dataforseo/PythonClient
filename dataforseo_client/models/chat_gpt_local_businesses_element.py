from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_info import RatingInfo



class ChatGptLocalBusinessesElement(BaseModel):
    """
    ChatGptLocalBusinessesElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    title: Optional[StrictStr] = Field(default=None, description=r"title of the element")
    description: Optional[StrictStr] = Field(default=None, description=r"description of the local businesses")
    address: Optional[StrictStr] = Field(default=None, description=r"address of the local businesses")
    phone: Optional[StrictStr] = Field(default=None, description=r"phone of the local businesses")
    reviews_count: Optional[StrictInt] = Field(default=None, description=r"total number of reviews submitted for the local businesses")
    url: Optional[StrictStr] = Field(default=None, description=r"URL")
    domain: Optional[StrictStr] = Field(default=None, description=r"domain")
    rating: Optional[RatingInfo] = Field(default=None, description=r"rating of the corresponding local businesses. popularity rate based on reviews as displayed in the results")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "description", 
        "address", 
        "phone", 
        "reviews_count", 
        "url", 
        "domain", 
        "rating", 
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
        _dict['description'] = self.description
        _dict['address'] = self.address
        _dict['phone'] = self.phone
        _dict['reviews_count'] = self.reviews_count
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        _dict['rating'] = self.rating.to_dict() if self.rating else None
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
            "description": obj.get("description"),
            "address": obj.get("address"),
            "phone": obj.get("phone"),
            "reviews_count": obj.get("reviews_count"),
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "rating": RatingInfo.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj