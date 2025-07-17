from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.time_info import TimeInfo



class PopularWorkTimeInfo(BaseModel):
    """
    PopularWorkTimeInfo
    """ # noqa: E501
    time: Optional[TimeInfo] = Field(default=None, description="hours in the 24-hour format")
    popular_index: Optional[StrictInt] = Field(default=None, description="popularity index. relative time-bound popularity index measured from 0 to 100;. higher value corresponds to a busier time of a day")
    __properties: ClassVar[List[str]] = [
        "time", 
        "popular_index", 
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

        _dict['time'] = self.time.to_dict() if self.time else None
        _dict['popular_index'] = self.popular_index
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "time": TimeInfo.from_dict(obj["time"]) if obj.get("time") is not None else None,
            "popular_index": obj.get("popular_index"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj