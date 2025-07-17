from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.review_mention_info import ReviewMentionInfo
from dataforseo_client.models.other_sites_reviews_info import OtherSitesReviewsInfo



class HotelReviewInfo(BaseModel):
    """
    HotelReviewInfo
    """ # noqa: E501
    value: Optional[StrictFloat] = Field(default=None, description="overall hotel rating based on customer votes")
    votes_count: Optional[StrictInt] = Field(default=None, description="number of customer votes. the number of customer votes included in the calculation of the hotel rating")
    mentions: Optional[List[Optional[ReviewMentionInfo]]] = Field(default=None, description="hotel mentions. information about hotel reviews by criteria")
    rating_distribution: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="rating distribution by votes. the distribution of votes across the rating in the range from 1 to 5")
    other_sites_reviews: Optional[List[Optional[OtherSitesReviewsInfo]]] = Field(default=None, description="reviews on third-party sites. reviews from third-paty sites")
    __properties: ClassVar[List[str]] = [
        "value", 
        "votes_count", 
        "mentions", 
        "rating_distribution", 
        "other_sites_reviews", 
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

        _dict['value'] = self.value
        _dict['votes_count'] = self.votes_count
        mentions_items = []
        if self.mentions:
            for _item in self.mentions:
                if _item:
                    mentions_items.append(_item.to_dict())
            _dict['mentions'] = mentions_items
        _dict['rating_distribution'] = self.rating_distribution
        other_sites_reviews_items = []
        if self.other_sites_reviews:
            for _item in self.other_sites_reviews:
                if _item:
                    other_sites_reviews_items.append(_item.to_dict())
            _dict['other_sites_reviews'] = other_sites_reviews_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "value": obj.get("value"),
            "votes_count": obj.get("votes_count"),
            "mentions": [ReviewMentionInfo.from_dict(_item) for _item in obj["mentions"]] if obj.get("mentions") is not None else None,
            "rating_distribution": obj.get("rating_distribution"),
            "other_sites_reviews": [OtherSitesReviewsInfo.from_dict(_item) for _item in obj["other_sites_reviews"]] if obj.get("other_sites_reviews") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj