from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.monthly_searches_info import MonthlySearchesInfo



class KeywordsDataClickstreamDataSearchVolumeLiveItem(BaseModel):
    """
    KeywordsDataClickstreamDataSearchVolumeLiveItem
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword provided in the POST array")
    search_volume: Optional[StrictInt] = Field(default=None, description="current search volume rate of a keyword")
    monthly_searches: Optional[List[Optional[MonthlySearchesInfo]]] = Field(default=None, description="monthly search volume rates. array of objects with search volume rates in a certain month of a year")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "search_volume", 
        "monthly_searches", 
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

        _dict['keyword'] = self.keyword
        _dict['search_volume'] = self.search_volume
        monthly_searches_items = []
        if self.monthly_searches:
            for _item in self.monthly_searches:
                if _item:
                    monthly_searches_items.append(_item.to_dict())
            _dict['monthly_searches'] = monthly_searches_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "search_volume": obj.get("search_volume"),
            "monthly_searches": [MonthlySearchesInfo.from_dict(_item) for _item in obj["monthly_searches"]] if obj.get("monthly_searches") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj