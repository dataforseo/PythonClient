from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BulkMetricsInfo(BaseModel):
    """
    BulkMetricsInfo
    """ # noqa: E501
    etv: Optional[StrictFloat] = Field(default=None, description="estimated traffic volume. estimated organic monthly traffic to the domain. calculated as the product of CTR (click-through-rate) and search volume values of all keywords the domain ranks for. learn more about how the metric is calculated in this help center article")
    count: Optional[StrictInt] = Field(default=None, description="total count of organic SERPs that contain the domain")
    __properties: ClassVar[List[str]] = [
        "etv", 
        "count", 
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

        _dict['etv'] = self.etv
        _dict['count'] = self.count
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "etv": obj.get("etv"),
            "count": obj.get("count"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj