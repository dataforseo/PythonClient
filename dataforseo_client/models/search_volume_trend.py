from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SearchVolumeTrend(BaseModel):
    """
    SearchVolumeTrend
    """ # noqa: E501
    monthly: Optional[StrictInt] = Field(default=None, description="search volume change in percent compared to the previous month")
    quarterly: Optional[StrictInt] = Field(default=None, description="search volume change in percent compared to the previous quarter")
    yearly: Optional[StrictInt] = Field(default=None, description="search volume change in percent compared to the previous year")
    __properties: ClassVar[List[str]] = [
        "monthly", 
        "quarterly", 
        "yearly", 
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

        _dict['monthly'] = self.monthly
        _dict['quarterly'] = self.quarterly
        _dict['yearly'] = self.yearly
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "monthly": obj.get("monthly"),
            "quarterly": obj.get("quarterly"),
            "yearly": obj.get("yearly"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj