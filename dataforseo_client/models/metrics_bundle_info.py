from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.metrics_info import MetricsInfo



class MetricsBundleInfo(BaseModel):
    """
    MetricsBundleInfo
    """ # noqa: E501
    organic: Optional[MetricsInfo] = Field(default=None, description="ranking and traffic data from organic search")
    paid: Optional[MetricsInfo] = Field(default=None, description="ranking and traffic data from paid search")
    __properties: ClassVar[List[str]] = [
        "organic", 
        "paid", 
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

        _dict['organic'] = self.organic.to_dict() if self.organic else None
        _dict['paid'] = self.paid.to_dict() if self.paid else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "organic": MetricsInfo.from_dict(obj["organic"]) if obj.get("organic") is not None else None,
            "paid": MetricsInfo.from_dict(obj["paid"]) if obj.get("paid") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj