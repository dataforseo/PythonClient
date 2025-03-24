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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.appendix_bing_keywords_data_price_data_info import AppendixBingKeywordsDataPriceDataInfo
from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo
from typing import Optional, Set
from typing_extensions import Self

class AppendixDataforseoLabsPriceData(BaseModel):
    """
    AppendixDataforseoLabsPriceData
    """ # noqa: E501
    app_competitors: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    app_intersection: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    bulk_app_metrics: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    bulk_keyword_difficulty: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    bulk_search_volume: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    bulk_traffic_estimation: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    categories: Optional[AppendixTaskKeywordsDataPriceDataInfo] = None
    categories_for_domain: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    categories_for_keywords: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    competitors_domain: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    domain_intersection: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    domain_metrics_by_categories: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    domain_rank_overview: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    domain_whois_overview: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    errors: Optional[AppendixTaskKeywordsDataPriceDataInfo] = None
    historical_bulk_traffic_estimation: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    historical_keyword_data: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    historical_rank_overview: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    historical_serps: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    keyword_ideas: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    keyword_overview: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    keywords_for_app: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    keywords_for_categories: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    keywords_for_site: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    keyword_suggestions: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    locations_and_languages: Optional[AppendixTaskKeywordsDataPriceDataInfo] = None
    page_intersection: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    product_competitors: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    product_keyword_intersections: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    product_rank_overview: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    ranked_keywords: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    related_keywords: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    relevant_pages: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    search_intent: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    serp_competitors: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    subdomains: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    top_searches: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    __properties: ClassVar[List[str]] = ["app_competitors", "app_intersection", "bulk_app_metrics", "bulk_keyword_difficulty", "bulk_search_volume", "bulk_traffic_estimation", "categories", "categories_for_domain", "categories_for_keywords", "competitors_domain", "domain_intersection", "domain_metrics_by_categories", "domain_rank_overview", "domain_whois_overview", "errors", "historical_bulk_traffic_estimation", "historical_keyword_data", "historical_rank_overview", "historical_serps", "keyword_ideas", "keyword_overview", "keywords_for_app", "keywords_for_categories", "keywords_for_site", "keyword_suggestions", "locations_and_languages", "page_intersection", "product_competitors", "product_keyword_intersections", "product_rank_overview", "ranked_keywords", "related_keywords", "relevant_pages", "search_intent", "serp_competitors", "subdomains", "top_searches"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AppendixDataforseoLabsPriceData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of app_competitors
        if self.app_competitors:
            _dict['app_competitors'] = self.app_competitors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of app_intersection
        if self.app_intersection:
            _dict['app_intersection'] = self.app_intersection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_app_metrics
        if self.bulk_app_metrics:
            _dict['bulk_app_metrics'] = self.bulk_app_metrics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_keyword_difficulty
        if self.bulk_keyword_difficulty:
            _dict['bulk_keyword_difficulty'] = self.bulk_keyword_difficulty.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_search_volume
        if self.bulk_search_volume:
            _dict['bulk_search_volume'] = self.bulk_search_volume.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_traffic_estimation
        if self.bulk_traffic_estimation:
            _dict['bulk_traffic_estimation'] = self.bulk_traffic_estimation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of categories
        if self.categories:
            _dict['categories'] = self.categories.to_dict()
        # override the default output from pydantic by calling `to_dict()` of categories_for_domain
        if self.categories_for_domain:
            _dict['categories_for_domain'] = self.categories_for_domain.to_dict()
        # override the default output from pydantic by calling `to_dict()` of categories_for_keywords
        if self.categories_for_keywords:
            _dict['categories_for_keywords'] = self.categories_for_keywords.to_dict()
        # override the default output from pydantic by calling `to_dict()` of competitors_domain
        if self.competitors_domain:
            _dict['competitors_domain'] = self.competitors_domain.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_intersection
        if self.domain_intersection:
            _dict['domain_intersection'] = self.domain_intersection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_metrics_by_categories
        if self.domain_metrics_by_categories:
            _dict['domain_metrics_by_categories'] = self.domain_metrics_by_categories.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_rank_overview
        if self.domain_rank_overview:
            _dict['domain_rank_overview'] = self.domain_rank_overview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_whois_overview
        if self.domain_whois_overview:
            _dict['domain_whois_overview'] = self.domain_whois_overview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of errors
        if self.errors:
            _dict['errors'] = self.errors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of historical_bulk_traffic_estimation
        if self.historical_bulk_traffic_estimation:
            _dict['historical_bulk_traffic_estimation'] = self.historical_bulk_traffic_estimation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of historical_keyword_data
        if self.historical_keyword_data:
            _dict['historical_keyword_data'] = self.historical_keyword_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of historical_rank_overview
        if self.historical_rank_overview:
            _dict['historical_rank_overview'] = self.historical_rank_overview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of historical_serps
        if self.historical_serps:
            _dict['historical_serps'] = self.historical_serps.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keyword_ideas
        if self.keyword_ideas:
            _dict['keyword_ideas'] = self.keyword_ideas.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keyword_overview
        if self.keyword_overview:
            _dict['keyword_overview'] = self.keyword_overview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keywords_for_app
        if self.keywords_for_app:
            _dict['keywords_for_app'] = self.keywords_for_app.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keywords_for_categories
        if self.keywords_for_categories:
            _dict['keywords_for_categories'] = self.keywords_for_categories.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keywords_for_site
        if self.keywords_for_site:
            _dict['keywords_for_site'] = self.keywords_for_site.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keyword_suggestions
        if self.keyword_suggestions:
            _dict['keyword_suggestions'] = self.keyword_suggestions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of locations_and_languages
        if self.locations_and_languages:
            _dict['locations_and_languages'] = self.locations_and_languages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of page_intersection
        if self.page_intersection:
            _dict['page_intersection'] = self.page_intersection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product_competitors
        if self.product_competitors:
            _dict['product_competitors'] = self.product_competitors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product_keyword_intersections
        if self.product_keyword_intersections:
            _dict['product_keyword_intersections'] = self.product_keyword_intersections.to_dict()
        # override the default output from pydantic by calling `to_dict()` of product_rank_overview
        if self.product_rank_overview:
            _dict['product_rank_overview'] = self.product_rank_overview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ranked_keywords
        if self.ranked_keywords:
            _dict['ranked_keywords'] = self.ranked_keywords.to_dict()
        # override the default output from pydantic by calling `to_dict()` of related_keywords
        if self.related_keywords:
            _dict['related_keywords'] = self.related_keywords.to_dict()
        # override the default output from pydantic by calling `to_dict()` of relevant_pages
        if self.relevant_pages:
            _dict['relevant_pages'] = self.relevant_pages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of search_intent
        if self.search_intent:
            _dict['search_intent'] = self.search_intent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of serp_competitors
        if self.serp_competitors:
            _dict['serp_competitors'] = self.serp_competitors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subdomains
        if self.subdomains:
            _dict['subdomains'] = self.subdomains.to_dict()
        # override the default output from pydantic by calling `to_dict()` of top_searches
        if self.top_searches:
            _dict['top_searches'] = self.top_searches.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppendixDataforseoLabsPriceData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app_competitors": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["app_competitors"]) if obj.get("app_competitors") is not None else None,
            "app_intersection": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["app_intersection"]) if obj.get("app_intersection") is not None else None,
            "bulk_app_metrics": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["bulk_app_metrics"]) if obj.get("bulk_app_metrics") is not None else None,
            "bulk_keyword_difficulty": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["bulk_keyword_difficulty"]) if obj.get("bulk_keyword_difficulty") is not None else None,
            "bulk_search_volume": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["bulk_search_volume"]) if obj.get("bulk_search_volume") is not None else None,
            "bulk_traffic_estimation": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["bulk_traffic_estimation"]) if obj.get("bulk_traffic_estimation") is not None else None,
            "categories": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["categories"]) if obj.get("categories") is not None else None,
            "categories_for_domain": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["categories_for_domain"]) if obj.get("categories_for_domain") is not None else None,
            "categories_for_keywords": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["categories_for_keywords"]) if obj.get("categories_for_keywords") is not None else None,
            "competitors_domain": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["competitors_domain"]) if obj.get("competitors_domain") is not None else None,
            "domain_intersection": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["domain_intersection"]) if obj.get("domain_intersection") is not None else None,
            "domain_metrics_by_categories": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["domain_metrics_by_categories"]) if obj.get("domain_metrics_by_categories") is not None else None,
            "domain_rank_overview": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["domain_rank_overview"]) if obj.get("domain_rank_overview") is not None else None,
            "domain_whois_overview": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["domain_whois_overview"]) if obj.get("domain_whois_overview") is not None else None,
            "errors": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["errors"]) if obj.get("errors") is not None else None,
            "historical_bulk_traffic_estimation": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["historical_bulk_traffic_estimation"]) if obj.get("historical_bulk_traffic_estimation") is not None else None,
            "historical_keyword_data": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["historical_keyword_data"]) if obj.get("historical_keyword_data") is not None else None,
            "historical_rank_overview": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["historical_rank_overview"]) if obj.get("historical_rank_overview") is not None else None,
            "historical_serps": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["historical_serps"]) if obj.get("historical_serps") is not None else None,
            "keyword_ideas": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["keyword_ideas"]) if obj.get("keyword_ideas") is not None else None,
            "keyword_overview": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["keyword_overview"]) if obj.get("keyword_overview") is not None else None,
            "keywords_for_app": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["keywords_for_app"]) if obj.get("keywords_for_app") is not None else None,
            "keywords_for_categories": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["keywords_for_categories"]) if obj.get("keywords_for_categories") is not None else None,
            "keywords_for_site": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["keywords_for_site"]) if obj.get("keywords_for_site") is not None else None,
            "keyword_suggestions": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["keyword_suggestions"]) if obj.get("keyword_suggestions") is not None else None,
            "locations_and_languages": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["locations_and_languages"]) if obj.get("locations_and_languages") is not None else None,
            "page_intersection": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["page_intersection"]) if obj.get("page_intersection") is not None else None,
            "product_competitors": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["product_competitors"]) if obj.get("product_competitors") is not None else None,
            "product_keyword_intersections": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["product_keyword_intersections"]) if obj.get("product_keyword_intersections") is not None else None,
            "product_rank_overview": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["product_rank_overview"]) if obj.get("product_rank_overview") is not None else None,
            "ranked_keywords": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["ranked_keywords"]) if obj.get("ranked_keywords") is not None else None,
            "related_keywords": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["related_keywords"]) if obj.get("related_keywords") is not None else None,
            "relevant_pages": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["relevant_pages"]) if obj.get("relevant_pages") is not None else None,
            "search_intent": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["search_intent"]) if obj.get("search_intent") is not None else None,
            "serp_competitors": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["serp_competitors"]) if obj.get("serp_competitors") is not None else None,
            "subdomains": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["subdomains"]) if obj.get("subdomains") is not None else None,
            "top_searches": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["top_searches"]) if obj.get("top_searches") is not None else None
        })
        return _obj


