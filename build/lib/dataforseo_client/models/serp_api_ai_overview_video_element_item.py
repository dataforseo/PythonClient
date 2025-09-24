from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_serp_api_ai_overview_element_item import BaseSerpApiAiOverviewElementItem



class SerpApiAiOverviewVideoElementItem(BaseSerpApiAiOverviewElementItem):
    """
    SerpApiAiOverviewVideoElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    position: Optional[StrictStr] = Field(default=None, description=r"the alignment of the element in SERP. can take the following values:. left, right")
    title: Optional[StrictStr] = Field(default=None, description=r"title of the element")
    snippet: Optional[StrictStr] = Field(default=None, description=r"additional information for the video")
    url: Optional[StrictStr] = Field(default=None, description=r"relevant URL")
    domain: Optional[StrictStr] = Field(default=None, description=r"domain name of the reference")
    image_url: Optional[StrictStr] = Field(default=None, description=r"URL of the image")
    source: Optional[StrictStr] = Field(default=None, description=r"reference source name or title")
    date: Optional[StrictStr] = Field(default=None, description=r"date when the video was published or indexed. example:. Apr 26, 2024")
    timestamp: Optional[StrictStr] = Field(default=None, description=r"date and time when the result was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "title", 
        "snippet", 
        "url", 
        "domain", 
        "image_url", 
        "source", 
        "date", 
        "timestamp", 
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
        _dict['position'] = self.position
        _dict['title'] = self.title
        _dict['snippet'] = self.snippet
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        _dict['image_url'] = self.image_url
        _dict['source'] = self.source
        _dict['date'] = self.date
        _dict['timestamp'] = self.timestamp
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "position": obj.get("position"),
            "title": obj.get("title"),
            "snippet": obj.get("snippet"),
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "image_url": obj.get("image_url"),
            "source": obj.get("source"),
            "date": obj.get("date"),
            "timestamp": obj.get("timestamp"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj