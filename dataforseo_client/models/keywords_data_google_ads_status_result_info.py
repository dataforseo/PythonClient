from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class KeywordsDataGoogleAdsStatusResultInfo(BaseModel):
    """
    KeywordsDataGoogleAdsStatusResultInfo
    """ # noqa: E501
    actual_data: Optional[StrictBool] = Field(default=None, description="indicates whether Google updated keyword data for the previous month. generally, Google updates keyword data in the middle of the month. if the value is true, Google currently provides up-to-date data for the previous month. if the value is false, we are not able to provide data for the previous month")
    date_update: Optional[StrictStr] = Field(default=None, description="date of the latest update of Google Ads data. indicates the latest date when Google updated search volume, CPC, and other keyword metrics. example:. 2020-05-15")
    last_year_in_monthly_searches: Optional[StrictInt] = Field(default=None, description="the latest year for which search volume data is available")
    last_month_in_monthly_searches: Optional[StrictInt] = Field(default=None, description="the latest month for which search volume data is available")
    __properties: ClassVar[List[str]] = [
        "actual_data", 
        "date_update", 
        "last_year_in_monthly_searches", 
        "last_month_in_monthly_searches", 
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

        _dict['actual_data'] = self.actual_data
        _dict['date_update'] = self.date_update
        _dict['last_year_in_monthly_searches'] = self.last_year_in_monthly_searches
        _dict['last_month_in_monthly_searches'] = self.last_month_in_monthly_searches
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actual_data": obj.get("actual_data"),
            "date_update": obj.get("date_update"),
            "last_year_in_monthly_searches": obj.get("last_year_in_monthly_searches"),
            "last_month_in_monthly_searches": obj.get("last_month_in_monthly_searches"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj