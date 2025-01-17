# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.monthly_searches import MonthlySearches
from dataforseo_client.models.search_volume_trend_info import SearchVolumeTrendInfo
from typing import Optional, Set
from typing_extensions import Self

class KeywordInfo(BaseModel):
    """
    KeywordInfo
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    last_updated_time: Optional[StrictStr] = Field(default=None, description="date and time when keyword data was updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    competition: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="competition represents the relative amount of competition associated with the given keyword. This value is based on Google Ads data and can be between 0 and 1 (inclusive)")
    competition_level: Optional[StrictStr] = Field(default=None, description="competition level represents the relative level of competition associated with the given keyword in paid SERP only; possible values: LOW, MEDIUM, HIGH if competition level is unknown, the value is null; learn more about the metric in this help center article")
    cpc: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="cost-per-click represents the average cost per click (USD) historically paid for the keyword")
    search_volume: Optional[StrictInt] = Field(default=None, description="average monthly search volume rate represents the (approximate) number of searches for the given keyword idea on google.com")
    low_top_of_page_bid: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="minimum bid for the ad to be displayed at the top of the first page indicates the value greater than about 20% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers) the value may differ depending on the location specified in a POST request")
    high_top_of_page_bid: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="maximum bid for the ad to be displayed at the top of the first page indicates the value greater than about 80% of the lowest bids for which ads were displayed (based on Google Ads statistics for advertisers) the value may differ depending on the location specified in a POST request")
    categories: Optional[List[StrictInt]] = Field(default=None, description="product and service categories you can download the full list of possible categories")
    monthly_searches: Optional[List[MonthlySearches]] = Field(default=None, description="monthly searches represents the (approximate) number of searches on this keyword idea (as available for the past twelve months), targeted to the specified geographic locations")
    search_volume_trend: Optional[SearchVolumeTrendInfo] = None
    __properties: ClassVar[List[str]] = ["se_type", "last_updated_time", "competition", "competition_level", "cpc", "search_volume", "low_top_of_page_bid", "high_top_of_page_bid", "categories", "monthly_searches", "search_volume_trend"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of KeywordInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in monthly_searches (list)
        _items = []
        if self.monthly_searches:
            for _item_monthly_searches in self.monthly_searches:
                if _item_monthly_searches:
                    _items.append(_item_monthly_searches.to_dict())
            _dict['monthly_searches'] = _items
        # override the default output from pydantic by calling `to_dict()` of search_volume_trend
        if self.search_volume_trend:
            _dict['search_volume_trend'] = self.search_volume_trend.to_dict()
        # set to None if se_type (nullable) is None
        # and model_fields_set contains the field
        if self.se_type is None and "se_type" in self.model_fields_set:
            _dict['se_type'] = None

        # set to None if last_updated_time (nullable) is None
        # and model_fields_set contains the field
        if self.last_updated_time is None and "last_updated_time" in self.model_fields_set:
            _dict['last_updated_time'] = None

        # set to None if competition (nullable) is None
        # and model_fields_set contains the field
        if self.competition is None and "competition" in self.model_fields_set:
            _dict['competition'] = None

        # set to None if competition_level (nullable) is None
        # and model_fields_set contains the field
        if self.competition_level is None and "competition_level" in self.model_fields_set:
            _dict['competition_level'] = None

        # set to None if cpc (nullable) is None
        # and model_fields_set contains the field
        if self.cpc is None and "cpc" in self.model_fields_set:
            _dict['cpc'] = None

        # set to None if search_volume (nullable) is None
        # and model_fields_set contains the field
        if self.search_volume is None and "search_volume" in self.model_fields_set:
            _dict['search_volume'] = None

        # set to None if low_top_of_page_bid (nullable) is None
        # and model_fields_set contains the field
        if self.low_top_of_page_bid is None and "low_top_of_page_bid" in self.model_fields_set:
            _dict['low_top_of_page_bid'] = None

        # set to None if high_top_of_page_bid (nullable) is None
        # and model_fields_set contains the field
        if self.high_top_of_page_bid is None and "high_top_of_page_bid" in self.model_fields_set:
            _dict['high_top_of_page_bid'] = None

        # set to None if categories (nullable) is None
        # and model_fields_set contains the field
        if self.categories is None and "categories" in self.model_fields_set:
            _dict['categories'] = None

        # set to None if monthly_searches (nullable) is None
        # and model_fields_set contains the field
        if self.monthly_searches is None and "monthly_searches" in self.model_fields_set:
            _dict['monthly_searches'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KeywordInfo from a dict"""
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
            "monthly_searches": [MonthlySearches.from_dict(_item) for _item in obj["monthly_searches"]] if obj.get("monthly_searches") is not None else None,
            "search_volume_trend": SearchVolumeTrendInfo.from_dict(obj["search_volume_trend"]) if obj.get("search_volume_trend") is not None else None
        })
        return _obj


