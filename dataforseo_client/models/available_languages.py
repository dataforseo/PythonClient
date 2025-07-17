from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AvailableLanguages(BaseModel):
    """
    AvailableLanguages
    """ # noqa: E501
    available_sources: Optional[List[Optional[StrictStr]]] = Field(default=None, description="supported sources. contains the sources of data supported for a specific location and language combination. only google and bing are currently available")
    language_name: Optional[StrictStr] = Field(default=None, description="language name")
    language_code: Optional[StrictStr] = Field(default=None, description="language code according to ISO 639-1")
    keywords: Optional[StrictInt] = Field(default=None, description="the number of keywords available for the given location and language")
    serps: Optional[StrictInt] = Field(default=None, description="the number of SERP pages available for the given location and language")
    __properties: ClassVar[List[str]] = [
        "available_sources", 
        "language_name", 
        "language_code", 
        "keywords", 
        "serps", 
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

        _dict['available_sources'] = self.available_sources
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['keywords'] = self.keywords
        _dict['serps'] = self.serps
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "available_sources": obj.get("available_sources"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "keywords": obj.get("keywords"),
            "serps": obj.get("serps"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj