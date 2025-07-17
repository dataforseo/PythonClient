from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.keyword_intent_info import KeywordIntentInfo



class DataforseoLabsGoogleSearchIntentLiveItem(BaseModel):
    """
    DataforseoLabsGoogleSearchIntentLiveItem
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="target keyword in a POST array")
    keyword_intent: Optional[KeywordIntentInfo] = Field(default=None, description="search intent data relevant for the specified keyword")
    secondary_keyword_intents: Optional[List[Optional[KeywordIntentInfo]]] = Field(default=None, description="contains objects with other possible search intents for the specified keyword")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "keyword_intent", 
        "secondary_keyword_intents", 
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

        _dict['keyword'] = self.keyword
        _dict['keyword_intent'] = self.keyword_intent.to_dict() if self.keyword_intent else None
        secondary_keyword_intents_items = []
        if self.secondary_keyword_intents:
            for _item in self.secondary_keyword_intents:
                if _item:
                    secondary_keyword_intents_items.append(_item.to_dict())
            _dict['secondary_keyword_intents'] = secondary_keyword_intents_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "keyword_intent": KeywordIntentInfo.from_dict(obj["keyword_intent"]) if obj.get("keyword_intent") is not None else None,
            "secondary_keyword_intents": [KeywordIntentInfo.from_dict(_item) for _item in obj["secondary_keyword_intents"]] if obj.get("secondary_keyword_intents") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj