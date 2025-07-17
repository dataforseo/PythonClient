from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ContentGenerationTextSummaryLiveRequestInfo(BaseModel):
    """
    ContentGenerationTextSummaryLiveRequestInfo
    """ # noqa: E501
    text: Optional[StrictStr] = Field(default=None, description="target text. required field. can contain from 1 to 10000 tokens. learn more about tokens on our help center")
    language_name: Optional[StrictStr] = Field(default=None, description="name of the text language. required field if you do not specify language_code. see the List of Languages for Content Generation Text Summary API")
    language_code: Optional[StrictStr] = Field(default=None, description="code of the text language. required field if you do not specify language_name. see the List of Languages for Content Generation Text Summary API")
    internal_list_limit: Optional[StrictInt] = Field(default=None, description="maximum number of elements within internal arrays. optional field. you can use this field to limit the number of elements within the keyword_density array. default value: 10")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "text", 
        "language_name", 
        "language_code", 
        "internal_list_limit", 
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
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['internal_list_limit'] = self.internal_list_limit
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
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "internal_list_limit": obj.get("internal_list_limit"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj