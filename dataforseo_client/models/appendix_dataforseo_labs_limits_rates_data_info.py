from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_info import AppendixInfo



class AppendixDataforseoLabsLimitsRatesDataInfo(BaseModel):
    """
    AppendixDataforseoLabsLimitsRatesDataInfo
    """ # noqa: E501
    locations_and_languages: Optional[StrictFloat] = Field(default=None, description="")
    categories: Optional[StrictFloat] = Field(default=None, description="")
    errors: Optional[StrictFloat] = Field(default=None, description="")
    product_competitors: Optional[AppendixInfo] = Field(default=None, description="")
    product_keyword_intersections: Optional[AppendixInfo] = Field(default=None, description="")
    product_rank_overview: Optional[AppendixInfo] = Field(default=None, description="")
    ranked_keywords: Optional[AppendixInfo] = Field(default=None, description="")
    serp_competitors: Optional[AppendixInfo] = Field(default=None, description="")
    subdomains: Optional[AppendixInfo] = Field(default=None, description="")
    relevant_pages: Optional[AppendixInfo] = Field(default=None, description="")
    competitors_domain: Optional[AppendixInfo] = Field(default=None, description="")
    related_keywords: Optional[AppendixInfo] = Field(default=None, description="")
    domain_rank_overview: Optional[AppendixInfo] = Field(default=None, description="")
    domain_intersection: Optional[AppendixInfo] = Field(default=None, description="")
    page_intersection: Optional[AppendixInfo] = Field(default=None, description="")
    bulk_traffic_estimation: Optional[AppendixInfo] = Field(default=None, description="")
    bulk_keyword_difficulty: Optional[AppendixInfo] = Field(default=None, description="")
    bulk_search_volume: Optional[AppendixInfo] = Field(default=None, description="")
    keywords_for_site: Optional[AppendixInfo] = Field(default=None, description="")
    keyword_suggestions: Optional[AppendixInfo] = Field(default=None, description="")
    keyword_ideas: Optional[AppendixInfo] = Field(default=None, description="")
    historical_search_volume: Optional[AppendixInfo] = Field(default=None, description="")
    categories_for_domain: Optional[AppendixInfo] = Field(default=None, description="")
    domain_metrics_by_categories: Optional[AppendixInfo] = Field(default=None, description="")
    top_searches: Optional[AppendixInfo] = Field(default=None, description="")
    domain_whois_overview: Optional[AppendixInfo] = Field(default=None, description="")
    historical_rank_overview: Optional[AppendixInfo] = Field(default=None, description="")
    keywords_for_categories: Optional[AppendixInfo] = Field(default=None, description="")
    historical_serps: Optional[AppendixInfo] = Field(default=None, description="")
    app_competitors: Optional[AppendixInfo] = Field(default=None, description="")
    keywords_for_app: Optional[AppendixInfo] = Field(default=None, description="")
    app_intersection: Optional[AppendixInfo] = Field(default=None, description="")
    bulk_app_metrics: Optional[AppendixInfo] = Field(default=None, description="")
    search_intent: Optional[AppendixInfo] = Field(default=None, description="")
    historical_bulk_traffic_estimation: Optional[AppendixInfo] = Field(default=None, description="")
    categories_for_keywords: Optional[AppendixInfo] = Field(default=None, description="")
    keyword_overview: Optional[AppendixInfo] = Field(default=None, description="")
    historical_keyword_data: Optional[AppendixInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "locations_and_languages", 
        "categories", 
        "errors", 
        "product_competitors", 
        "product_keyword_intersections", 
        "product_rank_overview", 
        "ranked_keywords", 
        "serp_competitors", 
        "subdomains", 
        "relevant_pages", 
        "competitors_domain", 
        "related_keywords", 
        "domain_rank_overview", 
        "domain_intersection", 
        "page_intersection", 
        "bulk_traffic_estimation", 
        "bulk_keyword_difficulty", 
        "bulk_search_volume", 
        "keywords_for_site", 
        "keyword_suggestions", 
        "keyword_ideas", 
        "historical_search_volume", 
        "categories_for_domain", 
        "domain_metrics_by_categories", 
        "top_searches", 
        "domain_whois_overview", 
        "historical_rank_overview", 
        "keywords_for_categories", 
        "historical_serps", 
        "app_competitors", 
        "keywords_for_app", 
        "app_intersection", 
        "bulk_app_metrics", 
        "search_intent", 
        "historical_bulk_traffic_estimation", 
        "categories_for_keywords", 
        "keyword_overview", 
        "historical_keyword_data", 
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

        _dict['locations_and_languages'] = self.locations_and_languages
        _dict['categories'] = self.categories
        _dict['errors'] = self.errors
        _dict['product_competitors'] = self.product_competitors.to_dict() if self.product_competitors else None
        _dict['product_keyword_intersections'] = self.product_keyword_intersections.to_dict() if self.product_keyword_intersections else None
        _dict['product_rank_overview'] = self.product_rank_overview.to_dict() if self.product_rank_overview else None
        _dict['ranked_keywords'] = self.ranked_keywords.to_dict() if self.ranked_keywords else None
        _dict['serp_competitors'] = self.serp_competitors.to_dict() if self.serp_competitors else None
        _dict['subdomains'] = self.subdomains.to_dict() if self.subdomains else None
        _dict['relevant_pages'] = self.relevant_pages.to_dict() if self.relevant_pages else None
        _dict['competitors_domain'] = self.competitors_domain.to_dict() if self.competitors_domain else None
        _dict['related_keywords'] = self.related_keywords.to_dict() if self.related_keywords else None
        _dict['domain_rank_overview'] = self.domain_rank_overview.to_dict() if self.domain_rank_overview else None
        _dict['domain_intersection'] = self.domain_intersection.to_dict() if self.domain_intersection else None
        _dict['page_intersection'] = self.page_intersection.to_dict() if self.page_intersection else None
        _dict['bulk_traffic_estimation'] = self.bulk_traffic_estimation.to_dict() if self.bulk_traffic_estimation else None
        _dict['bulk_keyword_difficulty'] = self.bulk_keyword_difficulty.to_dict() if self.bulk_keyword_difficulty else None
        _dict['bulk_search_volume'] = self.bulk_search_volume.to_dict() if self.bulk_search_volume else None
        _dict['keywords_for_site'] = self.keywords_for_site.to_dict() if self.keywords_for_site else None
        _dict['keyword_suggestions'] = self.keyword_suggestions.to_dict() if self.keyword_suggestions else None
        _dict['keyword_ideas'] = self.keyword_ideas.to_dict() if self.keyword_ideas else None
        _dict['historical_search_volume'] = self.historical_search_volume.to_dict() if self.historical_search_volume else None
        _dict['categories_for_domain'] = self.categories_for_domain.to_dict() if self.categories_for_domain else None
        _dict['domain_metrics_by_categories'] = self.domain_metrics_by_categories.to_dict() if self.domain_metrics_by_categories else None
        _dict['top_searches'] = self.top_searches.to_dict() if self.top_searches else None
        _dict['domain_whois_overview'] = self.domain_whois_overview.to_dict() if self.domain_whois_overview else None
        _dict['historical_rank_overview'] = self.historical_rank_overview.to_dict() if self.historical_rank_overview else None
        _dict['keywords_for_categories'] = self.keywords_for_categories.to_dict() if self.keywords_for_categories else None
        _dict['historical_serps'] = self.historical_serps.to_dict() if self.historical_serps else None
        _dict['app_competitors'] = self.app_competitors.to_dict() if self.app_competitors else None
        _dict['keywords_for_app'] = self.keywords_for_app.to_dict() if self.keywords_for_app else None
        _dict['app_intersection'] = self.app_intersection.to_dict() if self.app_intersection else None
        _dict['bulk_app_metrics'] = self.bulk_app_metrics.to_dict() if self.bulk_app_metrics else None
        _dict['search_intent'] = self.search_intent.to_dict() if self.search_intent else None
        _dict['historical_bulk_traffic_estimation'] = self.historical_bulk_traffic_estimation.to_dict() if self.historical_bulk_traffic_estimation else None
        _dict['categories_for_keywords'] = self.categories_for_keywords.to_dict() if self.categories_for_keywords else None
        _dict['keyword_overview'] = self.keyword_overview.to_dict() if self.keyword_overview else None
        _dict['historical_keyword_data'] = self.historical_keyword_data.to_dict() if self.historical_keyword_data else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
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
            "historical_search_volume": AppendixInfo.from_dict(obj["historical_search_volume"]) if obj.get("historical_search_volume") is not None else None,
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
            "historical_keyword_data": AppendixInfo.from_dict(obj["historical_keyword_data"]) if obj.get("historical_keyword_data") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj