from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_mode_images_element_info import AiModeImagesElementInfo
from dataforseo_client.models.video_element import VideoElement
from dataforseo_client.models.user_profile_info import UserProfileInfo
from dataforseo_client.models.rating_element import RatingElement



class AmazonReviewItem(BaseModel):
    """
    AmazonReviewItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank among all the listed reviews. absolute position among all reviews on the list")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the review in SERP. can take the following values: right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    verified: Optional[StrictBool] = Field(default=None, description="indicates whether the review has the “Verified Purchase” mark")
    subtitle: Optional[StrictStr] = Field(default=None, description="subtitle of the review")
    helpful_votes: Optional[StrictStr] = Field(default=None, description="helpful votes count. number of users who clicked on the ‘Helpful” button under the review text")
    images: Optional[List[Optional[AiModeImagesElementInfo]]] = Field(default=None, description="images of the product submitted by the reviewer")
    videos: Optional[List[Optional[VideoElement]]] = Field(default=None, description="videos of the product submitted by the reviewer")
    user_profile: Optional[UserProfileInfo] = Field(default=None, description="user profile of the reviewer")
    title: Optional[StrictStr] = Field(default=None, description="title of the review")
    url: Optional[StrictStr] = Field(default=None, description="URL to the reviewer’s profile")
    review_text: Optional[StrictStr] = Field(default=None, description="content of the review")
    publication_date: Optional[StrictStr] = Field(default=None, description="date and time when the review was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;. example:. 2019-11-15 12:57:46 +00:00")
    rating: Optional[RatingElement] = Field(default=None, description="the rating score submitted by the reviewer")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "verified", 
        "subtitle", 
        "helpful_votes", 
        "images", 
        "videos", 
        "user_profile", 
        "title", 
        "url", 
        "review_text", 
        "publication_date", 
        "rating", 
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
        _dict['verified'] = self.verified
        _dict['subtitle'] = self.subtitle
        _dict['helpful_votes'] = self.helpful_votes
        images_items = []
        if self.images:
            for _item in self.images:
                if _item:
                    images_items.append(_item.to_dict())
            _dict['images'] = images_items
        videos_items = []
        if self.videos:
            for _item in self.videos:
                if _item:
                    videos_items.append(_item.to_dict())
            _dict['videos'] = videos_items
        _dict['user_profile'] = self.user_profile.to_dict() if self.user_profile else None
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['review_text'] = self.review_text
        _dict['publication_date'] = self.publication_date
        _dict['rating'] = self.rating.to_dict() if self.rating else None
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
            "verified": obj.get("verified"),
            "subtitle": obj.get("subtitle"),
            "helpful_votes": obj.get("helpful_votes"),
            "images": [AiModeImagesElementInfo.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "videos": [VideoElement.from_dict(_item) for _item in obj["videos"]] if obj.get("videos") is not None else None,
            "user_profile": UserProfileInfo.from_dict(obj["user_profile"]) if obj.get("user_profile") is not None else None,
            "title": obj.get("title"),
            "url": obj.get("url"),
            "review_text": obj.get("review_text"),
            "publication_date": obj.get("publication_date"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj