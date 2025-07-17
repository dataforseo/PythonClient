from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.on_page_resource_location_info import OnPageResourceLocationInfo



class WaterfallResourceInfo(BaseModel):
    """
    WaterfallResourceInfo
    """ # noqa: E501
    resource_type: Optional[StrictStr] = Field(default=None, description="")
    url: Optional[StrictStr] = Field(default=None, description="resource URL")
    initiator: Optional[StrictStr] = Field(default=None, description="resource initiator")
    duration_time: Optional[StrictInt] = Field(default=None, description="total time it takes until a browser receives a complete response from a server (in milliseconds)")
    fetch_start: Optional[StrictInt] = Field(default=None, description="time to start downloading the resource. the amount of time the browser needs to start downloading a resource")
    fetch_end: Optional[StrictInt] = Field(default=None, description="time to complete downloading the resource. the amount of time the browser needs to complete downloading a resource")
    location: Optional[OnPageResourceLocationInfo] = Field(default=None, description="location of the resource in the document. parameters defining the location of the specific resource within the document’s HTML")
    is_render_blocking: Optional[StrictBool] = Field(default=None, description="indicates whether the resource blocks rendering")
    __properties: ClassVar[List[str]] = [
        "resource_type", 
        "url", 
        "initiator", 
        "duration_time", 
        "fetch_start", 
        "fetch_end", 
        "location", 
        "is_render_blocking", 
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

        _dict['resource_type'] = self.resource_type
        _dict['url'] = self.url
        _dict['initiator'] = self.initiator
        _dict['duration_time'] = self.duration_time
        _dict['fetch_start'] = self.fetch_start
        _dict['fetch_end'] = self.fetch_end
        _dict['location'] = self.location.to_dict() if self.location else None
        _dict['is_render_blocking'] = self.is_render_blocking
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "resource_type": obj.get("resource_type"),
            "url": obj.get("url"),
            "initiator": obj.get("initiator"),
            "duration_time": obj.get("duration_time"),
            "fetch_start": obj.get("fetch_start"),
            "fetch_end": obj.get("fetch_end"),
            "location": OnPageResourceLocationInfo.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "is_render_blocking": obj.get("is_render_blocking"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj