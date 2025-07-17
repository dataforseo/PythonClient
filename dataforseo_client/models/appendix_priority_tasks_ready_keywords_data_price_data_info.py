from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AppendixPriorityTasksReadyKeywordsDataPriceDataInfo(BaseModel):
    """
    AppendixPriorityTasksReadyKeywordsDataPriceDataInfo
    """ # noqa: E501
    cost_type: Optional[StrictStr] = Field(default=None, description="charge type. can take the following values:. per_result – charge for every row in the result array. per_request – charge for a GET or POST request")
    cost: Optional[StrictFloat] = Field(default=None, description="cost, USD")
    __properties: ClassVar[List[str]] = [
        "cost_type", 
        "cost", 
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

        _dict['cost_type'] = self.cost_type
        _dict['cost'] = self.cost
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cost_type": obj.get("cost_type"),
            "cost": obj.get("cost"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj