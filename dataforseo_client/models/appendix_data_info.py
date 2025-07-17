from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_serp_data_info import AppendixSerpDataInfo
from dataforseo_client.models.appendix_keywords_data_data_info import AppendixKeywordsDataDataInfo
from dataforseo_client.models.appendix_appendix_data_info import AppendixAppendixDataInfo
from dataforseo_client.models.appendix_dataforseo_labs_limits_rates_data_info import AppendixDataforseoLabsLimitsRatesDataInfo
from dataforseo_client.models.appendix_domain_analytics_limits_rates_data_info import AppendixDomainAnalyticsLimitsRatesDataInfo
from dataforseo_client.models.appendix_merchant_limits_rates_data_info import AppendixMerchantLimitsRatesDataInfo
from dataforseo_client.models.appendix_on_page_limits_rates_data_info import AppendixOnPageLimitsRatesDataInfo
from dataforseo_client.models.appendix_business_data_limits_rates_data_info import AppendixBusinessDataLimitsRatesDataInfo
from dataforseo_client.models.appendix_backlinks_limits_rates_data_info import AppendixBacklinksLimitsRatesDataInfo
from dataforseo_client.models.appendix_app_data_limits_rates_data_info import AppendixAppDataLimitsRatesDataInfo
from dataforseo_client.models.appendix_content_analysis_limits_rates_data_info import AppendixContentAnalysisLimitsRatesDataInfo
from dataforseo_client.models.appendix_content_generation_limits_rates_data_info import AppendixContentGenerationLimitsRatesDataInfo
from dataforseo_client.models.appendix_serp_days_rates_data_info import AppendixSerpDaysRatesDataInfo



class AppendixDataInfo(BaseModel):
    """
    AppendixDataInfo
    """ # noqa: E501
    serp: Optional[AppendixSerpDataInfo] = Field(default=None, description="")
    total: Optional[StrictFloat] = Field(default=None, description="total amount of money deposited to your account")
    total_serp: Optional[StrictFloat] = Field(default=None, description="")
    keywords_data: Optional[AppendixKeywordsDataDataInfo] = Field(default=None, description="")
    total_keywords_data: Optional[StrictFloat] = Field(default=None, description="")
    appendix: Optional[AppendixAppendixDataInfo] = Field(default=None, description="")
    total_appendix: Optional[StrictFloat] = Field(default=None, description="")
    dataforseo_labs: Optional[AppendixDataforseoLabsLimitsRatesDataInfo] = Field(default=None, description="")
    total_dataforseo_labs: Optional[StrictFloat] = Field(default=None, description="")
    domain_analytics: Optional[AppendixDomainAnalyticsLimitsRatesDataInfo] = Field(default=None, description="")
    total_domain_analytics: Optional[StrictFloat] = Field(default=None, description="")
    merchant: Optional[AppendixMerchantLimitsRatesDataInfo] = Field(default=None, description="")
    total_merchant: Optional[StrictFloat] = Field(default=None, description="")
    on_page: Optional[AppendixOnPageLimitsRatesDataInfo] = Field(default=None, description="")
    total_on_page: Optional[StrictFloat] = Field(default=None, description="")
    business_data: Optional[AppendixBusinessDataLimitsRatesDataInfo] = Field(default=None, description="")
    total_business_data: Optional[StrictFloat] = Field(default=None, description="")
    backlinks: Optional[AppendixBacklinksLimitsRatesDataInfo] = Field(default=None, description="")
    total_backlinks: Optional[StrictFloat] = Field(default=None, description="")
    app_data: Optional[AppendixAppDataLimitsRatesDataInfo] = Field(default=None, description="")
    total_app_data: Optional[StrictFloat] = Field(default=None, description="")
    content_analysis: Optional[AppendixContentAnalysisLimitsRatesDataInfo] = Field(default=None, description="")
    total_content_analysis: Optional[StrictFloat] = Field(default=None, description="")
    content_generation: Optional[AppendixContentGenerationLimitsRatesDataInfo] = Field(default=None, description="")
    total_content_generation: Optional[StrictFloat] = Field(default=None, description="")
    total_traffic_analytics: Optional[StrictFloat] = Field(default=None, description="")
    traffic_analytics: Optional[AppendixSerpDaysRatesDataInfo] = Field(default=None, description="")
    total_reviews: Optional[StrictFloat] = Field(default=None, description="")
    reviews: Optional[AppendixSerpDaysRatesDataInfo] = Field(default=None, description="")
    total_social: Optional[StrictFloat] = Field(default=None, description="")
    social: Optional[AppendixSerpDaysRatesDataInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "serp", 
        "total", 
        "total_serp", 
        "keywords_data", 
        "total_keywords_data", 
        "appendix", 
        "total_appendix", 
        "dataforseo_labs", 
        "total_dataforseo_labs", 
        "domain_analytics", 
        "total_domain_analytics", 
        "merchant", 
        "total_merchant", 
        "on_page", 
        "total_on_page", 
        "business_data", 
        "total_business_data", 
        "backlinks", 
        "total_backlinks", 
        "app_data", 
        "total_app_data", 
        "content_analysis", 
        "total_content_analysis", 
        "content_generation", 
        "total_content_generation", 
        "total_traffic_analytics", 
        "traffic_analytics", 
        "total_reviews", 
        "reviews", 
        "total_social", 
        "social", 
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

        _dict['serp'] = self.serp.to_dict() if self.serp else None
        _dict['total'] = self.total
        _dict['total_serp'] = self.total_serp
        _dict['keywords_data'] = self.keywords_data.to_dict() if self.keywords_data else None
        _dict['total_keywords_data'] = self.total_keywords_data
        _dict['appendix'] = self.appendix.to_dict() if self.appendix else None
        _dict['total_appendix'] = self.total_appendix
        _dict['dataforseo_labs'] = self.dataforseo_labs.to_dict() if self.dataforseo_labs else None
        _dict['total_dataforseo_labs'] = self.total_dataforseo_labs
        _dict['domain_analytics'] = self.domain_analytics.to_dict() if self.domain_analytics else None
        _dict['total_domain_analytics'] = self.total_domain_analytics
        _dict['merchant'] = self.merchant.to_dict() if self.merchant else None
        _dict['total_merchant'] = self.total_merchant
        _dict['on_page'] = self.on_page.to_dict() if self.on_page else None
        _dict['total_on_page'] = self.total_on_page
        _dict['business_data'] = self.business_data.to_dict() if self.business_data else None
        _dict['total_business_data'] = self.total_business_data
        _dict['backlinks'] = self.backlinks.to_dict() if self.backlinks else None
        _dict['total_backlinks'] = self.total_backlinks
        _dict['app_data'] = self.app_data.to_dict() if self.app_data else None
        _dict['total_app_data'] = self.total_app_data
        _dict['content_analysis'] = self.content_analysis.to_dict() if self.content_analysis else None
        _dict['total_content_analysis'] = self.total_content_analysis
        _dict['content_generation'] = self.content_generation.to_dict() if self.content_generation else None
        _dict['total_content_generation'] = self.total_content_generation
        _dict['total_traffic_analytics'] = self.total_traffic_analytics
        _dict['traffic_analytics'] = self.traffic_analytics.to_dict() if self.traffic_analytics else None
        _dict['total_reviews'] = self.total_reviews
        _dict['reviews'] = self.reviews.to_dict() if self.reviews else None
        _dict['total_social'] = self.total_social
        _dict['social'] = self.social.to_dict() if self.social else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "serp": AppendixSerpDataInfo.from_dict(obj["serp"]) if obj.get("serp") is not None else None,
            "total": obj.get("total"),
            "total_serp": obj.get("total_serp"),
            "keywords_data": AppendixKeywordsDataDataInfo.from_dict(obj["keywords_data"]) if obj.get("keywords_data") is not None else None,
            "total_keywords_data": obj.get("total_keywords_data"),
            "appendix": AppendixAppendixDataInfo.from_dict(obj["appendix"]) if obj.get("appendix") is not None else None,
            "total_appendix": obj.get("total_appendix"),
            "dataforseo_labs": AppendixDataforseoLabsLimitsRatesDataInfo.from_dict(obj["dataforseo_labs"]) if obj.get("dataforseo_labs") is not None else None,
            "total_dataforseo_labs": obj.get("total_dataforseo_labs"),
            "domain_analytics": AppendixDomainAnalyticsLimitsRatesDataInfo.from_dict(obj["domain_analytics"]) if obj.get("domain_analytics") is not None else None,
            "total_domain_analytics": obj.get("total_domain_analytics"),
            "merchant": AppendixMerchantLimitsRatesDataInfo.from_dict(obj["merchant"]) if obj.get("merchant") is not None else None,
            "total_merchant": obj.get("total_merchant"),
            "on_page": AppendixOnPageLimitsRatesDataInfo.from_dict(obj["on_page"]) if obj.get("on_page") is not None else None,
            "total_on_page": obj.get("total_on_page"),
            "business_data": AppendixBusinessDataLimitsRatesDataInfo.from_dict(obj["business_data"]) if obj.get("business_data") is not None else None,
            "total_business_data": obj.get("total_business_data"),
            "backlinks": AppendixBacklinksLimitsRatesDataInfo.from_dict(obj["backlinks"]) if obj.get("backlinks") is not None else None,
            "total_backlinks": obj.get("total_backlinks"),
            "app_data": AppendixAppDataLimitsRatesDataInfo.from_dict(obj["app_data"]) if obj.get("app_data") is not None else None,
            "total_app_data": obj.get("total_app_data"),
            "content_analysis": AppendixContentAnalysisLimitsRatesDataInfo.from_dict(obj["content_analysis"]) if obj.get("content_analysis") is not None else None,
            "total_content_analysis": obj.get("total_content_analysis"),
            "content_generation": AppendixContentGenerationLimitsRatesDataInfo.from_dict(obj["content_generation"]) if obj.get("content_generation") is not None else None,
            "total_content_generation": obj.get("total_content_generation"),
            "total_traffic_analytics": obj.get("total_traffic_analytics"),
            "traffic_analytics": AppendixSerpDaysRatesDataInfo.from_dict(obj["traffic_analytics"]) if obj.get("traffic_analytics") is not None else None,
            "total_reviews": obj.get("total_reviews"),
            "reviews": AppendixSerpDaysRatesDataInfo.from_dict(obj["reviews"]) if obj.get("reviews") is not None else None,
            "total_social": obj.get("total_social"),
            "social": AppendixSerpDaysRatesDataInfo.from_dict(obj["social"]) if obj.get("social") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj