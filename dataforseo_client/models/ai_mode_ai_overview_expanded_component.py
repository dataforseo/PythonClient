from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_mode_images_element import AiModeImagesElement
from dataforseo_client.models.information_and_tickets_element import InformationAndTicketsElement
from dataforseo_client.models.ai_ai_overview_reference_info import AiAiOverviewReferenceInfo



class AiModeAiOverviewExpandedComponent(BaseModel):
    """
    AiModeAiOverviewExpandedComponent
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="reference page title")
    text: Optional[StrictStr] = Field(default=None, description="additional text of the element in SERP")
    markdown: Optional[StrictStr] = Field(default=None, description="content of the element in markdown format")
    images: Optional[List[Optional[AiModeImagesElement]]] = Field(default=None, description="images of the component. if there are none, equals null")
    links: Optional[List[Optional[InformationAndTicketsElement]]] = Field(default=None, description="sitelinks. the links shown below some of Google’s search results. if there are none, equals null")
    references: Optional[List[Optional[AiAiOverviewReferenceInfo]]] = Field(default=None, description="references relevant to the element. includes references to webpages that were used to generate the ai_overview_element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "text", 
        "markdown", 
        "images", 
        "links", 
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
        _dict['title'] = self.title
        _dict['text'] = self.text
        _dict['markdown'] = self.markdown
        images_items = []
        if self.images:
            for _item in self.images:
                if _item:
                    images_items.append(_item.to_dict())
            _dict['images'] = images_items
        links_items = []
        if self.links:
            for _item in self.links:
                if _item:
                    links_items.append(_item.to_dict())
            _dict['links'] = links_items
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
            "title": obj.get("title"),
            "text": obj.get("text"),
            "markdown": obj.get("markdown"),
            "images": [AiModeImagesElement.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "links": [InformationAndTicketsElement.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "references": [AiAiOverviewReferenceInfo.from_dict(_item) for _item in obj["references"]] if obj.get("references") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj