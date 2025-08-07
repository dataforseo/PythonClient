from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.event_dates import EventDates
from dataforseo_client.models.location_info import LocationInfo
from dataforseo_client.models.ai_mode_link_element_info import AiModeLinkElementInfo



class EventItem(BaseModel):
    """
    EventItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    title: Optional[StrictStr] = Field(default=None, description="title of the element")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    url: Optional[StrictStr] = Field(default=None, description="search URL with refinement parameters")
    image_url: Optional[StrictStr] = Field(default=None, description="URL of the image featured in the element")
    event_dates: Optional[EventDates] = Field(default=None, description="dates when the event takes place. if there are none, equals null")
    location_info: Optional[LocationInfo] = Field(default=None, description="information about the event’s venue")
    information_and_tickets: Optional[List[Optional[AiModeLinkElementInfo]]] = Field(default=None, description="additional information and ticket purchase options")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "title", 
        "description", 
        "url", 
        "image_url", 
        "event_dates", 
        "location_info", 
        "information_and_tickets", 
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
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
        _dict['title'] = self.title
        _dict['description'] = self.description
        _dict['url'] = self.url
        _dict['image_url'] = self.image_url
        _dict['event_dates'] = self.event_dates.to_dict() if self.event_dates else None
        _dict['location_info'] = self.location_info.to_dict() if self.location_info else None
        information_and_tickets_items = []
        if self.information_and_tickets:
            for _item in self.information_and_tickets:
                if _item:
                    information_and_tickets_items.append(_item.to_dict())
            _dict['information_and_tickets'] = information_and_tickets_items
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
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "url": obj.get("url"),
            "image_url": obj.get("image_url"),
            "event_dates": EventDates.from_dict(obj["event_dates"]) if obj.get("event_dates") is not None else None,
            "location_info": LocationInfo.from_dict(obj["location_info"]) if obj.get("location_info") is not None else None,
            "information_and_tickets": [AiModeLinkElementInfo.from_dict(_item) for _item in obj["information_and_tickets"]] if obj.get("information_and_tickets") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj