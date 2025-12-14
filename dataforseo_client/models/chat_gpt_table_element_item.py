from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.table import Table
from dataforseo_client.models.chat_gpt_brand_entity import ChatGptBrandEntity
from dataforseo_client.models.base_chat_gpt_llm_scraper_element_item import BaseChatGptLlmScraperElementItem



class ChatGptTableElementItem(BaseChatGptLlmScraperElementItem):
    """
    ChatGptTableElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description=r"group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description=r"absolute rank in SERP. absolute position among all the elements")
    text: Optional[StrictStr] = Field(default=None, description=r"text of the element")
    markdown: Optional[StrictStr] = Field(default=None, description=r"content of the element in markdown format. content of the result formatted in the markdown markup language")
    table: Optional[Table] = Field(default=None, description=r"table present in the element. the header and content of the table present in the element")
    brand_entities: Optional[List[Optional[ChatGptBrandEntity]]] = Field(default=None, description=r"array of brand entities. contains information on brands mentioned in the text")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "text", 
        "markdown", 
        "table", 
        "brand_entities", 
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
        _dict['text'] = self.text
        _dict['markdown'] = self.markdown
        _dict['table'] = self.table.to_dict() if self.table else None
        brand_entities_items = []
        if self.brand_entities:
            for _item in self.brand_entities:
                if _item:
                    brand_entities_items.append(_item.to_dict())
            _dict['brand_entities'] = brand_entities_items
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
            "text": obj.get("text"),
            "markdown": obj.get("markdown"),
            "table": Table.from_dict(obj["table"]) if obj.get("table") is not None else None,
            "brand_entities": [ChatGptBrandEntity.from_dict(_item) for _item in obj["brand_entities"]] if obj.get("brand_entities") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj