from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.section_content_item_info import SectionContentItemInfo
from dataforseo_client.models.table_content_info import TableContentInfo



class PageSectionContentInfo(BaseModel):
    """
    PageSectionContentInfo
    """ # noqa: E501
    primary_content: Optional[List[Optional[SectionContentItemInfo]]] = Field(default=None, description="primary content on the page. you can find more information about content priority calculation in this help center article")
    secondary_content: Optional[List[Optional[SectionContentItemInfo]]] = Field(default=None, description="secondary content on the page. you can find more information about content priority calculation in this help center article")
    table_content: Optional[List[Optional[TableContentInfo]]] = Field(default=None, description="content of the table on the page")
    __properties: ClassVar[List[str]] = [
        "primary_content", 
        "secondary_content", 
        "table_content", 
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

        primary_content_items = []
        if self.primary_content:
            for _item in self.primary_content:
                if _item:
                    primary_content_items.append(_item.to_dict())
            _dict['primary_content'] = primary_content_items
        secondary_content_items = []
        if self.secondary_content:
            for _item in self.secondary_content:
                if _item:
                    secondary_content_items.append(_item.to_dict())
            _dict['secondary_content'] = secondary_content_items
        table_content_items = []
        if self.table_content:
            for _item in self.table_content:
                if _item:
                    table_content_items.append(_item.to_dict())
            _dict['table_content'] = table_content_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "primary_content": [SectionContentItemInfo.from_dict(_item) for _item in obj["primary_content"]] if obj.get("primary_content") is not None else None,
            "secondary_content": [SectionContentItemInfo.from_dict(_item) for _item in obj["secondary_content"]] if obj.get("secondary_content") is not None else None,
            "table_content": [TableContentInfo.from_dict(_item) for _item in obj["table_content"]] if obj.get("table_content") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj