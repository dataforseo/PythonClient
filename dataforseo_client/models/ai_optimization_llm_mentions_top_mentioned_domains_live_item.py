from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.aggregated_metrics_item_info import AggregatedMetricsItemInfo
from dataforseo_client.models.aggregated_metrics_info_total_info import AggregatedMetricsInfoTotalInfo



class AiOptimizationLlmMentionsTopMentionedDomainsLiveItem(BaseModel):
    """
    AiOptimizationLlmMentionsTopMentionedDomainsLiveItem
    """ # noqa: E501
    domain: Optional[StrictStr] = Field(default=None, description=r"*domain name*. the domain name of the website found in LLM mentions for the specified target")
    location: Optional[List[Optional[AggregatedMetricsItemInfo]]] = Field(default=None, description=r"*location-based grouping*. array of objects containing mention metrics segmented by geographical location")
    language: Optional[List[Optional[AggregatedMetricsItemInfo]]] = Field(default=None, description=r"*language-based grouping*. array of objects containing mention metrics segmented by content language")
    platform: Optional[List[Optional[AggregatedMetricsItemInfo]]] = Field(default=None, description=r"*platform-based grouping*. array of group elements containing mention metrics segmented by AI platform")
    sources_domain: Optional[List[Optional[AggregatedMetricsItemInfo]]] = Field(default=None, description=r"*found top source domains relevant to the target*. array of objects containing data on top domains that are cited as sources in LLM responses. learn more about the sources and how to retrieve LLM citation data at our [Help Center](https://dataforseo.com/help-center/how-to-get-llm-citation-data-with-llm-mentions-api)")
    search_results_domain: Optional[List[Optional[AggregatedMetricsItemInfo]]] = Field(default=None, description=r"*found top search results domains relevant to the target*. array of objects containing data on top domains that appear in search results related to LLM queries;. **Note:** available only for `chat_gpt`")
    brand_entities_title: Optional[List[Optional[AggregatedMetricsItemInfo]]] = Field(default=None, description=r"*data on brand entities relevant to the target*. array of objects containing data on brand entity titles that appear in search results related to LLM queries;. **Note:** available only for `chat_gpt`")
    brand_entities_category: Optional[List[Optional[AggregatedMetricsItemInfo]]] = Field(default=None, description=r"*data on brand entities relevant to the target*. array of objects containing data on brand entity categories that appear in search results related to LLM queries;. **Note:** available only for `chat_gpt`")
    total: Optional[AggregatedMetricsInfoTotalInfo] = Field(default=None, description=r"*aggregated mentions metrics summary*. contains overall aggregated LLM mention metrics across all dimensions")
    __properties: ClassVar[List[str]] = [
        "domain", 
        "location", 
        "language", 
        "platform", 
        "sources_domain", 
        "search_results_domain", 
        "brand_entities_title", 
        "brand_entities_category", 
        "total", 
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

        _dict['domain'] = self.domain
        location_items = []
        if self.location:
            for _item in self.location:
                if _item:
                    location_items.append(_item.to_dict())
            _dict['location'] = location_items
        language_items = []
        if self.language:
            for _item in self.language:
                if _item:
                    language_items.append(_item.to_dict())
            _dict['language'] = language_items
        platform_items = []
        if self.platform:
            for _item in self.platform:
                if _item:
                    platform_items.append(_item.to_dict())
            _dict['platform'] = platform_items
        sources_domain_items = []
        if self.sources_domain:
            for _item in self.sources_domain:
                if _item:
                    sources_domain_items.append(_item.to_dict())
            _dict['sources_domain'] = sources_domain_items
        search_results_domain_items = []
        if self.search_results_domain:
            for _item in self.search_results_domain:
                if _item:
                    search_results_domain_items.append(_item.to_dict())
            _dict['search_results_domain'] = search_results_domain_items
        brand_entities_title_items = []
        if self.brand_entities_title:
            for _item in self.brand_entities_title:
                if _item:
                    brand_entities_title_items.append(_item.to_dict())
            _dict['brand_entities_title'] = brand_entities_title_items
        brand_entities_category_items = []
        if self.brand_entities_category:
            for _item in self.brand_entities_category:
                if _item:
                    brand_entities_category_items.append(_item.to_dict())
            _dict['brand_entities_category'] = brand_entities_category_items
        _dict['total'] = self.total.to_dict() if self.total else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "domain": obj.get("domain"),
            "location": [AggregatedMetricsItemInfo.from_dict(_item) for _item in obj["location"]] if obj.get("location") is not None else None,
            "language": [AggregatedMetricsItemInfo.from_dict(_item) for _item in obj["language"]] if obj.get("language") is not None else None,
            "platform": [AggregatedMetricsItemInfo.from_dict(_item) for _item in obj["platform"]] if obj.get("platform") is not None else None,
            "sources_domain": [AggregatedMetricsItemInfo.from_dict(_item) for _item in obj["sources_domain"]] if obj.get("sources_domain") is not None else None,
            "search_results_domain": [AggregatedMetricsItemInfo.from_dict(_item) for _item in obj["search_results_domain"]] if obj.get("search_results_domain") is not None else None,
            "brand_entities_title": [AggregatedMetricsItemInfo.from_dict(_item) for _item in obj["brand_entities_title"]] if obj.get("brand_entities_title") is not None else None,
            "brand_entities_category": [AggregatedMetricsItemInfo.from_dict(_item) for _item in obj["brand_entities_category"]] if obj.get("brand_entities_category") is not None else None,
            "total": AggregatedMetricsInfoTotalInfo.from_dict(obj["total"]) if obj.get("total") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj