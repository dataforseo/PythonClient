# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class ContentGenerationGenerateLiveRequestInfo(BaseModel):
    """
    ContentGenerationGenerateLiveRequestInfo
    """ # noqa: E501
    text: Optional[StrictStr] = Field(default=None, description="initial target text required field text input for content generation; can contain from 1 to 500 tokens learn more about tokens on our help center")
    max_new_tokens: Optional[StrictInt] = Field(default=None, description="generation limit for new tokens required field if max_tokens is not specified the maximum number of new tokens for generated content; maximum value: 300; Note: the number does not include tokens specified in the text field; learn more about this parameter on our help center")
    max_tokens: Optional[StrictInt] = Field(default=None, description="generation limit for all tokens required field if max_new_tokens is not specified the maximum total number of tokens for generated content; maximum value: 1024; Note: the number includes tokens specified in the text field learn more about this parameter on our help center")
    creativity_index: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="creativity of content generation optional field if you use this field, you don’t need to use top_k / top_p / temperature the randomness of the selection of equally probable subsequent tokens; can take values from 0 to 1 default value: 0.8 learn more about this parameter on our help center")
    token_repetition_penalty: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="token repetition optional field limits the repetition of the same tokens in the generated content; can take values from 0.5 to 2; default value: 1")
    top_k: Optional[StrictInt] = Field(default=None, description="the number of initial tokens in each iteration for choosing a subsequent word optional field if you use creativity_index, this field will be ignored the higher the number, the more high-probability tokens will be shortlisted for generation; can take values from 1 to 100; default value: 40 learn more about this parameter on our help center")
    top_p: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="excludes initial tokens with probability lower than one optional field if you use creativity_index, this field will be ignored the higher the value, the less low-probability tokens may be shortlisted for generation; can take values from 0 to 1 default value: 0.9 Note:if both top_k and top_p are used, top_k acts first; learn more about this parameter on our help center")
    temperature: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="controls the randomness in the output optional field if you use creativity_index, this field will be ignored the lower the temperature, the more likely the model will choose words with a higher probability of occurrence; can take values from 0 to 1; default value: 0.7 learn more about this parameter on our help center")
    avoid_words: Optional[List[StrictStr]] = Field(default=None, description="words or phrases to avoid when generating a text optional field you can specify up to 50 terms; example: [\"term\", \"optimization\"]")
    avoid_starting_words: Optional[List[StrictStr]] = Field(default=None, description="words or phrases to avoid in the beginning of the generated text optional field you can specify up to 50 terms; example: [\"SEO\", \"search engine optimization\"]")
    stop_words: Optional[List[StrictStr]] = Field(default=None, description="words or phrases to end the text optional field you can specify up to 50 terms; example: [\"now\",\"subscribe\"]")
    supplement_token: Optional[StrictStr] = Field(default=None, description="token for generating subsequent results optional field provided in the identical filed of the response to each request; you can use this parameter to continue the generation of text from the initial response supplement_token values are unique for each subsequent task")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = ["text", "max_new_tokens", "max_tokens", "creativity_index", "token_repetition_penalty", "top_k", "top_p", "temperature", "avoid_words", "avoid_starting_words", "stop_words", "supplement_token", "tag"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ContentGenerationGenerateLiveRequestInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if max_new_tokens (nullable) is None
        # and model_fields_set contains the field
        if self.max_new_tokens is None and "max_new_tokens" in self.model_fields_set:
            _dict['max_new_tokens'] = None

        # set to None if max_tokens (nullable) is None
        # and model_fields_set contains the field
        if self.max_tokens is None and "max_tokens" in self.model_fields_set:
            _dict['max_tokens'] = None

        # set to None if creativity_index (nullable) is None
        # and model_fields_set contains the field
        if self.creativity_index is None and "creativity_index" in self.model_fields_set:
            _dict['creativity_index'] = None

        # set to None if token_repetition_penalty (nullable) is None
        # and model_fields_set contains the field
        if self.token_repetition_penalty is None and "token_repetition_penalty" in self.model_fields_set:
            _dict['token_repetition_penalty'] = None

        # set to None if top_k (nullable) is None
        # and model_fields_set contains the field
        if self.top_k is None and "top_k" in self.model_fields_set:
            _dict['top_k'] = None

        # set to None if top_p (nullable) is None
        # and model_fields_set contains the field
        if self.top_p is None and "top_p" in self.model_fields_set:
            _dict['top_p'] = None

        # set to None if temperature (nullable) is None
        # and model_fields_set contains the field
        if self.temperature is None and "temperature" in self.model_fields_set:
            _dict['temperature'] = None

        # set to None if avoid_words (nullable) is None
        # and model_fields_set contains the field
        if self.avoid_words is None and "avoid_words" in self.model_fields_set:
            _dict['avoid_words'] = None

        # set to None if avoid_starting_words (nullable) is None
        # and model_fields_set contains the field
        if self.avoid_starting_words is None and "avoid_starting_words" in self.model_fields_set:
            _dict['avoid_starting_words'] = None

        # set to None if stop_words (nullable) is None
        # and model_fields_set contains the field
        if self.stop_words is None and "stop_words" in self.model_fields_set:
            _dict['stop_words'] = None

        # set to None if supplement_token (nullable) is None
        # and model_fields_set contains the field
        if self.supplement_token is None and "supplement_token" in self.model_fields_set:
            _dict['supplement_token'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ContentGenerationGenerateLiveRequestInfo from a dict"""
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
            "tag": obj.get("tag")
        })
        return _obj


