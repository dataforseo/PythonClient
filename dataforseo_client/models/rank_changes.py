from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class RankChanges(BaseModel):
    """
    RankChanges
    """ # noqa: E501
    previous_rank_absolute: Optional[StrictInt] = Field(default=None, description="previous absolute rank in SERP. indicates previous rank of the element in Google SERP;. if this element is new, the value will be null")
    is_new: Optional[StrictBool] = Field(default=None, description="element was previously present in SERP. if the value is true, previously collected SERP didn’t contain this element")
    is_up: Optional[StrictBool] = Field(default=None, description="rank of this element went up. if the value is true, position of the element in SERP is higher compared to the previous check")
    is_down: Optional[StrictBool] = Field(default=None, description="rank of this element went down. if the value is true, position of the element in SERP is lower compared to the previous check")
    __properties: ClassVar[List[str]] = [
        "previous_rank_absolute", 
        "is_new", 
        "is_up", 
        "is_down", 
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

        _dict['previous_rank_absolute'] = self.previous_rank_absolute
        _dict['is_new'] = self.is_new
        _dict['is_up'] = self.is_up
        _dict['is_down'] = self.is_down
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "previous_rank_absolute": obj.get("previous_rank_absolute"),
            "is_new": obj.get("is_new"),
            "is_up": obj.get("is_up"),
            "is_down": obj.get("is_down"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj