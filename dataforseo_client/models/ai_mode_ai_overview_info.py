from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_serp_api_ai_mode_ai_overview_element_item import BaseSerpApiAiModeAiOverviewElementItem
from dataforseo_client.models.ai_mode_ai_overview_reference_info import AiModeAiOverviewReferenceInfo
from dataforseo_client.models.ai_mode_rectangle_info import AiModeRectangleInfo



class AiModeAiOverviewInfo(BaseModel):
    """
    AiModeAiOverviewInfo
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    markdown: Optional[StrictStr] = Field(default=None, description="content of the element in markdown format. the text of the ai_overview formatted in the markdown markup language")
    items: Optional[List[Optional[BaseSerpApiAiModeAiOverviewElementItem]]] = Field(default=None, description="items of the element")
    references: Optional[List[Optional[AiModeAiOverviewReferenceInfo]]] = Field(default=None, description="additional references relevant to the item. includes references to webpages that may have been used to generate the ai_overview")
    rectangle: Optional[AiModeRectangleInfo] = Field(default=None, description="rectangle parameters. contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP. equals null if calculate_rectangles in the POST request is not set to true")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "markdown", 
        "items", 
        "references", 
        "rectangle", 
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
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
        _dict['markdown'] = self.markdown
        items_items = []
        if self.items:
            for _item in self.items:
                if _item:
                    items_items.append(_item.to_dict())
            _dict['items'] = items_items
        references_items = []
        if self.references:
            for _item in self.references:
                if _item:
                    references_items.append(_item.to_dict())
            _dict['references'] = references_items
        _dict['rectangle'] = self.rectangle.to_dict() if self.rectangle else None
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
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "markdown": obj.get("markdown"),
            "items": [BaseSerpApiAiModeAiOverviewElementItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "references": [AiModeAiOverviewReferenceInfo.from_dict(_item) for _item in obj["references"]] if obj.get("references") is not None else None,
            "rectangle": AiModeRectangleInfo.from_dict(obj["rectangle"]) if obj.get("rectangle") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj