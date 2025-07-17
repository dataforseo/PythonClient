from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.google_business_answer_element import GoogleBusinessAnswerElement



class GoogleBusinessQuestionItem(BaseModel):
    """
    GoogleBusinessQuestionItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank among all the elements")
    question_id: Optional[StrictStr] = Field(default=None, description="ID of the question")
    url: Optional[StrictStr] = Field(default=None, description="URL of the question")
    profile_image_url: Optional[StrictStr] = Field(default=None, description="URL of the user’s profile image")
    profile_url: Optional[StrictStr] = Field(default=None, description="URL of the user’s profile")
    profile_name: Optional[StrictStr] = Field(default=None, description="displayed name of the user")
    question_text: Optional[StrictStr] = Field(default=None, description="current text of the question")
    original_question_text: Optional[StrictStr] = Field(default=None, description="original text of the question")
    time_ago: Optional[StrictStr] = Field(default=None, description="estimated time when the question was posted")
    timestamp: Optional[StrictStr] = Field(default=None, description="exact time when the question was posted")
    items: Optional[List[Optional[GoogleBusinessAnswerElement]]] = Field(default=None, description="array of items. items within google_business_question_item")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "question_id", 
        "url", 
        "profile_image_url", 
        "profile_url", 
        "profile_name", 
        "question_text", 
        "original_question_text", 
        "time_ago", 
        "timestamp", 
        "items", 
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
        _dict['question_id'] = self.question_id
        _dict['url'] = self.url
        _dict['profile_image_url'] = self.profile_image_url
        _dict['profile_url'] = self.profile_url
        _dict['profile_name'] = self.profile_name
        _dict['question_text'] = self.question_text
        _dict['original_question_text'] = self.original_question_text
        _dict['time_ago'] = self.time_ago
        _dict['timestamp'] = self.timestamp
        items_items = []
        if self.items:
            for _item in self.items:
                if _item:
                    items_items.append(_item.to_dict())
            _dict['items'] = items_items
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
            "question_id": obj.get("question_id"),
            "url": obj.get("url"),
            "profile_image_url": obj.get("profile_image_url"),
            "profile_url": obj.get("profile_url"),
            "profile_name": obj.get("profile_name"),
            "question_text": obj.get("question_text"),
            "original_question_text": obj.get("original_question_text"),
            "time_ago": obj.get("time_ago"),
            "timestamp": obj.get("timestamp"),
            "items": [GoogleBusinessAnswerElement.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj