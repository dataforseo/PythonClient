from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ResultAvailableLanguages(BaseModel):
    """
    ResultAvailableLanguages
    """ # noqa: E501
    available_platforms: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"supported LLM platforms. contains the sources of data supported for a specific location and language combination. only google and chat_gpt are currently available")
    language_name: Optional[StrictStr] = Field(default=None, description=r"language name")
    language_code: Optional[StrictStr] = Field(default=None, description=r"language code according to ISO 639-1")
    responses_count: Optional[StrictInt] = Field(default=None, description=r"number of LLM responses. the number of LLM responses available in the database for the certain location and language parameters")
    __properties: ClassVar[List[str]] = [
        "available_platforms", 
        "language_name", 
        "language_code", 
        "responses_count", 
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

        _dict['available_platforms'] = self.available_platforms
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['responses_count'] = self.responses_count
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "available_platforms": obj.get("available_platforms"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "responses_count": obj.get("responses_count"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj