from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.app_metrics_info import AppMetricsInfo



class DataforseoLabsleAppCompetitorsLiveItem(BaseModel):
    """
    DataforseoLabsleAppCompetitorsLiveItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    app_id: Optional[StrictStr] = Field(default=None, description="id of the competitor app")
    avg_position: Optional[StrictFloat] = Field(default=None, description="average position of the app in Google Play SERP. Note: average position is calculated for intersected keywords only;. the value for a given application may differ when combined with different target applications")
    sum_position: Optional[StrictInt] = Field(default=None, description="sum of all app positions in Google Play SERP. Note: sum position is calculated for intersected keywords only;. the value for a given application may differ when combined with different target applications")
    intersections: Optional[StrictInt] = Field(default=None, description="number of intersecting keywords")
    competitor_metrics: Optional[Dict[str, Optional[AppMetricsInfo]]] = Field(default=None, description="metrics for intersecting keywords. ranking data relevant to the keywords that the provided competitor application shares with the app in a POST request;. note: in this array ranking data is provided for the returned competitor’s app_id")
    full_metrics: Optional[Dict[str, Optional[AppMetricsInfo]]] = Field(default=None, description="metrics for all keywords of the application. full overview of ranking data relevant to all keywords that the provided app_id is ranking for")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "app_id", 
        "avg_position", 
        "sum_position", 
        "intersections", 
        "competitor_metrics", 
        "full_metrics", 
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

        _dict['se_type'] = self.se_type
        _dict['app_id'] = self.app_id
        _dict['avg_position'] = self.avg_position
        _dict['sum_position'] = self.sum_position
        _dict['intersections'] = self.intersections
        _dict['competitor_metrics'] = self.competitor_metrics
        _dict['full_metrics'] = self.full_metrics
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "app_id": obj.get("app_id"),
            "avg_position": obj.get("avg_position"),
            "sum_position": obj.get("sum_position"),
            "intersections": obj.get("intersections"),
            "competitor_metrics": obj.get("competitor_metrics"),
            "full_metrics": obj.get("full_metrics"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj