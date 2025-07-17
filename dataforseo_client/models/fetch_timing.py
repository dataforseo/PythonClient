from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class FetchTiming(BaseModel):
    """
    FetchTiming
    """ # noqa: E501
    duration_time: Optional[StrictInt] = Field(default=None, description="indicates how many seconds it took to download a page")
    fetch_start: Optional[StrictInt] = Field(default=None, description="time to start downloading the HTML resource. the amount of time the browser needs to start downloading a page")
    fetch_end: Optional[StrictInt] = Field(default=None, description="time to complete downloading the HTML resource. the amount of time the browser needs to complete downloading a page")
    __properties: ClassVar[List[str]] = [
        "duration_time", 
        "fetch_start", 
        "fetch_end", 
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

        _dict['duration_time'] = self.duration_time
        _dict['fetch_start'] = self.fetch_start
        _dict['fetch_end'] = self.fetch_end
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "duration_time": obj.get("duration_time"),
            "fetch_start": obj.get("fetch_start"),
            "fetch_end": obj.get("fetch_end"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj