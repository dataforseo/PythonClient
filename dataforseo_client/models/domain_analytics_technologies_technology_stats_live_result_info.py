from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.domain_analytics_technologies_technology_stats_live_item import DomainAnalyticsTechnologiesTechnologyStatsLiveItem



class DomainAnalyticsTechnologiesTechnologyStatsLiveResultInfo(BaseModel):
    """
    DomainAnalyticsTechnologiesTechnologyStatsLiveResultInfo
    """ # noqa: E501
    technology: Optional[StrictStr] = Field(default=None, description="target technology")
    date_from: Optional[StrictStr] = Field(default=None, description="starting date of the time range")
    date_to: Optional[StrictStr] = Field(default=None, description="ending date of the time range")
    items_count: Optional[StrictInt] = Field(default=None, description="number of items in the results array")
    items: Optional[List[Optional[DomainAnalyticsTechnologiesTechnologyStatsLiveItem]]] = Field(default=None, description="items array")
    __properties: ClassVar[List[str]] = [
        "technology", 
        "date_from", 
        "date_to", 
        "items_count", 
        "items", 
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

        _dict['technology'] = self.technology
        _dict['date_from'] = self.date_from
        _dict['date_to'] = self.date_to
        _dict['items_count'] = self.items_count
        items_items = []
        if self.items:
            for _item in self.items:
                if _item:
                    items_items.append(_item.to_dict())
            _dict['items'] = items_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "technology": obj.get("technology"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "items_count": obj.get("items_count"),
            "items": [DomainAnalyticsTechnologiesTechnologyStatsLiveItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj