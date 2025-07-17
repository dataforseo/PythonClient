from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class Subtitles(BaseModel):
    """
    Subtitles
    """ # noqa: E501
    language: Optional[StrictStr] = Field(default=None, description="language of subtitles")
    is_translatable: Optional[StrictBool] = Field(default=None, description="defines if subtitles are translatable")
    is_auto_generated: Optional[StrictBool] = Field(default=None, description="defines if subtitles are auto generated")
    __properties: ClassVar[List[str]] = [
        "language", 
        "is_translatable", 
        "is_auto_generated", 
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

        _dict['language'] = self.language
        _dict['is_translatable'] = self.is_translatable
        _dict['is_auto_generated'] = self.is_auto_generated
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "language": obj.get("language"),
            "is_translatable": obj.get("is_translatable"),
            "is_auto_generated": obj.get("is_auto_generated"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj