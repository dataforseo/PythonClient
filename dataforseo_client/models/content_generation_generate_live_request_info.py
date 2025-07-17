from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ContentGenerationGenerateLiveRequestInfo(BaseModel):
    """
    ContentGenerationGenerateLiveRequestInfo
    """ # noqa: E501
    text: Optional[StrictStr] = Field(default=None, description="initial target text. required field. text input for content generation;. can contain from 1 to 500 tokens. learn more about tokens on our help center")
    max_new_tokens: Optional[StrictInt] = Field(default=None, description="generation limit for new tokens. required field if max_tokens is not specified. the maximum number of new tokens for generated content;. maximum value: 300;. Note: the number does not include tokens specified in the text field;. learn more about this parameter on our help center")
    max_tokens: Optional[StrictInt] = Field(default=None, description="generation limit for all tokens. required field if max_new_tokens is not specified. the maximum total number of tokens for generated content;. maximum value: 1024;. Note: the number includes tokens specified in the text field. learn more about this parameter on our help center")
    creativity_index: Optional[StrictFloat] = Field(default=None, description="creativity of content generation. optional field. if you use this field, you don’t need to use top_k / top_p / temperature. the randomness of the selection of equally probable subsequent tokens;. can take values from 0 to 1. default value: 0.8. learn more about this parameter on our help center")
    token_repetition_penalty: Optional[StrictFloat] = Field(default=None, description="token repetition. optional field. limits the repetition of the same tokens in the generated content;. can take values from 0.5 to 2;. default value: 1")
    top_k: Optional[StrictInt] = Field(default=None, description="the number of initial tokens in each iteration for choosing a subsequent word. optional field. if you use creativity_index, this field will be ignored. the higher the number, the more high-probability tokens will be shortlisted for generation;. can take values from 1 to 100;. default value: 40. learn more about this parameter on our help center")
    top_p: Optional[StrictFloat] = Field(default=None, description="excludes initial tokens with probability lower than one. optional field. if you use creativity_index, this field will be ignored. the higher the value, the less low-probability tokens may be shortlisted for generation;. can take values from 0 to 1. default value: 0.9. Note:if both top_k and top_p are used, top_k acts first;. learn more about this parameter on our help center")
    temperature: Optional[StrictFloat] = Field(default=None, description="controls the randomness in the output. optional field. if you use creativity_index, this field will be ignored. the lower the temperature, the more likely the model will choose words with a higher probability of occurrence;. can take values from 0 to 1;. default value: 0.7. learn more about this parameter on our help center")
    avoid_words: Optional[List[Optional[StrictStr]]] = Field(default=None, description="words or phrases to avoid when generating a text. optional field. you can specify up to 50 terms;. example:. ['term', 'optimization']")
    avoid_starting_words: Optional[List[Optional[StrictStr]]] = Field(default=None, description="words or phrases to avoid in the beginning of the generated text. optional field. you can specify up to 50 terms;. example:. ['SEO', 'search engine optimization']")
    stop_words: Optional[List[Optional[StrictStr]]] = Field(default=None, description="words or phrases to end the text. optional field. you can specify up to 50 terms;. example:. ['now','subscribe']")
    supplement_token: Optional[StrictStr] = Field(default=None, description="token for generating subsequent results. optional field. provided in the identical filed of the response to each request;. you can use this parameter to continue the generation of text from the initial response. supplement_token values are unique for each subsequent task")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "text", 
        "max_new_tokens", 
        "max_tokens", 
        "creativity_index", 
        "token_repetition_penalty", 
        "top_k", 
        "top_p", 
        "temperature", 
        "avoid_words", 
        "avoid_starting_words", 
        "stop_words", 
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

        _dict['text'] = self.text
        _dict['max_new_tokens'] = self.max_new_tokens
        _dict['max_tokens'] = self.max_tokens
        _dict['creativity_index'] = self.creativity_index
        _dict['token_repetition_penalty'] = self.token_repetition_penalty
        _dict['top_k'] = self.top_k
        _dict['top_p'] = self.top_p
        _dict['temperature'] = self.temperature
        _dict['avoid_words'] = self.avoid_words
        _dict['avoid_starting_words'] = self.avoid_starting_words
        _dict['stop_words'] = self.stop_words
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
            "text": obj.get("text"),
            "max_new_tokens": obj.get("max_new_tokens"),
            "max_tokens": obj.get("max_tokens"),
            "creativity_index": obj.get("creativity_index"),
            "token_repetition_penalty": obj.get("token_repetition_penalty"),
            "top_k": obj.get("top_k"),
            "top_p": obj.get("top_p"),
            "temperature": obj.get("temperature"),
            "avoid_words": obj.get("avoid_words"),
            "avoid_starting_words": obj.get("avoid_starting_words"),
            "stop_words": obj.get("stop_words"),
            "supplement_token": obj.get("supplement_token"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj