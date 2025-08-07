from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.on_page_html_resource_item import OnPageHtmlResourceItem



class OnPageDuplicateTagsItem(BaseModel):
    """
    OnPageDuplicateTagsItem
    """ # noqa: E501
    accumulator: Optional[StrictStr] = Field(default=None, description="contains the value of duplicated tag")
    total_count: Optional[StrictInt] = Field(default=None, description="total count of duplicate pages")
    pages: Optional[List[Optional[OnPageHtmlResourceItem]]] = Field(default=None, description="pages with duplicate tags")
    __properties: ClassVar[List[str]] = [
        "accumulator", 
        "total_count", 
        "pages", 
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

        _dict['accumulator'] = self.accumulator
        _dict['total_count'] = self.total_count
        pages_items = []
        if self.pages:
            for _item in self.pages:
                if _item:
                    pages_items.append(_item.to_dict())
            _dict['pages'] = pages_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accumulator": obj.get("accumulator"),
            "total_count": obj.get("total_count"),
            "pages": [OnPageHtmlResourceItem.from_dict(_item) for _item in obj["pages"]] if obj.get("pages") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj