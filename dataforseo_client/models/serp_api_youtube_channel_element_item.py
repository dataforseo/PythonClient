from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_serp_api_youtube_organic_element_item import BaseSerpApiYoutubeOrganicElementItem



class SerpApiYoutubeChannelElementItem(BaseSerpApiYoutubeOrganicElementItem):
    """
    SerpApiYoutubeChannelElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description=r"group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description=r"absolute rank in SERP for the target domain. absolute position among all the elements in SERP")
    block_rank: Optional[StrictInt] = Field(default=None, description=r"block rank in SERP. position among all the blocks in SERP")
    block_name: Optional[StrictStr] = Field(default=None, description=r"name of the block in SERP. example:. 'People also watched'")
    channel_id: Optional[StrictStr] = Field(default=None, description=r"ID of the channel")
    url: Optional[StrictStr] = Field(default=None, description=r"URL of the channel")
    name: Optional[StrictStr] = Field(default=None, description=r"name of the channel")
    logo: Optional[StrictStr] = Field(default=None, description=r"the URL of the page where the logo image is hosted")
    video_count: Optional[StrictInt] = Field(default=None, description=r"the number of videos counted on the channel")
    is_verified: Optional[StrictBool] = Field(default=None, description=r"indicates whether the channel has a “verified” label")
    description: Optional[StrictStr] = Field(default=None, description=r"description of the channel")
    highlighted: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"highlighted keywords in the description")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "block_rank", 
        "block_name", 
        "channel_id", 
        "url", 
        "name", 
        "logo", 
        "video_count", 
        "is_verified", 
        "description", 
        "highlighted", 
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
        _dict['name'] = self.name
        _dict['logo'] = self.logo
        _dict['video_count'] = self.video_count
        _dict['is_verified'] = self.is_verified
        _dict['description'] = self.description
        _dict['highlighted'] = self.highlighted
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
            "name": obj.get("name"),
            "logo": obj.get("logo"),
            "video_count": obj.get("video_count"),
            "is_verified": obj.get("is_verified"),
            "description": obj.get("description"),
            "highlighted": obj.get("highlighted"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj