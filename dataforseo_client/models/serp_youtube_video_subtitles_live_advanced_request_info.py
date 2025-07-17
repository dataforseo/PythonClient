from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpYoutubeVideoSubtitlesLiveAdvancedRequestInfo(BaseModel):
    """
    SerpYoutubeVideoSubtitlesLiveAdvancedRequestInfo
    """ # noqa: E501
    video_id: Optional[StrictStr] = Field(default=None, description="ID of the video. required field. you can find video ID in the URL or ‘youtube_video’ item of YouTube Organic result. example:. Y8Wu4rSNJms")
    subtitles_language: Optional[StrictStr] = Field(default=None, description="language code of original text. you can get the language code from YouTube Video Info result")
    subtitles_translate_language: Optional[StrictStr] = Field(default=None, description="language code of translated text. possible values:. 'az', 'ay', 'ak', 'sq', 'am', 'en', 'ar', 'hy', 'as', 'af', 'eu', 'be', 'bn', 'my', 'bg', 'bs', 'bho', 'cy', 'hu', 'vi', 'haw', 'ht', 'gl', 'lg', 'el', 'ka', 'gn', 'gu', 'gd', 'da', 'fy', 'zu', 'iw', 'ig', 'yi', 'id', 'ga', 'is', 'es', 'it', 'yo', 'kk', 'kn', 'ca', 'qu', 'rw', 'ky', 'zh-Hant', 'zh-Hans', 'ko', 'co', 'xh', 'ku', 'km', 'lo', 'la', 'lv', 'ln', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'dv', 'mt', 'mi', 'mr', 'mn', 'und', 'de', 'ne', 'nl', 'no', 'ny', 'or', 'om', 'pa', 'fa', 'pl', 'pt', 'ps', 'ro', 'ru', 'sm', 'sa', 'ceb', 'nso', 'sr', 'si', 'sd', 'sk', 'sl', 'so', 'sw', 'su', 'tg', 'th', 'ta', 'tt', 'te', 'ti', 'ts', 'tr', 'tk', 'uz', 'ug', 'uk', 'ur', 'fil', 'fi', 'fr', 'ha', 'hi', 'hmn', 'hr', 'cs', 'sv', 'sn', 'ee', 'eo', 'et', 'st', 'jv', 'ja', 'kri'")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location. required field if you don’t specify location_code. if you use this field, you don’t need to specify location_code. you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/locations. example:. United States")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code. required field if you don’t specify location_name . if you use this field, you don’t need to specify location_name. you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/locations. example:. 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language. required field if you don’t specify language_code. if you use this field, you don’t need to specify language_code. you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code. required field if you don’t specify language_name. if you use this field, you don’t need to specify language_name. you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/languages. example:. en")
    device: Optional[StrictStr] = Field(default=None, description="device type. optional field. only value: desktop")
    os: Optional[StrictStr] = Field(default=None, description="device operating system. optional field. choose from the following values: windows, macos. default value: windows")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "video_id", 
        "subtitles_language", 
        "subtitles_translate_language", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "device", 
        "os", 
        "tag", 
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
        _dict['subtitles_language'] = self.subtitles_language
        _dict['subtitles_translate_language'] = self.subtitles_translate_language
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['device'] = self.device
        _dict['os'] = self.os
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "video_id": obj.get("video_id"),
            "subtitles_language": obj.get("subtitles_language"),
            "subtitles_translate_language": obj.get("subtitles_translate_language"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "device": obj.get("device"),
            "os": obj.get("os"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj