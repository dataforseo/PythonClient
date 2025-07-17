from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class TwitterElement(BaseModel):
    """
    TwitterElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    tweet: Optional[StrictStr] = Field(default=None, description="tweet message")
    date: Optional[StrictStr] = Field(default=None, description="the date when the page source of the element was published")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the result was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    url: Optional[StrictStr] = Field(default=None, description="URL")
    __properties: ClassVar[List[str]] = [
        "type", 
        "tweet", 
        "date", 
        "timestamp", 
        "url", 
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
        _dict['tweet'] = self.tweet
        _dict['date'] = self.date
        _dict['timestamp'] = self.timestamp
        _dict['url'] = self.url
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "tweet": obj.get("tweet"),
            "date": obj.get("date"),
            "timestamp": obj.get("timestamp"),
            "url": obj.get("url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj