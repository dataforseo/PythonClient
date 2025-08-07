from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ContentRatingInfo(BaseModel):
    """
    ContentRatingInfo
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="rating name. here you can find the following elements: Max5, Percents, CustomMax")
    rating_value: Optional[StrictFloat] = Field(default=None, description="the value of the rating")
    rating_count: Optional[StrictFloat] = Field(default=None, description="number of votes")
    max_rating_value: Optional[StrictFloat] = Field(default=None, description="maximum value for the rating name")
    relative_rating: Optional[StrictFloat] = Field(default=None, description="relative rating")
    __properties: ClassVar[List[str]] = [
        "name", 
        "rating_value", 
        "rating_count", 
        "max_rating_value", 
        "relative_rating", 
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

        _dict['name'] = self.name
        _dict['rating_value'] = self.rating_value
        _dict['rating_count'] = self.rating_count
        _dict['max_rating_value'] = self.max_rating_value
        _dict['relative_rating'] = self.relative_rating
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "rating_value": obj.get("rating_value"),
            "rating_count": obj.get("rating_count"),
            "max_rating_value": obj.get("max_rating_value"),
            "relative_rating": obj.get("relative_rating"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj