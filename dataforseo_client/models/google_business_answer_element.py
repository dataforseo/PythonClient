from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class GoogleBusinessAnswerElement(BaseModel):
    """
    GoogleBusinessAnswerElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    answer_id: Optional[StrictStr] = Field(default=None, description="ID of the answer")
    profile_image_url: Optional[StrictStr] = Field(default=None, description="URL of the user’s profile image")
    profile_url: Optional[StrictStr] = Field(default=None, description="URL of the user’s profile")
    profile_name: Optional[StrictStr] = Field(default=None, description="displayed name of the user")
    answer_text: Optional[StrictStr] = Field(default=None, description="current text of the answer")
    original_answer_text: Optional[StrictStr] = Field(default=None, description="original text of the answer")
    time_ago: Optional[StrictStr] = Field(default=None, description="estimated time when the answer was posted")
    timestamp: Optional[StrictStr] = Field(default=None, description="exact time when the answer was posted")
    __properties: ClassVar[List[str]] = [
        "type", 
        "answer_id", 
        "profile_image_url", 
        "profile_url", 
        "profile_name", 
        "answer_text", 
        "original_answer_text", 
        "time_ago", 
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
        _dict['answer_id'] = self.answer_id
        _dict['profile_image_url'] = self.profile_image_url
        _dict['profile_url'] = self.profile_url
        _dict['profile_name'] = self.profile_name
        _dict['answer_text'] = self.answer_text
        _dict['original_answer_text'] = self.original_answer_text
        _dict['time_ago'] = self.time_ago
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
            "answer_id": obj.get("answer_id"),
            "profile_image_url": obj.get("profile_image_url"),
            "profile_url": obj.get("profile_url"),
            "profile_name": obj.get("profile_name"),
            "answer_text": obj.get("answer_text"),
            "original_answer_text": obj.get("original_answer_text"),
            "time_ago": obj.get("time_ago"),
            "timestamp": obj.get("timestamp"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj