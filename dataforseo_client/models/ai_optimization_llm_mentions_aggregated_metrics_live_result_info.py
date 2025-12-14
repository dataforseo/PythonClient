from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_optimization_result_total_info import AiOptimizationResultTotalInfo



class AiOptimizationLlmMentionsAggregatedMetricsLiveResultInfo(BaseModel):
    """
    AiOptimizationLlmMentionsAggregatedMetricsLiveResultInfo
    """ # noqa: E501
    total: Optional[AiOptimizationResultTotalInfo] = Field(default=None, description=r"aggregated mentions metrics summary. contains overall aggregated LLM mention metrics across all found domains, grouped by various dimensions")
    items: Optional[Any] = Field(default=None, description=r"individual pages results. array containing detailed mention metrics for each of the found top pages. in this case, equals null")
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
        _dict['items'] = self.items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "total": AiOptimizationResultTotalInfo.from_dict(obj["total"]) if obj.get("total") is not None else None,
            "items": obj.get("items"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj