from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class PreviewVideos(BaseModel):
    """
    PreviewVideos
    """ # noqa: E501
    video_id: Optional[StrictStr] = Field(default=None, description=r"ID of the video")
    title: Optional[StrictStr] = Field(default=None, description=r"title of the video")
    url: Optional[StrictStr] = Field(default=None, description=r"URL of the video")
    duration_time: Optional[StrictStr] = Field(default=None, description=r"duration of the video")
    duration_time_seconds: Optional[StrictInt] = Field(default=None, description=r"duration of the video in seconds")
    __properties: ClassVar[List[str]] = [
        "video_id", 
        "title", 
        "url", 
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

        _dict['video_id'] = self.video_id
        _dict['title'] = self.title
        _dict['url'] = self.url
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
            "video_id": obj.get("video_id"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "duration_time": obj.get("duration_time"),
            "duration_time_seconds": obj.get("duration_time_seconds"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj