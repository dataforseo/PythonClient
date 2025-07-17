from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.technology_category_info import TechnologyCategoryInfo



class Groups(BaseModel):
    """
    Groups
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="id of the technology group. example:. marketing, sales")
    title: Optional[StrictStr] = Field(default=None, description="title of the technology group")
    categories: Optional[List[Optional[TechnologyCategoryInfo]]] = Field(default=None, description="technology categories in this group")
    __properties: ClassVar[List[str]] = [
        "id", 
        "title", 
        "categories", 
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

        _dict['id'] = self.id
        _dict['title'] = self.title
        categories_items = []
        if self.categories:
            for _item in self.categories:
                if _item:
                    categories_items.append(_item.to_dict())
            _dict['categories'] = categories_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "categories": [TechnologyCategoryInfo.from_dict(_item) for _item in obj["categories"]] if obj.get("categories") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj