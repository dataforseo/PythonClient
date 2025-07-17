from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_limits_money_data import AppendixLimitsMoneyData
from dataforseo_client.models.appendix_statistics_data_info import AppendixStatisticsDataInfo



class AppendixMoneyData(BaseModel):
    """
    AppendixMoneyData
    """ # noqa: E501
    total: Optional[StrictFloat] = Field(default=None, description="total amount of money deposited to your account")
    balance: Optional[StrictFloat] = Field(default=None, description="amount of money left in your account")
    limits: Optional[AppendixLimitsMoneyData] = Field(default=None, description="cost limits")
    statistics: Optional[AppendixStatisticsDataInfo] = Field(default=None, description="statistics of your spending")
    __properties: ClassVar[List[str]] = [
        "total", 
        "balance", 
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

        _dict['total'] = self.total
        _dict['balance'] = self.balance
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
            "total": obj.get("total"),
            "balance": obj.get("balance"),
            "limits": AppendixLimitsMoneyData.from_dict(obj["limits"]) if obj.get("limits") is not None else None,
            "statistics": AppendixStatisticsDataInfo.from_dict(obj["statistics"]) if obj.get("statistics") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj