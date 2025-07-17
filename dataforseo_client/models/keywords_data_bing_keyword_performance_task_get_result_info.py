from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.keyword_kpi import KeywordKpi



class KeywordsDataBingKeywordPerformanceTaskGetResultInfo(BaseModel):
    """
    KeywordsDataBingKeywordPerformanceTaskGetResultInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword in a POST array")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array. if there is no data, then the value is null")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array. if there is no data, then the value is null")
    year: Optional[StrictInt] = Field(default=None, description="indicates the year for which the data is provided for. example:. 2020")
    month: Optional[StrictInt] = Field(default=None, description="indicates the month for which the data is provided for. example:. 10")
    keyword_kpi: Optional[KeywordKpi] = Field(default=None, description="object containing keyword metrics. if there is no data, then the value is null")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_code", 
        "language_code", 
        "year", 
        "month", 
        "keyword_kpi", 
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

        _dict['keyword'] = self.keyword
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['year'] = self.year
        _dict['month'] = self.month
        _dict['keyword_kpi'] = self.keyword_kpi.to_dict() if self.keyword_kpi else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "year": obj.get("year"),
            "month": obj.get("month"),
            "keyword_kpi": KeywordKpi.from_dict(obj["keyword_kpi"]) if obj.get("keyword_kpi") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj