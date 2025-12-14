from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_optimization_result_total_info import AiOptimizationResultTotalInfo
from dataforseo_client.models.ai_optimization_llm_mentionss_live_item import AiOptimizationLlmMentionssLiveItem



class AiOptimizationLlmMentionsCrossAggregatedMetricsLiveResultInfo(BaseModel):
    """
    AiOptimizationLlmMentionsCrossAggregatedMetricsLiveResultInfo
    """ # noqa: E501
    total: Optional[AiOptimizationResultTotalInfo] = Field(default=None, description=r"aggregated mentions metrics summary. contains overall aggregated LLM mention metrics across all found domains, grouped by various dimensions")
    items: Optional[List[Optional[AiOptimizationLlmMentionssLiveItem]]] = Field(default=None, description=r"contains relevant mentions data")
    __properties: ClassVar[List[str]] = [
        "total", 
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

        _dict['total'] = self.total.to_dict() if self.total else None
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
            "total": AiOptimizationResultTotalInfo.from_dict(obj["total"]) if obj.get("total") is not None else None,
            "items": [AiOptimizationLlmMentionssLiveItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj