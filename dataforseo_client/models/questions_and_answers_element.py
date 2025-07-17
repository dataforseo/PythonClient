from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class QuestionsAndAnswersElement(BaseModel):
    """
    QuestionsAndAnswersElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    url: Optional[StrictStr] = Field(default=None, description="URL")
    question_text: Optional[StrictStr] = Field(default=None, description="question included in the item")
    answer_text: Optional[StrictStr] = Field(default=None, description="answer included in the item")
    source: Optional[StrictStr] = Field(default=None, description="source of the element. indicates the source of information included in the top_stories_element")
    domain: Optional[StrictStr] = Field(default=None, description="website domain")
    votes: Optional[StrictInt] = Field(default=None, description="answer upvotes from the source")
    __properties: ClassVar[List[str]] = [
        "type", 
        "url", 
        "question_text", 
        "answer_text", 
        "source", 
        "domain", 
        "votes", 
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
        _dict['url'] = self.url
        _dict['question_text'] = self.question_text
        _dict['answer_text'] = self.answer_text
        _dict['source'] = self.source
        _dict['domain'] = self.domain
        _dict['votes'] = self.votes
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "url": obj.get("url"),
            "question_text": obj.get("question_text"),
            "answer_text": obj.get("answer_text"),
            "source": obj.get("source"),
            "domain": obj.get("domain"),
            "votes": obj.get("votes"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj