from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.licenses_element import LicensesElement



class RefinementChipsElement(BaseModel):
    """
    RefinementChipsElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="title of the element")
    url: Optional[StrictStr] = Field(default=None, description="search URL with refinement parameters")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    options: Optional[List[Optional[LicensesElement]]] = Field(default=None, description="further search refinement options")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "url", 
        "domain", 
        "options", 
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
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        options_items = []
        if self.options:
            for _item in self.options:
                if _item:
                    options_items.append(_item.to_dict())
            _dict['options'] = options_items
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
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "options": [LicensesElement.from_dict(_item) for _item in obj["options"]] if obj.get("options") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj