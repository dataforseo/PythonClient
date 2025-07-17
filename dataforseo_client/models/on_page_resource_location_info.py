from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class OnPageResourceLocationInfo(BaseModel):
    """
    OnPageResourceLocationInfo
    """ # noqa: E501
    line: Optional[StrictInt] = Field(default=None, description="line number. the number of the line on which the resource is located")
    offset_left: Optional[StrictInt] = Field(default=None, description="position in line. the number of line characters before the resource;. sometimes referred to as column. Note: counts from 1, i.e. if the resource doesn’t have any characters to the left, the value will be 1")
    offset_top: Optional[StrictInt] = Field(default=None, description="position in the document. the total number of characters between the resource and the top of HTML")
    __properties: ClassVar[List[str]] = [
        "line", 
        "offset_left", 
        "offset_top", 
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

        _dict['line'] = self.line
        _dict['offset_left'] = self.offset_left
        _dict['offset_top'] = self.offset_top
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "line": obj.get("line"),
            "offset_left": obj.get("offset_left"),
            "offset_top": obj.get("offset_top"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj