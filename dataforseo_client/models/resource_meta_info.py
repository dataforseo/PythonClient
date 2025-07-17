from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ResourceMetaInfo(BaseModel):
    """
    ResourceMetaInfo
    """ # noqa: E501
    alternative_text: Optional[StrictStr] = Field(default=None, description="content of the image alt attribute")
    title: Optional[StrictStr] = Field(default=None, description="title")
    original_width: Optional[StrictFloat] = Field(default=None, description="original image width in px")
    original_height: Optional[StrictFloat] = Field(default=None, description="original image height in px")
    width: Optional[StrictFloat] = Field(default=None, description="image width in px")
    height: Optional[StrictFloat] = Field(default=None, description="image height in px")
    __properties: ClassVar[List[str]] = [
        "alternative_text", 
        "title", 
        "original_width", 
        "original_height", 
        "width", 
        "height", 
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

        _dict['alternative_text'] = self.alternative_text
        _dict['title'] = self.title
        _dict['original_width'] = self.original_width
        _dict['original_height'] = self.original_height
        _dict['width'] = self.width
        _dict['height'] = self.height
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alternative_text": obj.get("alternative_text"),
            "title": obj.get("title"),
            "original_width": obj.get("original_width"),
            "original_height": obj.get("original_height"),
            "width": obj.get("width"),
            "height": obj.get("height"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj