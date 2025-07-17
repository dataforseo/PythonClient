from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.graph_element import GraphElement



class Graph(BaseModel):
    """
    Graph
    """ # noqa: E501
    items: Optional[List[Optional[GraphElement]]] = Field(default=None, description="items present in the element")
    previous_items: Optional[List[Optional[GraphElement]]] = Field(default=None, description="previous close data. contains stock price data based on the preceding time period")
    __properties: ClassVar[List[str]] = [
        "items", 
        "previous_items", 
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

        items_items = []
        if self.items:
            for _item in self.items:
                if _item:
                    items_items.append(_item.to_dict())
            _dict['items'] = items_items
        previous_items_items = []
        if self.previous_items:
            for _item in self.previous_items:
                if _item:
                    previous_items_items.append(_item.to_dict())
            _dict['previous_items'] = previous_items_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "items": [GraphElement.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "previous_items": [GraphElement.from_dict(_item) for _item in obj["previous_items"]] if obj.get("previous_items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj