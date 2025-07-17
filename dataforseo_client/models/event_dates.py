from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class EventDates(BaseModel):
    """
    EventDates
    """ # noqa: E501
    start_datetime: Optional[StrictStr] = Field(default=None, description="date and time when the event starts. if time zone is specified in the event, value will be returned in the UTC format:. “yyyy-mm-ddThh-mm-ss+00:00”. example:. 2019-11-15T12:57:46+00:00. if time zone is not specified in the event, unspecified local time will be returned in the following format:. “yyyy-mm-ddThh-mm-ss”. example:. 2019-11-15T12:57:46")
    end_datetime: Optional[StrictStr] = Field(default=None, description="date and time when the event ends. if time zone is specified in the event, value will be returned in the UTC format:. “yyyy-mm-ddThh-mm-ss+00:00”. example:. 2019-11-15T12:57:46+00:00. if time zone is not specified in the event, unspecified local time will be returned in the following format:. “yyyy-mm-ddThh-mm-ss”. example:. 2019-11-15T12:57:46")
    displayed_dates: Optional[StrictStr] = Field(default=None, description="date or date range as it is displayed in SERP")
    __properties: ClassVar[List[str]] = [
        "start_datetime", 
        "end_datetime", 
        "displayed_dates", 
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

        _dict['start_datetime'] = self.start_datetime
        _dict['end_datetime'] = self.end_datetime
        _dict['displayed_dates'] = self.displayed_dates
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "start_datetime": obj.get("start_datetime"),
            "end_datetime": obj.get("end_datetime"),
            "displayed_dates": obj.get("displayed_dates"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj