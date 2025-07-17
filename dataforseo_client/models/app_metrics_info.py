from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AppMetricsInfo(BaseModel):
    """
    AppMetricsInfo
    """ # noqa: E501
    pos_1: Optional[StrictInt] = Field(default=None, description="number of organic SERPs where the product ranks #1")
    pos_2_3: Optional[StrictInt] = Field(default=None, description="number of organic SERPs where the product ranks #2-3")
    pos_4_10: Optional[StrictInt] = Field(default=None, description="number of organic SERPs where the product ranks #4-10")
    pos_11_100: Optional[StrictInt] = Field(default=None, description="number of organic SERPs where the product ranks #11-100")
    count: Optional[StrictInt] = Field(default=None, description="total count of Amazon organic SERPs that contain the product")
    search_volume: Optional[StrictInt] = Field(default=None, description="total search volume of the product’s ranking keywords in organic SERP")
    __properties: ClassVar[List[str]] = [
        "pos_1", 
        "pos_2_3", 
        "pos_4_10", 
        "pos_11_100", 
        "count", 
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

        _dict['pos_1'] = self.pos_1
        _dict['pos_2_3'] = self.pos_2_3
        _dict['pos_4_10'] = self.pos_4_10
        _dict['pos_11_100'] = self.pos_11_100
        _dict['count'] = self.count
        _dict['search_volume'] = self.search_volume
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pos_1": obj.get("pos_1"),
            "pos_2_3": obj.get("pos_2_3"),
            "pos_4_10": obj.get("pos_4_10"),
            "pos_11_100": obj.get("pos_11_100"),
            "count": obj.get("count"),
            "search_volume": obj.get("search_volume"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj