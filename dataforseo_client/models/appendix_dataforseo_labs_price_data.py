from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_bing_keywords_data_price_data_info import AppendixBingKeywordsDataPriceDataInfo
from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo



class AppendixDataforseoLabsPriceData(BaseModel):
    """
    AppendixDataforseoLabsPriceData
    """ # noqa: E501
    app_competitors: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    app_intersection: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    bulk_app_metrics: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    bulk_keyword_difficulty: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    bulk_search_volume: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    bulk_traffic_estimation: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    categories: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    categories_for_domain: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    categories_for_keywords: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    competitors_domain: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    domain_intersection: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    domain_metrics_by_categories: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    domain_rank_overview: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    domain_whois_overview: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    errors: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    historical_bulk_traffic_estimation: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    historical_keyword_data: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    historical_rank_overview: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    historical_search_volume: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    historical_serps: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    keyword_ideas: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    keyword_overview: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    keywords_for_app: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    keywords_for_categories: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    keywords_for_site: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    keyword_suggestions: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    locations_and_languages: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    page_intersection: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    product_competitors: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    product_keyword_intersections: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    product_rank_overview: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    ranked_keywords: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    related_keywords: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    relevant_pages: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    search_intent: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    serp_competitors: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    subdomains: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    top_searches: Optional[AppendixBingKeywordsDataPriceDataInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "app_competitors", 
        "app_intersection", 
        "bulk_app_metrics", 
        "bulk_keyword_difficulty", 
        "bulk_search_volume", 
        "bulk_traffic_estimation", 
        "categories", 
        "categories_for_domain", 
        "categories_for_keywords", 
        "competitors_domain", 
        "domain_intersection", 
        "domain_metrics_by_categories", 
        "domain_rank_overview", 
        "domain_whois_overview", 
        "errors", 
        "historical_bulk_traffic_estimation", 
        "historical_keyword_data", 
        "historical_rank_overview", 
        "historical_search_volume", 
        "historical_serps", 
        "keyword_ideas", 
        "keyword_overview", 
        "keywords_for_app", 
        "keywords_for_categories", 
        "keywords_for_site", 
        "keyword_suggestions", 
        "locations_and_languages", 
        "page_intersection", 
        "product_competitors", 
        "product_keyword_intersections", 
        "product_rank_overview", 
        "ranked_keywords", 
        "related_keywords", 
        "relevant_pages", 
        "search_intent", 
        "serp_competitors", 
        "subdomains", 
        "top_searches", 
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

        _dict['app_competitors'] = self.app_competitors.to_dict() if self.app_competitors else None
        _dict['app_intersection'] = self.app_intersection.to_dict() if self.app_intersection else None
        _dict['bulk_app_metrics'] = self.bulk_app_metrics.to_dict() if self.bulk_app_metrics else None
        _dict['bulk_keyword_difficulty'] = self.bulk_keyword_difficulty.to_dict() if self.bulk_keyword_difficulty else None
        _dict['bulk_search_volume'] = self.bulk_search_volume.to_dict() if self.bulk_search_volume else None
        _dict['bulk_traffic_estimation'] = self.bulk_traffic_estimation.to_dict() if self.bulk_traffic_estimation else None
        _dict['categories'] = self.categories.to_dict() if self.categories else None
        _dict['categories_for_domain'] = self.categories_for_domain.to_dict() if self.categories_for_domain else None
        _dict['categories_for_keywords'] = self.categories_for_keywords.to_dict() if self.categories_for_keywords else None
        _dict['competitors_domain'] = self.competitors_domain.to_dict() if self.competitors_domain else None
        _dict['domain_intersection'] = self.domain_intersection.to_dict() if self.domain_intersection else None
        _dict['domain_metrics_by_categories'] = self.domain_metrics_by_categories.to_dict() if self.domain_metrics_by_categories else None
        _dict['domain_rank_overview'] = self.domain_rank_overview.to_dict() if self.domain_rank_overview else None
        _dict['domain_whois_overview'] = self.domain_whois_overview.to_dict() if self.domain_whois_overview else None
        _dict['errors'] = self.errors.to_dict() if self.errors else None
        _dict['historical_bulk_traffic_estimation'] = self.historical_bulk_traffic_estimation.to_dict() if self.historical_bulk_traffic_estimation else None
        _dict['historical_keyword_data'] = self.historical_keyword_data.to_dict() if self.historical_keyword_data else None
        _dict['historical_rank_overview'] = self.historical_rank_overview.to_dict() if self.historical_rank_overview else None
        _dict['historical_search_volume'] = self.historical_search_volume.to_dict() if self.historical_search_volume else None
        _dict['historical_serps'] = self.historical_serps.to_dict() if self.historical_serps else None
        _dict['keyword_ideas'] = self.keyword_ideas.to_dict() if self.keyword_ideas else None
        _dict['keyword_overview'] = self.keyword_overview.to_dict() if self.keyword_overview else None
        _dict['keywords_for_app'] = self.keywords_for_app.to_dict() if self.keywords_for_app else None
        _dict['keywords_for_categories'] = self.keywords_for_categories.to_dict() if self.keywords_for_categories else None
        _dict['keywords_for_site'] = self.keywords_for_site.to_dict() if self.keywords_for_site else None
        _dict['keyword_suggestions'] = self.keyword_suggestions.to_dict() if self.keyword_suggestions else None
        _dict['locations_and_languages'] = self.locations_and_languages.to_dict() if self.locations_and_languages else None
        _dict['page_intersection'] = self.page_intersection.to_dict() if self.page_intersection else None
        _dict['product_competitors'] = self.product_competitors.to_dict() if self.product_competitors else None
        _dict['product_keyword_intersections'] = self.product_keyword_intersections.to_dict() if self.product_keyword_intersections else None
        _dict['product_rank_overview'] = self.product_rank_overview.to_dict() if self.product_rank_overview else None
        _dict['ranked_keywords'] = self.ranked_keywords.to_dict() if self.ranked_keywords else None
        _dict['related_keywords'] = self.related_keywords.to_dict() if self.related_keywords else None
        _dict['relevant_pages'] = self.relevant_pages.to_dict() if self.relevant_pages else None
        _dict['search_intent'] = self.search_intent.to_dict() if self.search_intent else None
        _dict['serp_competitors'] = self.serp_competitors.to_dict() if self.serp_competitors else None
        _dict['subdomains'] = self.subdomains.to_dict() if self.subdomains else None
        _dict['top_searches'] = self.top_searches.to_dict() if self.top_searches else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
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
            "historical_search_volume": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["historical_search_volume"]) if obj.get("historical_search_volume") is not None else None,
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
            "top_searches": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["top_searches"]) if obj.get("top_searches") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj