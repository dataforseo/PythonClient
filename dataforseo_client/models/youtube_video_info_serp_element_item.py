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
from dataforseo_client.models.base_youtube_serp_element_item import BaseYoutubeSerpElementItem
from dataforseo_client.models.channel_subscribers_count import ChannelSubscribersCount
from dataforseo_client.models.streaming_quality_element import StreamingQualityElement
from dataforseo_client.models.subtitles import Subtitles
from typing import Optional, Set
from typing_extensions import Self

class YoutubeVideoInfoSerpElementItem(BaseYoutubeSerpElementItem):
    """
    YoutubeVideoInfoSerpElementItem
    """ # noqa: E501
    video_id: Optional[StrictStr] = Field(default=None, description="ID of the video received in a POST array")
    title: Optional[StrictStr] = Field(default=None, description="title of the video")
    url: Optional[StrictStr] = Field(default=None, description="URL of the video")
    thumbnail_url: Optional[StrictStr] = Field(default=None, description="the URL of the page where the thumbnail is hosted")
    channel_id: Optional[StrictStr] = Field(default=None, description="the ID of the channel where the video is published")
    channel_name: Optional[StrictStr] = Field(default=None, description="the name of the channel where the video is published")
    channel_url: Optional[StrictStr] = Field(default=None, description="the URL of the channel where the video is published")
    channel_logo: Optional[StrictStr] = Field(default=None, description="the URL of the page where the logo image of the channel is hosted")
    description: Optional[StrictStr] = Field(default=None, description="description of the video")
    views_count: Optional[StrictInt] = Field(default=None, description="number of views of the video")
    likes_count: Optional[StrictInt] = Field(default=None, description="number of likes on the video")
    comments_count: Optional[StrictInt] = Field(default=None, description="number of comments on the video")
    channel_subscribers_count: Optional[ChannelSubscribersCount] = None
    publication_date: Optional[StrictStr] = Field(default=None, description="the date when the video is published")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the result is published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2022-11-15 12:57:46 +00:00")
    keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="keywords relevant to the video")
    category: Optional[StrictStr] = Field(default=None, description="the category the video belongs to")
    is_live: Optional[StrictBool] = Field(default=None, description="indicates whether the video is on live")
    is_embeddable: Optional[StrictBool] = Field(default=None, description="indicates whether the video is embeddable")
    duration_time: Optional[StrictStr] = Field(default=None, description="duration of the video")
    duration_time_seconds: Optional[StrictInt] = Field(default=None, description="duration of the video in seconds")
    subtitles: Optional[List[Subtitles]] = Field(default=None, description="array of elements describing properties of subtitles in the video")
    streaming_quality: Optional[List[StreamingQualityElement]] = Field(default=None, description="array of elements that contain information about all possible streaming qualities of the video")
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "video_id", "title", "url", "thumbnail_url", "channel_id", "channel_name", "channel_url", "channel_logo", "description", "views_count", "likes_count", "comments_count", "channel_subscribers_count", "publication_date", "timestamp", "keywords", "category", "is_live", "is_embeddable", "duration_time", "duration_time_seconds", "subtitles", "streaming_quality"]

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
        """Create an instance of YoutubeVideoInfoSerpElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of channel_subscribers_count
        if self.channel_subscribers_count:
            _dict['channel_subscribers_count'] = self.channel_subscribers_count.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in subtitles (list)
        _items = []
        if self.subtitles:
            for _item_subtitles in self.subtitles:
                if _item_subtitles:
                    _items.append(_item_subtitles.to_dict())
            _dict['subtitles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in streaming_quality (list)
        _items = []
        if self.streaming_quality:
            for _item_streaming_quality in self.streaming_quality:
                if _item_streaming_quality:
                    _items.append(_item_streaming_quality.to_dict())
            _dict['streaming_quality'] = _items
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

        # set to None if video_id (nullable) is None
        # and model_fields_set contains the field
        if self.video_id is None and "video_id" in self.model_fields_set:
            _dict['video_id'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if thumbnail_url (nullable) is None
        # and model_fields_set contains the field
        if self.thumbnail_url is None and "thumbnail_url" in self.model_fields_set:
            _dict['thumbnail_url'] = None

        # set to None if channel_id (nullable) is None
        # and model_fields_set contains the field
        if self.channel_id is None and "channel_id" in self.model_fields_set:
            _dict['channel_id'] = None

        # set to None if channel_name (nullable) is None
        # and model_fields_set contains the field
        if self.channel_name is None and "channel_name" in self.model_fields_set:
            _dict['channel_name'] = None

        # set to None if channel_url (nullable) is None
        # and model_fields_set contains the field
        if self.channel_url is None and "channel_url" in self.model_fields_set:
            _dict['channel_url'] = None

        # set to None if channel_logo (nullable) is None
        # and model_fields_set contains the field
        if self.channel_logo is None and "channel_logo" in self.model_fields_set:
            _dict['channel_logo'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if views_count (nullable) is None
        # and model_fields_set contains the field
        if self.views_count is None and "views_count" in self.model_fields_set:
            _dict['views_count'] = None

        # set to None if likes_count (nullable) is None
        # and model_fields_set contains the field
        if self.likes_count is None and "likes_count" in self.model_fields_set:
            _dict['likes_count'] = None

        # set to None if comments_count (nullable) is None
        # and model_fields_set contains the field
        if self.comments_count is None and "comments_count" in self.model_fields_set:
            _dict['comments_count'] = None

        # set to None if publication_date (nullable) is None
        # and model_fields_set contains the field
        if self.publication_date is None and "publication_date" in self.model_fields_set:
            _dict['publication_date'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        # set to None if keywords (nullable) is None
        # and model_fields_set contains the field
        if self.keywords is None and "keywords" in self.model_fields_set:
            _dict['keywords'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if is_live (nullable) is None
        # and model_fields_set contains the field
        if self.is_live is None and "is_live" in self.model_fields_set:
            _dict['is_live'] = None

        # set to None if is_embeddable (nullable) is None
        # and model_fields_set contains the field
        if self.is_embeddable is None and "is_embeddable" in self.model_fields_set:
            _dict['is_embeddable'] = None

        # set to None if duration_time (nullable) is None
        # and model_fields_set contains the field
        if self.duration_time is None and "duration_time" in self.model_fields_set:
            _dict['duration_time'] = None

        # set to None if duration_time_seconds (nullable) is None
        # and model_fields_set contains the field
        if self.duration_time_seconds is None and "duration_time_seconds" in self.model_fields_set:
            _dict['duration_time_seconds'] = None

        # set to None if subtitles (nullable) is None
        # and model_fields_set contains the field
        if self.subtitles is None and "subtitles" in self.model_fields_set:
            _dict['subtitles'] = None

        # set to None if streaming_quality (nullable) is None
        # and model_fields_set contains the field
        if self.streaming_quality is None and "streaming_quality" in self.model_fields_set:
            _dict['streaming_quality'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of YoutubeVideoInfoSerpElementItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "video_id": obj.get("video_id"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "thumbnail_url": obj.get("thumbnail_url"),
            "channel_id": obj.get("channel_id"),
            "channel_name": obj.get("channel_name"),
            "channel_url": obj.get("channel_url"),
            "channel_logo": obj.get("channel_logo"),
            "description": obj.get("description"),
            "views_count": obj.get("views_count"),
            "likes_count": obj.get("likes_count"),
            "comments_count": obj.get("comments_count"),
            "channel_subscribers_count": ChannelSubscribersCount.from_dict(obj["channel_subscribers_count"]) if obj.get("channel_subscribers_count") is not None else None,
            "publication_date": obj.get("publication_date"),
            "timestamp": obj.get("timestamp"),
            "keywords": obj.get("keywords"),
            "category": obj.get("category"),
            "is_live": obj.get("is_live"),
            "is_embeddable": obj.get("is_embeddable"),
            "duration_time": obj.get("duration_time"),
            "duration_time_seconds": obj.get("duration_time_seconds"),
            "subtitles": [Subtitles.from_dict(_item) for _item in obj["subtitles"]] if obj.get("subtitles") is not None else None,
            "streaming_quality": [StreamingQualityElement.from_dict(_item) for _item in obj["streaming_quality"]] if obj.get("streaming_quality") is not None else None
        })
        return _obj


