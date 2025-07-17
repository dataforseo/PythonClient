from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsAvailableFiltersResultInfo(BaseModel):
    """
    DataforseoLabsAvailableFiltersResultInfo
    """ # noqa: E501
    related_keywords: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    keyword_suggestions: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    ranked_keywords: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    keyword_ideas: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    serp_competitors: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    relevant_pages: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    subdomains: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    competitors_domain: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    categories_for_domain: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    keywords_for_categories: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    domain_intersection: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    page_intersection: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    domain_whois_overview: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    top_searches: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    domain_metrics_by_categories: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    keywords_for_site: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    product_competitors: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    product_keyword_intersections: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    app_intersection: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    app_competitors: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    keywords_for_app: Optional[Dict[str, Optional[Dict[str, Optional[StrictStr]]]]] = Field(default=None, description="")
    database_rows_count: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "related_keywords", 
        "keyword_suggestions", 
        "ranked_keywords", 
        "keyword_ideas", 
        "serp_competitors", 
        "relevant_pages", 
        "subdomains", 
        "competitors_domain", 
        "categories_for_domain", 
        "keywords_for_categories", 
        "domain_intersection", 
        "page_intersection", 
        "domain_whois_overview", 
        "top_searches", 
        "domain_metrics_by_categories", 
        "keywords_for_site", 
        "product_competitors", 
        "product_keyword_intersections", 
        "app_intersection", 
        "app_competitors", 
        "keywords_for_app", 
        "database_rows_count", 
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

        _dict['related_keywords'] = self.related_keywords
        _dict['keyword_suggestions'] = self.keyword_suggestions
        _dict['ranked_keywords'] = self.ranked_keywords
        _dict['keyword_ideas'] = self.keyword_ideas
        _dict['serp_competitors'] = self.serp_competitors
        _dict['relevant_pages'] = self.relevant_pages
        _dict['subdomains'] = self.subdomains
        _dict['competitors_domain'] = self.competitors_domain
        _dict['categories_for_domain'] = self.categories_for_domain
        _dict['keywords_for_categories'] = self.keywords_for_categories
        _dict['domain_intersection'] = self.domain_intersection
        _dict['page_intersection'] = self.page_intersection
        _dict['domain_whois_overview'] = self.domain_whois_overview
        _dict['top_searches'] = self.top_searches
        _dict['domain_metrics_by_categories'] = self.domain_metrics_by_categories
        _dict['keywords_for_site'] = self.keywords_for_site
        _dict['product_competitors'] = self.product_competitors
        _dict['product_keyword_intersections'] = self.product_keyword_intersections
        _dict['app_intersection'] = self.app_intersection
        _dict['app_competitors'] = self.app_competitors
        _dict['keywords_for_app'] = self.keywords_for_app
        _dict['database_rows_count'] = self.database_rows_count
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "related_keywords": obj.get("related_keywords"),
            "keyword_suggestions": obj.get("keyword_suggestions"),
            "ranked_keywords": obj.get("ranked_keywords"),
            "keyword_ideas": obj.get("keyword_ideas"),
            "serp_competitors": obj.get("serp_competitors"),
            "relevant_pages": obj.get("relevant_pages"),
            "subdomains": obj.get("subdomains"),
            "competitors_domain": obj.get("competitors_domain"),
            "categories_for_domain": obj.get("categories_for_domain"),
            "keywords_for_categories": obj.get("keywords_for_categories"),
            "domain_intersection": obj.get("domain_intersection"),
            "page_intersection": obj.get("page_intersection"),
            "domain_whois_overview": obj.get("domain_whois_overview"),
            "top_searches": obj.get("top_searches"),
            "domain_metrics_by_categories": obj.get("domain_metrics_by_categories"),
            "keywords_for_site": obj.get("keywords_for_site"),
            "product_competitors": obj.get("product_competitors"),
            "product_keyword_intersections": obj.get("product_keyword_intersections"),
            "app_intersection": obj.get("app_intersection"),
            "app_competitors": obj.get("app_competitors"),
            "keywords_for_app": obj.get("keywords_for_app"),
            "database_rows_count": obj.get("database_rows_count"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj