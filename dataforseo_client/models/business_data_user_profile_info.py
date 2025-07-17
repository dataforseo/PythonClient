from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BusinessDataUserProfileInfo(BaseModel):
    """
    BusinessDataUserProfileInfo
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="the name of the reviewer")
    url: Optional[StrictStr] = Field(default=None, description="URL to the reviewer’s profile")
    image_url: Optional[StrictStr] = Field(default=None, description="URL to the reviewer’s profile picture")
    location: Optional[StrictStr] = Field(default=None, description="country of the reviewer")
    reviews_count: Optional[StrictInt] = Field(default=None, description="total number of reviews submitted by the reviewer")
    __properties: ClassVar[List[str]] = [
        "name", 
        "url", 
        "image_url", 
        "location", 
        "reviews_count", 
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
        _dict['url'] = self.url
        _dict['image_url'] = self.image_url
        _dict['location'] = self.location
        _dict['reviews_count'] = self.reviews_count
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "url": obj.get("url"),
            "image_url": obj.get("image_url"),
            "location": obj.get("location"),
            "reviews_count": obj.get("reviews_count"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj