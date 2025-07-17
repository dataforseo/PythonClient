from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class RankedKeywordsInfo(BaseModel):
    """
    RankedKeywordsInfo
    """ # noqa: E501
    page_from_keywords_count_top_3: Optional[StrictInt] = Field(default=None, description="number of keywords for which the page is ranked in top 3 search results")
    page_from_keywords_count_top_10: Optional[StrictInt] = Field(default=None, description="number of keywords for which the page is ranked in top 10 search results")
    page_from_keywords_count_top_100: Optional[StrictInt] = Field(default=None, description="number of keywords for which the page is ranked in top 100 search results")
    __properties: ClassVar[List[str]] = [
        "page_from_keywords_count_top_3", 
        "page_from_keywords_count_top_10", 
        "page_from_keywords_count_top_100", 
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

        _dict['page_from_keywords_count_top_3'] = self.page_from_keywords_count_top_3
        _dict['page_from_keywords_count_top_10'] = self.page_from_keywords_count_top_10
        _dict['page_from_keywords_count_top_100'] = self.page_from_keywords_count_top_100
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "page_from_keywords_count_top_3": obj.get("page_from_keywords_count_top_3"),
            "page_from_keywords_count_top_10": obj.get("page_from_keywords_count_top_10"),
            "page_from_keywords_count_top_100": obj.get("page_from_keywords_count_top_100"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj