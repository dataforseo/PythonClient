from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AmazonKeywordInfo(BaseModel):
    """
    AmazonKeywordInfo
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    last_updated_time: Optional[StrictStr] = Field(default=None, description="date and time when keyword data was updated. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:    '2019-11-15 12:57:46 +00:00'")
    search_volume: Optional[StrictInt] = Field(default=None, description="average monthly search volume rate. represents the (approximate) number of searches for the provided keyword idea on Amazon")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "last_updated_time", 
        "search_volume", 
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
        _dict['last_updated_time'] = self.last_updated_time
        _dict['search_volume'] = self.search_volume
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "last_updated_time": obj.get("last_updated_time"),
            "search_volume": obj.get("search_volume"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj