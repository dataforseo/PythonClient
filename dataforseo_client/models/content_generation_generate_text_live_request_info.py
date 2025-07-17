from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ContentGenerationGenerateTextLiveRequestInfo(BaseModel):
    """
    ContentGenerationGenerateTextLiveRequestInfo
    """ # noqa: E501
    topic: Optional[StrictStr] = Field(default=None, description="main topic of the content to generate. required field. main topic for generating content;. can contain from 1 to 50 tokens")
    word_count: Optional[StrictInt] = Field(default=None, description="number of words in content. required field. the number of tokens in the generated text;. can take values from 1 to 1000")
    sub_topics: Optional[List[Optional[StrictStr]]] = Field(default=None, description="secondary topics of the content to generate. optional field. secondary topics for generating content;. can contain up to 10 terms;. example: 'sub_topics': ['Apple','Pixar','Amazing Products']")
    description: Optional[StrictStr] = Field(default=None, description="meta description of the content to generate. optional field. can contain from 1 to 1000 tokens. learn more about this parameter on our help center")
    meta_keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="keywords for the content to generate. optional field. can contain up to 10 terms;. learn more about this parameter on our help center. example: 'meta_keywords': ['iPhone','sell','CEO']")
    creativity_index: Optional[StrictFloat] = Field(default=None, description="creativity of content generation. optional field. the randomness of the selection of equally probable subsequent tokens;. can take values from 0 to 1. default value: 0.8. learn more about this parameter on our help center")
    include_conclusion: Optional[StrictBool] = Field(default=None, description="include conclusion in generated text. optional field. if set to true, generated content will include a logical conclusion")
    supplement_token: Optional[StrictStr] = Field(default=None, description="token for generating subsequent results. optional field. provided in the identical filed of the response to each request;. you can use this parameter to continue the generation of text from the initial response. supplement_token values are unique for each subsequent task")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "topic", 
        "word_count", 
        "sub_topics", 
        "description", 
        "meta_keywords", 
        "creativity_index", 
        "include_conclusion", 
        "supplement_token", 
        "tag", 
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

        _dict['topic'] = self.topic
        _dict['word_count'] = self.word_count
        _dict['sub_topics'] = self.sub_topics
        _dict['description'] = self.description
        _dict['meta_keywords'] = self.meta_keywords
        _dict['creativity_index'] = self.creativity_index
        _dict['include_conclusion'] = self.include_conclusion
        _dict['supplement_token'] = self.supplement_token
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "topic": obj.get("topic"),
            "word_count": obj.get("word_count"),
            "sub_topics": obj.get("sub_topics"),
            "description": obj.get("description"),
            "meta_keywords": obj.get("meta_keywords"),
            "creativity_index": obj.get("creativity_index"),
            "include_conclusion": obj.get("include_conclusion"),
            "supplement_token": obj.get("supplement_token"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj