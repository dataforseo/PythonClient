from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpApiStopCrawlOnMatchInfo(BaseModel):
    """
    SerpApiStopCrawlOnMatchInfo
    """ # noqa: E501
    match_value: Optional[StrictStr] = Field(default=None, description=r"arget domain or wildcard value. required field if stop_crawl_on_match is specified;. specify a target domain or wildcard value;. Note: domain name must be specified without a request protocol;. example: dataforseo.com")
    match_type: Optional[StrictStr] = Field(default=None, description=r"target match type. required field if stop_crawl_on_match is specified;. type of match for the match_value. possible values: domain, with_subdomains, wildcard")
    __properties: ClassVar[List[str]] = [
        "match_value", 
        "match_type", 
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

        _dict['match_value'] = self.match_value
        _dict['match_type'] = self.match_type
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "match_value": obj.get("match_value"),
            "match_type": obj.get("match_type"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj