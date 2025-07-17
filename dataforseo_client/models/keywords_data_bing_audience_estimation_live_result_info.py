from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.audience_estimation_info import AudienceEstimationInfo



class KeywordsDataBingAudienceEstimationLiveResultInfo(BaseModel):
    """
    KeywordsDataBingAudienceEstimationLiveResultInfo
    """ # noqa: E501
    est_impressions: Optional[AudienceEstimationInfo] = Field(default=None, description="monthly estimated impressions range")
    est_audience_size: Optional[AudienceEstimationInfo] = Field(default=None, description="monthly estimated reach user count range")
    est_clicks: Optional[AudienceEstimationInfo] = Field(default=None, description="monthly estimated click count range")
    est_spend: Optional[AudienceEstimationInfo] = Field(default=None, description="monthly estimated spending range")
    est_cost_per_event: Optional[AudienceEstimationInfo] = Field(default=None, description="indicates the estimated cost per event with range result")
    est_ctr: Optional[AudienceEstimationInfo] = Field(default=None, description="estimated click-through rate range")
    suggested_bid: Optional[StrictFloat] = Field(default=None, description="suggested bid value under the current targeting")
    suggested_budget: Optional[StrictFloat] = Field(default=None, description="suggested daily budget value under the current targeting and bid")
    events_lost_to_bid: Optional[StrictInt] = Field(default=None, description="indicates event lost count due to insufficient input bid")
    events_lost_to_budget: Optional[StrictInt] = Field(default=None, description="indicates the event lost count due to insufficient input budget")
    est_reach_audience_size: Optional[StrictInt] = Field(default=None, description="monthly estimated user count")
    est_reach_impressions: Optional[StrictInt] = Field(default=None, description="monthly estimated impressions")
    currency: Optional[StrictStr] = Field(default=None, description="currency name. example: USDollar")
    __properties: ClassVar[List[str]] = [
        "est_impressions", 
        "est_audience_size", 
        "est_clicks", 
        "est_spend", 
        "est_cost_per_event", 
        "est_ctr", 
        "suggested_bid", 
        "suggested_budget", 
        "events_lost_to_bid", 
        "events_lost_to_budget", 
        "est_reach_audience_size", 
        "est_reach_impressions", 
        "currency", 
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

        _dict['est_impressions'] = self.est_impressions.to_dict() if self.est_impressions else None
        _dict['est_audience_size'] = self.est_audience_size.to_dict() if self.est_audience_size else None
        _dict['est_clicks'] = self.est_clicks.to_dict() if self.est_clicks else None
        _dict['est_spend'] = self.est_spend.to_dict() if self.est_spend else None
        _dict['est_cost_per_event'] = self.est_cost_per_event.to_dict() if self.est_cost_per_event else None
        _dict['est_ctr'] = self.est_ctr.to_dict() if self.est_ctr else None
        _dict['suggested_bid'] = self.suggested_bid
        _dict['suggested_budget'] = self.suggested_budget
        _dict['events_lost_to_bid'] = self.events_lost_to_bid
        _dict['events_lost_to_budget'] = self.events_lost_to_budget
        _dict['est_reach_audience_size'] = self.est_reach_audience_size
        _dict['est_reach_impressions'] = self.est_reach_impressions
        _dict['currency'] = self.currency
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "est_impressions": AudienceEstimationInfo.from_dict(obj["est_impressions"]) if obj.get("est_impressions") is not None else None,
            "est_audience_size": AudienceEstimationInfo.from_dict(obj["est_audience_size"]) if obj.get("est_audience_size") is not None else None,
            "est_clicks": AudienceEstimationInfo.from_dict(obj["est_clicks"]) if obj.get("est_clicks") is not None else None,
            "est_spend": AudienceEstimationInfo.from_dict(obj["est_spend"]) if obj.get("est_spend") is not None else None,
            "est_cost_per_event": AudienceEstimationInfo.from_dict(obj["est_cost_per_event"]) if obj.get("est_cost_per_event") is not None else None,
            "est_ctr": AudienceEstimationInfo.from_dict(obj["est_ctr"]) if obj.get("est_ctr") is not None else None,
            "suggested_bid": obj.get("suggested_bid"),
            "suggested_budget": obj.get("suggested_budget"),
            "events_lost_to_bid": obj.get("events_lost_to_bid"),
            "events_lost_to_budget": obj.get("events_lost_to_budget"),
            "est_reach_audience_size": obj.get("est_reach_audience_size"),
            "est_reach_impressions": obj.get("est_reach_impressions"),
            "currency": obj.get("currency"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj