from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ChatGptBrandEntity(BaseModel):
    """
    ChatGptBrandEntity
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    title: Optional[StrictStr] = Field(default=None, description=r"name of the brand")
    category: Optional[StrictStr] = Field(default=None, description=r"category of the brand")
    markdown: Optional[StrictStr] = Field(default=None, description=r"brand name in markdown format. contains brand name formatted in the markdown markup language")
    urls: Optional[Any] = Field(default=None, description=r"array of URLs and domains relevant to the brand")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "category", 
        "markdown", 
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

        _dict['type'] = self.type
        _dict['title'] = self.title
        _dict['category'] = self.category
        _dict['markdown'] = self.markdown
        _dict['urls'] = self.urls
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
            "category": obj.get("category"),
            "markdown": obj.get("markdown"),
            "urls": obj.get("urls"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj