from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.positive_connotation_distribution import PositiveConnotationDistribution
from dataforseo_client.models.sentiment_connotation_distribution import SentimentConnotationDistribution



class ContentAnalysisSentimentAnalysisLiveResultInfo(BaseModel):
    """
    ContentAnalysisSentimentAnalysisLiveResultInfo
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    positive_connotation_distribution: Optional[PositiveConnotationDistribution] = Field(default=None, description="citation distribution by sentiment connotation types. contains objects with citation counts and relevant data distributed by types of sentiments (sentiment polarity);. possible sentiment connotation types: positive, negative, neutral")
    sentiment_connotation_distribution: Optional[SentimentConnotationDistribution] = Field(default=None, description="citation distribution by sentiment connotations. contains objects with citation counts and relevant data distributed by sentiments (emotional reactions);. possible sentiment connotation types: anger, happiness, love, sadness, share, fun")
    __properties: ClassVar[List[str]] = [
        "type", 
        "positive_connotation_distribution", 
        "sentiment_connotation_distribution", 
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
        _dict['positive_connotation_distribution'] = self.positive_connotation_distribution.to_dict() if self.positive_connotation_distribution else None
        _dict['sentiment_connotation_distribution'] = self.sentiment_connotation_distribution.to_dict() if self.sentiment_connotation_distribution else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "positive_connotation_distribution": PositiveConnotationDistribution.from_dict(obj["positive_connotation_distribution"]) if obj.get("positive_connotation_distribution") is not None else None,
            "sentiment_connotation_distribution": SentimentConnotationDistribution.from_dict(obj["sentiment_connotation_distribution"]) if obj.get("sentiment_connotation_distribution") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj