from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.waterfall_resource_info import WaterfallResourceInfo



class OnPageWaterfallItem(BaseModel):
    """
    OnPageWaterfallItem
    """ # noqa: E501
    page_url: Optional[StrictStr] = Field(default=None, description="URL of the page")
    time_to_interactive: Optional[StrictInt] = Field(default=None, description="Time To Interactive (TTI) metric. the time it takes until the user can interact with a page (in milliseconds)")
    dom_complete: Optional[StrictInt] = Field(default=None, description="time to load resources. the time it takes until the page and all of its subresources are downloaded (in milliseconds)")
    connection_time: Optional[StrictInt] = Field(default=None, description="time to connect to a server. the time it takes until the connection with a server is established (in milliseconds)")
    time_to_secure_connection: Optional[StrictInt] = Field(default=None, description="time to establish a secure connection. the time it takes until the secure connection with a server is established (in milliseconds)")
    request_sent_time: Optional[StrictInt] = Field(default=None, description="time to send a request to a server. the time it takes until the request to a server is sent (in milliseconds)")
    waiting_time: Optional[StrictInt] = Field(default=None, description="time to first byte (TTFB) in milliseconds")
    download_time: Optional[StrictInt] = Field(default=None, description="time it takes for a browser to receive a response (in milliseconds)")
    duration_time: Optional[StrictInt] = Field(default=None, description="total time it takes until a browser receives a complete response from a server (in milliseconds)")
    fetch_start: Optional[StrictInt] = Field(default=None, description="time to start downloading the HTML resource. the amount of time the browser needs to start downloading a page")
    fetch_end: Optional[StrictInt] = Field(default=None, description="time to complete downloading the HTML resource. the amount of time the browser needs to complete downloading a page")
    resources: Optional[List[Optional[WaterfallResourceInfo]]] = Field(default=None, description="resource-specific timing. contains separate arrays with timing for each resource found on the page")
    __properties: ClassVar[List[str]] = [
        "page_url", 
        "time_to_interactive", 
        "dom_complete", 
        "connection_time", 
        "time_to_secure_connection", 
        "request_sent_time", 
        "waiting_time", 
        "download_time", 
        "duration_time", 
        "fetch_start", 
        "fetch_end", 
        "resources", 
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

        _dict['page_url'] = self.page_url
        _dict['time_to_interactive'] = self.time_to_interactive
        _dict['dom_complete'] = self.dom_complete
        _dict['connection_time'] = self.connection_time
        _dict['time_to_secure_connection'] = self.time_to_secure_connection
        _dict['request_sent_time'] = self.request_sent_time
        _dict['waiting_time'] = self.waiting_time
        _dict['download_time'] = self.download_time
        _dict['duration_time'] = self.duration_time
        _dict['fetch_start'] = self.fetch_start
        _dict['fetch_end'] = self.fetch_end
        resources_items = []
        if self.resources:
            for _item in self.resources:
                if _item:
                    resources_items.append(_item.to_dict())
            _dict['resources'] = resources_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "page_url": obj.get("page_url"),
            "time_to_interactive": obj.get("time_to_interactive"),
            "dom_complete": obj.get("dom_complete"),
            "connection_time": obj.get("connection_time"),
            "time_to_secure_connection": obj.get("time_to_secure_connection"),
            "request_sent_time": obj.get("request_sent_time"),
            "waiting_time": obj.get("waiting_time"),
            "download_time": obj.get("download_time"),
            "duration_time": obj.get("duration_time"),
            "fetch_start": obj.get("fetch_start"),
            "fetch_end": obj.get("fetch_end"),
            "resources": [WaterfallResourceInfo.from_dict(_item) for _item in obj["resources"]] if obj.get("resources") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj