from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class KeywordKpiItemInfo(BaseModel):
    """
    KeywordKpiItemInfo
    """ # noqa: E501
    ad_position: Optional[StrictStr] = Field(default=None, description="represents the position of the relevant ad in SERP. can take the following values:. FirstPage1: The first ad to appear on the right side of the first search results page. FirstPage2: The second ad to appear on the right side of the first search results page. FirstPage3: The third ad to appear on the right side of the first search results page. FirstPage4: The fourth ad to appear on the right side of the first search results page. FirstPage5: The fifth ad to appear on the right side of the first search results page. FirstPage6: The sixth ad to appear on the right side of the first search results page. FirstPage7: The seventh ad to appear on the right side of the first search results page. FirstPage8: The eighth ad to appear on the right side of the first search results page. FirstPage9: The ninth ad to appear on the right side of the first search results page. FirstPage10: The tenth ad to appear on the right side of the first search results page. MainLine1: The first ad to appear at the top of the search results page. MainLine2: The second ad to appear at the top of the search results page. MainLine3: The third ad to appear at the top of the search results page. MainLine4: The fourth ad to appear at the top of the search results page")
    clicks: Optional[StrictInt] = Field(default=None, description="ad clicks. the number of clicks that the keyword and match type generated during the last month")
    impressions: Optional[StrictInt] = Field(default=None, description="ad impressions. the number of impressions that the keyword and match type generated during the last month")
    average_cpc: Optional[StrictFloat] = Field(default=None, description="average cost per click, USD. calculated by dividing the cost of all clicks by the number of clicks")
    ctr: Optional[StrictFloat] = Field(default=None, description="click-through rate as a percentage. calculated by dividing the number of clicks by the number of impressions and multiplying the result by 100")
    total_cost: Optional[StrictFloat] = Field(default=None, description="total cost of an ad, USD. the cost of using the specified keyword and match type during the last month")
    average_bid: Optional[StrictFloat] = Field(default=None, description="average bid of the keyword")
    __properties: ClassVar[List[str]] = [
        "ad_position", 
        "clicks", 
        "impressions", 
        "average_cpc", 
        "ctr", 
        "total_cost", 
        "average_bid", 
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

        _dict['ad_position'] = self.ad_position
        _dict['clicks'] = self.clicks
        _dict['impressions'] = self.impressions
        _dict['average_cpc'] = self.average_cpc
        _dict['ctr'] = self.ctr
        _dict['total_cost'] = self.total_cost
        _dict['average_bid'] = self.average_bid
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ad_position": obj.get("ad_position"),
            "clicks": obj.get("clicks"),
            "impressions": obj.get("impressions"),
            "average_cpc": obj.get("average_cpc"),
            "ctr": obj.get("ctr"),
            "total_cost": obj.get("total_cost"),
            "average_bid": obj.get("average_bid"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj