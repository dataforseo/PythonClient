from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AiModeAiOverviewReferenceInfo(BaseModel):
    """
    AiModeAiOverviewReferenceInfo
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    source: Optional[StrictStr] = Field(default=None, description="reference source name or title")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    url: Optional[StrictStr] = Field(default=None, description="image source URL")
    title: Optional[StrictStr] = Field(default=None, description="title of the element")
    text: Optional[StrictStr] = Field(default=None, description="text of the component")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "source", 
        "domain", 
        "url", 
        "title", 
        "text", 
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
        _dict['source'] = self.source
        _dict['domain'] = self.domain
        _dict['url'] = self.url
        _dict['title'] = self.title
        _dict['text'] = self.text
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
            "source": obj.get("source"),
            "domain": obj.get("domain"),
            "url": obj.get("url"),
            "title": obj.get("title"),
            "text": obj.get("text"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj