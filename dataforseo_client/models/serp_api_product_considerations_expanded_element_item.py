from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.about_this_result_element import AboutThisResultElement
from dataforseo_client.models.base_serp_api_product_consideration_expanded_element_item import BaseSerpApiProductConsiderationExpandedElementItem



class SerpApiProductConsiderationsExpandedElementItem(BaseSerpApiProductConsiderationExpandedElementItem):
    """
    SerpApiProductConsiderationsExpandedElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="title of the row")
    featured_title: Optional[StrictStr] = Field(default=None, description="the title of the featured snippets source page")
    breadcrumb: Optional[StrictStr] = Field(default=None, description="breadcrumb of the Ad element in SERP")
    snippet: Optional[StrictStr] = Field(default=None, description="text alongside the title")
    domain: Optional[StrictStr] = Field(default=None, description="domain where a link points")
    url: Optional[StrictStr] = Field(default=None, description="URL of element")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the result was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    related_searches: Optional[List[Optional[StrictStr]]] = Field(default=None, description="search queries related to the elment")
    about_this_result: Optional[AboutThisResultElement] = Field(default=None, description="contains information from the ‘About this result’ panel. ‘About this result’ panel provides additional context about why Google returned this result for the given query;. this feature appears after clicking on the three dots next to most results")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "featured_title", 
        "breadcrumb", 
        "snippet", 
        "domain", 
        "url", 
        "timestamp", 
        "related_searches", 
        "about_this_result", 
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
        _dict['title'] = self.title
        _dict['featured_title'] = self.featured_title
        _dict['breadcrumb'] = self.breadcrumb
        _dict['snippet'] = self.snippet
        _dict['domain'] = self.domain
        _dict['url'] = self.url
        _dict['timestamp'] = self.timestamp
        _dict['related_searches'] = self.related_searches
        _dict['about_this_result'] = self.about_this_result.to_dict() if self.about_this_result else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "featured_title": obj.get("featured_title"),
            "breadcrumb": obj.get("breadcrumb"),
            "snippet": obj.get("snippet"),
            "domain": obj.get("domain"),
            "url": obj.get("url"),
            "timestamp": obj.get("timestamp"),
            "related_searches": obj.get("related_searches"),
            "about_this_result": AboutThisResultElement.from_dict(obj["about_this_result"]) if obj.get("about_this_result") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj