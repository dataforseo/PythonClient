from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ResponseDataInfo(BaseModel):
    """
    ResponseDataInfo
    """ # noqa: E501
    author: Optional[StrictStr] = Field(default=None, description="author of the response")
    title: Optional[StrictStr] = Field(default=None, description="title of the response. in this case, will equal null")
    text: Optional[StrictStr] = Field(default=None, description="content of the response")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the response was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;. example:. 2019-11-15 12:57:46 +00:00")
    __properties: ClassVar[List[str]] = [
        "author", 
        "title", 
        "text", 
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

        _dict['author'] = self.author
        _dict['title'] = self.title
        _dict['text'] = self.text
        _dict['timestamp'] = self.timestamp
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "author": obj.get("author"),
            "title": obj.get("title"),
            "text": obj.get("text"),
            "timestamp": obj.get("timestamp"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj