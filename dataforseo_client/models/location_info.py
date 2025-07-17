from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class LocationInfo(BaseModel):
    """
    LocationInfo
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="name of the event’s venue")
    address: Optional[StrictStr] = Field(default=None, description="address of the event’s venue")
    url: Optional[StrictStr] = Field(default=None, description="search URL with refinement parameters")
    cid: Optional[StrictStr] = Field(default=None, description="google-defined client id. can be used with Google Reviews API to get a full list of reviews")
    feature_id: Optional[StrictStr] = Field(default=None, description="the unique identifier of the element in SERP")
    __properties: ClassVar[List[str]] = [
        "name", 
        "address", 
        "url", 
        "cid", 
        "feature_id", 
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
        _dict['address'] = self.address
        _dict['url'] = self.url
        _dict['cid'] = self.cid
        _dict['feature_id'] = self.feature_id
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "address": obj.get("address"),
            "url": obj.get("url"),
            "cid": obj.get("cid"),
            "feature_id": obj.get("feature_id"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj