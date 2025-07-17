from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_priority_tasks_ready_keywords_data_price_data_info import AppendixPriorityTasksReadyKeywordsDataPriceDataInfo



class AppendixTaskKeywordsDataPriceDataInfo(BaseModel):
    """
    AppendixTaskKeywordsDataPriceDataInfo
    """ # noqa: E501
    priority_low: Optional[List[Optional[AppendixPriorityTasksReadyKeywordsDataPriceDataInfo]]] = Field(default=None, description="")
    priority_normal: Optional[List[Optional[AppendixPriorityTasksReadyKeywordsDataPriceDataInfo]]] = Field(default=None, description="")
    priority_high: Optional[List[Optional[AppendixPriorityTasksReadyKeywordsDataPriceDataInfo]]] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "priority_low", 
        "priority_normal", 
        "priority_high", 
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

        priority_low_items = []
        if self.priority_low:
            for _item in self.priority_low:
                if _item:
                    priority_low_items.append(_item.to_dict())
            _dict['priority_low'] = priority_low_items
        priority_normal_items = []
        if self.priority_normal:
            for _item in self.priority_normal:
                if _item:
                    priority_normal_items.append(_item.to_dict())
            _dict['priority_normal'] = priority_normal_items
        priority_high_items = []
        if self.priority_high:
            for _item in self.priority_high:
                if _item:
                    priority_high_items.append(_item.to_dict())
            _dict['priority_high'] = priority_high_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "priority_low": [AppendixPriorityTasksReadyKeywordsDataPriceDataInfo.from_dict(_item) for _item in obj["priority_low"]] if obj.get("priority_low") is not None else None,
            "priority_normal": [AppendixPriorityTasksReadyKeywordsDataPriceDataInfo.from_dict(_item) for _item in obj["priority_normal"]] if obj.get("priority_normal") is not None else None,
            "priority_high": [AppendixPriorityTasksReadyKeywordsDataPriceDataInfo.from_dict(_item) for _item in obj["priority_high"]] if obj.get("priority_high") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj