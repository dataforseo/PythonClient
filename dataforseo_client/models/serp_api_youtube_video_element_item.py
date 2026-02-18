from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_serp_api_youtube_organic_element_item import BaseSerpApiYoutubeOrganicElementItem



class SerpApiYoutubeVideoElementItem(BaseSerpApiYoutubeOrganicElementItem):
    """
    SerpApiYoutubeVideoElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description=r"group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description=r"absolute rank in SERP for the target domain. absolute position among all the elements in SERP")
    block_rank: Optional[StrictInt] = Field(default=None, description=r"block rank in SERP. position among all the blocks in SERP")
    block_name: Optional[StrictStr] = Field(default=None, description=r"name of the block in SERP. example:. 'People also watched'")
    channel_id: Optional[StrictStr] = Field(default=None, description=r"ID of the channel")
    url: Optional[StrictStr] = Field(default=None, description=r"URL of the channel")
    title: Optional[StrictStr] = Field(default=None, description=r"title of the video")
    video_id: Optional[StrictStr] = Field(default=None, description=r"ID of the video")
    thumbnail_url: Optional[StrictStr] = Field(default=None, description=r"the URL of the page where the thumbnail is hosted")
    channel_name: Optional[StrictStr] = Field(default=None, description=r"the name of the channel where the video is published")
    channel_url: Optional[StrictStr] = Field(default=None, description=r"the URL of the channel where the video is published")
    channel_logo: Optional[StrictStr] = Field(default=None, description=r"the URL of the page where the logo image of the channel is hosted")
    description: Optional[StrictStr] = Field(default=None, description=r"description of the channel")
    highlighted: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"highlighted keywords in the description")
    badges: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"video badges. example:. New, CC, 4K")
    is_live: Optional[StrictBool] = Field(default=None, description=r"indicates whether the video is a live broadcast")
    is_shorts: Optional[StrictBool] = Field(default=None, description=r"indicates whether the video is shorts")
    is_movie: Optional[StrictBool] = Field(default=None, description=r"indicates whether the video is a movie")
    views_count: Optional[StrictInt] = Field(default=None, description=r"number of views of the video")
    publication_date: Optional[StrictStr] = Field(default=None, description=r"the date when the video is published")
    timestamp: Optional[StrictStr] = Field(default=None, description=r"date and time when the result is published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2022-11-15 12:57:46 +00:00")
    duration_time: Optional[StrictStr] = Field(default=None, description=r"duration of the video")
    duration_time_seconds: Optional[StrictInt] = Field(default=None, description=r"duration of the video in seconds")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "block_rank", 
        "block_name", 
        "channel_id", 
        "url", 
        "title", 
        "video_id", 
        "thumbnail_url", 
        "channel_name", 
        "channel_url", 
        "channel_logo", 
        "description", 
        "highlighted", 
        "badges", 
        "is_live", 
        "is_shorts", 
        "is_movie", 
        "views_count", 
        "publication_date", 
        "timestamp", 
        "duration_time", 
        "duration_time_seconds", 
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
        _dict['block_rank'] = self.block_rank
        _dict['block_name'] = self.block_name
        _dict['channel_id'] = self.channel_id
        _dict['url'] = self.url
        _dict['title'] = self.title
        _dict['video_id'] = self.video_id
        _dict['thumbnail_url'] = self.thumbnail_url
        _dict['channel_name'] = self.channel_name
        _dict['channel_url'] = self.channel_url
        _dict['channel_logo'] = self.channel_logo
        _dict['description'] = self.description
        _dict['highlighted'] = self.highlighted
        _dict['badges'] = self.badges
        _dict['is_live'] = self.is_live
        _dict['is_shorts'] = self.is_shorts
        _dict['is_movie'] = self.is_movie
        _dict['views_count'] = self.views_count
        _dict['publication_date'] = self.publication_date
        _dict['timestamp'] = self.timestamp
        _dict['duration_time'] = self.duration_time
        _dict['duration_time_seconds'] = self.duration_time_seconds
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
            "block_rank": obj.get("block_rank"),
            "block_name": obj.get("block_name"),
            "channel_id": obj.get("channel_id"),
            "url": obj.get("url"),
            "title": obj.get("title"),
            "video_id": obj.get("video_id"),
            "thumbnail_url": obj.get("thumbnail_url"),
            "channel_name": obj.get("channel_name"),
            "channel_url": obj.get("channel_url"),
            "channel_logo": obj.get("channel_logo"),
            "description": obj.get("description"),
            "highlighted": obj.get("highlighted"),
            "badges": obj.get("badges"),
            "is_live": obj.get("is_live"),
            "is_shorts": obj.get("is_shorts"),
            "is_movie": obj.get("is_movie"),
            "views_count": obj.get("views_count"),
            "publication_date": obj.get("publication_date"),
            "timestamp": obj.get("timestamp"),
            "duration_time": obj.get("duration_time"),
            "duration_time_seconds": obj.get("duration_time_seconds"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj