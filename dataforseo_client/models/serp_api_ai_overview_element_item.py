from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.link_element import LinkElement
from dataforseo_client.models.ai_mode_images_element import AiModeImagesElement
from dataforseo_client.models.ai_ai_overview_reference_info import AiAiOverviewReferenceInfo
from dataforseo_client.models.base_serp_api_ai_overview_element_item import BaseSerpApiAiOverviewElementItem



class SerpApiAiOverviewElementItem(BaseSerpApiAiOverviewElementItem):
    """
    SerpApiAiOverviewElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    title: Optional[StrictStr] = Field(default=None, description="title of a given link element")
    text: Optional[StrictStr] = Field(default=None, description="reference text. text snippet from the page that was used to generate the ai_overview_element")
    markdown: Optional[StrictStr] = Field(default=None, description="text of the component in the markdwon format")
    links: Optional[List[Optional[LinkElement]]] = Field(default=None, description="sitelinks. the links shown below some of Google’s search results. if there are none, equals null")
    images: Optional[List[Optional[AiModeImagesElement]]] = Field(default=None, description="images of the element. if there are none, equals null")
    references: Optional[List[Optional[AiAiOverviewReferenceInfo]]] = Field(default=None, description="additional references relevant to the item. includes references to webpages that may have been used to generate the product_considerations_ai_overview_expanded_element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "title", 
        "text", 
        "markdown", 
        "links", 
        "images", 
        "references", 
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
        _dict['position'] = self.position
        _dict['title'] = self.title
        _dict['text'] = self.text
        _dict['markdown'] = self.markdown
        links_items = []
        if self.links:
            for _item in self.links:
                if _item:
                    links_items.append(_item.to_dict())
            _dict['links'] = links_items
        images_items = []
        if self.images:
            for _item in self.images:
                if _item:
                    images_items.append(_item.to_dict())
            _dict['images'] = images_items
        references_items = []
        if self.references:
            for _item in self.references:
                if _item:
                    references_items.append(_item.to_dict())
            _dict['references'] = references_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "position": obj.get("position"),
            "title": obj.get("title"),
            "text": obj.get("text"),
            "markdown": obj.get("markdown"),
            "links": [LinkElement.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "images": [AiModeImagesElement.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "references": [AiAiOverviewReferenceInfo.from_dict(_item) for _item in obj["references"]] if obj.get("references") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj