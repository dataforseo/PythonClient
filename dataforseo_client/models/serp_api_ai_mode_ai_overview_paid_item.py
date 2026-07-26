from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_mode_ai_overview_paid_element_info import AiModeAiOverviewPaidElementInfo
from dataforseo_client.models.base_serp_api_ai_mode_ai_overview_element_item import BaseSerpApiAiModeAiOverviewElementItem



class SerpApiAiModeAiOverviewPaidItem(BaseSerpApiAiModeAiOverviewElementItem):
    """
    SerpApiAiModeAiOverviewPaidItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    position: Optional[StrictStr] = Field(default=None, description=r"*the alignment of the element in SERP*. can take the following values:. `left`, `right`")
    text: Optional[StrictStr] = Field(default=None, description=r"*reference text*. text snippet from the page that was used to generate the `ai_overview_element`")
    markdown: Optional[StrictStr] = Field(default=None, description=r"*content of the element in markdown format*. the text of the `ai_overview_paid` formatted in the [markdown markup language](https://en.wikipedia.org/wiki/Markdown)")
    items: Optional[List[Optional[AiModeAiOverviewPaidElementInfo]]] = Field(default=None, description=r"*elements of search results found in SERP*")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "text", 
        "markdown", 
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

        _dict['type'] = self.type
        _dict['position'] = self.position
        _dict['text'] = self.text
        _dict['markdown'] = self.markdown
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
            "type": obj.get("type"),
            "position": obj.get("position"),
            "text": obj.get("text"),
            "markdown": obj.get("markdown"),
            "items": [AiModeAiOverviewPaidElementInfo.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj