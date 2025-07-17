from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ReviewMentionInfo(BaseModel):
    """
    ReviewMentionInfo
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description="title of the evaluated criterion")
    positive_score: Optional[StrictFloat] = Field(default=None, description="positive score by criterion")
    positive_count: Optional[StrictInt] = Field(default=None, description="count of positive reviews by criterion")
    negative_count: Optional[StrictInt] = Field(default=None, description="count of negative reviews by criterion")
    total_count: Optional[StrictInt] = Field(default=None, description="count of all reviews by criterion")
    visible_by_default: Optional[StrictBool] = Field(default=None, description="element is visible by default. indicates whether the review element is visible by default")
    __properties: ClassVar[List[str]] = [
        "title", 
        "positive_score", 
        "positive_count", 
        "negative_count", 
        "total_count", 
        "visible_by_default", 
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

        _dict['title'] = self.title
        _dict['positive_score'] = self.positive_score
        _dict['positive_count'] = self.positive_count
        _dict['negative_count'] = self.negative_count
        _dict['total_count'] = self.total_count
        _dict['visible_by_default'] = self.visible_by_default
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "positive_score": obj.get("positive_score"),
            "positive_count": obj.get("positive_count"),
            "negative_count": obj.get("negative_count"),
            "total_count": obj.get("total_count"),
            "visible_by_default": obj.get("visible_by_default"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj