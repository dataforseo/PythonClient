from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_overview_element import AiOverviewElement
from dataforseo_client.models.ai_mode_ai_overview_reference_info import AiModeAiOverviewReferenceInfo
from dataforseo_client.models.base_serp_api_product_consideration_expanded_element_item import BaseSerpApiProductConsiderationExpandedElementItem



class SerpApiProductConsiderationsAiOverviewExpandedElementItem(BaseSerpApiProductConsiderationExpandedElementItem):
    """
    SerpApiProductConsiderationsAiOverviewExpandedElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    items: Optional[List[Optional[AiOverviewElement]]] = Field(default=None, description="contains arrays of elements available in the list")
    references: Optional[List[Optional[AiModeAiOverviewReferenceInfo]]] = Field(default=None, description="additional references relevant to the item. includes references to webpages that may have been used to generate the ai_overview")
    __properties: ClassVar[List[str]] = [
        "type", 
        "items", 
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
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "items": [AiOverviewElement.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "references": [AiModeAiOverviewReferenceInfo.from_dict(_item) for _item in obj["references"]] if obj.get("references") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj