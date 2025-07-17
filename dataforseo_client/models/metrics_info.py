from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class MetricsInfo(BaseModel):
    """
    MetricsInfo
    """ # noqa: E501
    pos_1: Optional[StrictInt] = Field(default=None, description="number of organic SERPs where the domain ranks #1")
    pos_2_3: Optional[StrictInt] = Field(default=None, description="number of organic SERPs where the domain ranks #2-3")
    pos_4_10: Optional[StrictInt] = Field(default=None, description="number of organic SERPs where the domain ranks #4-10")
    pos_11_20: Optional[StrictInt] = Field(default=None, description="number of organic SERPs where the domain ranks #11-20")
    pos_21_30: Optional[StrictInt] = Field(default=None, description="number of organic SERPs where the domain ranks #21-30")
    pos_31_40: Optional[StrictInt] = Field(default=None, description="number of organic SERPs where the domain ranks #31-40")
    pos_41_50: Optional[StrictInt] = Field(default=None, description="number of organic SERPs where the domain ranks #41-50")
    pos_51_60: Optional[StrictInt] = Field(default=None, description="number of organic SERPs where the domain ranks #51-60")
    pos_61_70: Optional[StrictInt] = Field(default=None, description="number of organic SERPs where the domain ranks #61-70")
    pos_71_80: Optional[StrictInt] = Field(default=None, description="number of organic SERPs where the domain ranks #71-80")
    pos_81_90: Optional[StrictInt] = Field(default=None, description="number of organic SERPs where the domain ranks #81-90")
    pos_91_100: Optional[StrictInt] = Field(default=None, description="number of organic SERPs where the domain ranks #91-100")
    etv: Optional[StrictFloat] = Field(default=None, description="estimated traffic volume. estimated organic monthly traffic to the domain. calculated as the product of CTR (click-through-rate) and search volume values of all keywords the domain ranks for. learn more about how the metric is calculated in this help center article")
    count: Optional[StrictInt] = Field(default=None, description="total count of organic SERPs that contain the domain")
    estimated_paid_traffic_cost: Optional[StrictFloat] = Field(default=None, description="estimated cost of converting organic search traffic into paid. represents the estimated monthly cost of running ads (USD) for all keywords a domain ranks for. the metric is calculated as the product of organic etv and paid cpc values and indicates the cost of driving the estimated volume of monthly organic traffic through PPC advertising in Google Search. learn more about how the metric is calculated in this help center article")
    is_new: Optional[StrictInt] = Field(default=None, description="number of new ranked elements. indicates how many new ranked elements were found for this domain")
    is_up: Optional[StrictInt] = Field(default=None, description="rank went up. indicates how many ranked elements of this domain went up in Google Search")
    is_down: Optional[StrictInt] = Field(default=None, description="rank went down. indicates how many ranked elements of this domain went down in Google Search")
    is_lost: Optional[StrictInt] = Field(default=None, description="lost ranked elements. indicates how many ranked elements of this domain were previously presented in SERPs, but weren’t found during the last check")
    __properties: ClassVar[List[str]] = [
        "pos_1", 
        "pos_2_3", 
        "pos_4_10", 
        "pos_11_20", 
        "pos_21_30", 
        "pos_31_40", 
        "pos_41_50", 
        "pos_51_60", 
        "pos_61_70", 
        "pos_71_80", 
        "pos_81_90", 
        "pos_91_100", 
        "etv", 
        "count", 
        "estimated_paid_traffic_cost", 
        "is_new", 
        "is_up", 
        "is_down", 
        "is_lost", 
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

        _dict['pos_1'] = self.pos_1
        _dict['pos_2_3'] = self.pos_2_3
        _dict['pos_4_10'] = self.pos_4_10
        _dict['pos_11_20'] = self.pos_11_20
        _dict['pos_21_30'] = self.pos_21_30
        _dict['pos_31_40'] = self.pos_31_40
        _dict['pos_41_50'] = self.pos_41_50
        _dict['pos_51_60'] = self.pos_51_60
        _dict['pos_61_70'] = self.pos_61_70
        _dict['pos_71_80'] = self.pos_71_80
        _dict['pos_81_90'] = self.pos_81_90
        _dict['pos_91_100'] = self.pos_91_100
        _dict['etv'] = self.etv
        _dict['count'] = self.count
        _dict['estimated_paid_traffic_cost'] = self.estimated_paid_traffic_cost
        _dict['is_new'] = self.is_new
        _dict['is_up'] = self.is_up
        _dict['is_down'] = self.is_down
        _dict['is_lost'] = self.is_lost
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pos_1": obj.get("pos_1"),
            "pos_2_3": obj.get("pos_2_3"),
            "pos_4_10": obj.get("pos_4_10"),
            "pos_11_20": obj.get("pos_11_20"),
            "pos_21_30": obj.get("pos_21_30"),
            "pos_31_40": obj.get("pos_31_40"),
            "pos_41_50": obj.get("pos_41_50"),
            "pos_51_60": obj.get("pos_51_60"),
            "pos_61_70": obj.get("pos_61_70"),
            "pos_71_80": obj.get("pos_71_80"),
            "pos_81_90": obj.get("pos_81_90"),
            "pos_91_100": obj.get("pos_91_100"),
            "etv": obj.get("etv"),
            "count": obj.get("count"),
            "estimated_paid_traffic_cost": obj.get("estimated_paid_traffic_cost"),
            "is_new": obj.get("is_new"),
            "is_up": obj.get("is_up"),
            "is_down": obj.get("is_down"),
            "is_lost": obj.get("is_lost"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj