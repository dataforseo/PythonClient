from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.monthly_searches_info import MonthlySearchesInfo
from dataforseo_client.models.search_volume_trend import SearchVolumeTrend



class KeywordInfo(BaseModel):
    """
    KeywordInfo
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    last_updated_time: Optional[StrictStr] = Field(default=None, description="date and time when keyword data was updated. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    competition: Optional[StrictFloat] = Field(default=None, description="competition. represents the relative amount of competition associated with the given keyword. This value is based on Google Ads data and can be between 0 and 1 (inclusive)")
    competition_level: Optional[StrictStr] = Field(default=None, description="competition level. represents the relative level of competition associated with the given keyword in paid SERP only;. possible values: LOW, MEDIUM, HIGH. if competition level is unknown, the value is null;. learn more about the metric in this help center article")
    cpc: Optional[StrictFloat] = Field(default=None, description="cost-per-click. represents the average cost per click (USD) historically paid for the keyword")
    search_volume: Optional[StrictInt] = Field(default=None, description="average monthly search volume rate. represents the (approximate) number of searches for the given keyword idea on google.com")
    low_top_of_page_bid: Optional[StrictFloat] = Field(default=None, description="minimum bid for the ad to be displayed at the top of the first page. indicates the value greater than about 20% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers). the value may differ depending on the location specified in a POST request")
    high_top_of_page_bid: Optional[StrictFloat] = Field(default=None, description="maximum bid for the ad to be displayed at the top of the first page. indicates the value greater than about 80% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers). the value may differ depending on the location specified in a POST request")
    categories: Optional[List[Optional[StrictInt]]] = Field(default=None, description="product and service categories. you can download the full list of possible categories")
    monthly_searches: Optional[List[Optional[MonthlySearchesInfo]]] = Field(default=None, description="monthly searches. represents the (approximate) number of searches on this keyword idea (as available for the past twelve months), targeted to the specified geographic locations")
    search_volume_trend: Optional[SearchVolumeTrend] = Field(default=None, description="search volume trend changes. represents search volume change in percent compared to the previous period")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "last_updated_time", 
        "competition", 
        "competition_level", 
        "cpc", 
        "search_volume", 
        "low_top_of_page_bid", 
        "high_top_of_page_bid", 
        "categories", 
        "monthly_searches", 
        "search_volume_trend", 
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
        _dict['last_updated_time'] = self.last_updated_time
        _dict['competition'] = self.competition
        _dict['competition_level'] = self.competition_level
        _dict['cpc'] = self.cpc
        _dict['search_volume'] = self.search_volume
        _dict['low_top_of_page_bid'] = self.low_top_of_page_bid
        _dict['high_top_of_page_bid'] = self.high_top_of_page_bid
        _dict['categories'] = self.categories
        monthly_searches_items = []
        if self.monthly_searches:
            for _item in self.monthly_searches:
                if _item:
                    monthly_searches_items.append(_item.to_dict())
            _dict['monthly_searches'] = monthly_searches_items
        _dict['search_volume_trend'] = self.search_volume_trend.to_dict() if self.search_volume_trend else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "last_updated_time": obj.get("last_updated_time"),
            "competition": obj.get("competition"),
            "competition_level": obj.get("competition_level"),
            "cpc": obj.get("cpc"),
            "search_volume": obj.get("search_volume"),
            "low_top_of_page_bid": obj.get("low_top_of_page_bid"),
            "high_top_of_page_bid": obj.get("high_top_of_page_bid"),
            "categories": obj.get("categories"),
            "monthly_searches": [MonthlySearchesInfo.from_dict(_item) for _item in obj["monthly_searches"]] if obj.get("monthly_searches") is not None else None,
            "search_volume_trend": SearchVolumeTrend.from_dict(obj["search_volume_trend"]) if obj.get("search_volume_trend") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj