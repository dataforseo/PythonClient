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
from dataforseo_client.models.est_c_info import EstCInfo
from dataforseo_client.models.est_info import EstInfo
from typing import Optional, Set
from typing_extensions import Self

class KeywordsDataBingAudienceEstimationLiveResultInfo(BaseModel):
    """
    KeywordsDataBingAudienceEstimationLiveResultInfo
    """ # noqa: E501
    est_impressions: Optional[EstInfo] = None
    est_audience_size: Optional[EstInfo] = None
    est_clicks: Optional[EstInfo] = None
    est_spend: Optional[EstInfo] = None
    est_cost_per_event: Optional[EstCInfo] = None
    est_ctr: Optional[EstCInfo] = None
    suggested_bid: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="suggested bid value under the current targeting")
    suggested_budget: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="suggested daily budget value under the current targeting and bid")
    events_lost_to_bid: Optional[StrictInt] = Field(default=None, description="indicates event lost count due to insufficient input bid")
    events_lost_to_budget: Optional[StrictInt] = Field(default=None, description="indicates the event lost count due to insufficient input budget")
    est_reach_audience_size: Optional[StrictInt] = Field(default=None, description="monthly estimated user count")
    est_reach_impressions: Optional[StrictInt] = Field(default=None, description="monthly estimated impressions")
    currency: Optional[StrictStr] = Field(default=None, description="currency name example: USDollar")
    __properties: ClassVar[List[str]] = ["est_impressions", "est_audience_size", "est_clicks", "est_spend", "est_cost_per_event", "est_ctr", "suggested_bid", "suggested_budget", "events_lost_to_bid", "events_lost_to_budget", "est_reach_audience_size", "est_reach_impressions", "currency"]

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
        """Create an instance of KeywordsDataBingAudienceEstimationLiveResultInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of est_impressions
        if self.est_impressions:
            _dict['est_impressions'] = self.est_impressions.to_dict()
        # override the default output from pydantic by calling `to_dict()` of est_audience_size
        if self.est_audience_size:
            _dict['est_audience_size'] = self.est_audience_size.to_dict()
        # override the default output from pydantic by calling `to_dict()` of est_clicks
        if self.est_clicks:
            _dict['est_clicks'] = self.est_clicks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of est_spend
        if self.est_spend:
            _dict['est_spend'] = self.est_spend.to_dict()
        # override the default output from pydantic by calling `to_dict()` of est_cost_per_event
        if self.est_cost_per_event:
            _dict['est_cost_per_event'] = self.est_cost_per_event.to_dict()
        # override the default output from pydantic by calling `to_dict()` of est_ctr
        if self.est_ctr:
            _dict['est_ctr'] = self.est_ctr.to_dict()
        # set to None if suggested_bid (nullable) is None
        # and model_fields_set contains the field
        if self.suggested_bid is None and "suggested_bid" in self.model_fields_set:
            _dict['suggested_bid'] = None

        # set to None if suggested_budget (nullable) is None
        # and model_fields_set contains the field
        if self.suggested_budget is None and "suggested_budget" in self.model_fields_set:
            _dict['suggested_budget'] = None

        # set to None if events_lost_to_bid (nullable) is None
        # and model_fields_set contains the field
        if self.events_lost_to_bid is None and "events_lost_to_bid" in self.model_fields_set:
            _dict['events_lost_to_bid'] = None

        # set to None if events_lost_to_budget (nullable) is None
        # and model_fields_set contains the field
        if self.events_lost_to_budget is None and "events_lost_to_budget" in self.model_fields_set:
            _dict['events_lost_to_budget'] = None

        # set to None if est_reach_audience_size (nullable) is None
        # and model_fields_set contains the field
        if self.est_reach_audience_size is None and "est_reach_audience_size" in self.model_fields_set:
            _dict['est_reach_audience_size'] = None

        # set to None if est_reach_impressions (nullable) is None
        # and model_fields_set contains the field
        if self.est_reach_impressions is None and "est_reach_impressions" in self.model_fields_set:
            _dict['est_reach_impressions'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KeywordsDataBingAudienceEstimationLiveResultInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "est_impressions": EstInfo.from_dict(obj["est_impressions"]) if obj.get("est_impressions") is not None else None,
            "est_audience_size": EstInfo.from_dict(obj["est_audience_size"]) if obj.get("est_audience_size") is not None else None,
            "est_clicks": EstInfo.from_dict(obj["est_clicks"]) if obj.get("est_clicks") is not None else None,
            "est_spend": EstInfo.from_dict(obj["est_spend"]) if obj.get("est_spend") is not None else None,
            "est_cost_per_event": EstCInfo.from_dict(obj["est_cost_per_event"]) if obj.get("est_cost_per_event") is not None else None,
            "est_ctr": EstCInfo.from_dict(obj["est_ctr"]) if obj.get("est_ctr") is not None else None,
            "suggested_bid": obj.get("suggested_bid"),
            "suggested_budget": obj.get("suggested_budget"),
            "events_lost_to_bid": obj.get("events_lost_to_bid"),
            "events_lost_to_budget": obj.get("events_lost_to_budget"),
            "est_reach_audience_size": obj.get("est_reach_audience_size"),
            "est_reach_impressions": obj.get("est_reach_impressions"),
            "currency": obj.get("currency")
        })
        return _obj


