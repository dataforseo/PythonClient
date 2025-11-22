from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.sources import Sources
from dataforseo_client.models.search_results import SearchResults
from dataforseo_client.models.monthly_searches_info import MonthlySearchesInfo



class AiOptimizationLlmMentionsSearchLiveItem(BaseModel):
    """
    AiOptimizationLlmMentionsSearchLiveItem
    """ # noqa: E501
    platform: Optional[StrictStr] = Field(default=None, description=r"platform received in a POST array")
    location_code: Optional[StrictInt] = Field(default=None, description=r"location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description=r"language code in a POST array")
    question: Optional[StrictStr] = Field(default=None, description=r"relevant question")
    answer: Optional[StrictStr] = Field(default=None, description=r"relevant answer in markdown format. content of the result formatted in the markdown markup language")
    sources: Optional[List[Optional[Sources]]] = Field(default=None, description=r"array of sources. the sources the model cited or relied on in its final answer")
    search_results: Optional[List[Optional[SearchResults]]] = Field(default=None, description=r"array of search results. all web search outputs the model retrieved when looking up information, including duplicates and unused entries")
    ai_search_volume: Optional[StrictInt] = Field(default=None, description=r"current AI search volume rate of a keyword. learn more about this metric here")
    monthly_searches: Optional[List[Optional[MonthlySearchesInfo]]] = Field(default=None, description=r"")
    __properties: ClassVar[List[str]] = [
        "platform", 
        "location_code", 
        "language_code", 
        "question", 
        "answer", 
        "sources", 
        "search_results", 
        "ai_search_volume", 
        "monthly_searches", 
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

        _dict['platform'] = self.platform
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['question'] = self.question
        _dict['answer'] = self.answer
        sources_items = []
        if self.sources:
            for _item in self.sources:
                if _item:
                    sources_items.append(_item.to_dict())
            _dict['sources'] = sources_items
        search_results_items = []
        if self.search_results:
            for _item in self.search_results:
                if _item:
                    search_results_items.append(_item.to_dict())
            _dict['search_results'] = search_results_items
        _dict['ai_search_volume'] = self.ai_search_volume
        monthly_searches_items = []
        if self.monthly_searches:
            for _item in self.monthly_searches:
                if _item:
                    monthly_searches_items.append(_item.to_dict())
            _dict['monthly_searches'] = monthly_searches_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "platform": obj.get("platform"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "question": obj.get("question"),
            "answer": obj.get("answer"),
            "sources": [Sources.from_dict(_item) for _item in obj["sources"]] if obj.get("sources") is not None else None,
            "search_results": [SearchResults.from_dict(_item) for _item in obj["search_results"]] if obj.get("search_results") is not None else None,
            "ai_search_volume": obj.get("ai_search_volume"),
            "monthly_searches": [MonthlySearchesInfo.from_dict(_item) for _item in obj["monthly_searches"]] if obj.get("monthly_searches") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj