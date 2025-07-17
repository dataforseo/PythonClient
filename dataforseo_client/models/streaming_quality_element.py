from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class StreamingQualityElement(BaseModel):
    """
    StreamingQualityElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    label: Optional[StrictStr] = Field(default=None, description="label of the quality element")
    width: Optional[StrictInt] = Field(default=None, description="video width in pixels")
    height: Optional[StrictInt] = Field(default=None, description="video height in pixels")
    bitrate: Optional[StrictInt] = Field(default=None, description="bit rate of the video")
    mime_type: Optional[StrictStr] = Field(default=None, description="media type of the video")
    fps: Optional[StrictInt] = Field(default=None, description="frame rate of the video")
    __properties: ClassVar[List[str]] = [
        "type", 
        "label", 
        "width", 
        "height", 
        "bitrate", 
        "mime_type", 
        "fps", 
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
        _dict['label'] = self.label
        _dict['width'] = self.width
        _dict['height'] = self.height
        _dict['bitrate'] = self.bitrate
        _dict['mime_type'] = self.mime_type
        _dict['fps'] = self.fps
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "label": obj.get("label"),
            "width": obj.get("width"),
            "height": obj.get("height"),
            "bitrate": obj.get("bitrate"),
            "mime_type": obj.get("mime_type"),
            "fps": obj.get("fps"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj