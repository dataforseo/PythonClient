from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.spell_info import SpellInfo
from dataforseo_client.models.youtube_subtitles import YoutubeSubtitles



class SerpYoutubeVideoSubtitlesLiveAdvancedResultInfo(BaseModel):
    """
    SerpYoutubeVideoSubtitlesLiveAdvancedResultInfo
    """ # noqa: E501
    video_id: Optional[StrictStr] = Field(default=None, description="ID of the video received in a POST array")
    se_domain: Optional[StrictStr] = Field(default=None, description="search engine domain in a POST array")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to search engine results. you can use it to make sure that we provided accurate results")
    datetime: Optional[StrictStr] = Field(default=None, description="date and time when the result was received. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    spell: Optional[SpellInfo] = Field(default=None, description="autocorrection of the search engine. if the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="types of search results in SERP. contains types of search results (items) found in SERP.. possible item:. youtube_subtitles")
    unsupported_language: Optional[StrictBool] = Field(default=None, description="indicates whether the language is unsupported by the system")
    translate_language: Optional[StrictStr] = Field(default=None, description="language code of translated text")
    origin_language: Optional[StrictStr] = Field(default=None, description="language code of original text")
    category: Optional[StrictStr] = Field(default=None, description="the category the video belongs to")
    subtitles_count: Optional[StrictInt] = Field(default=None, description="number of subtitles in the video")
    title: Optional[StrictStr] = Field(default=None, description="title of the video")
    items_count: Optional[StrictInt] = Field(default=None, description="the number of results returned in the items array")
    items: Optional[List[Optional[YoutubeSubtitles]]] = Field(default=None, description="elements of search results found in SERP")
    __properties: ClassVar[List[str]] = [
        "video_id", 
        "se_domain", 
        "location_code", 
        "language_code", 
        "check_url", 
        "datetime", 
        "spell", 
        "item_types", 
        "unsupported_language", 
        "translate_language", 
        "origin_language", 
        "category", 
        "subtitles_count", 
        "title", 
        "items_count", 
        "items", 
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

        _dict['video_id'] = self.video_id
        _dict['se_domain'] = self.se_domain
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['check_url'] = self.check_url
        _dict['datetime'] = self.datetime
        _dict['spell'] = self.spell.to_dict() if self.spell else None
        _dict['item_types'] = self.item_types
        _dict['unsupported_language'] = self.unsupported_language
        _dict['translate_language'] = self.translate_language
        _dict['origin_language'] = self.origin_language
        _dict['category'] = self.category
        _dict['subtitles_count'] = self.subtitles_count
        _dict['title'] = self.title
        _dict['items_count'] = self.items_count
        items_items = []
        if self.items:
            for _item in self.items:
                if _item:
                    items_items.append(_item.to_dict())
            _dict['items'] = items_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "video_id": obj.get("video_id"),
            "se_domain": obj.get("se_domain"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "check_url": obj.get("check_url"),
            "datetime": obj.get("datetime"),
            "spell": SpellInfo.from_dict(obj["spell"]) if obj.get("spell") is not None else None,
            "item_types": obj.get("item_types"),
            "unsupported_language": obj.get("unsupported_language"),
            "translate_language": obj.get("translate_language"),
            "origin_language": obj.get("origin_language"),
            "category": obj.get("category"),
            "subtitles_count": obj.get("subtitles_count"),
            "title": obj.get("title"),
            "items_count": obj.get("items_count"),
            "items": [YoutubeSubtitles.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj