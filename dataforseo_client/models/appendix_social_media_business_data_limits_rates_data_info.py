from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_info import AppendixInfo



class AppendixSocialMediaBusinessDataLimitsRatesDataInfo(BaseModel):
    """
    AppendixSocialMediaBusinessDataLimitsRatesDataInfo
    """ # noqa: E501
    facebook: Optional[AppendixInfo] = Field(default=None, description="")
    pinterest: Optional[AppendixInfo] = Field(default=None, description="")
    reddit: Optional[AppendixInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "facebook", 
        "pinterest", 
        "reddit", 
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

        _dict['facebook'] = self.facebook.to_dict() if self.facebook else None
        _dict['pinterest'] = self.pinterest.to_dict() if self.pinterest else None
        _dict['reddit'] = self.reddit.to_dict() if self.reddit else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "facebook": AppendixInfo.from_dict(obj["facebook"]) if obj.get("facebook") is not None else None,
            "pinterest": AppendixInfo.from_dict(obj["pinterest"]) if obj.get("pinterest") is not None else None,
            "reddit": AppendixInfo.from_dict(obj["reddit"]) if obj.get("reddit") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj