from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ContentGenerationCheckGrammarLiveItem(BaseModel):
    """
    ContentGenerationCheckGrammarLiveItem
    """ # noqa: E501
    message: Optional[StrictStr] = Field(default=None, description="message of the grammar or spelling error")
    description: Optional[StrictStr] = Field(default=None, description="description of the grammar or spelling error")
    suggestions: Optional[List[Optional[StrictStr]]] = Field(default=None, description="suggested corrections")
    offset: Optional[StrictInt] = Field(default=None, description="offset token for subsequent requests")
    length: Optional[StrictInt] = Field(default=None, description="offset token for subsequent requests")
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rule_id: Optional[StrictStr] = Field(default=None, description="id of the grammar or spelling rule. see the List of Grammar Rules for Content Generation API")
    rule_description: Optional[StrictStr] = Field(default=None, description="description of the grammar or spelling rule")
    rule_issue_type: Optional[StrictStr] = Field(default=None, description="type of the issue found by the relevant rule")
    rule_category_id: Optional[StrictStr] = Field(default=None, description="id of the rule category")
    rule_category_name: Optional[StrictStr] = Field(default=None, description="name of the rule category")
    __properties: ClassVar[List[str]] = [
        "message", 
        "description", 
        "suggestions", 
        "offset", 
        "length", 
        "type", 
        "rule_id", 
        "rule_description", 
        "rule_issue_type", 
        "rule_category_id", 
        "rule_category_name", 
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

        _dict['message'] = self.message
        _dict['description'] = self.description
        _dict['suggestions'] = self.suggestions
        _dict['offset'] = self.offset
        _dict['length'] = self.length
        _dict['type'] = self.type
        _dict['rule_id'] = self.rule_id
        _dict['rule_description'] = self.rule_description
        _dict['rule_issue_type'] = self.rule_issue_type
        _dict['rule_category_id'] = self.rule_category_id
        _dict['rule_category_name'] = self.rule_category_name
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "message": obj.get("message"),
            "description": obj.get("description"),
            "suggestions": obj.get("suggestions"),
            "offset": obj.get("offset"),
            "length": obj.get("length"),
            "type": obj.get("type"),
            "rule_id": obj.get("rule_id"),
            "rule_description": obj.get("rule_description"),
            "rule_issue_type": obj.get("rule_issue_type"),
            "rule_category_id": obj.get("rule_category_id"),
            "rule_category_name": obj.get("rule_category_name"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj