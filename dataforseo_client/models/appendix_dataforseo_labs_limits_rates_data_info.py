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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.appendix_info import AppendixInfo
from typing import Optional, Set
from typing_extensions import Self

class AppendixDataforseoLabsLimitsRatesDataInfo(BaseModel):
    """
    AppendixDataforseoLabsLimitsRatesDataInfo
    """ # noqa: E501
    locations_and_languages: Optional[Union[StrictFloat, StrictInt]] = None
    categories: Optional[Union[StrictFloat, StrictInt]] = None
    errors: Optional[Union[StrictFloat, StrictInt]] = None
    product_competitors: Optional[AppendixInfo] = None
    product_keyword_intersections: Optional[AppendixInfo] = None
    product_rank_overview: Optional[AppendixInfo] = None
    ranked_keywords: Optional[AppendixInfo] = None
    serp_competitors: Optional[AppendixInfo] = None
    subdomains: Optional[AppendixInfo] = None
    relevant_pages: Optional[AppendixInfo] = None
    competitors_domain: Optional[AppendixInfo] = None
    related_keywords: Optional[AppendixInfo] = None
    domain_rank_overview: Optional[AppendixInfo] = None
    domain_intersection: Optional[AppendixInfo] = None
    page_intersection: Optional[AppendixInfo] = None
    bulk_traffic_estimation: Optional[AppendixInfo] = None
    bulk_keyword_difficulty: Optional[AppendixInfo] = None
    bulk_search_volume: Optional[AppendixInfo] = None
    keywords_for_site: Optional[AppendixInfo] = None
    keyword_suggestions: Optional[AppendixInfo] = None
    keyword_ideas: Optional[AppendixInfo] = None
    categories_for_domain: Optional[AppendixInfo] = None
    domain_metrics_by_categories: Optional[AppendixInfo] = None
    top_searches: Optional[AppendixInfo] = None
    domain_whois_overview: Optional[AppendixInfo] = None
    historical_rank_overview: Optional[AppendixInfo] = None
    keywords_for_categories: Optional[AppendixInfo] = None
    historical_serps: Optional[AppendixInfo] = None
    app_competitors: Optional[AppendixInfo] = None
    keywords_for_app: Optional[AppendixInfo] = None
    app_intersection: Optional[AppendixInfo] = None
    bulk_app_metrics: Optional[AppendixInfo] = None
    search_intent: Optional[AppendixInfo] = None
    historical_bulk_traffic_estimation: Optional[AppendixInfo] = None
    categories_for_keywords: Optional[AppendixInfo] = None
    keyword_overview: Optional[AppendixInfo] = None
    historical_keyword_data: Optional[AppendixInfo] = None
    __properties: ClassVar[List[str]] = ["locations_and_languages", "categories", "errors", "product_competitors", "product_keyword_intersections", "product_rank_overview", "ranked_keywords", "serp_competitors", "subdomains", "relevant_pages", "competitors_domain", "related_keywords", "domain_rank_overview", "domain_intersection", "page_intersection", "bulk_traffic_estimation", "bulk_keyword_difficulty", "bulk_search_volume", "keywords_for_site", "keyword_suggestions", "keyword_ideas", "categories_for_domain", "domain_metrics_by_categories", "top_searches", "domain_whois_overview", "historical_rank_overview", "keywords_for_categories", "historical_serps", "app_competitors", "keywords_for_app", "app_intersection", "bulk_app_metrics", "search_intent", "historical_bulk_traffic_estimation", "categories_for_keywords", "keyword_overview", "historical_keyword_data"]

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
        """Create an instance of AppendixDataforseoLabsLimitsRatesDataInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of serp_competitors
        if self.serp_competitors:
            _dict['serp_competitors'] = self.serp_competitors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of subdomains
        if self.subdomains:
            _dict['subdomains'] = self.subdomains.to_dict()
        # override the default output from pydantic by calling `to_dict()` of relevant_pages
        if self.relevant_pages:
            _dict['relevant_pages'] = self.relevant_pages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of competitors_domain
        if self.competitors_domain:
            _dict['competitors_domain'] = self.competitors_domain.to_dict()
        # override the default output from pydantic by calling `to_dict()` of related_keywords
        if self.related_keywords:
            _dict['related_keywords'] = self.related_keywords.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_rank_overview
        if self.domain_rank_overview:
            _dict['domain_rank_overview'] = self.domain_rank_overview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_intersection
        if self.domain_intersection:
            _dict['domain_intersection'] = self.domain_intersection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of page_intersection
        if self.page_intersection:
            _dict['page_intersection'] = self.page_intersection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_traffic_estimation
        if self.bulk_traffic_estimation:
            _dict['bulk_traffic_estimation'] = self.bulk_traffic_estimation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_keyword_difficulty
        if self.bulk_keyword_difficulty:
            _dict['bulk_keyword_difficulty'] = self.bulk_keyword_difficulty.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_search_volume
        if self.bulk_search_volume:
            _dict['bulk_search_volume'] = self.bulk_search_volume.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keywords_for_site
        if self.keywords_for_site:
            _dict['keywords_for_site'] = self.keywords_for_site.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keyword_suggestions
        if self.keyword_suggestions:
            _dict['keyword_suggestions'] = self.keyword_suggestions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keyword_ideas
        if self.keyword_ideas:
            _dict['keyword_ideas'] = self.keyword_ideas.to_dict()
        # override the default output from pydantic by calling `to_dict()` of categories_for_domain
        if self.categories_for_domain:
            _dict['categories_for_domain'] = self.categories_for_domain.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_metrics_by_categories
        if self.domain_metrics_by_categories:
            _dict['domain_metrics_by_categories'] = self.domain_metrics_by_categories.to_dict()
        # override the default output from pydantic by calling `to_dict()` of top_searches
        if self.top_searches:
            _dict['top_searches'] = self.top_searches.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_whois_overview
        if self.domain_whois_overview:
            _dict['domain_whois_overview'] = self.domain_whois_overview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of historical_rank_overview
        if self.historical_rank_overview:
            _dict['historical_rank_overview'] = self.historical_rank_overview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keywords_for_categories
        if self.keywords_for_categories:
            _dict['keywords_for_categories'] = self.keywords_for_categories.to_dict()
        # override the default output from pydantic by calling `to_dict()` of historical_serps
        if self.historical_serps:
            _dict['historical_serps'] = self.historical_serps.to_dict()
        # override the default output from pydantic by calling `to_dict()` of app_competitors
        if self.app_competitors:
            _dict['app_competitors'] = self.app_competitors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keywords_for_app
        if self.keywords_for_app:
            _dict['keywords_for_app'] = self.keywords_for_app.to_dict()
        # override the default output from pydantic by calling `to_dict()` of app_intersection
        if self.app_intersection:
            _dict['app_intersection'] = self.app_intersection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_app_metrics
        if self.bulk_app_metrics:
            _dict['bulk_app_metrics'] = self.bulk_app_metrics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of search_intent
        if self.search_intent:
            _dict['search_intent'] = self.search_intent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of historical_bulk_traffic_estimation
        if self.historical_bulk_traffic_estimation:
            _dict['historical_bulk_traffic_estimation'] = self.historical_bulk_traffic_estimation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of categories_for_keywords
        if self.categories_for_keywords:
            _dict['categories_for_keywords'] = self.categories_for_keywords.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keyword_overview
        if self.keyword_overview:
            _dict['keyword_overview'] = self.keyword_overview.to_dict()
        # override the default output from pydantic by calling `to_dict()` of historical_keyword_data
        if self.historical_keyword_data:
            _dict['historical_keyword_data'] = self.historical_keyword_data.to_dict()
        # set to None if locations_and_languages (nullable) is None
        # and model_fields_set contains the field
        if self.locations_and_languages is None and "locations_and_languages" in self.model_fields_set:
            _dict['locations_and_languages'] = None

        # set to None if categories (nullable) is None
        # and model_fields_set contains the field
        if self.categories is None and "categories" in self.model_fields_set:
            _dict['categories'] = None

        # set to None if errors (nullable) is None
        # and model_fields_set contains the field
        if self.errors is None and "errors" in self.model_fields_set:
            _dict['errors'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppendixDataforseoLabsLimitsRatesDataInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "locations_and_languages": obj.get("locations_and_languages"),
            "categories": obj.get("categories"),
            "errors": obj.get("errors"),
            "product_competitors": AppendixInfo.from_dict(obj["product_competitors"]) if obj.get("product_competitors") is not None else None,
            "product_keyword_intersections": AppendixInfo.from_dict(obj["product_keyword_intersections"]) if obj.get("product_keyword_intersections") is not None else None,
            "product_rank_overview": AppendixInfo.from_dict(obj["product_rank_overview"]) if obj.get("product_rank_overview") is not None else None,
            "ranked_keywords": AppendixInfo.from_dict(obj["ranked_keywords"]) if obj.get("ranked_keywords") is not None else None,
            "serp_competitors": AppendixInfo.from_dict(obj["serp_competitors"]) if obj.get("serp_competitors") is not None else None,
            "subdomains": AppendixInfo.from_dict(obj["subdomains"]) if obj.get("subdomains") is not None else None,
            "relevant_pages": AppendixInfo.from_dict(obj["relevant_pages"]) if obj.get("relevant_pages") is not None else None,
            "competitors_domain": AppendixInfo.from_dict(obj["competitors_domain"]) if obj.get("competitors_domain") is not None else None,
            "related_keywords": AppendixInfo.from_dict(obj["related_keywords"]) if obj.get("related_keywords") is not None else None,
            "domain_rank_overview": AppendixInfo.from_dict(obj["domain_rank_overview"]) if obj.get("domain_rank_overview") is not None else None,
            "domain_intersection": AppendixInfo.from_dict(obj["domain_intersection"]) if obj.get("domain_intersection") is not None else None,
            "page_intersection": AppendixInfo.from_dict(obj["page_intersection"]) if obj.get("page_intersection") is not None else None,
            "bulk_traffic_estimation": AppendixInfo.from_dict(obj["bulk_traffic_estimation"]) if obj.get("bulk_traffic_estimation") is not None else None,
            "bulk_keyword_difficulty": AppendixInfo.from_dict(obj["bulk_keyword_difficulty"]) if obj.get("bulk_keyword_difficulty") is not None else None,
            "bulk_search_volume": AppendixInfo.from_dict(obj["bulk_search_volume"]) if obj.get("bulk_search_volume") is not None else None,
            "keywords_for_site": AppendixInfo.from_dict(obj["keywords_for_site"]) if obj.get("keywords_for_site") is not None else None,
            "keyword_suggestions": AppendixInfo.from_dict(obj["keyword_suggestions"]) if obj.get("keyword_suggestions") is not None else None,
            "keyword_ideas": AppendixInfo.from_dict(obj["keyword_ideas"]) if obj.get("keyword_ideas") is not None else None,
            "categories_for_domain": AppendixInfo.from_dict(obj["categories_for_domain"]) if obj.get("categories_for_domain") is not None else None,
            "domain_metrics_by_categories": AppendixInfo.from_dict(obj["domain_metrics_by_categories"]) if obj.get("domain_metrics_by_categories") is not None else None,
            "top_searches": AppendixInfo.from_dict(obj["top_searches"]) if obj.get("top_searches") is not None else None,
            "domain_whois_overview": AppendixInfo.from_dict(obj["domain_whois_overview"]) if obj.get("domain_whois_overview") is not None else None,
            "historical_rank_overview": AppendixInfo.from_dict(obj["historical_rank_overview"]) if obj.get("historical_rank_overview") is not None else None,
            "keywords_for_categories": AppendixInfo.from_dict(obj["keywords_for_categories"]) if obj.get("keywords_for_categories") is not None else None,
            "historical_serps": AppendixInfo.from_dict(obj["historical_serps"]) if obj.get("historical_serps") is not None else None,
            "app_competitors": AppendixInfo.from_dict(obj["app_competitors"]) if obj.get("app_competitors") is not None else None,
            "keywords_for_app": AppendixInfo.from_dict(obj["keywords_for_app"]) if obj.get("keywords_for_app") is not None else None,
            "app_intersection": AppendixInfo.from_dict(obj["app_intersection"]) if obj.get("app_intersection") is not None else None,
            "bulk_app_metrics": AppendixInfo.from_dict(obj["bulk_app_metrics"]) if obj.get("bulk_app_metrics") is not None else None,
            "search_intent": AppendixInfo.from_dict(obj["search_intent"]) if obj.get("search_intent") is not None else None,
            "historical_bulk_traffic_estimation": AppendixInfo.from_dict(obj["historical_bulk_traffic_estimation"]) if obj.get("historical_bulk_traffic_estimation") is not None else None,
            "categories_for_keywords": AppendixInfo.from_dict(obj["categories_for_keywords"]) if obj.get("categories_for_keywords") is not None else None,
            "keyword_overview": AppendixInfo.from_dict(obj["keyword_overview"]) if obj.get("keyword_overview") is not None else None,
            "historical_keyword_data": AppendixInfo.from_dict(obj["historical_keyword_data"]) if obj.get("historical_keyword_data") is not None else None
        })
        return _obj


