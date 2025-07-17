from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo
from dataforseo_client.models.appendix_a_keywords_data_price_data_info import AppendixAKeywordsDataPriceDataInfo
from dataforseo_client.models.appendix_bing_keywords_data_price_data import AppendixBingKeywordsDataPriceData
from dataforseo_client.models.appendix_clickstream_data_keywords_data_price_data import AppendixClickstreamDataKeywordsDataPriceData
from dataforseo_client.models.appendix_google_ads_keywords_data_price_data import AppendixGoogleAdsKeywordsDataPriceData
from dataforseo_client.models.appendix_dataforseo_trends_keywords_data_price_data import AppendixDataforseoTrendsKeywordsDataPriceData
from dataforseo_client.models.appendix_explore_keywords_data_price_data import AppendixExploreKeywordsDataPriceData



class AppendixKeywordsDataPriceData(BaseModel):
    """
    AppendixKeywordsDataPriceData
    """ # noqa: E501
    tasks_ready: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    ad_traffic_by_keywords: Optional[AppendixAKeywordsDataPriceDataInfo] = Field(default=None, description="")
    audience_estimation: Optional[AppendixAKeywordsDataPriceDataInfo] = Field(default=None, description="")
    bing: Optional[AppendixBingKeywordsDataPriceData] = Field(default=None, description="")
    categories: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    clickstream_data: Optional[AppendixClickstreamDataKeywordsDataPriceData] = Field(default=None, description="")
    errors: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    google_ads: Optional[AppendixGoogleAdsKeywordsDataPriceData] = Field(default=None, description="")
    keyword_performance: Optional[AppendixAKeywordsDataPriceDataInfo] = Field(default=None, description="")
    keywords_for_keywords: Optional[AppendixAKeywordsDataPriceDataInfo] = Field(default=None, description="")
    keywords_for_site: Optional[AppendixAKeywordsDataPriceDataInfo] = Field(default=None, description="")
    keyword_suggestions_for_url: Optional[AppendixAKeywordsDataPriceDataInfo] = Field(default=None, description="")
    languages: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    locations: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    locations_and_languages: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    search_volume: Optional[AppendixAKeywordsDataPriceDataInfo] = Field(default=None, description="")
    dataforseo_trends: Optional[AppendixDataforseoTrendsKeywordsDataPriceData] = Field(default=None, description="")
    explore: Optional[AppendixExploreKeywordsDataPriceData] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "tasks_ready", 
        "ad_traffic_by_keywords", 
        "audience_estimation", 
        "bing", 
        "categories", 
        "clickstream_data", 
        "errors", 
        "google_ads", 
        "keyword_performance", 
        "keywords_for_keywords", 
        "keywords_for_site", 
        "keyword_suggestions_for_url", 
        "languages", 
        "locations", 
        "locations_and_languages", 
        "search_volume", 
        "dataforseo_trends", 
        "explore", 
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

        _dict['tasks_ready'] = self.tasks_ready.to_dict() if self.tasks_ready else None
        _dict['ad_traffic_by_keywords'] = self.ad_traffic_by_keywords.to_dict() if self.ad_traffic_by_keywords else None
        _dict['audience_estimation'] = self.audience_estimation.to_dict() if self.audience_estimation else None
        _dict['bing'] = self.bing.to_dict() if self.bing else None
        _dict['categories'] = self.categories.to_dict() if self.categories else None
        _dict['clickstream_data'] = self.clickstream_data.to_dict() if self.clickstream_data else None
        _dict['errors'] = self.errors.to_dict() if self.errors else None
        _dict['google_ads'] = self.google_ads.to_dict() if self.google_ads else None
        _dict['keyword_performance'] = self.keyword_performance.to_dict() if self.keyword_performance else None
        _dict['keywords_for_keywords'] = self.keywords_for_keywords.to_dict() if self.keywords_for_keywords else None
        _dict['keywords_for_site'] = self.keywords_for_site.to_dict() if self.keywords_for_site else None
        _dict['keyword_suggestions_for_url'] = self.keyword_suggestions_for_url.to_dict() if self.keyword_suggestions_for_url else None
        _dict['languages'] = self.languages.to_dict() if self.languages else None
        _dict['locations'] = self.locations.to_dict() if self.locations else None
        _dict['locations_and_languages'] = self.locations_and_languages.to_dict() if self.locations_and_languages else None
        _dict['search_volume'] = self.search_volume.to_dict() if self.search_volume else None
        _dict['dataforseo_trends'] = self.dataforseo_trends.to_dict() if self.dataforseo_trends else None
        _dict['explore'] = self.explore.to_dict() if self.explore else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tasks_ready": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["tasks_ready"]) if obj.get("tasks_ready") is not None else None,
            "ad_traffic_by_keywords": AppendixAKeywordsDataPriceDataInfo.from_dict(obj["ad_traffic_by_keywords"]) if obj.get("ad_traffic_by_keywords") is not None else None,
            "audience_estimation": AppendixAKeywordsDataPriceDataInfo.from_dict(obj["audience_estimation"]) if obj.get("audience_estimation") is not None else None,
            "bing": AppendixBingKeywordsDataPriceData.from_dict(obj["bing"]) if obj.get("bing") is not None else None,
            "categories": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["categories"]) if obj.get("categories") is not None else None,
            "clickstream_data": AppendixClickstreamDataKeywordsDataPriceData.from_dict(obj["clickstream_data"]) if obj.get("clickstream_data") is not None else None,
            "errors": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["errors"]) if obj.get("errors") is not None else None,
            "google_ads": AppendixGoogleAdsKeywordsDataPriceData.from_dict(obj["google_ads"]) if obj.get("google_ads") is not None else None,
            "keyword_performance": AppendixAKeywordsDataPriceDataInfo.from_dict(obj["keyword_performance"]) if obj.get("keyword_performance") is not None else None,
            "keywords_for_keywords": AppendixAKeywordsDataPriceDataInfo.from_dict(obj["keywords_for_keywords"]) if obj.get("keywords_for_keywords") is not None else None,
            "keywords_for_site": AppendixAKeywordsDataPriceDataInfo.from_dict(obj["keywords_for_site"]) if obj.get("keywords_for_site") is not None else None,
            "keyword_suggestions_for_url": AppendixAKeywordsDataPriceDataInfo.from_dict(obj["keyword_suggestions_for_url"]) if obj.get("keyword_suggestions_for_url") is not None else None,
            "languages": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["languages"]) if obj.get("languages") is not None else None,
            "locations": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["locations"]) if obj.get("locations") is not None else None,
            "locations_and_languages": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["locations_and_languages"]) if obj.get("locations_and_languages") is not None else None,
            "search_volume": AppendixAKeywordsDataPriceDataInfo.from_dict(obj["search_volume"]) if obj.get("search_volume") is not None else None,
            "dataforseo_trends": AppendixDataforseoTrendsKeywordsDataPriceData.from_dict(obj["dataforseo_trends"]) if obj.get("dataforseo_trends") is not None else None,
            "explore": AppendixExploreKeywordsDataPriceData.from_dict(obj["explore"]) if obj.get("explore") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj