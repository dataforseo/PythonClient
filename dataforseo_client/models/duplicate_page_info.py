from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.on_page_html_resource_item import OnPageHtmlResourceItem



class DuplicatePageInfo(BaseModel):
    """
    DuplicatePageInfo
    """ # noqa: E501
    similarity: Optional[StrictInt] = Field(default=None, description="content similarity score. by default, the content is considered duplicate if the value is greater than or equals 6. can take values from 0 to 10")
    page: Optional[List[Optional[OnPageHtmlResourceItem]]] = Field(default=None, description="information about the page with duplicate content")
    __properties: ClassVar[List[str]] = [
        "similarity", 
        "page", 
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

        _dict['similarity'] = self.similarity
        page_items = []
        if self.page:
            for _item in self.page:
                if _item:
                    page_items.append(_item.to_dict())
            _dict['page'] = page_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "similarity": obj.get("similarity"),
            "page": [OnPageHtmlResourceItem.from_dict(_item) for _item in obj["page"]] if obj.get("page") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj