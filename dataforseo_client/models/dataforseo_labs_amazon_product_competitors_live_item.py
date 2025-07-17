from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.amazon_metrics_bundle_info import AmazonMetricsBundleInfo



class DataforseoLabsAmazonProductCompetitorsLiveItem(BaseModel):
    """
    DataforseoLabsAmazonProductCompetitorsLiveItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    asin: Optional[StrictStr] = Field(default=None, description="ASIN of the product. unique product identifier on Amazon;. for more information, refer to this help center guide")
    avg_position: Optional[StrictFloat] = Field(default=None, description="average position of the product in Amazon SERP. Note: average position is calculated for intersected keywords only;. the value for a given product may differ when combined with different target products")
    sum_position: Optional[StrictInt] = Field(default=None, description="sum of all product positions in Amazon SERP. Note: average position is calculated for intersected keywords only;. the value for a given product may differ when combined with different target products")
    intersections: Optional[StrictInt] = Field(default=None, description="number of intersecting keywords")
    competitor_metrics: Optional[AmazonMetricsBundleInfo] = Field(default=None, description="metrics for intersecting keywords. ranking data relevant to the keywords that the provided asin shares with the target asin;. Note: in this object ranking data is provided for the returned competitor’s asin")
    full_metrics: Optional[AmazonMetricsBundleInfo] = Field(default=None, description="metrics for all keywords of the product. full overview of ranking data relevant to all keywords that the provided asin is ranking for")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "asin", 
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
        _dict['asin'] = self.asin
        _dict['avg_position'] = self.avg_position
        _dict['sum_position'] = self.sum_position
        _dict['intersections'] = self.intersections
        _dict['competitor_metrics'] = self.competitor_metrics.to_dict() if self.competitor_metrics else None
        _dict['full_metrics'] = self.full_metrics.to_dict() if self.full_metrics else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "asin": obj.get("asin"),
            "avg_position": obj.get("avg_position"),
            "sum_position": obj.get("sum_position"),
            "intersections": obj.get("intersections"),
            "competitor_metrics": AmazonMetricsBundleInfo.from_dict(obj["competitor_metrics"]) if obj.get("competitor_metrics") is not None else None,
            "full_metrics": AmazonMetricsBundleInfo.from_dict(obj["full_metrics"]) if obj.get("full_metrics") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj