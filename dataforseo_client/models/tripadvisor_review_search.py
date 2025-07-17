from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.image_url_info import ImageUrlInfo
from dataforseo_client.models.business_data_user_profile_info import BusinessDataUserProfileInfo
from dataforseo_client.models.review_response_item_info import ReviewResponseItemInfo



class TripadvisorReviewSearch(BaseModel):
    """
    TripadvisorReviewSearch
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank among all the listed reviews. absolute position among all reviews on the list")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the review in SERP. can take the following values: right")
    url: Optional[StrictStr] = Field(default=None, description="URL of the review")
    rating: Optional[RatingElement] = Field(default=None, description="the rating score submitted by the reviewer")
    date_of_visit: Optional[StrictStr] = Field(default=None, description="date of the reviewer’s visit to the local establishment. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the review was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    review_id: Optional[StrictStr] = Field(default=None, description="ID of the review")
    title: Optional[StrictStr] = Field(default=None, description="title of the review")
    review_text: Optional[StrictStr] = Field(default=None, description="content of the review")
    language: Optional[StrictStr] = Field(default=None, description="language of the review text")
    original_language: Optional[StrictStr] = Field(default=None, description="language of the untranslated review text")
    review_images: Optional[List[Optional[ImageUrlInfo]]] = Field(default=None, description="contains URLs of the images used in the review")
    user_profile: Optional[BusinessDataUserProfileInfo] = Field(default=None, description="information from the reviewer’s profile")
    responses: Optional[List[Optional[ReviewResponseItemInfo]]] = Field(default=None, description="contains information about the owner’s response")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "url", 
        "rating", 
        "date_of_visit", 
        "timestamp", 
        "review_id", 
        "title", 
        "review_text", 
        "language", 
        "original_language", 
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
        _dict['date_of_visit'] = self.date_of_visit
        _dict['timestamp'] = self.timestamp
        _dict['review_id'] = self.review_id
        _dict['title'] = self.title
        _dict['review_text'] = self.review_text
        _dict['language'] = self.language
        _dict['original_language'] = self.original_language
        review_images_items = []
        if self.review_images:
            for _item in self.review_images:
                if _item:
                    review_images_items.append(_item.to_dict())
            _dict['review_images'] = review_images_items
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
            "date_of_visit": obj.get("date_of_visit"),
            "timestamp": obj.get("timestamp"),
            "review_id": obj.get("review_id"),
            "title": obj.get("title"),
            "review_text": obj.get("review_text"),
            "language": obj.get("language"),
            "original_language": obj.get("original_language"),
            "review_images": [ImageUrlInfo.from_dict(_item) for _item in obj["review_images"]] if obj.get("review_images") is not None else None,
            "user_profile": BusinessDataUserProfileInfo.from_dict(obj["user_profile"]) if obj.get("user_profile") is not None else None,
            "responses": [ReviewResponseItemInfo.from_dict(_item) for _item in obj["responses"]] if obj.get("responses") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj