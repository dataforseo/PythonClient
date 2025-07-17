from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_info import AppendixInfo



class AppendixContentAnalysisLimitsRatesDataInfo(BaseModel):
    """
    AppendixContentAnalysisLimitsRatesDataInfo
    """ # noqa: E501
    search: Optional[AppendixInfo] = Field(default=None, description="")
    summary: Optional[AppendixInfo] = Field(default=None, description="")
    sentiment_analysis: Optional[AppendixInfo] = Field(default=None, description="")
    rating_distribution: Optional[AppendixInfo] = Field(default=None, description="")
    phrase_trends: Optional[AppendixInfo] = Field(default=None, description="")
    category_trends: Optional[AppendixInfo] = Field(default=None, description="")
    locations: Optional[StrictFloat] = Field(default=None, description="")
    languages: Optional[StrictFloat] = Field(default=None, description="")
    categories: Optional[StrictFloat] = Field(default=None, description="")
    errors: Optional[StrictFloat] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "search", 
        "summary", 
        "sentiment_analysis", 
        "rating_distribution", 
        "phrase_trends", 
        "category_trends", 
        "locations", 
        "languages", 
        "categories", 
        "errors", 
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

        _dict['search'] = self.search.to_dict() if self.search else None
        _dict['summary'] = self.summary.to_dict() if self.summary else None
        _dict['sentiment_analysis'] = self.sentiment_analysis.to_dict() if self.sentiment_analysis else None
        _dict['rating_distribution'] = self.rating_distribution.to_dict() if self.rating_distribution else None
        _dict['phrase_trends'] = self.phrase_trends.to_dict() if self.phrase_trends else None
        _dict['category_trends'] = self.category_trends.to_dict() if self.category_trends else None
        _dict['locations'] = self.locations
        _dict['languages'] = self.languages
        _dict['categories'] = self.categories
        _dict['errors'] = self.errors
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "search": AppendixInfo.from_dict(obj["search"]) if obj.get("search") is not None else None,
            "summary": AppendixInfo.from_dict(obj["summary"]) if obj.get("summary") is not None else None,
            "sentiment_analysis": AppendixInfo.from_dict(obj["sentiment_analysis"]) if obj.get("sentiment_analysis") is not None else None,
            "rating_distribution": AppendixInfo.from_dict(obj["rating_distribution"]) if obj.get("rating_distribution") is not None else None,
            "phrase_trends": AppendixInfo.from_dict(obj["phrase_trends"]) if obj.get("phrase_trends") is not None else None,
            "category_trends": AppendixInfo.from_dict(obj["category_trends"]) if obj.get("category_trends") is not None else None,
            "locations": obj.get("locations"),
            "languages": obj.get("languages"),
            "categories": obj.get("categories"),
            "errors": obj.get("errors"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj