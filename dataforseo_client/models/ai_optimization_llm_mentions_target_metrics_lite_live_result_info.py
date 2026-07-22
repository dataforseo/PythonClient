from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_optimization_llm_mentions_target_metrics_lite_live_item import AiOptimizationLlmMentionsTargetMetricsLiteLiveItem



class AiOptimizationLlmMentionsTargetMetricsLiteLiveResultInfo(BaseModel):
    """
    AiOptimizationLlmMentionsTargetMetricsLiteLiveResultInfo
    """ # noqa: E501
    total_count: Optional[StrictInt] = Field(default=None, description=r"total amount of results relevant the request")
    offset: Optional[StrictInt] = Field(default=None, description=r"the number of mentions objects that are omitted in the items array")
    items_count: Optional[StrictInt] = Field(default=None, description=r"the number of results returned in the items array")
    aggregated_metrics: Optional[Any] = Field(default=None, description=r"aggregated mentions metrics. in this case, always returns null")
    items: Optional[List[Optional[AiOptimizationLlmMentionsTargetMetricsLiteLiveItem]]] = Field(default=None, description=r"array of aggregated mentions metrics. contains objects with aggregated mention metrics for the specified target")
    __properties: ClassVar[List[str]] = [
        "total_count", 
        "offset", 
        "items_count", 
        "aggregated_metrics", 
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

        _dict['total_count'] = self.total_count
        _dict['offset'] = self.offset
        _dict['items_count'] = self.items_count
        _dict['aggregated_metrics'] = self.aggregated_metrics
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
            "total_count": obj.get("total_count"),
            "offset": obj.get("offset"),
            "items_count": obj.get("items_count"),
            "aggregated_metrics": obj.get("aggregated_metrics"),
            "items": [AiOptimizationLlmMentionsTargetMetricsLiteLiveItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj