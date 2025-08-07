from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_serp_api_google_news_element_item import BaseSerpApiGoogleNewsElementItem
from dataforseo_client.models.ai_mode_rectangle_info import AiModeRectangleInfo



class SerpApiGoogleNewsNewsSearchElementItem(BaseSerpApiGoogleNewsElementItem):
    """
    SerpApiGoogleNewsNewsSearchElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    title: Optional[StrictStr] = Field(default=None, description="title of the element")
    rectangle: Optional[AiModeRectangleInfo] = Field(default=None, description="rectangle parameters. contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP. equals null if calculate_rectangles in the POST request is not set to true")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    url: Optional[StrictStr] = Field(default=None, description="search URL with refinement parameters")
    image_url: Optional[StrictStr] = Field(default=None, description="URL of the image. the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available)")
    snippet: Optional[StrictStr] = Field(default=None, description="snippet of the result in SERP")
    time_published: Optional[StrictStr] = Field(default=None, description="indicates the time the result was published")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the news was published. in the format “year-month-date:minutes:UTC_difference_hours:UTC_difference_minutes”. example:. 2019-11-15 12:57:46 +00:00")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "xpath", 
        "title", 
        "rectangle", 
        "domain", 
        "url", 
        "image_url", 
        "snippet", 
        "time_published", 
        "timestamp", 
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
        _dict['xpath'] = self.xpath
        _dict['title'] = self.title
        _dict['rectangle'] = self.rectangle.to_dict() if self.rectangle else None
        _dict['domain'] = self.domain
        _dict['url'] = self.url
        _dict['image_url'] = self.image_url
        _dict['snippet'] = self.snippet
        _dict['time_published'] = self.time_published
        _dict['timestamp'] = self.timestamp
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
            "xpath": obj.get("xpath"),
            "title": obj.get("title"),
            "rectangle": AiModeRectangleInfo.from_dict(obj["rectangle"]) if obj.get("rectangle") is not None else None,
            "domain": obj.get("domain"),
            "url": obj.get("url"),
            "image_url": obj.get("image_url"),
            "snippet": obj.get("snippet"),
            "time_published": obj.get("time_published"),
            "timestamp": obj.get("timestamp"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj