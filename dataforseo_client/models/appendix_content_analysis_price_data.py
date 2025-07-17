from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo
from dataforseo_client.models.appendix_bing_keywords_data_price_data_info import AppendixBingKeywordsDataPriceDataInfo



class AppendixContentAnalysisPriceData(BaseModel):
    """
    AppendixContentAnalysisPriceData
    """ # noqa: E501
    categories: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    category_trends: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    errors: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    languages: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    locations: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    phrase_trends: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    rating_distribution: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    search: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    sentiment_analysis: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    summary: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "categories", 
        "category_trends", 
        "errors", 
        "languages", 
        "locations", 
        "phrase_trends", 
        "rating_distribution", 
        "search", 
        "sentiment_analysis", 
        "summary", 
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

        _dict['categories'] = self.categories.to_dict() if self.categories else None
        _dict['category_trends'] = self.category_trends.to_dict() if self.category_trends else None
        _dict['errors'] = self.errors.to_dict() if self.errors else None
        _dict['languages'] = self.languages.to_dict() if self.languages else None
        _dict['locations'] = self.locations.to_dict() if self.locations else None
        _dict['phrase_trends'] = self.phrase_trends.to_dict() if self.phrase_trends else None
        _dict['rating_distribution'] = self.rating_distribution.to_dict() if self.rating_distribution else None
        _dict['search'] = self.search.to_dict() if self.search else None
        _dict['sentiment_analysis'] = self.sentiment_analysis.to_dict() if self.sentiment_analysis else None
        _dict['summary'] = self.summary.to_dict() if self.summary else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "categories": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["categories"]) if obj.get("categories") is not None else None,
            "category_trends": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["category_trends"]) if obj.get("category_trends") is not None else None,
            "errors": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["errors"]) if obj.get("errors") is not None else None,
            "languages": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["languages"]) if obj.get("languages") is not None else None,
            "locations": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["locations"]) if obj.get("locations") is not None else None,
            "phrase_trends": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["phrase_trends"]) if obj.get("phrase_trends") is not None else None,
            "rating_distribution": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["rating_distribution"]) if obj.get("rating_distribution") is not None else None,
            "search": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["search"]) if obj.get("search") is not None else None,
            "sentiment_analysis": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["sentiment_analysis"]) if obj.get("sentiment_analysis") is not None else None,
            "summary": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["summary"]) if obj.get("summary") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj