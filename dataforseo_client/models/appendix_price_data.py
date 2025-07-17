from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_keywords_data_price_data import AppendixKeywordsDataPriceData
from dataforseo_client.models.appendix_merchant_price_data import AppendixMerchantPriceData
from dataforseo_client.models.appendix_serp_price_data import AppendixSerpPriceData
from dataforseo_client.models.appendix_appendix_price_data import AppendixAppendixPriceData
from dataforseo_client.models.appendix_app_data_price_data import AppendixAppDataPriceData
from dataforseo_client.models.appendix_backlinks_price_data import AppendixBacklinksPriceData
from dataforseo_client.models.appendix_business_data_price_data import AppendixBusinessDataPriceData
from dataforseo_client.models.appendix_content_analysis_price_data import AppendixContentAnalysisPriceData
from dataforseo_client.models.appendix_content_generation_price_data import AppendixContentGenerationPriceData
from dataforseo_client.models.appendix_dataforseo_labs_price_data import AppendixDataforseoLabsPriceData
from dataforseo_client.models.appendix_domain_analytics_price_data import AppendixDomainAnalyticsPriceData
from dataforseo_client.models.appendix_on_page_price_data import AppendixOnPagePriceData



class AppendixPriceData(BaseModel):
    """
    AppendixPriceData
    """ # noqa: E501
    keywords_data: Optional[AppendixKeywordsDataPriceData] = Field(default=None, description="")
    merchant: Optional[AppendixMerchantPriceData] = Field(default=None, description="")
    serp: Optional[AppendixSerpPriceData] = Field(default=None, description="")
    appendix: Optional[AppendixAppendixPriceData] = Field(default=None, description="")
    app_data: Optional[AppendixAppDataPriceData] = Field(default=None, description="")
    backlinks: Optional[AppendixBacklinksPriceData] = Field(default=None, description="")
    business_data: Optional[AppendixBusinessDataPriceData] = Field(default=None, description="")
    content_analysis: Optional[AppendixContentAnalysisPriceData] = Field(default=None, description="")
    content_generation: Optional[AppendixContentGenerationPriceData] = Field(default=None, description="")
    dataforseo_labs: Optional[AppendixDataforseoLabsPriceData] = Field(default=None, description="")
    domain_analytics: Optional[AppendixDomainAnalyticsPriceData] = Field(default=None, description="")
    on_page: Optional[AppendixOnPagePriceData] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "keywords_data", 
        "merchant", 
        "serp", 
        "appendix", 
        "app_data", 
        "backlinks", 
        "business_data", 
        "content_analysis", 
        "content_generation", 
        "dataforseo_labs", 
        "domain_analytics", 
        "on_page", 
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

        _dict['keywords_data'] = self.keywords_data.to_dict() if self.keywords_data else None
        _dict['merchant'] = self.merchant.to_dict() if self.merchant else None
        _dict['serp'] = self.serp.to_dict() if self.serp else None
        _dict['appendix'] = self.appendix.to_dict() if self.appendix else None
        _dict['app_data'] = self.app_data.to_dict() if self.app_data else None
        _dict['backlinks'] = self.backlinks.to_dict() if self.backlinks else None
        _dict['business_data'] = self.business_data.to_dict() if self.business_data else None
        _dict['content_analysis'] = self.content_analysis.to_dict() if self.content_analysis else None
        _dict['content_generation'] = self.content_generation.to_dict() if self.content_generation else None
        _dict['dataforseo_labs'] = self.dataforseo_labs.to_dict() if self.dataforseo_labs else None
        _dict['domain_analytics'] = self.domain_analytics.to_dict() if self.domain_analytics else None
        _dict['on_page'] = self.on_page.to_dict() if self.on_page else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keywords_data": AppendixKeywordsDataPriceData.from_dict(obj["keywords_data"]) if obj.get("keywords_data") is not None else None,
            "merchant": AppendixMerchantPriceData.from_dict(obj["merchant"]) if obj.get("merchant") is not None else None,
            "serp": AppendixSerpPriceData.from_dict(obj["serp"]) if obj.get("serp") is not None else None,
            "appendix": AppendixAppendixPriceData.from_dict(obj["appendix"]) if obj.get("appendix") is not None else None,
            "app_data": AppendixAppDataPriceData.from_dict(obj["app_data"]) if obj.get("app_data") is not None else None,
            "backlinks": AppendixBacklinksPriceData.from_dict(obj["backlinks"]) if obj.get("backlinks") is not None else None,
            "business_data": AppendixBusinessDataPriceData.from_dict(obj["business_data"]) if obj.get("business_data") is not None else None,
            "content_analysis": AppendixContentAnalysisPriceData.from_dict(obj["content_analysis"]) if obj.get("content_analysis") is not None else None,
            "content_generation": AppendixContentGenerationPriceData.from_dict(obj["content_generation"]) if obj.get("content_generation") is not None else None,
            "dataforseo_labs": AppendixDataforseoLabsPriceData.from_dict(obj["dataforseo_labs"]) if obj.get("dataforseo_labs") is not None else None,
            "domain_analytics": AppendixDomainAnalyticsPriceData.from_dict(obj["domain_analytics"]) if obj.get("domain_analytics") is not None else None,
            "on_page": AppendixOnPagePriceData.from_dict(obj["on_page"]) if obj.get("on_page") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj