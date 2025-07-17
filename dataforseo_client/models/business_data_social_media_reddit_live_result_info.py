from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.reddit_reviews import RedditReviews



class BusinessDataSocialMediaRedditLiveResultInfo(BaseModel):
    """
    BusinessDataSocialMediaRedditLiveResultInfo
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    page_url: Optional[StrictStr] = Field(default=None, description="URL of the page the data is provided for. corresponding URL you specified in the targets array when setting a task")
    reddit_reviews: Optional[List[Optional[RedditReviews]]] = Field(default=None, description="reddit reviews for the page_url")
    __properties: ClassVar[List[str]] = [
        "type", 
        "page_url", 
        "reddit_reviews", 
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
        _dict['page_url'] = self.page_url
        reddit_reviews_items = []
        if self.reddit_reviews:
            for _item in self.reddit_reviews:
                if _item:
                    reddit_reviews_items.append(_item.to_dict())
            _dict['reddit_reviews'] = reddit_reviews_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "page_url": obj.get("page_url"),
            "reddit_reviews": [RedditReviews.from_dict(_item) for _item in obj["reddit_reviews"]] if obj.get("reddit_reviews") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj