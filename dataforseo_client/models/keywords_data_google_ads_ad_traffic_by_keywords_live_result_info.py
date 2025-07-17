from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class KeywordsDataGoogleAdsAdTrafficByKeywordsLiveResultInfo(BaseModel):
    """
    KeywordsDataGoogleAdsAdTrafficByKeywordsLiveResultInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword in a POST array")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array. if there is no data, then the value is null")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array. if there is no data, then the value is null")
    date_interval: Optional[StrictStr] = Field(default=None, description="forecasting date interval in a POST array")
    search_partners: Optional[StrictBool] = Field(default=None, description="include Google search partners. the value you specified when setting the task. if true, the results are returned for owned, operated, and syndicated networks across Google and partner sites that host Google search;. if false, the results are returned for Google search sites only")
    bid: Optional[StrictFloat] = Field(default=None, description="the maximum custom bid. the bid you have specified when setting the task. represents the price you are willing to pay for an ad. the higher value you have specified, the higher metrics and cost you receive in response. learn more in this help center article")
    match: Optional[StrictStr] = Field(default=None, description="keywords match-type. can take the following values: exact, broad, phrase")
    impressions: Optional[StrictInt] = Field(default=None, description="projected number of ad impressions. number of impressions an ad is projected to get within the specified time period. if there is no data, then the value is null. learn more about impressions in this help center article")
    ctr: Optional[StrictFloat] = Field(default=None, description="projected click through rate (CTR) of the advertisement. number of clicks an ad is projected to receive divided by the number of ad impressions; the CTR is projected for the specified time period. if there is no data, then the value is null")
    average_cpc: Optional[StrictFloat] = Field(default=None, description="the average cost-per-click value. represents the cost-per-click (USD) estimated for a keyword based on the specified time period and historical data;. if there is no data, then the value is null")
    cost: Optional[StrictFloat] = Field(default=None, description="charge for an ad. amount that will be charged for running an ad within the specified time period. if there is no data, then the value is null")
    clicks: Optional[StrictFloat] = Field(default=None, description="number of clicks on an ad. number of clicks an ad is projected to get within the specified time period. if there is no data, then the value is null")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_code", 
        "language_code", 
        "date_interval", 
        "search_partners", 
        "bid", 
        "match", 
        "impressions", 
        "ctr", 
        "average_cpc", 
        "cost", 
        "clicks", 
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
        _dict['date_interval'] = self.date_interval
        _dict['search_partners'] = self.search_partners
        _dict['bid'] = self.bid
        _dict['match'] = self.match
        _dict['impressions'] = self.impressions
        _dict['ctr'] = self.ctr
        _dict['average_cpc'] = self.average_cpc
        _dict['cost'] = self.cost
        _dict['clicks'] = self.clicks
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
            "date_interval": obj.get("date_interval"),
            "search_partners": obj.get("search_partners"),
            "bid": obj.get("bid"),
            "match": obj.get("match"),
            "impressions": obj.get("impressions"),
            "ctr": obj.get("ctr"),
            "average_cpc": obj.get("average_cpc"),
            "cost": obj.get("cost"),
            "clicks": obj.get("clicks"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj