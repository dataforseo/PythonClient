from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ChatGptSource(BaseModel):
    """
    ChatGptSource
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    title: Optional[StrictStr] = Field(default=None, description=r"source title")
    snippet: Optional[StrictStr] = Field(default=None, description=r"source description")
    domain: Optional[StrictStr] = Field(default=None, description=r"source domain in SERP")
    url: Optional[StrictStr] = Field(default=None, description=r"source URL")
    thumbnail: Optional[StrictStr] = Field(default=None, description=r"source thumbnail")
    source_name: Optional[StrictStr] = Field(default=None, description=r"source name")
    publication_date: Optional[StrictStr] = Field(default=None, description=r"date and time when the result was published. in the format: “year-month-date:minutes:UTC_difference_hours:UTC_difference_minutes”. example:. 2019-11-15 12:57:46 +00:00")
    markdown: Optional[StrictStr] = Field(default=None, description=r"content of the element in markdown format. content of the result formatted in the markdown markup language")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "snippet", 
        "domain", 
        "url", 
        "thumbnail", 
        "source_name", 
        "publication_date", 
        "markdown", 
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
        _dict['snippet'] = self.snippet
        _dict['domain'] = self.domain
        _dict['url'] = self.url
        _dict['thumbnail'] = self.thumbnail
        _dict['source_name'] = self.source_name
        _dict['publication_date'] = self.publication_date
        _dict['markdown'] = self.markdown
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
            "snippet": obj.get("snippet"),
            "domain": obj.get("domain"),
            "url": obj.get("url"),
            "thumbnail": obj.get("thumbnail"),
            "source_name": obj.get("source_name"),
            "publication_date": obj.get("publication_date"),
            "markdown": obj.get("markdown"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj