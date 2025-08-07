from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_monthly_searches import AiMonthlySearches



class AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveItem(BaseModel):
    """
    AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveItem
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="specified keyword")
    ai_search_volume: Optional[StrictInt] = Field(default=None, description="current AI search volume rate of a keyword")
    ai_monthly_searches: Optional[List[Optional[AiMonthlySearches]]] = Field(default=None, description="monthly AI search volume rates. array of objects with AI search volume rates in a certain month of a year")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "ai_search_volume", 
        "ai_monthly_searches", 
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
        _dict['ai_search_volume'] = self.ai_search_volume
        ai_monthly_searches_items = []
        if self.ai_monthly_searches:
            for _item in self.ai_monthly_searches:
                if _item:
                    ai_monthly_searches_items.append(_item.to_dict())
            _dict['ai_monthly_searches'] = ai_monthly_searches_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "ai_search_volume": obj.get("ai_search_volume"),
            "ai_monthly_searches": [AiMonthlySearches.from_dict(_item) for _item in obj["ai_monthly_searches"]] if obj.get("ai_monthly_searches") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj