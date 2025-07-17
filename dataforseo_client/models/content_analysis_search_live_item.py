from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.content_rating_info import ContentRatingInfo
from dataforseo_client.models.social_metrics_info import SocialMetricsInfo
from dataforseo_client.models.analysis_content_info import AnalysisContentInfo



class ContentAnalysisSearchLiveItem(BaseModel):
    """
    ContentAnalysisSearchLiveItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    url: Optional[StrictStr] = Field(default=None, description="URL where the citation was found")
    domain: Optional[StrictStr] = Field(default=None, description="domain name")
    main_domain: Optional[StrictStr] = Field(default=None, description="main domain")
    url_rank: Optional[StrictInt] = Field(default=None, description="rank of the url. this value is based on backlink data for the given URL from DataForSEO Backlink Index;. url_rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm. learn more about the metric and how it is calculated in this help center article")
    spam_score: Optional[StrictInt] = Field(default=None, description="backlink spam score of the url. this value is based on backlink data for the given URL from DataForSEO Backlink Index;. learn more about how the metric is calculated on this help center page")
    domain_rank: Optional[StrictInt] = Field(default=None, description="rank of the domain. this value is based on backlink data for the given domain from DataForSEO Backlink Index;. domain_rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm. learn more about the metric and how it is calculated in this help center article")
    fetch_time: Optional[StrictStr] = Field(default=None, description="date and time when our crawler visited the page. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2017-01-24 13:20:59 +00:00")
    country: Optional[StrictStr] = Field(default=None, description="country code of the domain registration. to obtain a full list of available countries, refer to the Locations endpoint")
    language: Optional[StrictStr] = Field(default=None, description="main language of the domain. to obtain a full list of available languages, refer to the Languages endpoint")
    score: Optional[StrictFloat] = Field(default=None, description="citation prominence score. this value is based on url_rank, domain_rank, keyword presence in title, main_title, url, snippet. the higher the score, the more value the related citation has")
    page_category: Optional[List[Optional[StrictInt]]] = Field(default=None, description="contains all relevant page categories. product and service categories relevant for the page. to obtain a full list of available categories, refer to the Categories endpoint")
    page_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="page types")
    ratings: Optional[List[Optional[ContentRatingInfo]]] = Field(default=None, description="ratings found on the page. all ratings found on the page based on microdata")
    social_metrics: Optional[List[Optional[SocialMetricsInfo]]] = Field(default=None, description="social media engagement metrics. data on social media interactions associated with the content based on website embeds developed and supported by social media platforms")
    content_info: Optional[AnalysisContentInfo] = Field(default=None, description="contains data on citations from the given url")
    __properties: ClassVar[List[str]] = [
        "type", 
        "url", 
        "domain", 
        "main_domain", 
        "url_rank", 
        "spam_score", 
        "domain_rank", 
        "fetch_time", 
        "country", 
        "language", 
        "score", 
        "page_category", 
        "page_types", 
        "ratings", 
        "social_metrics", 
        "content_info", 
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

        _dict['type'] = self.type
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        _dict['main_domain'] = self.main_domain
        _dict['url_rank'] = self.url_rank
        _dict['spam_score'] = self.spam_score
        _dict['domain_rank'] = self.domain_rank
        _dict['fetch_time'] = self.fetch_time
        _dict['country'] = self.country
        _dict['language'] = self.language
        _dict['score'] = self.score
        _dict['page_category'] = self.page_category
        _dict['page_types'] = self.page_types
        ratings_items = []
        if self.ratings:
            for _item in self.ratings:
                if _item:
                    ratings_items.append(_item.to_dict())
            _dict['ratings'] = ratings_items
        social_metrics_items = []
        if self.social_metrics:
            for _item in self.social_metrics:
                if _item:
                    social_metrics_items.append(_item.to_dict())
            _dict['social_metrics'] = social_metrics_items
        _dict['content_info'] = self.content_info.to_dict() if self.content_info else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "main_domain": obj.get("main_domain"),
            "url_rank": obj.get("url_rank"),
            "spam_score": obj.get("spam_score"),
            "domain_rank": obj.get("domain_rank"),
            "fetch_time": obj.get("fetch_time"),
            "country": obj.get("country"),
            "language": obj.get("language"),
            "score": obj.get("score"),
            "page_category": obj.get("page_category"),
            "page_types": obj.get("page_types"),
            "ratings": [ContentRatingInfo.from_dict(_item) for _item in obj["ratings"]] if obj.get("ratings") is not None else None,
            "social_metrics": [SocialMetricsInfo.from_dict(_item) for _item in obj["social_metrics"]] if obj.get("social_metrics") is not None else None,
            "content_info": AnalysisContentInfo.from_dict(obj["content_info"]) if obj.get("content_info") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj