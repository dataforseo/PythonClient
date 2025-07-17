from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.historical_metrics_info import HistoricalMetricsInfo



class HistoricalMetricsBundleInfo(BaseModel):
    """
    HistoricalMetricsBundleInfo
    """ # noqa: E501
    organic: Optional[List[Optional[HistoricalMetricsInfo]]] = Field(default=None, description="traffic data from organic search")
    paid: Optional[List[Optional[HistoricalMetricsInfo]]] = Field(default=None, description="traffic data from paid search")
    local_pack: Optional[List[Optional[HistoricalMetricsInfo]]] = Field(default=None, description="traffic data from the local pack results in SERP")
    featured_snippet: Optional[List[Optional[HistoricalMetricsInfo]]] = Field(default=None, description="traffic data from the featured snippet results in Google SERP")
    __properties: ClassVar[List[str]] = [
        "organic", 
        "paid", 
        "local_pack", 
        "featured_snippet", 
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

        organic_items = []
        if self.organic:
            for _item in self.organic:
                if _item:
                    organic_items.append(_item.to_dict())
            _dict['organic'] = organic_items
        paid_items = []
        if self.paid:
            for _item in self.paid:
                if _item:
                    paid_items.append(_item.to_dict())
            _dict['paid'] = paid_items
        local_pack_items = []
        if self.local_pack:
            for _item in self.local_pack:
                if _item:
                    local_pack_items.append(_item.to_dict())
            _dict['local_pack'] = local_pack_items
        featured_snippet_items = []
        if self.featured_snippet:
            for _item in self.featured_snippet:
                if _item:
                    featured_snippet_items.append(_item.to_dict())
            _dict['featured_snippet'] = featured_snippet_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "organic": [HistoricalMetricsInfo.from_dict(_item) for _item in obj["organic"]] if obj.get("organic") is not None else None,
            "paid": [HistoricalMetricsInfo.from_dict(_item) for _item in obj["paid"]] if obj.get("paid") is not None else None,
            "local_pack": [HistoricalMetricsInfo.from_dict(_item) for _item in obj["local_pack"]] if obj.get("local_pack") is not None else None,
            "featured_snippet": [HistoricalMetricsInfo.from_dict(_item) for _item in obj["featured_snippet"]] if obj.get("featured_snippet") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj