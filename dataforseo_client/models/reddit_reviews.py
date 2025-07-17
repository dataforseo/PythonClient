from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class RedditReviews(BaseModel):
    """
    RedditReviews
    """ # noqa: E501
    subreddit: Optional[StrictStr] = Field(default=None, description="the name of the subreddit")
    author_name: Optional[StrictStr] = Field(default=None, description="nickname of the author. nicknname of the user who published the post in the subreddit and shared the URL")
    title: Optional[StrictStr] = Field(default=None, description="title of the subreddit post")
    permalink: Optional[StrictStr] = Field(default=None, description="URL to the subreddit post")
    subreddit_members: Optional[StrictInt] = Field(default=None, description="number of subreddit members")
    __properties: ClassVar[List[str]] = [
        "subreddit", 
        "author_name", 
        "title", 
        "permalink", 
        "subreddit_members", 
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

        _dict['subreddit'] = self.subreddit
        _dict['author_name'] = self.author_name
        _dict['title'] = self.title
        _dict['permalink'] = self.permalink
        _dict['subreddit_members'] = self.subreddit_members
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "subreddit": obj.get("subreddit"),
            "author_name": obj.get("author_name"),
            "title": obj.get("title"),
            "permalink": obj.get("permalink"),
            "subreddit_members": obj.get("subreddit_members"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj