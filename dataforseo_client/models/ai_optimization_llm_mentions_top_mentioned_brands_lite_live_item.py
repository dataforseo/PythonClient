from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.aggregated_metrics_info_total_info import AggregatedMetricsInfoTotalInfo



class AiOptimizationLlmMentionsTopMentionedBrandsLiteLiveItem(BaseModel):
    """
    AiOptimizationLlmMentionsTopMentionedBrandsLiteLiveItem
    """ # noqa: E501
    brand: Optional[StrictStr] = Field(default=None, description=r"brand name. brand identifier of aggregated metrics")
    location: Optional[StrictInt] = Field(default=None, description=r"location identifier. location of aggregated metrics")
    language: Optional[StrictStr] = Field(default=None, description=r"language identifier. language of aggregated metrics")
    platform: Optional[StrictStr] = Field(default=None, description=r"LLM platform identifiers. LLM platform of aggregated metrics")
    metrics: Optional[AggregatedMetricsInfoTotalInfo] = Field(default=None, description=r"LLM metrics. metrics aggregated by specific parameters and respective identifiers")
    __properties: ClassVar[List[str]] = [
        "brand", 
        "location", 
        "language", 
        "platform", 
        "metrics", 
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

        _dict['brand'] = self.brand
        _dict['location'] = self.location
        _dict['language'] = self.language
        _dict['platform'] = self.platform
        _dict['metrics'] = self.metrics.to_dict() if self.metrics else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "brand": obj.get("brand"),
            "location": obj.get("location"),
            "language": obj.get("language"),
            "platform": obj.get("platform"),
            "metrics": AggregatedMetricsInfoTotalInfo.from_dict(obj["metrics"]) if obj.get("metrics") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj