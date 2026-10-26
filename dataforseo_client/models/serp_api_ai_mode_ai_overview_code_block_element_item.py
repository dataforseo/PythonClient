from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_serp_api_ai_mode_ai_overview_element_item import BaseSerpApiAiModeAiOverviewElementItem



class SerpApiAiModeAiOverviewCodeBlockElementItem(BaseSerpApiAiModeAiOverviewElementItem):
    """
    SerpApiAiModeAiOverviewCodeBlockElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    position: Optional[StrictStr] = Field(default=None, description=r"*the alignment of the element in SERP*. can take the following values:. `left`, `right`")
    code_type: Optional[StrictStr] = Field(default=None, description=r"*programming language or data format of the code block*. indicates the syntax the code block is rendered in. examples:. `json`, `python`")
    text: Optional[StrictStr] = Field(default=None, description=r"*text description in the element*")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "code_type", 
        "text", 
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
        _dict['position'] = self.position
        _dict['code_type'] = self.code_type
        _dict['text'] = self.text
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "position": obj.get("position"),
            "code_type": obj.get("code_type"),
            "text": obj.get("text"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj