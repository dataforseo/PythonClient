from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.preview_image import PreviewImage



class AdsSearch(BaseModel):
    """
    AdsSearch
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    advertiser_id: Optional[StrictStr] = Field(default=None, description="unique identifier of the advertiser account")
    creative_id: Optional[StrictStr] = Field(default=None, description="unique identifier of the advertisement")
    title: Optional[StrictStr] = Field(default=None, description="title of the element")
    url: Optional[StrictStr] = Field(default=None, description="search URL with refinement parameters")
    verified: Optional[StrictBool] = Field(default=None, description="verified advertiser account. equals true if advertiser account is verified by Google Ads")
    format: Optional[StrictStr] = Field(default=None, description="format of the advertisement. possible values: text, image, video")
    preview_image: Optional[PreviewImage] = Field(default=None, description="preview image of the advertisement")
    preview_url: Optional[StrictStr] = Field(default=None, description="url pointing to the ad preview")
    first_shown: Optional[StrictStr] = Field(default=None, description="date and time when the ad was shown for the first time. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”")
    last_shown: Optional[StrictStr] = Field(default=None, description="date and time when the ad was shown the last time. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "advertiser_id", 
        "creative_id", 
        "title", 
        "url", 
        "verified", 
        "format", 
        "preview_image", 
        "preview_url", 
        "first_shown", 
        "last_shown", 
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
        _dict['advertiser_id'] = self.advertiser_id
        _dict['creative_id'] = self.creative_id
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['verified'] = self.verified
        _dict['format'] = self.format
        _dict['preview_image'] = self.preview_image.to_dict() if self.preview_image else None
        _dict['preview_url'] = self.preview_url
        _dict['first_shown'] = self.first_shown
        _dict['last_shown'] = self.last_shown
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
            "advertiser_id": obj.get("advertiser_id"),
            "creative_id": obj.get("creative_id"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "verified": obj.get("verified"),
            "format": obj.get("format"),
            "preview_image": PreviewImage.from_dict(obj["preview_image"]) if obj.get("preview_image") is not None else None,
            "preview_url": obj.get("preview_url"),
            "first_shown": obj.get("first_shown"),
            "last_shown": obj.get("last_shown"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj