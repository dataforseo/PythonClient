from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class PeriodCovered(BaseModel):
    """
    PeriodCovered
    """ # noqa: E501
    start_date: Optional[StrictStr] = Field(default=None, description="date and time when the period starts. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2020-03-02 02:00:00 +00:00")
    end_date: Optional[StrictStr] = Field(default=None, description="date and time when the period ends. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2022-12-09 02:00:00 +00:00")
    displayed_date: Optional[StrictStr] = Field(default=None, description="period displayed in SERP. example:. Mar 2, 2020 - Dec 9, 2022")
    __properties: ClassVar[List[str]] = [
        "start_date", 
        "end_date", 
        "displayed_date", 
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

        _dict['start_date'] = self.start_date
        _dict['end_date'] = self.end_date
        _dict['displayed_date'] = self.displayed_date
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "start_date": obj.get("start_date"),
            "end_date": obj.get("end_date"),
            "displayed_date": obj.get("displayed_date"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj