from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.amazon_metrics_bundle_info import AmazonMetricsBundleInfo



class DataforseoLabsAmazonProductRankOverviewLiveItem(BaseModel):
    """
    DataforseoLabsAmazonProductRankOverviewLiveItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    asin: Optional[StrictStr] = Field(default=None, description="ASIN of the product. unique product identifier on Amazon;. for more information, refer to this help center guide")
    metrics: Optional[AmazonMetricsBundleInfo] = Field(default=None, description="average keyword position of the product")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "asin", 
        "metrics", 
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
        _dict['metrics'] = self.metrics.to_dict() if self.metrics else None
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
            "metrics": AmazonMetricsBundleInfo.from_dict(obj["metrics"]) if obj.get("metrics") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj