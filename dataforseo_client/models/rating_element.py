from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class RatingElement(BaseModel):
    """
    RatingElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in Google Shopping SERP. possible values:. left, right")
    rating_type: Optional[StrictStr] = Field(default=None, description="the type of rating. here you can find the following elements: Max5, Percents, CustomMax")
    value: Optional[StrictFloat] = Field(default=None, description="value of the rating")
    votes_count: Optional[StrictInt] = Field(default=None, description="the amount of feedback")
    rating_max: Optional[StrictFloat] = Field(default=None, description="the maximum value for a rating_type")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "rating_type", 
        "value", 
        "votes_count", 
        "rating_max", 
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

        _dict['type'] = self.type
        _dict['position'] = self.position
        _dict['rating_type'] = self.rating_type
        _dict['value'] = self.value
        _dict['votes_count'] = self.votes_count
        _dict['rating_max'] = self.rating_max
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "position": obj.get("position"),
            "rating_type": obj.get("rating_type"),
            "value": obj.get("value"),
            "votes_count": obj.get("votes_count"),
            "rating_max": obj.get("rating_max"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj