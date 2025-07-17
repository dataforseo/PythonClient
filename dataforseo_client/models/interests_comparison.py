from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.absolute_items import AbsoluteItems



class InterestsComparison(BaseModel):
    """
    InterestsComparison
    """ # noqa: E501
    items: Optional[List[Optional[AbsoluteItems]]] = Field(default=None, description="contains keyword popularity and related data")
    absolute_items: Optional[List[Optional[AbsoluteItems]]] = Field(default=None, description="keyword popularity rates across all locations. values in this array represent percentages relative to the maximum value across all locations")
    __properties: ClassVar[List[str]] = [
        "items", 
        "absolute_items", 
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
        absolute_items_items = []
        if self.absolute_items:
            for _item in self.absolute_items:
                if _item:
                    absolute_items_items.append(_item.to_dict())
            _dict['absolute_items'] = absolute_items_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "items": [AbsoluteItems.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "absolute_items": [AbsoluteItems.from_dict(_item) for _item in obj["absolute_items"]] if obj.get("absolute_items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj