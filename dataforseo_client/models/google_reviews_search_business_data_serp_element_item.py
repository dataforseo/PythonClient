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

from pydantic import ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.base_business_data_serp_element_item import BaseBusinessDataSerpElementItem
from dataforseo_client.models.images_element import ImagesElement
from dataforseo_client.models.rating_info import RatingInfo
from dataforseo_client.models.review_highlights import ReviewHighlights
from typing import Optional, Set
from typing_extensions import Self

class GoogleReviewsSearchBusinessDataSerpElementItem(BaseBusinessDataSerpElementItem):
    """
    GoogleReviewsSearchBusinessDataSerpElementItem
    """ # noqa: E501
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the review in SERP can take the following values: right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the review")
    review_text: Optional[StrictStr] = Field(default=None, description="the content of the review")
    original_review_text: Optional[StrictStr] = Field(default=None, description="original content of the review the original content of the review, no auto-translate applied")
    time_ago: Optional[StrictStr] = Field(default=None, description="the time of publication indicates the time (in the ‘time ago’ format) when the review was listed")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when a review was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    rating: Optional[RatingInfo] = None
    reviews_count: Optional[StrictInt] = Field(default=None, description="total number of reviews submitted by the reviewer")
    photos_count: Optional[StrictInt] = Field(default=None, description="total number of photos submitted by the reviewer")
    local_guide: Optional[StrictBool] = Field(default=None, description="indicates whether the reviewer has a ‘local guide’ status")
    profile_name: Optional[StrictStr] = Field(default=None, description="profile name of the reviewer")
    profile_url: Optional[StrictStr] = Field(default=None, description="URL of the reviewer’s profile")
    review_url: Optional[StrictStr] = Field(default=None, description="the URL of the review")
    profile_image_url: Optional[StrictStr] = Field(default=None, description="URL of the reviewer’s profile image")
    owner_answer: Optional[StrictStr] = Field(default=None, description="text of the owner’s response the owner’s response to the review")
    original_owner_answer: Optional[StrictStr] = Field(default=None, description="original text of the owner’s response the original response to the review, no auto-translate applied")
    owner_time_ago: Optional[StrictStr] = Field(default=None, description="publication time indicates the time (in the ‘time ago’ format) when the owner submitted the response to the review")
    owner_timestamp: Optional[StrictStr] = Field(default=None, description="date and time of the owner’s reply to the review in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    review_id: Optional[StrictStr] = Field(default=None, description="the unique identifier of a review on Google example: ChZDSUhNMG9nS0VJQ0FnSUMxbHFyMFlnEAE")
    images: Optional[List[ImagesElement]] = Field(default=None, description="images submitted by the reviewer")
    review_highlights: Optional[List[ReviewHighlights]] = Field(default=None, description="review highlights contains highlighted review criteria and assessments")
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "position", "xpath", "review_text", "original_review_text", "time_ago", "timestamp", "rating", "reviews_count", "photos_count", "local_guide", "profile_name", "profile_url", "review_url", "profile_image_url", "owner_answer", "original_owner_answer", "owner_time_ago", "owner_timestamp", "review_id", "images", "review_highlights"]

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
        """Create an instance of GoogleReviewsSearchBusinessDataSerpElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rating
        if self.rating:
            _dict['rating'] = self.rating.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item_images in self.images:
                if _item_images:
                    _items.append(_item_images.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in review_highlights (list)
        _items = []
        if self.review_highlights:
            for _item_review_highlights in self.review_highlights:
                if _item_review_highlights:
                    _items.append(_item_review_highlights.to_dict())
            _dict['review_highlights'] = _items
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if rank_group (nullable) is None
        # and model_fields_set contains the field
        if self.rank_group is None and "rank_group" in self.model_fields_set:
            _dict['rank_group'] = None

        # set to None if rank_absolute (nullable) is None
        # and model_fields_set contains the field
        if self.rank_absolute is None and "rank_absolute" in self.model_fields_set:
            _dict['rank_absolute'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if xpath (nullable) is None
        # and model_fields_set contains the field
        if self.xpath is None and "xpath" in self.model_fields_set:
            _dict['xpath'] = None

        # set to None if review_text (nullable) is None
        # and model_fields_set contains the field
        if self.review_text is None and "review_text" in self.model_fields_set:
            _dict['review_text'] = None

        # set to None if original_review_text (nullable) is None
        # and model_fields_set contains the field
        if self.original_review_text is None and "original_review_text" in self.model_fields_set:
            _dict['original_review_text'] = None

        # set to None if time_ago (nullable) is None
        # and model_fields_set contains the field
        if self.time_ago is None and "time_ago" in self.model_fields_set:
            _dict['time_ago'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        # set to None if reviews_count (nullable) is None
        # and model_fields_set contains the field
        if self.reviews_count is None and "reviews_count" in self.model_fields_set:
            _dict['reviews_count'] = None

        # set to None if photos_count (nullable) is None
        # and model_fields_set contains the field
        if self.photos_count is None and "photos_count" in self.model_fields_set:
            _dict['photos_count'] = None

        # set to None if local_guide (nullable) is None
        # and model_fields_set contains the field
        if self.local_guide is None and "local_guide" in self.model_fields_set:
            _dict['local_guide'] = None

        # set to None if profile_name (nullable) is None
        # and model_fields_set contains the field
        if self.profile_name is None and "profile_name" in self.model_fields_set:
            _dict['profile_name'] = None

        # set to None if profile_url (nullable) is None
        # and model_fields_set contains the field
        if self.profile_url is None and "profile_url" in self.model_fields_set:
            _dict['profile_url'] = None

        # set to None if review_url (nullable) is None
        # and model_fields_set contains the field
        if self.review_url is None and "review_url" in self.model_fields_set:
            _dict['review_url'] = None

        # set to None if profile_image_url (nullable) is None
        # and model_fields_set contains the field
        if self.profile_image_url is None and "profile_image_url" in self.model_fields_set:
            _dict['profile_image_url'] = None

        # set to None if owner_answer (nullable) is None
        # and model_fields_set contains the field
        if self.owner_answer is None and "owner_answer" in self.model_fields_set:
            _dict['owner_answer'] = None

        # set to None if original_owner_answer (nullable) is None
        # and model_fields_set contains the field
        if self.original_owner_answer is None and "original_owner_answer" in self.model_fields_set:
            _dict['original_owner_answer'] = None

        # set to None if owner_time_ago (nullable) is None
        # and model_fields_set contains the field
        if self.owner_time_ago is None and "owner_time_ago" in self.model_fields_set:
            _dict['owner_time_ago'] = None

        # set to None if owner_timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.owner_timestamp is None and "owner_timestamp" in self.model_fields_set:
            _dict['owner_timestamp'] = None

        # set to None if review_id (nullable) is None
        # and model_fields_set contains the field
        if self.review_id is None and "review_id" in self.model_fields_set:
            _dict['review_id'] = None

        # set to None if images (nullable) is None
        # and model_fields_set contains the field
        if self.images is None and "images" in self.model_fields_set:
            _dict['images'] = None

        # set to None if review_highlights (nullable) is None
        # and model_fields_set contains the field
        if self.review_highlights is None and "review_highlights" in self.model_fields_set:
            _dict['review_highlights'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GoogleReviewsSearchBusinessDataSerpElementItem from a dict"""
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
            "rating": RatingInfo.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
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
            "images": [ImagesElement.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "review_highlights": [ReviewHighlights.from_dict(_item) for _item in obj["review_highlights"]] if obj.get("review_highlights") is not None else None
        })
        return _obj


