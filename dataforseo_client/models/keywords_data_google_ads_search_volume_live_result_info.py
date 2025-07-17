from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.monthly_searches_info import MonthlySearchesInfo



class KeywordsDataGoogleAdsSearchVolumeLiveResultInfo(BaseModel):
    """
    KeywordsDataGoogleAdsSearchVolumeLiveResultInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword. keyword is returned with decoded %## (plus character ‘+’ will be decoded to a space character)")
    spell: Optional[StrictStr] = Field(default=None, description="correct spelling of the keyword. Note:if the keyword in the POST array appears to be misspelled, data will be returned for the correctly spelled keyword;. we use the functionality of Google Ads API to check and validate the spelling of keywords, learn more by this link")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array. if there is no data, then the value is null")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array. if there is no data, then the value is null")
    search_partners: Optional[StrictBool] = Field(default=None, description="indicates whether data from partner networks included in the response")
    competition: Optional[StrictStr] = Field(default=None, description="competition. represents the relative amount of competition associated with the given keyword in paid SERP only;. this value is based on Google Ads data and can take the following values: HIGH, MEDIUM, LOW;. if there is no data the value is null;. learn more about the metric in this help center article")
    competition_index: Optional[StrictInt] = Field(default=None, description="competition. represents the relative amount of competition associated with the given keyword in paid SERP only;. this value is based on Google Ads data and can be between 0 and 100 (inclusive);. if there is no data the value is null;. learn more about the metric in this help center article")
    search_volume: Optional[StrictInt] = Field(default=None, description="monthly average search volume rate")
    low_top_of_page_bid: Optional[StrictFloat] = Field(default=None, description="minimum bid for the ad to be displayed at the top of the first page. indicates the value greater than about 20% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers);. the value may differ depending on the location specified in a POST request")
    high_top_of_page_bid: Optional[StrictFloat] = Field(default=None, description="maximum bid for the ad to be displayed at the top of the first page. indicates the value greater than about 80% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers);. the value may differ depending on the location specified in a POST request")
    cpc: Optional[StrictFloat] = Field(default=None, description="cost per click. indicates the amount paid for each click on the ad displayed for a given keyword")
    monthly_searches: Optional[List[Optional[MonthlySearchesInfo]]] = Field(default=None, description="monthly searches. represents the (approximate) number of searches on this keyword idea (as available for the past twelve months by default), targeted to the specified geographic locations;. if there is no data then the value is null")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "spell", 
        "location_code", 
        "language_code", 
        "search_partners", 
        "competition", 
        "competition_index", 
        "search_volume", 
        "low_top_of_page_bid", 
        "high_top_of_page_bid", 
        "cpc", 
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
        _dict['spell'] = self.spell
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['search_partners'] = self.search_partners
        _dict['competition'] = self.competition
        _dict['competition_index'] = self.competition_index
        _dict['search_volume'] = self.search_volume
        _dict['low_top_of_page_bid'] = self.low_top_of_page_bid
        _dict['high_top_of_page_bid'] = self.high_top_of_page_bid
        _dict['cpc'] = self.cpc
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
            "spell": obj.get("spell"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "search_partners": obj.get("search_partners"),
            "competition": obj.get("competition"),
            "competition_index": obj.get("competition_index"),
            "search_volume": obj.get("search_volume"),
            "low_top_of_page_bid": obj.get("low_top_of_page_bid"),
            "high_top_of_page_bid": obj.get("high_top_of_page_bid"),
            "cpc": obj.get("cpc"),
            "monthly_searches": [MonthlySearchesInfo.from_dict(_item) for _item in obj["monthly_searches"]] if obj.get("monthly_searches") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj