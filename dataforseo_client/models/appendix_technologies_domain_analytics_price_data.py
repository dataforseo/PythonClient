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
from dataforseo_client.models.appendix_keyword_bing_keywords_data_price_data_info import AppendixKeywordBingKeywordsDataPriceDataInfo
from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo
from typing import Optional, Set
from typing_extensions import Self

class AppendixTechnologiesDomainAnalyticsPriceData(BaseModel):
    """
    AppendixTechnologiesDomainAnalyticsPriceData
    """ # noqa: E501
    languages: Optional[AppendixTaskKeywordsDataPriceDataInfo] = None
    locations: Optional[AppendixTaskKeywordsDataPriceDataInfo] = None
    technologies: Optional[AppendixTaskKeywordsDataPriceDataInfo] = None
    aggregation_technologies: Optional[AppendixKeywordBingKeywordsDataPriceDataInfo] = None
    domains_by_html_terms: Optional[AppendixKeywordBingKeywordsDataPriceDataInfo] = None
    domains_by_technology: Optional[AppendixKeywordBingKeywordsDataPriceDataInfo] = None
    domain_technologies: Optional[AppendixKeywordBingKeywordsDataPriceDataInfo] = None
    technologies_summary: Optional[AppendixKeywordBingKeywordsDataPriceDataInfo] = None
    technology_stats: Optional[AppendixKeywordBingKeywordsDataPriceDataInfo] = None
    __properties: ClassVar[List[str]] = ["languages", "locations", "technologies", "aggregation_technologies", "domains_by_html_terms", "domains_by_technology", "domain_technologies", "technologies_summary", "technology_stats"]

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
        """Create an instance of AppendixTechnologiesDomainAnalyticsPriceData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of languages
        if self.languages:
            _dict['languages'] = self.languages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of locations
        if self.locations:
            _dict['locations'] = self.locations.to_dict()
        # override the default output from pydantic by calling `to_dict()` of technologies
        if self.technologies:
            _dict['technologies'] = self.technologies.to_dict()
        # override the default output from pydantic by calling `to_dict()` of aggregation_technologies
        if self.aggregation_technologies:
            _dict['aggregation_technologies'] = self.aggregation_technologies.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domains_by_html_terms
        if self.domains_by_html_terms:
            _dict['domains_by_html_terms'] = self.domains_by_html_terms.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domains_by_technology
        if self.domains_by_technology:
            _dict['domains_by_technology'] = self.domains_by_technology.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_technologies
        if self.domain_technologies:
            _dict['domain_technologies'] = self.domain_technologies.to_dict()
        # override the default output from pydantic by calling `to_dict()` of technologies_summary
        if self.technologies_summary:
            _dict['technologies_summary'] = self.technologies_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of technology_stats
        if self.technology_stats:
            _dict['technology_stats'] = self.technology_stats.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppendixTechnologiesDomainAnalyticsPriceData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "languages": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["languages"]) if obj.get("languages") is not None else None,
            "locations": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["locations"]) if obj.get("locations") is not None else None,
            "technologies": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["technologies"]) if obj.get("technologies") is not None else None,
            "aggregation_technologies": AppendixKeywordBingKeywordsDataPriceDataInfo.from_dict(obj["aggregation_technologies"]) if obj.get("aggregation_technologies") is not None else None,
            "domains_by_html_terms": AppendixKeywordBingKeywordsDataPriceDataInfo.from_dict(obj["domains_by_html_terms"]) if obj.get("domains_by_html_terms") is not None else None,
            "domains_by_technology": AppendixKeywordBingKeywordsDataPriceDataInfo.from_dict(obj["domains_by_technology"]) if obj.get("domains_by_technology") is not None else None,
            "domain_technologies": AppendixKeywordBingKeywordsDataPriceDataInfo.from_dict(obj["domain_technologies"]) if obj.get("domain_technologies") is not None else None,
            "technologies_summary": AppendixKeywordBingKeywordsDataPriceDataInfo.from_dict(obj["technologies_summary"]) if obj.get("technologies_summary") is not None else None,
            "technology_stats": AppendixKeywordBingKeywordsDataPriceDataInfo.from_dict(obj["technology_stats"]) if obj.get("technology_stats") is not None else None
        })
        return _obj


