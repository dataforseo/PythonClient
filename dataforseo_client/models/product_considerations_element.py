from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_serp_api_product_consideration_expanded_element_item import BaseSerpApiProductConsiderationExpandedElementItem



class ProductConsiderationsElement(BaseModel):
    """
    ProductConsiderationsElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="title of a given link element")
    consideration_category: Optional[StrictStr] = Field(default=None, description="category of the consideration element. the category is indicated just above the title fo the consideration element")
    expanded_element: Optional[List[Optional[BaseSerpApiProductConsiderationExpandedElementItem]]] = Field(default=None, description="expanded element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "consideration_category", 
        "expanded_element", 
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
        _dict['title'] = self.title
        _dict['consideration_category'] = self.consideration_category
        expanded_element_items = []
        if self.expanded_element:
            for _item in self.expanded_element:
                if _item:
                    expanded_element_items.append(_item.to_dict())
            _dict['expanded_element'] = expanded_element_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "consideration_category": obj.get("consideration_category"),
            "expanded_element": [BaseSerpApiProductConsiderationExpandedElementItem.from_dict(_item) for _item in obj["expanded_element"]] if obj.get("expanded_element") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj