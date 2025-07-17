from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ContentGenerationGenerateMetaTagsLiveResultInfo(BaseModel):
    """
    ContentGenerationGenerateMetaTagsLiveResultInfo
    """ # noqa: E501
    input_tokens: Optional[StrictInt] = Field(default=None, description="number of input tokens")
    output_tokens: Optional[StrictInt] = Field(default=None, description="number of output tokens")
    new_tokens: Optional[StrictInt] = Field(default=None, description="number of new tokens")
    title: Optional[StrictStr] = Field(default=None, description="generated title")
    description: Optional[StrictStr] = Field(default=None, description="generated description")
    __properties: ClassVar[List[str]] = [
        "input_tokens", 
        "output_tokens", 
        "new_tokens", 
        "title", 
        "description", 
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

        _dict['input_tokens'] = self.input_tokens
        _dict['output_tokens'] = self.output_tokens
        _dict['new_tokens'] = self.new_tokens
        _dict['title'] = self.title
        _dict['description'] = self.description
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "input_tokens": obj.get("input_tokens"),
            "output_tokens": obj.get("output_tokens"),
            "new_tokens": obj.get("new_tokens"),
            "title": obj.get("title"),
            "description": obj.get("description"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj