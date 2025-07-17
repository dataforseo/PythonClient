from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.serp_api_carousel_element import SerpApiCarouselElement



class MultiCarouselElement(BaseModel):
    """
    MultiCarouselElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="title of a given link element")
    multi_carousel_snippets: Optional[List[Optional[SerpApiCarouselElement]]] = Field(default=None, description="multi_carousel_snippet results")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "multi_carousel_snippets", 
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
        multi_carousel_snippets_items = []
        if self.multi_carousel_snippets:
            for _item in self.multi_carousel_snippets:
                if _item:
                    multi_carousel_snippets_items.append(_item.to_dict())
            _dict['multi_carousel_snippets'] = multi_carousel_snippets_items
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
            "multi_carousel_snippets": [SerpApiCarouselElement.from_dict(_item) for _item in obj["multi_carousel_snippets"]] if obj.get("multi_carousel_snippets") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj