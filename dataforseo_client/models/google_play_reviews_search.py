from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.app_user_profile_info import AppUserProfileInfo
from dataforseo_client.models.response_data_info import ResponseDataInfo



class GooglePlayReviewsSearch(BaseModel):
    """
    GooglePlayReviewsSearch
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank among all the listed reviews. absolute position among all reviews on the list")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the review in SERP. can take the following values: left")
    version: Optional[StrictStr] = Field(default=None, description="version of the app. version of the app for which the review is submitted")
    rating: Optional[RatingElement] = Field(default=None, description="the rating score submitted by the reviewer")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the review was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;. example:. 2019-11-15 12:57:46 +00:00")
    id: Optional[StrictStr] = Field(default=None, description="id of the review")
    helpful_count: Optional[StrictInt] = Field(default=None, description="number of helpful votes. indicates how many users considered the review helpful and voted with the thumbs up icon")
    title: Optional[StrictStr] = Field(default=None, description="title of the review. Google Play doesn’t provide an option to title reviews, so this parameter will always equal null")
    review_text: Optional[StrictStr] = Field(default=None, description="content of the review")
    user_profile: Optional[AppUserProfileInfo] = Field(default=None, description="user profile of the reviewer")
    responses: Optional[List[Optional[ResponseDataInfo]]] = Field(default=None, description="response from the developer")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "version", 
        "rating", 
        "timestamp", 
        "id", 
        "helpful_count", 
        "title", 
        "review_text", 
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
        _dict['version'] = self.version
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['timestamp'] = self.timestamp
        _dict['id'] = self.id
        _dict['helpful_count'] = self.helpful_count
        _dict['title'] = self.title
        _dict['review_text'] = self.review_text
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
            "version": obj.get("version"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "timestamp": obj.get("timestamp"),
            "id": obj.get("id"),
            "helpful_count": obj.get("helpful_count"),
            "title": obj.get("title"),
            "review_text": obj.get("review_text"),
            "user_profile": AppUserProfileInfo.from_dict(obj["user_profile"]) if obj.get("user_profile") is not None else None,
            "responses": [ResponseDataInfo.from_dict(_item) for _item in obj["responses"]] if obj.get("responses") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj