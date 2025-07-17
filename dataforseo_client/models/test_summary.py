from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class TestSummary(BaseModel):
    """
    TestSummary
    """ # noqa: E501
    fatal: Optional[StrictInt] = Field(default=None, description="number of fatal microdata errors")
    error: Optional[StrictInt] = Field(default=None, description="number of serious microdata errors")
    warning: Optional[StrictInt] = Field(default=None, description="number of microdata warnings")
    info: Optional[StrictInt] = Field(default=None, description="number of microdata information flags")
    __properties: ClassVar[List[str]] = [
        "fatal", 
        "error", 
        "warning", 
        "info", 
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

        _dict['fatal'] = self.fatal
        _dict['error'] = self.error
        _dict['warning'] = self.warning
        _dict['info'] = self.info
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "fatal": obj.get("fatal"),
            "error": obj.get("error"),
            "warning": obj.get("warning"),
            "info": obj.get("info"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj