from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.content_generation_check_grammar_live_item import ContentGenerationCheckGrammarLiveItem



class ContentGenerationCheckGrammarLiveResultInfo(BaseModel):
    """
    ContentGenerationCheckGrammarLiveResultInfo
    """ # noqa: E501
    input_tokens: Optional[StrictInt] = Field(default=None, description="number of input tokens in the POST request")
    output_tokens: Optional[StrictInt] = Field(default=None, description="number of output tokens in the response")
    new_tokens: Optional[StrictInt] = Field(default=None, description="number of new tokens in the response")
    initial_text: Optional[StrictStr] = Field(default=None, description="initial text in the POST request")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in the POST request")
    items_count: Optional[StrictInt] = Field(default=None, description="the number of results returned in the items array")
    items: Optional[List[Optional[ContentGenerationCheckGrammarLiveItem]]] = Field(default=None, description="contains grammar or spelling errors and related data")
    __properties: ClassVar[List[str]] = [
        "input_tokens", 
        "output_tokens", 
        "new_tokens", 
        "initial_text", 
        "language_code", 
        "items_count", 
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

        _dict['input_tokens'] = self.input_tokens
        _dict['output_tokens'] = self.output_tokens
        _dict['new_tokens'] = self.new_tokens
        _dict['initial_text'] = self.initial_text
        _dict['language_code'] = self.language_code
        _dict['items_count'] = self.items_count
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
            "input_tokens": obj.get("input_tokens"),
            "output_tokens": obj.get("output_tokens"),
            "new_tokens": obj.get("new_tokens"),
            "initial_text": obj.get("initial_text"),
            "language_code": obj.get("language_code"),
            "items_count": obj.get("items_count"),
            "items": [ContentGenerationCheckGrammarLiveItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj