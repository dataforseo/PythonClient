from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.content_url_info import ContentUrlInfo



class SectionContentItemInfo(BaseModel):
    """
    SectionContentItemInfo
    """ # noqa: E501
    text: Optional[StrictStr] = Field(default=None, description="secondary content on the page. you can find more information about content priority calculation in this help center article")
    url: Optional[StrictStr] = Field(default=None, description="page URL.. displayed in case the text is a link anchor")
    urls: Optional[List[Optional[ContentUrlInfo]]] = Field(default=None, description="contains other URLs and anchors found in the content element")
    __properties: ClassVar[List[str]] = [
        "text", 
        "url", 
        "urls", 
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
        _dict['url'] = self.url
        urls_items = []
        if self.urls:
            for _item in self.urls:
                if _item:
                    urls_items.append(_item.to_dict())
            _dict['urls'] = urls_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "text": obj.get("text"),
            "url": obj.get("url"),
            "urls": [ContentUrlInfo.from_dict(_item) for _item in obj["urls"]] if obj.get("urls") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj