from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.content_analysis_summary_info import ContentAnalysisSummaryInfo



class PositiveConnotationDistribution(BaseModel):
    """
    PositiveConnotationDistribution
    """ # noqa: E501
    positive: Optional[ContentAnalysisSummaryInfo] = Field(default=None, description="")
    negative: Optional[ContentAnalysisSummaryInfo] = Field(default=None, description="")
    neutral: Optional[ContentAnalysisSummaryInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "positive", 
        "negative", 
        "neutral", 
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

        _dict['positive'] = self.positive.to_dict() if self.positive else None
        _dict['negative'] = self.negative.to_dict() if self.negative else None
        _dict['neutral'] = self.neutral.to_dict() if self.neutral else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "positive": ContentAnalysisSummaryInfo.from_dict(obj["positive"]) if obj.get("positive") is not None else None,
            "negative": ContentAnalysisSummaryInfo.from_dict(obj["negative"]) if obj.get("negative") is not None else None,
            "neutral": ContentAnalysisSummaryInfo.from_dict(obj["neutral"]) if obj.get("neutral") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj