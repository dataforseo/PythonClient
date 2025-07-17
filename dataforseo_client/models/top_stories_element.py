from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class TopStoriesElement(BaseModel):
    """
    TopStoriesElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    source: Optional[StrictStr] = Field(default=None, description="source of the element. indicates the source of information included in the top_stories_element")
    domain: Optional[StrictStr] = Field(default=None, description="website domain")
    title: Optional[StrictStr] = Field(default=None, description="title of a given link element")
    date: Optional[StrictStr] = Field(default=None, description="the date when the page source of the element was published")
    amp_version: Optional[StrictBool] = Field(default=None, description="Accelerated Mobile Pages. indicates whether an item has the Accelerated Mobile Page (AMP) version")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the result was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    url: Optional[StrictStr] = Field(default=None, description="URL")
    image_url: Optional[StrictStr] = Field(default=None, description="URL of the image. the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available)")
    badges: Optional[List[Optional[StrictStr]]] = Field(default=None, description="badges relevant to the element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "source", 
        "domain", 
        "title", 
        "date", 
        "amp_version", 
        "timestamp", 
        "url", 
        "image_url", 
        "badges", 
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
        _dict['source'] = self.source
        _dict['domain'] = self.domain
        _dict['title'] = self.title
        _dict['date'] = self.date
        _dict['amp_version'] = self.amp_version
        _dict['timestamp'] = self.timestamp
        _dict['url'] = self.url
        _dict['image_url'] = self.image_url
        _dict['badges'] = self.badges
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "source": obj.get("source"),
            "domain": obj.get("domain"),
            "title": obj.get("title"),
            "date": obj.get("date"),
            "amp_version": obj.get("amp_version"),
            "timestamp": obj.get("timestamp"),
            "url": obj.get("url"),
            "image_url": obj.get("image_url"),
            "badges": obj.get("badges"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj