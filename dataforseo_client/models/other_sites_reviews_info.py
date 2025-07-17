from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement



class OtherSitesReviewsInfo(BaseModel):
    """
    OtherSitesReviewsInfo
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description="review title. contains a name of the third-party site where review initially appeared")
    url: Optional[StrictStr] = Field(default=None, description="review url. URL to the a third-party site where review initially appeared")
    review_text: Optional[StrictStr] = Field(default=None, description="review text. text of the review")
    rating: Optional[RatingElement] = Field(default=None, description="rating in the review. information about the rating enclosed in the review on a third-party site")
    __properties: ClassVar[List[str]] = [
        "title", 
        "url", 
        "review_text", 
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

        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['review_text'] = self.review_text
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "url": obj.get("url"),
            "review_text": obj.get("review_text"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj