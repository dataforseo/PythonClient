from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_optimization_ai_keyword_data_keywords_search_volume_live_item import AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveItem



class AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveResultInfo(BaseModel):
    """
    AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveResultInfo
    """ # noqa: E501
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    items_count: Optional[StrictInt] = Field(default=None, description="number of results returned in the items array")
    items: Optional[List[Optional[AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveItem]]] = Field(default=None, description="contains specified keywords with their AI search volume rates")
    __properties: ClassVar[List[str]] = [
        "location_code", 
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

        _dict['location_code'] = self.location_code
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
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "items_count": obj.get("items_count"),
            "items": [AiOptimizationAiKeywordDataKeywordsSearchVolumeLiveItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj