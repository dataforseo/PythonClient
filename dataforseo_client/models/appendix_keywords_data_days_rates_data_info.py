from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_info import AppendixInfo
from dataforseo_client.models.appendix_bing_keywords_data_limits_rates_data_info import AppendixBingKeywordsDataLimitsRatesDataInfo
from dataforseo_client.models.appendix_google_ads_keywords_data_limits_rates_data_info import AppendixGoogleAdsKeywordsDataLimitsRatesDataInfo
from dataforseo_client.models.appendix_dataforseo_trends_keywords_data_limits_rates_data_info import AppendixDataforseoTrendsKeywordsDataLimitsRatesDataInfo
from dataforseo_client.models.appendix_clickstream_data_keywords_data_limits_rates_data_info import AppendixClickstreamDataKeywordsDataLimitsRatesDataInfo



class AppendixKeywordsDataDaysRatesDataInfo(BaseModel):
    """
    AppendixKeywordsDataDaysRatesDataInfo
    """ # noqa: E501
    keywords_for_keywords: Optional[AppendixInfo] = Field(default=None, description="")
    keywords_for_site: Optional[AppendixInfo] = Field(default=None, description="")
    search_volume: Optional[AppendixInfo] = Field(default=None, description="")
    ad_traffic_by_keywords: Optional[AppendixInfo] = Field(default=None, description="")
    languages: Optional[StrictFloat] = Field(default=None, description="")
    locations: Optional[StrictFloat] = Field(default=None, description="")
    tasks_ready: Optional[StrictFloat] = Field(default=None, description="")
    explore: Optional[AppendixInfo] = Field(default=None, description="")
    categories: Optional[StrictFloat] = Field(default=None, description="")
    errors: Optional[StrictFloat] = Field(default=None, description="")
    bing: Optional[AppendixBingKeywordsDataLimitsRatesDataInfo] = Field(default=None, description="")
    keyword_performance: Optional[AppendixInfo] = Field(default=None, description="")
    locations_and_languages: Optional[StrictFloat] = Field(default=None, description="")
    google_ads: Optional[AppendixGoogleAdsKeywordsDataLimitsRatesDataInfo] = Field(default=None, description="")
    dataforseo_trends: Optional[AppendixDataforseoTrendsKeywordsDataLimitsRatesDataInfo] = Field(default=None, description="")
    clickstream_data: Optional[AppendixClickstreamDataKeywordsDataLimitsRatesDataInfo] = Field(default=None, description="")
    audience_estimation: Optional[AppendixInfo] = Field(default=None, description="")
    keyword_suggestions_for_url: Optional[AppendixInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "keywords_for_keywords", 
        "keywords_for_site", 
        "search_volume", 
        "ad_traffic_by_keywords", 
        "languages", 
        "locations", 
        "tasks_ready", 
        "explore", 
        "categories", 
        "errors", 
        "bing", 
        "keyword_performance", 
        "locations_and_languages", 
        "google_ads", 
        "dataforseo_trends", 
        "clickstream_data", 
        "audience_estimation", 
        "keyword_suggestions_for_url", 
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

        _dict['keywords_for_keywords'] = self.keywords_for_keywords.to_dict() if self.keywords_for_keywords else None
        _dict['keywords_for_site'] = self.keywords_for_site.to_dict() if self.keywords_for_site else None
        _dict['search_volume'] = self.search_volume.to_dict() if self.search_volume else None
        _dict['ad_traffic_by_keywords'] = self.ad_traffic_by_keywords.to_dict() if self.ad_traffic_by_keywords else None
        _dict['languages'] = self.languages
        _dict['locations'] = self.locations
        _dict['tasks_ready'] = self.tasks_ready
        _dict['explore'] = self.explore.to_dict() if self.explore else None
        _dict['categories'] = self.categories
        _dict['errors'] = self.errors
        _dict['bing'] = self.bing.to_dict() if self.bing else None
        _dict['keyword_performance'] = self.keyword_performance.to_dict() if self.keyword_performance else None
        _dict['locations_and_languages'] = self.locations_and_languages
        _dict['google_ads'] = self.google_ads.to_dict() if self.google_ads else None
        _dict['dataforseo_trends'] = self.dataforseo_trends.to_dict() if self.dataforseo_trends else None
        _dict['clickstream_data'] = self.clickstream_data.to_dict() if self.clickstream_data else None
        _dict['audience_estimation'] = self.audience_estimation.to_dict() if self.audience_estimation else None
        _dict['keyword_suggestions_for_url'] = self.keyword_suggestions_for_url.to_dict() if self.keyword_suggestions_for_url else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keywords_for_keywords": AppendixInfo.from_dict(obj["keywords_for_keywords"]) if obj.get("keywords_for_keywords") is not None else None,
            "keywords_for_site": AppendixInfo.from_dict(obj["keywords_for_site"]) if obj.get("keywords_for_site") is not None else None,
            "search_volume": AppendixInfo.from_dict(obj["search_volume"]) if obj.get("search_volume") is not None else None,
            "ad_traffic_by_keywords": AppendixInfo.from_dict(obj["ad_traffic_by_keywords"]) if obj.get("ad_traffic_by_keywords") is not None else None,
            "languages": obj.get("languages"),
            "locations": obj.get("locations"),
            "tasks_ready": obj.get("tasks_ready"),
            "explore": AppendixInfo.from_dict(obj["explore"]) if obj.get("explore") is not None else None,
            "categories": obj.get("categories"),
            "errors": obj.get("errors"),
            "bing": AppendixBingKeywordsDataLimitsRatesDataInfo.from_dict(obj["bing"]) if obj.get("bing") is not None else None,
            "keyword_performance": AppendixInfo.from_dict(obj["keyword_performance"]) if obj.get("keyword_performance") is not None else None,
            "locations_and_languages": obj.get("locations_and_languages"),
            "google_ads": AppendixGoogleAdsKeywordsDataLimitsRatesDataInfo.from_dict(obj["google_ads"]) if obj.get("google_ads") is not None else None,
            "dataforseo_trends": AppendixDataforseoTrendsKeywordsDataLimitsRatesDataInfo.from_dict(obj["dataforseo_trends"]) if obj.get("dataforseo_trends") is not None else None,
            "clickstream_data": AppendixClickstreamDataKeywordsDataLimitsRatesDataInfo.from_dict(obj["clickstream_data"]) if obj.get("clickstream_data") is not None else None,
            "audience_estimation": AppendixInfo.from_dict(obj["audience_estimation"]) if obj.get("audience_estimation") is not None else None,
            "keyword_suggestions_for_url": AppendixInfo.from_dict(obj["keyword_suggestions_for_url"]) if obj.get("keyword_suggestions_for_url") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj