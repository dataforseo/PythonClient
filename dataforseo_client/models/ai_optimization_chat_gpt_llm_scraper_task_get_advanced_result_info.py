from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.chatgpt_search_result import ChatgptSearchResult
from dataforseo_client.models.chat_gpt_source import ChatGptSource
from dataforseo_client.models.chat_gpt_brand_entity import ChatGptBrandEntity
from dataforseo_client.models.base_chat_gpt_llm_scraper_element_item import BaseChatGptLlmScraperElementItem



class AiOptimizationChatGptLlmScraperTaskGetAdvancedResultInfo(BaseModel):
    """
    AiOptimizationChatGptLlmScraperTaskGetAdvancedResultInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description=r"keyword received in a POST array. the keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character)")
    location_code: Optional[StrictInt] = Field(default=None, description=r"location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description=r"language code in a POST array")
    model: Optional[StrictStr] = Field(default=None, description=r"indicates the model version")
    check_url: Optional[StrictStr] = Field(default=None, description=r"direct URL to search engine results. you can use it to make sure that we provided exact results")
    datetime: Optional[StrictStr] = Field(default=None, description=r"date and time when the result was received. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    markdown: Optional[StrictStr] = Field(default=None, description=r"content of the element in markdown format. content of the result formatted in the markdown markup language")
    search_results: Optional[List[Optional[ChatgptSearchResult]]] = Field(default=None, description=r"array of search results. all web search outputs the model retrieved when looking up information, including duplicates and unused entries")
    sources: Optional[List[Optional[ChatGptSource]]] = Field(default=None, description=r"array of sources. the sources the model actually cited or relied on in its final answer")
    fan_out_queries: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"array of fan-out queries. contains related search queries derived from the main query to provide a more comprehensive response")
    brand_entities: Optional[List[Optional[ChatGptBrandEntity]]] = Field(default=None, description=r"array of brand entities. contains information on brands mentioned in the response")
    se_results_count: Optional[StrictInt] = Field(default=None, description=r"total number of results")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"types of search results. contains types of search results (items) found.. possible item types:. chat_gpt_text, chat_gpt_table, chat_gpt_navigation_list, chat_gpt_images, chat_gpt_local_businesses, chat_gpt_products")
    items_count: Optional[StrictInt] = Field(default=None, description=r"the number of results returned in the items array")
    items: Optional[List[Optional[BaseChatGptLlmScraperElementItem]]] = Field(default=None, description=r"items present in the element")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_code", 
        "language_code", 
        "model", 
        "check_url", 
        "datetime", 
        "markdown", 
        "search_results", 
        "sources", 
        "fan_out_queries", 
        "brand_entities", 
        "se_results_count", 
        "item_types", 
        "items_count", 
        "items", 
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

        _dict['keyword'] = self.keyword
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['model'] = self.model
        _dict['check_url'] = self.check_url
        _dict['datetime'] = self.datetime
        _dict['markdown'] = self.markdown
        search_results_items = []
        if self.search_results:
            for _item in self.search_results:
                if _item:
                    search_results_items.append(_item.to_dict())
            _dict['search_results'] = search_results_items
        sources_items = []
        if self.sources:
            for _item in self.sources:
                if _item:
                    sources_items.append(_item.to_dict())
            _dict['sources'] = sources_items
        _dict['fan_out_queries'] = self.fan_out_queries
        brand_entities_items = []
        if self.brand_entities:
            for _item in self.brand_entities:
                if _item:
                    brand_entities_items.append(_item.to_dict())
            _dict['brand_entities'] = brand_entities_items
        _dict['se_results_count'] = self.se_results_count
        _dict['item_types'] = self.item_types
        _dict['items_count'] = self.items_count
        items_items = []
        if self.items:
            for _item in self.items:
                if _item:
                    items_items.append(_item.to_dict())
            _dict['items'] = items_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "model": obj.get("model"),
            "check_url": obj.get("check_url"),
            "datetime": obj.get("datetime"),
            "markdown": obj.get("markdown"),
            "search_results": [ChatgptSearchResult.from_dict(_item) for _item in obj["search_results"]] if obj.get("search_results") is not None else None,
            "sources": [ChatGptSource.from_dict(_item) for _item in obj["sources"]] if obj.get("sources") is not None else None,
            "fan_out_queries": obj.get("fan_out_queries"),
            "brand_entities": [ChatGptBrandEntity.from_dict(_item) for _item in obj["brand_entities"]] if obj.get("brand_entities") is not None else None,
            "se_results_count": obj.get("se_results_count"),
            "item_types": obj.get("item_types"),
            "items_count": obj.get("items_count"),
            "items": [BaseChatGptLlmScraperElementItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj