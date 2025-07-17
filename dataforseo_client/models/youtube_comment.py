from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class YoutubeComment(BaseModel):
    """
    YoutubeComment
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP for the target domain. absolute position among all the elements in SERP")
    author_name: Optional[StrictStr] = Field(default=None, description="name of the author of the comment")
    author_thumbnail: Optional[StrictStr] = Field(default=None, description="the URL of the page where the author’s channel logo is hosted")
    author_url: Optional[StrictStr] = Field(default=None, description="URL of the author’s channel")
    text: Optional[StrictStr] = Field(default=None, description="text of the comment")
    publication_date: Optional[StrictStr] = Field(default=None, description="displayed publication date")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the result was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2022-11-15 12:57:46 +00:00")
    likes_count: Optional[StrictInt] = Field(default=None, description="number of likes on the comment")
    reply_count: Optional[StrictInt] = Field(default=None, description="number of replies on the comment")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "author_name", 
        "author_thumbnail", 
        "author_url", 
        "text", 
        "publication_date", 
        "timestamp", 
        "likes_count", 
        "reply_count", 
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
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['author_name'] = self.author_name
        _dict['author_thumbnail'] = self.author_thumbnail
        _dict['author_url'] = self.author_url
        _dict['text'] = self.text
        _dict['publication_date'] = self.publication_date
        _dict['timestamp'] = self.timestamp
        _dict['likes_count'] = self.likes_count
        _dict['reply_count'] = self.reply_count
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "author_name": obj.get("author_name"),
            "author_thumbnail": obj.get("author_thumbnail"),
            "author_url": obj.get("author_url"),
            "text": obj.get("text"),
            "publication_date": obj.get("publication_date"),
            "timestamp": obj.get("timestamp"),
            "likes_count": obj.get("likes_count"),
            "reply_count": obj.get("reply_count"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj