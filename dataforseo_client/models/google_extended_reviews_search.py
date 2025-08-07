from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.ai_mode_images_element_info import AiModeImagesElementInfo
from dataforseo_client.models.review_highlights import ReviewHighlights
from dataforseo_client.models.source import Source



class GoogleExtendedReviewsSearch(BaseModel):
    """
    GoogleExtendedReviewsSearch
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank among all the listed reviews. absolute position among all reviews on the list")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the review in SERP. can take the following values: right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the review")
    review_text: Optional[StrictStr] = Field(default=None, description="the content of the review")
    original_review_text: Optional[StrictStr] = Field(default=None, description="original content of the review. the original content of the review, no auto-translate applied")
    time_ago: Optional[StrictStr] = Field(default=None, description="the time of publication. indicates the time (in the ‘time ago’ format) when the review was listed")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when a review was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    rating: Optional[RatingElement] = Field(default=None, description="the rating score submitted by the reviewer")
    reviews_count: Optional[StrictInt] = Field(default=None, description="total number of reviews submitted by the reviewer")
    photos_count: Optional[StrictInt] = Field(default=None, description="total number of photos submitted by the reviewer")
    local_guide: Optional[StrictBool] = Field(default=None, description="indicates whether the reviewer has a ‘local guide’ status")
    profile_name: Optional[StrictStr] = Field(default=None, description="profile name of the reviewer")
    profile_url: Optional[StrictStr] = Field(default=None, description="URL of the reviewer’s profile")
    review_url: Optional[StrictStr] = Field(default=None, description="the URL of the review")
    profile_image_url: Optional[StrictStr] = Field(default=None, description="URL of the reviewer’s profile image")
    owner_answer: Optional[StrictStr] = Field(default=None, description="text of the owner’s response. the owner’s response to the review")
    original_owner_answer: Optional[StrictStr] = Field(default=None, description="original text of the owner’s response. the original response to the review, no auto-translate applied")
    owner_time_ago: Optional[StrictStr] = Field(default=None, description="publication time. indicates the time (in the ‘time ago’ format) when the owner submitted the response to the review")
    owner_timestamp: Optional[StrictStr] = Field(default=None, description="date and time of the owner’s reply to the review. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    review_id: Optional[StrictStr] = Field(default=None, description="the unique identifier of a review on Google. example:. ChZDSUhNMG9nS0VJQ0FnSUMxbHFyMFlnEAE")
    images: Optional[List[Optional[AiModeImagesElementInfo]]] = Field(default=None, description="images submitted by the reviewer")
    review_highlights: Optional[List[Optional[ReviewHighlights]]] = Field(default=None, description="review highlights. contains highlighted review criteria and assessments")
    source: Optional[Source] = Field(default=None, description="source of the review. contains information about the source where the review was posted")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "review_text", 
        "original_review_text", 
        "time_ago", 
        "timestamp", 
        "rating", 
        "reviews_count", 
        "photos_count", 
        "local_guide", 
        "profile_name", 
        "profile_url", 
        "review_url", 
        "profile_image_url", 
        "owner_answer", 
        "original_owner_answer", 
        "owner_time_ago", 
        "owner_timestamp", 
        "review_id", 
        "images", 
        "review_highlights", 
        "source", 
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
        _dict['xpath'] = self.xpath
        _dict['review_text'] = self.review_text
        _dict['original_review_text'] = self.original_review_text
        _dict['time_ago'] = self.time_ago
        _dict['timestamp'] = self.timestamp
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['reviews_count'] = self.reviews_count
        _dict['photos_count'] = self.photos_count
        _dict['local_guide'] = self.local_guide
        _dict['profile_name'] = self.profile_name
        _dict['profile_url'] = self.profile_url
        _dict['review_url'] = self.review_url
        _dict['profile_image_url'] = self.profile_image_url
        _dict['owner_answer'] = self.owner_answer
        _dict['original_owner_answer'] = self.original_owner_answer
        _dict['owner_time_ago'] = self.owner_time_ago
        _dict['owner_timestamp'] = self.owner_timestamp
        _dict['review_id'] = self.review_id
        images_items = []
        if self.images:
            for _item in self.images:
                if _item:
                    images_items.append(_item.to_dict())
            _dict['images'] = images_items
        review_highlights_items = []
        if self.review_highlights:
            for _item in self.review_highlights:
                if _item:
                    review_highlights_items.append(_item.to_dict())
            _dict['review_highlights'] = review_highlights_items
        _dict['source'] = self.source.to_dict() if self.source else None
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
            "xpath": obj.get("xpath"),
            "review_text": obj.get("review_text"),
            "original_review_text": obj.get("original_review_text"),
            "time_ago": obj.get("time_ago"),
            "timestamp": obj.get("timestamp"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "reviews_count": obj.get("reviews_count"),
            "photos_count": obj.get("photos_count"),
            "local_guide": obj.get("local_guide"),
            "profile_name": obj.get("profile_name"),
            "profile_url": obj.get("profile_url"),
            "review_url": obj.get("review_url"),
            "profile_image_url": obj.get("profile_image_url"),
            "owner_answer": obj.get("owner_answer"),
            "original_owner_answer": obj.get("original_owner_answer"),
            "owner_time_ago": obj.get("owner_time_ago"),
            "owner_timestamp": obj.get("owner_timestamp"),
            "review_id": obj.get("review_id"),
            "images": [AiModeImagesElementInfo.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "review_highlights": [ReviewHighlights.from_dict(_item) for _item in obj["review_highlights"]] if obj.get("review_highlights") is not None else None,
            "source": Source.from_dict(obj["source"]) if obj.get("source") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj