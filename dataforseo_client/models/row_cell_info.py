from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.content_url_info import ContentUrlInfo



class RowCellInfo(BaseModel):
    """
    RowCellInfo
    """ # noqa: E501
    text: Optional[StrictStr] = Field(default=None, description="content of the row cells of the header")
    urls: Optional[List[Optional[ContentUrlInfo]]] = Field(default=None, description="contains other URLs and anchors found in the content element")
    is_header: Optional[StrictBool] = Field(default=None, description="content of the row cells of the header")
    __properties: ClassVar[List[str]] = [
        "text", 
        "urls", 
        "is_header", 
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

        _dict['text'] = self.text
        urls_items = []
        if self.urls:
            for _item in self.urls:
                if _item:
                    urls_items.append(_item.to_dict())
            _dict['urls'] = urls_items
        _dict['is_header'] = self.is_header
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "text": obj.get("text"),
            "urls": [ContentUrlInfo.from_dict(_item) for _item in obj["urls"]] if obj.get("urls") is not None else None,
            "is_header": obj.get("is_header"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj