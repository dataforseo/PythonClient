from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsBulkKeywordDifficultyLiveItem(BaseModel):
    """
    DataforseoLabsBulkKeywordDifficultyLiveItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    keyword: Optional[StrictStr] = Field(default=None, description="keyword in a POST array")
    keyword_difficulty: Optional[StrictInt] = Field(default=None, description="difficulty of ranking in the first top-10 organic results for a keyword. indicates the chance of getting in top-10 organic results for a keyword on a logarithmic scale from 0 to 100;. calculated by analysing, among other parameters, link profiles of the first 10 pages in SERP;. learn more about the metric in this help center guide")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "keyword", 
        "keyword_difficulty", 
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

        _dict['se_type'] = self.se_type
        _dict['keyword'] = self.keyword
        _dict['keyword_difficulty'] = self.keyword_difficulty
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "keyword": obj.get("keyword"),
            "keyword_difficulty": obj.get("keyword_difficulty"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj