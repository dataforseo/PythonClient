from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.content_analysis_summary_info import ContentAnalysisSummaryInfo



class SentimentConnotationDistribution(BaseModel):
    """
    SentimentConnotationDistribution
    """ # noqa: E501
    anger: Optional[ContentAnalysisSummaryInfo] = Field(default=None, description="")
    happiness: Optional[ContentAnalysisSummaryInfo] = Field(default=None, description="")
    love: Optional[ContentAnalysisSummaryInfo] = Field(default=None, description="")
    sadness: Optional[ContentAnalysisSummaryInfo] = Field(default=None, description="")
    share: Optional[ContentAnalysisSummaryInfo] = Field(default=None, description="")
    fun: Optional[ContentAnalysisSummaryInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "anger", 
        "happiness", 
        "love", 
        "sadness", 
        "share", 
        "fun", 
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

        _dict['anger'] = self.anger.to_dict() if self.anger else None
        _dict['happiness'] = self.happiness.to_dict() if self.happiness else None
        _dict['love'] = self.love.to_dict() if self.love else None
        _dict['sadness'] = self.sadness.to_dict() if self.sadness else None
        _dict['share'] = self.share.to_dict() if self.share else None
        _dict['fun'] = self.fun.to_dict() if self.fun else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "anger": ContentAnalysisSummaryInfo.from_dict(obj["anger"]) if obj.get("anger") is not None else None,
            "happiness": ContentAnalysisSummaryInfo.from_dict(obj["happiness"]) if obj.get("happiness") is not None else None,
            "love": ContentAnalysisSummaryInfo.from_dict(obj["love"]) if obj.get("love") is not None else None,
            "sadness": ContentAnalysisSummaryInfo.from_dict(obj["sadness"]) if obj.get("sadness") is not None else None,
            "share": ContentAnalysisSummaryInfo.from_dict(obj["share"]) if obj.get("share") is not None else None,
            "fun": ContentAnalysisSummaryInfo.from_dict(obj["fun"]) if obj.get("fun") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj