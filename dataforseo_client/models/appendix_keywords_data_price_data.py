# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.appendix_bing_keywords_data_price_data import AppendixBingKeywordsDataPriceData
from dataforseo_client.models.appendix_clickstream_data_keywords_data_price_data import AppendixClickstreamDataKeywordsDataPriceData
from dataforseo_client.models.appendix_dataforseo_trends_keywords_data_price_data import AppendixDataforseoTrendsKeywordsDataPriceData
from dataforseo_client.models.appendix_explore_keywords_data_price_data import AppendixExploreKeywordsDataPriceData
from dataforseo_client.models.appendix_google_ads_keywords_data_price_data import AppendixGoogleAdsKeywordsDataPriceData
from dataforseo_client.models.appendix_keywords_data_price_data_info import AppendixKeywordsDataPriceDataInfo
from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo
from typing import Optional, Set
from typing_extensions import Self

class AppendixKeywordsDataPriceData(BaseModel):
    """
    AppendixKeywordsDataPriceData
    """ # noqa: E501
    tasks_ready: Optional[AppendixTaskKeywordsDataPriceDataInfo] = None
    ad_traffic_by_keywords: Optional[AppendixKeywordsDataPriceDataInfo] = None
    bing: Optional[AppendixBingKeywordsDataPriceData] = None
    categories: Optional[AppendixTaskKeywordsDataPriceDataInfo] = None
    clickstream_data: Optional[AppendixClickstreamDataKeywordsDataPriceData] = None
    errors: Optional[AppendixTaskKeywordsDataPriceDataInfo] = None
    google_ads: Optional[AppendixGoogleAdsKeywordsDataPriceData] = None
    keyword_performance: Optional[AppendixKeywordsDataPriceDataInfo] = None
    keywords_for_keywords: Optional[AppendixKeywordsDataPriceDataInfo] = None
    keywords_for_site: Optional[AppendixKeywordsDataPriceDataInfo] = None
    languages: Optional[AppendixTaskKeywordsDataPriceDataInfo] = None
    locations: Optional[AppendixTaskKeywordsDataPriceDataInfo] = None
    locations_and_languages: Optional[AppendixTaskKeywordsDataPriceDataInfo] = None
    search_volume: Optional[AppendixKeywordsDataPriceDataInfo] = None
    dataforseo_trends: Optional[AppendixDataforseoTrendsKeywordsDataPriceData] = None
    explore: Optional[AppendixExploreKeywordsDataPriceData] = None
    __properties: ClassVar[List[str]] = ["tasks_ready", "ad_traffic_by_keywords", "bing", "categories", "clickstream_data", "errors", "google_ads", "keyword_performance", "keywords_for_keywords", "keywords_for_site", "languages", "locations", "locations_and_languages", "search_volume", "dataforseo_trends", "explore"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AppendixKeywordsDataPriceData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of tasks_ready
        if self.tasks_ready:
            _dict['tasks_ready'] = self.tasks_ready.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ad_traffic_by_keywords
        if self.ad_traffic_by_keywords:
            _dict['ad_traffic_by_keywords'] = self.ad_traffic_by_keywords.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bing
        if self.bing:
            _dict['bing'] = self.bing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of categories
        if self.categories:
            _dict['categories'] = self.categories.to_dict()
        # override the default output from pydantic by calling `to_dict()` of clickstream_data
        if self.clickstream_data:
            _dict['clickstream_data'] = self.clickstream_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of errors
        if self.errors:
            _dict['errors'] = self.errors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of google_ads
        if self.google_ads:
            _dict['google_ads'] = self.google_ads.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keyword_performance
        if self.keyword_performance:
            _dict['keyword_performance'] = self.keyword_performance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keywords_for_keywords
        if self.keywords_for_keywords:
            _dict['keywords_for_keywords'] = self.keywords_for_keywords.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keywords_for_site
        if self.keywords_for_site:
            _dict['keywords_for_site'] = self.keywords_for_site.to_dict()
        # override the default output from pydantic by calling `to_dict()` of languages
        if self.languages:
            _dict['languages'] = self.languages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of locations
        if self.locations:
            _dict['locations'] = self.locations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of locations_and_languages
        if self.locations_and_languages:
            _dict['locations_and_languages'] = self.locations_and_languages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of search_volume
        if self.search_volume:
            _dict['search_volume'] = self.search_volume.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dataforseo_trends
        if self.dataforseo_trends:
            _dict['dataforseo_trends'] = self.dataforseo_trends.to_dict()
        # override the default output from pydantic by calling `to_dict()` of explore
        if self.explore:
            _dict['explore'] = self.explore.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppendixKeywordsDataPriceData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tasks_ready": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["tasks_ready"]) if obj.get("tasks_ready") is not None else None,
            "ad_traffic_by_keywords": AppendixKeywordsDataPriceDataInfo.from_dict(obj["ad_traffic_by_keywords"]) if obj.get("ad_traffic_by_keywords") is not None else None,
            "bing": AppendixBingKeywordsDataPriceData.from_dict(obj["bing"]) if obj.get("bing") is not None else None,
            "categories": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["categories"]) if obj.get("categories") is not None else None,
            "clickstream_data": AppendixClickstreamDataKeywordsDataPriceData.from_dict(obj["clickstream_data"]) if obj.get("clickstream_data") is not None else None,
            "errors": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["errors"]) if obj.get("errors") is not None else None,
            "google_ads": AppendixGoogleAdsKeywordsDataPriceData.from_dict(obj["google_ads"]) if obj.get("google_ads") is not None else None,
            "keyword_performance": AppendixKeywordsDataPriceDataInfo.from_dict(obj["keyword_performance"]) if obj.get("keyword_performance") is not None else None,
            "keywords_for_keywords": AppendixKeywordsDataPriceDataInfo.from_dict(obj["keywords_for_keywords"]) if obj.get("keywords_for_keywords") is not None else None,
            "keywords_for_site": AppendixKeywordsDataPriceDataInfo.from_dict(obj["keywords_for_site"]) if obj.get("keywords_for_site") is not None else None,
            "languages": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["languages"]) if obj.get("languages") is not None else None,
            "locations": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["locations"]) if obj.get("locations") is not None else None,
            "locations_and_languages": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["locations_and_languages"]) if obj.get("locations_and_languages") is not None else None,
            "search_volume": AppendixKeywordsDataPriceDataInfo.from_dict(obj["search_volume"]) if obj.get("search_volume") is not None else None,
            "dataforseo_trends": AppendixDataforseoTrendsKeywordsDataPriceData.from_dict(obj["dataforseo_trends"]) if obj.get("dataforseo_trends") is not None else None,
            "explore": AppendixExploreKeywordsDataPriceData.from_dict(obj["explore"]) if obj.get("explore") is not None else None
        })
        return _obj


