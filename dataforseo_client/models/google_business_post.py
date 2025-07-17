from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.link_element import LinkElement



class GoogleBusinessPost(BaseModel):
    """
    GoogleBusinessPost
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank among all the listed updates. absolute position among all present elements")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values: right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    author: Optional[StrictStr] = Field(default=None, description="author of the post")
    snippet: Optional[StrictStr] = Field(default=None, description="additional content of a post")
    post_text: Optional[StrictStr] = Field(default=None, description="main content of a post")
    url: Optional[StrictStr] = Field(default=None, description="url of a post")
    images_url: Optional[StrictStr] = Field(default=None, description="url of an image included in the post")
    post_date: Optional[StrictStr] = Field(default=None, description="date when a post was published. in the following format:. 'mm/dd/yyyy hh:mm:ss'")
    timestamp: Optional[StrictStr] = Field(default=None, description="time when a post was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    links: Optional[List[Optional[LinkElement]]] = Field(default=None, description="links included in the post")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "author", 
        "snippet", 
        "post_text", 
        "url", 
        "images_url", 
        "post_date", 
        "timestamp", 
        "links", 
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
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
        _dict['author'] = self.author
        _dict['snippet'] = self.snippet
        _dict['post_text'] = self.post_text
        _dict['url'] = self.url
        _dict['images_url'] = self.images_url
        _dict['post_date'] = self.post_date
        _dict['timestamp'] = self.timestamp
        links_items = []
        if self.links:
            for _item in self.links:
                if _item:
                    links_items.append(_item.to_dict())
            _dict['links'] = links_items
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
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "author": obj.get("author"),
            "snippet": obj.get("snippet"),
            "post_text": obj.get("post_text"),
            "url": obj.get("url"),
            "images_url": obj.get("images_url"),
            "post_date": obj.get("post_date"),
            "timestamp": obj.get("timestamp"),
            "links": [LinkElement.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj