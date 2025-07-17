from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_bing_keywords_data_price_data_info import AppendixBingKeywordsDataPriceDataInfo



class AppendixBingKeywordsDataPriceData(BaseModel):
    """
    AppendixBingKeywordsDataPriceData
    """ # noqa: E501
    audience_estimation: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    keyword_performance: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    keywords_for_keywords: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    keywords_for_site: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    keyword_suggestions_for_url: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    search_volume: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "audience_estimation", 
        "keyword_performance", 
        "keywords_for_keywords", 
        "keywords_for_site", 
        "keyword_suggestions_for_url", 
        "search_volume", 
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

        _dict['audience_estimation'] = self.audience_estimation.to_dict() if self.audience_estimation else None
        _dict['keyword_performance'] = self.keyword_performance.to_dict() if self.keyword_performance else None
        _dict['keywords_for_keywords'] = self.keywords_for_keywords.to_dict() if self.keywords_for_keywords else None
        _dict['keywords_for_site'] = self.keywords_for_site.to_dict() if self.keywords_for_site else None
        _dict['keyword_suggestions_for_url'] = self.keyword_suggestions_for_url.to_dict() if self.keyword_suggestions_for_url else None
        _dict['search_volume'] = self.search_volume.to_dict() if self.search_volume else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "audience_estimation": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["audience_estimation"]) if obj.get("audience_estimation") is not None else None,
            "keyword_performance": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["keyword_performance"]) if obj.get("keyword_performance") is not None else None,
            "keywords_for_keywords": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["keywords_for_keywords"]) if obj.get("keywords_for_keywords") is not None else None,
            "keywords_for_site": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["keywords_for_site"]) if obj.get("keywords_for_site") is not None else None,
            "keyword_suggestions_for_url": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["keyword_suggestions_for_url"]) if obj.get("keyword_suggestions_for_url") is not None else None,
            "search_volume": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["search_volume"]) if obj.get("search_volume") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj