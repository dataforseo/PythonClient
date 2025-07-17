from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.dataforseo_labs_metrics_info import DataforseoLabsMetricsInfo



class DataforseoLabsCompetitorsDomainLiveItem(BaseModel):
    """
    DataforseoLabsCompetitorsDomainLiveItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    domain: Optional[StrictStr] = Field(default=None, description="domain name")
    avg_position: Optional[StrictFloat] = Field(default=None, description="average position of the domain in SERP. Note: average position is calculated for intersected keywords only;. the value for a given domain may differ when combined with different target websites")
    sum_position: Optional[StrictInt] = Field(default=None, description="sum of all domain positions in SERP. Note: average position is calculated for intersected keywords only;. the value for a given domain may differ when combined with different target websites")
    intersections: Optional[StrictInt] = Field(default=None, description="number of intersecting keywords")
    full_domain_metrics: Optional[Dict[str, Optional[DataforseoLabsMetricsInfo]]] = Field(default=None, description="metrics for all keywords of the domain. full overview of ranking and traffic data relevant to all keywords that the provided domain is ranking for")
    metrics: Optional[Dict[str, Optional[DataforseoLabsMetricsInfo]]] = Field(default=None, description="metrics for intersecting keywords. ranking and traffic data relevant to the keywords that the provided domain shares with the target domain. note: in this array ranking and traffic data is provided for the target considering the keywords target shares in search with the competitor’s domain")
    competitor_metrics: Optional[Dict[str, Optional[DataforseoLabsMetricsInfo]]] = Field(default=None, description="metrics for intersecting keywords. ranking and traffic data relevant to the keywords that the provided domain shares with the target domain. note: in this array ranking and traffic data is provided for the returned competitor’s domain")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "domain", 
        "avg_position", 
        "sum_position", 
        "intersections", 
        "full_domain_metrics", 
        "metrics", 
        "competitor_metrics", 
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
        _dict['domain'] = self.domain
        _dict['avg_position'] = self.avg_position
        _dict['sum_position'] = self.sum_position
        _dict['intersections'] = self.intersections
        _dict['full_domain_metrics'] = self.full_domain_metrics
        _dict['metrics'] = self.metrics
        _dict['competitor_metrics'] = self.competitor_metrics
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "domain": obj.get("domain"),
            "avg_position": obj.get("avg_position"),
            "sum_position": obj.get("sum_position"),
            "intersections": obj.get("intersections"),
            "full_domain_metrics": obj.get("full_domain_metrics"),
            "metrics": obj.get("metrics"),
            "competitor_metrics": obj.get("competitor_metrics"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj