from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_limits_rates_data import AppendixLimitsRatesData
from dataforseo_client.models.appendix_statistics_data_info import AppendixStatisticsDataInfo



class AppendixRatesData(BaseModel):
    """
    AppendixRatesData
    """ # noqa: E501
    limits: Optional[AppendixLimitsRatesData] = Field(default=None, description="rate limits for API calls per a certain period of time")
    statistics: Optional[AppendixStatisticsDataInfo] = Field(default=None, description="statisctics for API calls")
    __properties: ClassVar[List[str]] = [
        "limits", 
        "statistics", 
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

        _dict['limits'] = self.limits.to_dict() if self.limits else None
        _dict['statistics'] = self.statistics.to_dict() if self.statistics else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "limits": AppendixLimitsRatesData.from_dict(obj["limits"]) if obj.get("limits") is not None else None,
            "statistics": AppendixStatisticsDataInfo.from_dict(obj["statistics"]) if obj.get("statistics") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj