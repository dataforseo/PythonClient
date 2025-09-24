from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.link_element import LinkElement
from dataforseo_client.models.base_serp_api_bing_ai_overview_element_item import BaseSerpApiBingAiOverviewElementItem



class SerpApiBingAiOverviewOrganicElementItem(BaseSerpApiBingAiOverviewElementItem):
    """
    SerpApiBingAiOverviewOrganicElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    title: Optional[StrictStr] = Field(default=None, description=r"title of the link")
    url: Optional[StrictStr] = Field(default=None, description=r"relevant URL")
    domain: Optional[StrictStr] = Field(default=None, description=r"domain in SERP")
    snippet: Optional[StrictStr] = Field(default=None, description=r"text snippet from the organic result")
    breadcrumb: Optional[StrictStr] = Field(default=None, description=r"breadcrumb in SERP")
    website_name: Optional[StrictStr] = Field(default=None, description=r"website name in SERP")
    links: Optional[List[Optional[LinkElement]]] = Field(default=None, description=r"links featured in the faq_box_element")
    highlighted: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"words highlighted in bold within the results description")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "url", 
        "domain", 
        "snippet", 
        "breadcrumb", 
        "website_name", 
        "links", 
        "highlighted", 
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
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        _dict['snippet'] = self.snippet
        _dict['breadcrumb'] = self.breadcrumb
        _dict['website_name'] = self.website_name
        links_items = []
        if self.links:
            for _item in self.links:
                if _item:
                    links_items.append(_item.to_dict())
            _dict['links'] = links_items
        _dict['highlighted'] = self.highlighted
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
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "snippet": obj.get("snippet"),
            "breadcrumb": obj.get("breadcrumb"),
            "website_name": obj.get("website_name"),
            "links": [LinkElement.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "highlighted": obj.get("highlighted"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj