from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class UserProfileInfo(BaseModel):
    """
    UserProfileInfo
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="the name of the reviewer")
    avatar: Optional[StrictStr] = Field(default=None, description="URL to the profile picture of the reviewer")
    url: Optional[StrictStr] = Field(default=None, description="relevant url")
    reviews_count: Optional[StrictInt] = Field(default=None, description="total number of reviews submitted by the reviewer")
    locations: Optional[StrictStr] = Field(default=None, description="country of the reviewer")
    __properties: ClassVar[List[str]] = [
        "name", 
        "avatar", 
        "url", 
        "reviews_count", 
        "locations", 
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
        _dict['avatar'] = self.avatar
        _dict['url'] = self.url
        _dict['reviews_count'] = self.reviews_count
        _dict['locations'] = self.locations
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "avatar": obj.get("avatar"),
            "url": obj.get("url"),
            "reviews_count": obj.get("reviews_count"),
            "locations": obj.get("locations"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj