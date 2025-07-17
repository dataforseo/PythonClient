from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.topic_list_data_item_info import TopicListDataItemInfo



class TrendsTopicListDataInfo(BaseModel):
    """
    TrendsTopicListDataInfo
    """ # noqa: E501
    top: Optional[List[Optional[TopicListDataItemInfo]]] = Field(default=None, description="the most popular related topics. represents the list of the most popular related topics")
    rising: Optional[List[Optional[TopicListDataItemInfo]]] = Field(default=None, description="emerging related topics. represents the list of related topics with the biggest increase in search frequency since the last time period")
    __properties: ClassVar[List[str]] = [
        "top", 
        "rising", 
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

        top_items = []
        if self.top:
            for _item in self.top:
                if _item:
                    top_items.append(_item.to_dict())
            _dict['top'] = top_items
        rising_items = []
        if self.rising:
            for _item in self.rising:
                if _item:
                    rising_items.append(_item.to_dict())
            _dict['rising'] = rising_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "top": [TopicListDataItemInfo.from_dict(_item) for _item in obj["top"]] if obj.get("top") is not None else None,
            "rising": [TopicListDataItemInfo.from_dict(_item) for _item in obj["rising"]] if obj.get("rising") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj