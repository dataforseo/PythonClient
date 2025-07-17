from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.content_analysis_summary_info import ContentAnalysisSummaryInfo



class ContentAnalysisRatingDistributionLiveResultInfo(BaseModel):
    """
    ContentAnalysisRatingDistributionLiveResultInfo
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    min: Optional[StrictFloat] = Field(default=None, description="min rating on a distribution scale")
    max: Optional[StrictFloat] = Field(default=None, description="max rating on a distribution scale")
    metrics: Optional[ContentAnalysisSummaryInfo] = Field(default=None, description="contains rating distribution metrics")
    __properties: ClassVar[List[str]] = [
        "type", 
        "min", 
        "max", 
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

        _dict['type'] = self.type
        _dict['min'] = self.min
        _dict['max'] = self.max
        _dict['metrics'] = self.metrics.to_dict() if self.metrics else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "min": obj.get("min"),
            "max": obj.get("max"),
            "metrics": ContentAnalysisSummaryInfo.from_dict(obj["metrics"]) if obj.get("metrics") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj