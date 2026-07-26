from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.llm_mentions_aggregated_metrics_info import LlmMentionsAggregatedMetricsInfo



class AiOptimizationLlmMentionsTargetMetricsLiveResultInfo(BaseModel):
    """
    AiOptimizationLlmMentionsTargetMetricsLiveResultInfo
    """ # noqa: E501
    total_count: Optional[StrictInt] = Field(default=None, description=r"*total amount of results relevant to the request*. in this case, always equals `0`")
    offset: Optional[StrictInt] = Field(default=None, description=r"*the number of mentions objects that are omitted in the `items` array*. in this case, always equals `0`")
    items_count: Optional[StrictInt] = Field(default=None, description=r"*the number of results returned in the `items` array*. in this case, always equals `0`")
    aggregated_metrics: Optional[LlmMentionsAggregatedMetricsInfo] = Field(default=None, description=r"*aggregated mentions metrics*. contains aggregated LLM mention metrics across all found domains, grouped by various dimensions")
    items: Optional[List[Optional[Any]]] = Field(default=None, description=r"*individual target results*. in this case, equals `null`")
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
        _dict['aggregated_metrics'] = self.aggregated_metrics.to_dict() if self.aggregated_metrics else None
        _dict['items'] = self.items
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
            "aggregated_metrics": LlmMentionsAggregatedMetricsInfo.from_dict(obj["aggregated_metrics"]) if obj.get("aggregated_metrics") is not None else None,
            "items": obj.get("items"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj