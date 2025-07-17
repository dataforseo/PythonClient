from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.channel_subscribers_count import ChannelSubscribersCount
from dataforseo_client.models.subtitles import Subtitles
from dataforseo_client.models.streaming_quality_element import StreamingQualityElement



class YoutubeVideoInfo(BaseModel):
    """
    YoutubeVideoInfo
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP for the target domain. absolute position among all the elements in SERP")
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
    channel_subscribers_count: Optional[ChannelSubscribersCount] = Field(default=None, description="number of subscribers of the channel")
    publication_date: Optional[StrictStr] = Field(default=None, description="the date when the video is published")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the result is published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2022-11-15 12:57:46 +00:00")
    keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="keywords relevant to the video")
    category: Optional[StrictStr] = Field(default=None, description="the category the video belongs to")
    is_live: Optional[StrictBool] = Field(default=None, description="indicates whether the video is on live")
    is_embeddable: Optional[StrictBool] = Field(default=None, description="indicates whether the video is embeddable")
    duration_time: Optional[StrictStr] = Field(default=None, description="duration of the video")
    duration_time_seconds: Optional[StrictInt] = Field(default=None, description="duration of the video in seconds")
    subtitles: Optional[List[Optional[Subtitles]]] = Field(default=None, description="array of elements describing properties of subtitles in the video")
    streaming_quality: Optional[List[Optional[StreamingQualityElement]]] = Field(default=None, description="array of elements that contain information about all possible streaming qualities of the video")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "video_id", 
        "title", 
        "url", 
        "thumbnail_url", 
        "channel_id", 
        "channel_name", 
        "channel_url", 
        "channel_logo", 
        "description", 
        "views_count", 
        "likes_count", 
        "comments_count", 
        "channel_subscribers_count", 
        "publication_date", 
        "timestamp", 
        "keywords", 
        "category", 
        "is_live", 
        "is_embeddable", 
        "duration_time", 
        "duration_time_seconds", 
        "subtitles", 
        "streaming_quality", 
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
        _dict['video_id'] = self.video_id
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['thumbnail_url'] = self.thumbnail_url
        _dict['channel_id'] = self.channel_id
        _dict['channel_name'] = self.channel_name
        _dict['channel_url'] = self.channel_url
        _dict['channel_logo'] = self.channel_logo
        _dict['description'] = self.description
        _dict['views_count'] = self.views_count
        _dict['likes_count'] = self.likes_count
        _dict['comments_count'] = self.comments_count
        _dict['channel_subscribers_count'] = self.channel_subscribers_count.to_dict() if self.channel_subscribers_count else None
        _dict['publication_date'] = self.publication_date
        _dict['timestamp'] = self.timestamp
        _dict['keywords'] = self.keywords
        _dict['category'] = self.category
        _dict['is_live'] = self.is_live
        _dict['is_embeddable'] = self.is_embeddable
        _dict['duration_time'] = self.duration_time
        _dict['duration_time_seconds'] = self.duration_time_seconds
        subtitles_items = []
        if self.subtitles:
            for _item in self.subtitles:
                if _item:
                    subtitles_items.append(_item.to_dict())
            _dict['subtitles'] = subtitles_items
        streaming_quality_items = []
        if self.streaming_quality:
            for _item in self.streaming_quality:
                if _item:
                    streaming_quality_items.append(_item.to_dict())
            _dict['streaming_quality'] = streaming_quality_items
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
            "streaming_quality": [StreamingQualityElement.from_dict(_item) for _item in obj["streaming_quality"]] if obj.get("streaming_quality") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj