from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.content_rating_info import ContentRatingInfo
from dataforseo_client.models.section_content_item_info import SectionContentItemInfo



class ContentCommentInfo(BaseModel):
    """
    ContentCommentInfo
    """ # noqa: E501
    rating: Optional[ContentRatingInfo] = Field(default=None, description="product’s rating. contains information about the rating a customer has given to the product")
    title: Optional[StrictStr] = Field(default=None, description="title of the customer’s comment")
    publish_date: Optional[StrictStr] = Field(default=None, description="date when the comment was published")
    author: Optional[StrictStr] = Field(default=None, description="author of the comment")
    have_form: Optional[StrictBool] = Field(default=None, description="")
    primary_content: Optional[List[Optional[SectionContentItemInfo]]] = Field(default=None, description="primary content on the page. you can find more information about content priority calculation in this help center article")
    __properties: ClassVar[List[str]] = [
        "rating", 
        "title", 
        "publish_date", 
        "author", 
        "have_form", 
        "primary_content", 
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

        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['title'] = self.title
        _dict['publish_date'] = self.publish_date
        _dict['author'] = self.author
        _dict['have_form'] = self.have_form
        primary_content_items = []
        if self.primary_content:
            for _item in self.primary_content:
                if _item:
                    primary_content_items.append(_item.to_dict())
            _dict['primary_content'] = primary_content_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "rating": ContentRatingInfo.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "title": obj.get("title"),
            "publish_date": obj.get("publish_date"),
            "author": obj.get("author"),
            "have_form": obj.get("have_form"),
            "primary_content": [SectionContentItemInfo.from_dict(_item) for _item in obj["primary_content"]] if obj.get("primary_content") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj