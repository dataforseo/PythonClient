from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.dataforseo_trends_data_info import DataforseoTrendsDataInfo



class Demography(BaseModel):
    """
    Demography
    """ # noqa: E501
    age: Optional[List[Optional[DataforseoTrendsDataInfo]]] = Field(default=None, description="distribution of keyword popularity by age")
    gender: Optional[List[Optional[DataforseoTrendsDataInfo]]] = Field(default=None, description="distribution of keyword popularity by gender")
    __properties: ClassVar[List[str]] = [
        "age", 
        "gender", 
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

        age_items = []
        if self.age:
            for _item in self.age:
                if _item:
                    age_items.append(_item.to_dict())
            _dict['age'] = age_items
        gender_items = []
        if self.gender:
            for _item in self.gender:
                if _item:
                    gender_items.append(_item.to_dict())
            _dict['gender'] = gender_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "age": [DataforseoTrendsDataInfo.from_dict(_item) for _item in obj["age"]] if obj.get("age") is not None else None,
            "gender": [DataforseoTrendsDataInfo.from_dict(_item) for _item in obj["gender"]] if obj.get("gender") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj