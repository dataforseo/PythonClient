from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self


from importlib import import_module
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dataforseo_client.models.serp_api_youtube_channel_element_item import SerpApiYoutubeChannelElementItem;
    from dataforseo_client.models.serp_api_youtube_video_element_item import SerpApiYoutubeVideoElementItem;
    from dataforseo_client.models.serp_api_youtube_video_paid_element_item import SerpApiYoutubeVideoPaidElementItem;
    from dataforseo_client.models.serp_api_youtube_playlist_element_item import SerpApiYoutubePlaylistElementItem;



class BaseSerpApiYoutubeOrganicElementItem(BaseModel):
    """
    BaseSerpApiYoutubeOrganicElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description=r"group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description=r"absolute rank in SERP for the target domain. absolute position among all the elements in SERP")
    block_rank: Optional[StrictInt] = Field(default=None, description=r"block rank in SERP. position among all the blocks in SERP")
    block_name: Optional[StrictStr] = Field(default=None, description=r"name of the block in SERP. example:. 'People also watched'")
    channel_id: Optional[StrictStr] = Field(default=None, description=r"ID of the channel")
    url: Optional[StrictStr] = Field(default=None, description=r"URL of the channel")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "block_rank", 
        "block_name", 
        "channel_id", 
        "url", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'youtube_channel': 'SerpApiYoutubeChannelElementItem',
        'youtube_video': 'SerpApiYoutubeVideoElementItem',
        'youtube_video_paid': 'SerpApiYoutubeVideoPaidElementItem',
        'youtube_playlist': 'SerpApiYoutubePlaylistElementItem',
    }

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
        return _dict


    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None
    
    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[
        SerpApiYoutubeChannelElementItem, 
        SerpApiYoutubeVideoElementItem, 
        SerpApiYoutubeVideoPaidElementItem, 
        SerpApiYoutubePlaylistElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'SerpApiYoutubeChannelElementItem':
            return import_module("dataforseo_client.models.serp_api_youtube_channel_element_item").SerpApiYoutubeChannelElementItem.from_dict(obj)
        if object_type == 'SerpApiYoutubeVideoElementItem':
            return import_module("dataforseo_client.models.serp_api_youtube_video_element_item").SerpApiYoutubeVideoElementItem.from_dict(obj)
        if object_type == 'SerpApiYoutubeVideoPaidElementItem':
            return import_module("dataforseo_client.models.serp_api_youtube_video_paid_element_item").SerpApiYoutubeVideoPaidElementItem.from_dict(obj)
        if object_type == 'SerpApiYoutubePlaylistElementItem':
            return import_module("dataforseo_client.models.serp_api_youtube_playlist_element_item").SerpApiYoutubePlaylistElementItem.from_dict(obj)

        return None