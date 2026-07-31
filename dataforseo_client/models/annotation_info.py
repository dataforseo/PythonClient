from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AnnotationInfo(BaseModel):
    """
    AnnotationInfo
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description=r"*the domain name or title of the quoted source*")
    url: Optional[StrictStr] = Field(default=None, description=r"*URL of the quoted source*")
    start_index: Optional[StrictInt] = Field(default=None, description=r"*start of the annotation indexing*")
    end_index: Optional[StrictInt] = Field(default=None, description=r"*end of the annotation indexing*")
    text: Optional[StrictStr] = Field(default=None, description=r"*text of the reasoning chain section*. text of the reasoning chain  section summarizing the model's thought process")
    __properties: ClassVar[List[str]] = [
        "title", 
        "url", 
        "start_index", 
        "end_index", 
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

        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['start_index'] = self.start_index
        _dict['end_index'] = self.end_index
        _dict['text'] = self.text
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
            "start_index": obj.get("start_index"),
            "end_index": obj.get("end_index"),
            "text": obj.get("text"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj