from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.backlinks_timeseries_new_lost_summary_live_item import BacklinksTimeseriesNewLostSummaryLiveItem



class BacklinksTimeseriesNewLostSummaryLiveResultInfo(BaseModel):
    """
    BacklinksTimeseriesNewLostSummaryLiveResultInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="target from a POST array")
    date_from: Optional[StrictStr] = Field(default=None, description="starting date of the time range. in the UTC format: “yyyy-mm-dd”. example:. 2019-01-01")
    date_to: Optional[StrictStr] = Field(default=None, description="ending date of the time range. in the UTC format: 'yyyy-mm-dd'. example:. '2019-01-15'")
    group_range: Optional[StrictStr] = Field(default=None, description="group_range from the POST array")
    items_count: Optional[StrictInt] = Field(default=None, description="the number of results returned in the items array")
    items: Optional[List[Optional[BacklinksTimeseriesNewLostSummaryLiveItem]]] = Field(default=None, description="contains relevant backlinks and referring domains data")
    __properties: ClassVar[List[str]] = [
        "target", 
        "date_from", 
        "date_to", 
        "group_range", 
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

        _dict['target'] = self.target
        _dict['date_from'] = self.date_from
        _dict['date_to'] = self.date_to
        _dict['group_range'] = self.group_range
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
            "target": obj.get("target"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "group_range": obj.get("group_range"),
            "items_count": obj.get("items_count"),
            "items": [BacklinksTimeseriesNewLostSummaryLiveItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj