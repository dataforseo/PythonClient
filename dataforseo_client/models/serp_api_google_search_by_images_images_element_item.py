from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_mode_images_element import AiModeImagesElement
from dataforseo_client.models.related_image_searches_element import RelatedImageSearchesElement
from dataforseo_client.models.base_serp_api_google_search_by_images_element_item import BaseSerpApiGoogleSearchByImagesElementItem
from dataforseo_client.models.rectangle_info import RectangleInfo



class SerpApiGoogleSearchByImagesImagesElementItem(BaseSerpApiGoogleSearchByImagesElementItem):
    """
    SerpApiGoogleSearchByImagesImagesElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    title: Optional[StrictStr] = Field(default=None, description="title of the element")
    url: Optional[StrictStr] = Field(default=None, description="search URL with refinement parameters")
    rectangle: Optional[RectangleInfo] = Field(default=None, description="rectangle parameters. contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP. equals null if calculate_rectangles in the POST request is not set to true")
    items: Optional[List[Optional[AiModeImagesElement]]] = Field(default=None, description="elements of search results found in SERP")
    related_image_searches: Optional[List[Optional[RelatedImageSearchesElement]]] = Field(default=None, description="contains keywords and images related to the specified search term. if there are none, equals null")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "title", 
        "url", 
        "rectangle", 
        "items", 
        "related_image_searches", 
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
        _dict['url'] = self.url
        _dict['rectangle'] = self.rectangle.to_dict() if self.rectangle else None
        items_items = []
        if self.items:
            for _item in self.items:
                if _item:
                    items_items.append(_item.to_dict())
            _dict['items'] = items_items
        related_image_searches_items = []
        if self.related_image_searches:
            for _item in self.related_image_searches:
                if _item:
                    related_image_searches_items.append(_item.to_dict())
            _dict['related_image_searches'] = related_image_searches_items
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
            "url": obj.get("url"),
            "rectangle": RectangleInfo.from_dict(obj["rectangle"]) if obj.get("rectangle") is not None else None,
            "items": [AiModeImagesElement.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "related_image_searches": [RelatedImageSearchesElement.from_dict(_item) for _item in obj["related_image_searches"]] if obj.get("related_image_searches") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj