from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.business_data_user_profile_info import BusinessDataUserProfileInfo
from dataforseo_client.models.review_response_item_info import ReviewResponseItemInfo



class TrustpilotReviewSearch(BaseModel):
    """
    TrustpilotReviewSearch
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank among all the listed reviews. absolute position among all reviews on the list")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the review in SERP. can take the following values: right")
    url: Optional[StrictStr] = Field(default=None, description="the URL of the review")
    rating: Optional[RatingElement] = Field(default=None, description="the rating score submitted by the reviewer")
    verified: Optional[StrictBool] = Field(default=None, description="indicates whether the review has the “Verified” mark")
    language: Optional[StrictStr] = Field(default=None, description="the language of the review")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when a review was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    title: Optional[StrictStr] = Field(default=None, description="the title of the review")
    review_text: Optional[StrictStr] = Field(default=None, description="the content of the review")
    review_images: Optional[List[Optional[StrictStr]]] = Field(default=None, description="images submitted by the reviewer. displays URLs to the images provided by the author of the review;. please note that Trustpilot doesn’t allow adding images to reviews, so the review_images parameter will always equal null")
    user_profile: Optional[BusinessDataUserProfileInfo] = Field(default=None, description="user profile of the reviewer")
    responses: Optional[List[Optional[ReviewResponseItemInfo]]] = Field(default=None, description="owner’s response to the submitted review")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "url", 
        "rating", 
        "verified", 
        "language", 
        "timestamp", 
        "title", 
        "review_text", 
        "review_images", 
        "user_profile", 
        "responses", 
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

        _dict['type'] = self.type
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['position'] = self.position
        _dict['url'] = self.url
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['verified'] = self.verified
        _dict['language'] = self.language
        _dict['timestamp'] = self.timestamp
        _dict['title'] = self.title
        _dict['review_text'] = self.review_text
        _dict['review_images'] = self.review_images
        _dict['user_profile'] = self.user_profile.to_dict() if self.user_profile else None
        responses_items = []
        if self.responses:
            for _item in self.responses:
                if _item:
                    responses_items.append(_item.to_dict())
            _dict['responses'] = responses_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "position": obj.get("position"),
            "url": obj.get("url"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "verified": obj.get("verified"),
            "language": obj.get("language"),
            "timestamp": obj.get("timestamp"),
            "title": obj.get("title"),
            "review_text": obj.get("review_text"),
            "review_images": obj.get("review_images"),
            "user_profile": BusinessDataUserProfileInfo.from_dict(obj["user_profile"]) if obj.get("user_profile") is not None else None,
            "responses": [ReviewResponseItemInfo.from_dict(_item) for _item in obj["responses"]] if obj.get("responses") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj