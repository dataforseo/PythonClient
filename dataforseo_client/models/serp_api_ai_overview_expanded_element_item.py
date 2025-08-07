from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_overview_expanded_component import AiOverviewExpandedComponent
from dataforseo_client.models.ai_mode_ai_overview_reference_info import AiModeAiOverviewReferenceInfo
from dataforseo_client.models.base_serp_api_ai_overview_element_item import BaseSerpApiAiOverviewElementItem



class SerpApiAiOverviewExpandedElementItem(BaseSerpApiAiOverviewElementItem):
    """
    SerpApiAiOverviewExpandedElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    title: Optional[StrictStr] = Field(default=None, description="title of the element")
    text: Optional[StrictStr] = Field(default=None, description="text of the component")
    components: Optional[List[Optional[AiOverviewExpandedComponent]]] = Field(default=None, description="array of components of the element")
    references: Optional[List[Optional[AiModeAiOverviewReferenceInfo]]] = Field(default=None, description="additional references relevant to the item. includes references to webpages that may have been used to generate the ai_overview")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "title", 
        "text", 
        "components", 
        "references", 
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
        _dict['title'] = self.title
        _dict['text'] = self.text
        components_items = []
        if self.components:
            for _item in self.components:
                if _item:
                    components_items.append(_item.to_dict())
            _dict['components'] = components_items
        references_items = []
        if self.references:
            for _item in self.references:
                if _item:
                    references_items.append(_item.to_dict())
            _dict['references'] = references_items
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
            "title": obj.get("title"),
            "text": obj.get("text"),
            "components": [AiOverviewExpandedComponent.from_dict(_item) for _item in obj["components"]] if obj.get("components") is not None else None,
            "references": [AiModeAiOverviewReferenceInfo.from_dict(_item) for _item in obj["references"]] if obj.get("references") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj