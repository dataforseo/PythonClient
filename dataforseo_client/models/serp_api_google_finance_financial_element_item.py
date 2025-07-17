from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.google_finance_metrics_bundle_info import GoogleFinanceMetricsBundleInfo
from dataforseo_client.models.base_serp_api_google_finance_element_item import BaseSerpApiGoogleFinanceElementItem



class SerpApiGoogleFinanceFinancialElementItem(BaseSerpApiGoogleFinanceElementItem):
    """
    SerpApiGoogleFinanceFinancialElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    quarterly_metrics: Optional[List[Optional[GoogleFinanceMetricsBundleInfo]]] = Field(default=None, description="quarterly google finance metrics")
    annual_metrics: Optional[List[Optional[GoogleFinanceMetricsBundleInfo]]] = Field(default=None, description="annual google finance metrics")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "quarterly_metrics", 
        "annual_metrics", 
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

        _dict['type'] = self.type
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        quarterly_metrics_items = []
        if self.quarterly_metrics:
            for _item in self.quarterly_metrics:
                if _item:
                    quarterly_metrics_items.append(_item.to_dict())
            _dict['quarterly_metrics'] = quarterly_metrics_items
        annual_metrics_items = []
        if self.annual_metrics:
            for _item in self.annual_metrics:
                if _item:
                    annual_metrics_items.append(_item.to_dict())
            _dict['annual_metrics'] = annual_metrics_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "quarterly_metrics": [GoogleFinanceMetricsBundleInfo.from_dict(_item) for _item in obj["quarterly_metrics"]] if obj.get("quarterly_metrics") is not None else None,
            "annual_metrics": [GoogleFinanceMetricsBundleInfo.from_dict(_item) for _item in obj["annual_metrics"]] if obj.get("annual_metrics") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj