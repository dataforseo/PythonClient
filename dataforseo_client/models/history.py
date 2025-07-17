from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.keyword_info import KeywordInfo



class History(BaseModel):
    """
    History
    """ # noqa: E501
    year: Optional[StrictInt] = Field(default=None, description="year")
    month: Optional[StrictInt] = Field(default=None, description="month")
    keyword_info: Optional[KeywordInfo] = Field(default=None, description="historical data for the keyword")
    __properties: ClassVar[List[str]] = [
        "year", 
        "month", 
        "keyword_info", 
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

        _dict['year'] = self.year
        _dict['month'] = self.month
        _dict['keyword_info'] = self.keyword_info.to_dict() if self.keyword_info else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "year": obj.get("year"),
            "month": obj.get("month"),
            "keyword_info": KeywordInfo.from_dict(obj["keyword_info"]) if obj.get("keyword_info") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj