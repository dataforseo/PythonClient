from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.keyword_data_info import KeywordDataInfo



class DataforseoLabsRelatedKeywordsLiveItem(BaseModel):
    """
    DataforseoLabsRelatedKeywordsLiveItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type. possible values: google")
    keyword_data: Optional[KeywordDataInfo] = Field(default=None, description="keyword data for the returned keyword")
    depth: Optional[StrictInt] = Field(default=None, description="keyword search depth")
    related_keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="list of related keywords. represents the list of search queries which are related to the keyword returned in the array above")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "keyword_data", 
        "depth", 
        "related_keywords", 
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
        _dict['keyword_data'] = self.keyword_data.to_dict() if self.keyword_data else None
        _dict['depth'] = self.depth
        _dict['related_keywords'] = self.related_keywords
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "keyword_data": KeywordDataInfo.from_dict(obj["keyword_data"]) if obj.get("keyword_data") is not None else None,
            "depth": obj.get("depth"),
            "related_keywords": obj.get("related_keywords"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj