from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.table_content_item_info import TableContentItemInfo



class TableContentInfo(BaseModel):
    """
    TableContentInfo
    """ # noqa: E501
    header: Optional[List[Optional[TableContentItemInfo]]] = Field(default=None, description="parsed content of the header")
    body: Optional[List[Optional[TableContentItemInfo]]] = Field(default=None, description="content of the body of the table")
    footer: Optional[List[Optional[TableContentItemInfo]]] = Field(default=None, description="content of the footer of the table")
    __properties: ClassVar[List[str]] = [
        "header", 
        "body", 
        "footer", 
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

        header_items = []
        if self.header:
            for _item in self.header:
                if _item:
                    header_items.append(_item.to_dict())
            _dict['header'] = header_items
        body_items = []
        if self.body:
            for _item in self.body:
                if _item:
                    body_items.append(_item.to_dict())
            _dict['body'] = body_items
        footer_items = []
        if self.footer:
            for _item in self.footer:
                if _item:
                    footer_items.append(_item.to_dict())
            _dict['footer'] = footer_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "header": [TableContentItemInfo.from_dict(_item) for _item in obj["header"]] if obj.get("header") is not None else None,
            "body": [TableContentItemInfo.from_dict(_item) for _item in obj["body"]] if obj.get("body") is not None else None,
            "footer": [TableContentItemInfo.from_dict(_item) for _item in obj["footer"]] if obj.get("footer") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj