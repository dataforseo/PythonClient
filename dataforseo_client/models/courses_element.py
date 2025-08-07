from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement



class CoursesElement(BaseModel):
    """
    CoursesElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="title of a given link element")
    url: Optional[StrictStr] = Field(default=None, description="URL")
    domain: Optional[StrictStr] = Field(default=None, description="website domain")
    source: Optional[StrictStr] = Field(default=None, description="source of the element. indicates the source of information included in the top_stories_element")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    date: Optional[StrictStr] = Field(default=None, description="the date when the page source of the element was published")
    image_url: Optional[StrictStr] = Field(default=None, description="URL of the image. the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available)")
    rating: Optional[RatingElement] = Field(default=None, description="the item’s rating . the popularity rate based on reviews and displayed in SERP")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "url", 
        "domain", 
        "source", 
        "description", 
        "date", 
        "image_url", 
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
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        _dict['source'] = self.source
        _dict['description'] = self.description
        _dict['date'] = self.date
        _dict['image_url'] = self.image_url
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
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "source": obj.get("source"),
            "description": obj.get("description"),
            "date": obj.get("date"),
            "image_url": obj.get("image_url"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj