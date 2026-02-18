from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.preview_videos import PreviewVideos
from dataforseo_client.models.base_serp_api_youtube_organic_element_item import BaseSerpApiYoutubeOrganicElementItem



class SerpApiYoutubePlaylistElementItem(BaseSerpApiYoutubeOrganicElementItem):
    """
    SerpApiYoutubePlaylistElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description=r"group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description=r"absolute rank in SERP for the target domain. absolute position among all the elements in SERP")
    block_rank: Optional[StrictInt] = Field(default=None, description=r"block rank in SERP. position among all the blocks in SERP")
    block_name: Optional[StrictStr] = Field(default=None, description=r"name of the block in SERP. example:. 'People also watched'")
    channel_id: Optional[StrictStr] = Field(default=None, description=r"ID of the channel")
    url: Optional[StrictStr] = Field(default=None, description=r"URL of the channel")
    title: Optional[StrictStr] = Field(default=None, description=r"title of the video")
    playlist_id: Optional[StrictStr] = Field(default=None, description=r"ID of the video")
    thumbnail_url: Optional[StrictStr] = Field(default=None, description=r"the URL of the page where the thumbnail is hosted")
    channel_name: Optional[StrictStr] = Field(default=None, description=r"the name of the channel where the video is published")
    channel_url: Optional[StrictStr] = Field(default=None, description=r"the URL of the channel where the video is published")
    channel_logo: Optional[StrictStr] = Field(default=None, description=r"the URL of the page where the logo image of the channel is hosted")
    videos_count: Optional[StrictInt] = Field(default=None, description=r"the number of videos in playlist")
    preview_videos: Optional[List[Optional[PreviewVideos]]] = Field(default=None, description=r"information about preview videos. array of objects containing information about videos in the preview block of the playlist element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "block_rank", 
        "block_name", 
        "channel_id", 
        "url", 
        "title", 
        "playlist_id", 
        "thumbnail_url", 
        "channel_name", 
        "channel_url", 
        "channel_logo", 
        "videos_count", 
        "preview_videos", 
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
        _dict['playlist_id'] = self.playlist_id
        _dict['thumbnail_url'] = self.thumbnail_url
        _dict['channel_name'] = self.channel_name
        _dict['channel_url'] = self.channel_url
        _dict['channel_logo'] = self.channel_logo
        _dict['videos_count'] = self.videos_count
        preview_videos_items = []
        if self.preview_videos:
            for _item in self.preview_videos:
                if _item:
                    preview_videos_items.append(_item.to_dict())
            _dict['preview_videos'] = preview_videos_items
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
            "playlist_id": obj.get("playlist_id"),
            "thumbnail_url": obj.get("thumbnail_url"),
            "channel_name": obj.get("channel_name"),
            "channel_url": obj.get("channel_url"),
            "channel_logo": obj.get("channel_logo"),
            "videos_count": obj.get("videos_count"),
            "preview_videos": [PreviewVideos.from_dict(_item) for _item in obj["preview_videos"]] if obj.get("preview_videos") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj