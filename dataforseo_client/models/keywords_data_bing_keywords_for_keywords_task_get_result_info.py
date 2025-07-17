from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.monthly_searches_info import MonthlySearchesInfo



class KeywordsDataBingKeywordsForKeywordsTaskGetResultInfo(BaseModel):
    """
    KeywordsDataBingKeywordsForKeywordsTaskGetResultInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword in a POST array")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    search_partners: Optional[StrictBool] = Field(default=None, description="indicates whether data from partner networks included in the response")
    device: Optional[StrictStr] = Field(default=None, description="device type. indicates for what device type the data is provided;. possible values: all, mobile, desktop, tablet")
    competition: Optional[StrictFloat] = Field(default=None, description="competition. represents the relative amount of competition associated with the given keyword in paid SERP only. This value is based on Bing Ads data.. Possible values: 0.1, 0.5,0.9 . 0.1 – low competition,. 0.5 – medium competition,. 0.9 – high competition;. if there is no data the value is null")
    cpc: Optional[StrictFloat] = Field(default=None, description="cost-per-click. represents the average cost per click (USD) historically paid for the keyword.. if there is no data, then the value is null")
    search_volume: Optional[StrictInt] = Field(default=None, description="monthly average search volume rate. represents the (approximate) number of searches for the keyword on the Bing search engine, depending on the user’s targeting. search volume is rounded to the closest decimal values. if there is no data, then the value is null")
    categories: Optional[List[Optional[StrictStr]]] = Field(default=None, description="product and service categories. legacy field, the value will always be null")
    monthly_searches: Optional[List[Optional[MonthlySearchesInfo]]] = Field(default=None, description="monthly searches. represents the (approximate) number of searches on this keyword (as available for the past twelve months), targeted to the specified geographic locations.. if there is no data, then the value is null")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_code", 
        "language_code", 
        "search_partners", 
        "device", 
        "competition", 
        "cpc", 
        "search_volume", 
        "categories", 
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
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['search_partners'] = self.search_partners
        _dict['device'] = self.device
        _dict['competition'] = self.competition
        _dict['cpc'] = self.cpc
        _dict['search_volume'] = self.search_volume
        _dict['categories'] = self.categories
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
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "search_partners": obj.get("search_partners"),
            "device": obj.get("device"),
            "competition": obj.get("competition"),
            "cpc": obj.get("cpc"),
            "search_volume": obj.get("search_volume"),
            "categories": obj.get("categories"),
            "monthly_searches": [MonthlySearchesInfo.from_dict(_item) for _item in obj["monthly_searches"]] if obj.get("monthly_searches") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj