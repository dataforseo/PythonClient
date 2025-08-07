from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AiModeRectangleInfo(BaseModel):
    """
    AiModeRectangleInfo
    """ # noqa: E501
    x: Optional[StrictFloat] = Field(default=None, description="x-axis coordinate. x-axis coordinate of the top-left corner of the result’s snippet, where top-left corner of the screen is the origin")
    y: Optional[StrictFloat] = Field(default=None, description="y-axis coordinate. y-axis coordinate of the top-left corner of the result’s snippet, where top-left corner of the screen is the origin")
    width: Optional[StrictFloat] = Field(default=None, description="width of the element in pixels")
    height: Optional[StrictFloat] = Field(default=None, description="height of the element in pixels")
    __properties: ClassVar[List[str]] = [
        "x", 
        "y", 
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

        _dict['x'] = self.x
        _dict['y'] = self.y
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
            "x": obj.get("x"),
            "y": obj.get("y"),
            "width": obj.get("width"),
            "height": obj.get("height"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj