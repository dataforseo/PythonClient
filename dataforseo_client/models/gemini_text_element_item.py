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



class GeminiTextElementItem(BaseGeminiLlmScraperElementItem):
    """
    GeminiTextElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description=r"group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description=r"absolute rank in SERP. absolute position among all the elements in SERP")
    markdown: Optional[StrictStr] = Field(default=None, description=r"content of the element in markdown format. content of the result formatted in the markdown markup language")
    original_text: Optional[StrictStr] = Field(default=None, description=r"unformatted text content of the element")
    sources: Optional[List[Optional[SourceInfo]]] = Field(default=None, description=r"array of sources")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "markdown", 
        "original_text", 
        "sources", 
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
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['markdown'] = self.markdown
        _dict['original_text'] = self.original_text
        sources_items = []
        if self.sources:
            for _item in self.sources:
                if _item:
                    sources_items.append(_item.to_dict())
            _dict['sources'] = sources_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "markdown": obj.get("markdown"),
            "original_text": obj.get("original_text"),
            "sources": [SourceInfo.from_dict(_item) for _item in obj["sources"]] if obj.get("sources") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj