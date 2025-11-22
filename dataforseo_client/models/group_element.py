from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class GroupElement(BaseModel):
    """
    GroupElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    key: Optional[StrictStr] = Field(default=None, description=r"grouping identifier. the specific identifier for the grouping dimension")
    mentions: Optional[StrictInt] = Field(default=None, description=r"total LLM mentions count. the number of times the target keyword or domain were mentioned in relation to this specific grouping key")
    ai_search_volume: Optional[StrictInt] = Field(default=None, description=r"current AI search volume rate of a keyword. learn more about this metric here")
    impressions: Optional[StrictInt] = Field(default=None, description=r"current AI impressions rate of a keyword")
    __properties: ClassVar[List[str]] = [
        "type", 
        "key", 
        "mentions", 
        "ai_search_volume", 
        "impressions", 
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
        _dict['key'] = self.key
        _dict['mentions'] = self.mentions
        _dict['ai_search_volume'] = self.ai_search_volume
        _dict['impressions'] = self.impressions
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "key": obj.get("key"),
            "mentions": obj.get("mentions"),
            "ai_search_volume": obj.get("ai_search_volume"),
            "impressions": obj.get("impressions"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj