from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.source_info import SourceInfo
from dataforseo_client.models.base_gemini_llm_scraper_element_item import BaseGeminiLlmScraperElementItem



class AiOptimizationGeminiLlmScraperTaskGetAdvancedResultInfo(BaseModel):
    """
    AiOptimizationGeminiLlmScraperTaskGetAdvancedResultInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description=r"keyword received in a POST array. the keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character)")
    location_code: Optional[StrictInt] = Field(default=None, description=r"location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description=r"language code in a POST array")
    model: Optional[StrictStr] = Field(default=None, description=r"indicates the model version")
    datetime: Optional[StrictStr] = Field(default=None, description=r"date and time when the result was received. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    markdown: Optional[StrictStr] = Field(default=None, description=r"content of the element in markdown format. content of the result formatted in the markdown markup language")
    sources: Optional[List[Optional[SourceInfo]]] = Field(default=None, description=r"array of sources. the sources the model actually cited or relied on in its final answer")
    se_results_count: Optional[StrictInt] = Field(default=None, description=r"total number of results")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"types of search results. contains types of search results (items) found in SERP.. possible item types:. gemini_text, gemini_table, gemini_images")
    items_count: Optional[StrictInt] = Field(default=None, description=r"the number of results returned in the items array")
    items: Optional[List[Optional[BaseGeminiLlmScraperElementItem]]] = Field(default=None, description=r"items present in the element")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_code", 
        "language_code", 
        "model", 
        "datetime", 
        "markdown", 
        "sources", 
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
        _dict['datetime'] = self.datetime
        _dict['markdown'] = self.markdown
        sources_items = []
        if self.sources:
            for _item in self.sources:
                if _item:
                    sources_items.append(_item.to_dict())
            _dict['sources'] = sources_items
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
            "datetime": obj.get("datetime"),
            "markdown": obj.get("markdown"),
            "sources": [SourceInfo.from_dict(_item) for _item in obj["sources"]] if obj.get("sources") is not None else None,
            "se_results_count": obj.get("se_results_count"),
            "item_types": obj.get("item_types"),
            "items_count": obj.get("items_count"),
            "items": [BaseGeminiLlmScraperElementItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj