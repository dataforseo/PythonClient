from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.app_metrics_info import AppMetricsInfo



class AmazonMetricsBundleInfo(BaseModel):
    """
    AmazonMetricsBundleInfo
    """ # noqa: E501
    amazon_serp: Optional[AppMetricsInfo] = Field(default=None, description="ranking data from Amazon organic SERP")
    amazon_paid: Optional[AppMetricsInfo] = Field(default=None, description="ranking data from Amazon paid SERP")
    __properties: ClassVar[List[str]] = [
        "amazon_serp", 
        "amazon_paid", 
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

        _dict['amazon_serp'] = self.amazon_serp.to_dict() if self.amazon_serp else None
        _dict['amazon_paid'] = self.amazon_paid.to_dict() if self.amazon_paid else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amazon_serp": AppMetricsInfo.from_dict(obj["amazon_serp"]) if obj.get("amazon_serp") is not None else None,
            "amazon_paid": AppMetricsInfo.from_dict(obj["amazon_paid"]) if obj.get("amazon_paid") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj