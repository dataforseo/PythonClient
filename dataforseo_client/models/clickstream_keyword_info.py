from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.monthly_searches_info import MonthlySearchesInfo



class ClickstreamKeywordInfo(BaseModel):
    """
    ClickstreamKeywordInfo
    """ # noqa: E501
    search_volume: Optional[StrictInt] = Field(default=None, description="current search volume rate of a keyword")
    last_updated_time: Optional[StrictStr] = Field(default=None, description="date and time when backlink data was updated. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    gender_distribution: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="distribution of estimated clickstream-based metrics by gender. learn more about how the metric is calculated in this help center article")
    age_distribution: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="distribution of clickstream-based metrics by age. learn more about how the metric is calculated in this help center article")
    monthly_searches: Optional[List[Optional[MonthlySearchesInfo]]] = Field(default=None, description="monthly searches. represents the (approximate) number of searches on this keyword idea (as available for the past twelve months), targeted to the specified geographic locations")
    __properties: ClassVar[List[str]] = [
        "search_volume", 
        "last_updated_time", 
        "gender_distribution", 
        "age_distribution", 
        "monthly_searches", 
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

        _dict['search_volume'] = self.search_volume
        _dict['last_updated_time'] = self.last_updated_time
        _dict['gender_distribution'] = self.gender_distribution
        _dict['age_distribution'] = self.age_distribution
        monthly_searches_items = []
        if self.monthly_searches:
            for _item in self.monthly_searches:
                if _item:
                    monthly_searches_items.append(_item.to_dict())
            _dict['monthly_searches'] = monthly_searches_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "search_volume": obj.get("search_volume"),
            "last_updated_time": obj.get("last_updated_time"),
            "gender_distribution": obj.get("gender_distribution"),
            "age_distribution": obj.get("age_distribution"),
            "monthly_searches": [MonthlySearchesInfo.from_dict(_item) for _item in obj["monthly_searches"]] if obj.get("monthly_searches") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj