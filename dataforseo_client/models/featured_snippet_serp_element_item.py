from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_mode_images_element_info import AiModeImagesElementInfo
from dataforseo_client.models.table import Table
from dataforseo_client.models.base_serp_api_element_item import BaseSerpApiElementItem
from dataforseo_client.models.ai_mode_rectangle_info import AiModeRectangleInfo



class FeaturedSnippetSerpElementItem(BaseSerpApiElementItem):
    """
    FeaturedSnippetSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    rectangle: Optional[AiModeRectangleInfo] = Field(default=None, description="rectangle parameters. contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP. equals null if calculate_rectangles in the POST request is not set to true")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements found in SERP. note values are returned in the ascending order, with values corresponding to advanced SERP features omitted from the results;. to get all items (including SERP features and rich snippets) with their positions, please refer to the Google Organiс Advanced SERP endpoint")
    domain: Optional[StrictStr] = Field(default=None, description="domain of the ad element in SERP")
    title: Optional[StrictStr] = Field(default=None, description="title of the ad element in SERP")
    description: Optional[StrictStr] = Field(default=None, description="description of the ad element in SERP")
    url: Optional[StrictStr] = Field(default=None, description="relevant URL of the ad element in SERP")
    breadcrumb: Optional[StrictStr] = Field(default=None, description="breadcrumb of the ad element in SERP")
    featured_title: Optional[StrictStr] = Field(default=None, description="title")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the result was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    images: Optional[List[Optional[AiModeImagesElementInfo]]] = Field(default=None, description="images of the element. if there are none, equals null")
    table: Optional[Table] = Field(default=None, description="table present in the element. the header and content of the table present in the element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "xpath", 
        "rectangle", 
        "rank_group", 
        "rank_absolute", 
        "domain", 
        "title", 
        "description", 
        "url", 
        "breadcrumb", 
        "featured_title", 
        "timestamp", 
        "images", 
        "table", 
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
        _dict['xpath'] = self.xpath
        _dict['rectangle'] = self.rectangle.to_dict() if self.rectangle else None
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['domain'] = self.domain
        _dict['title'] = self.title
        _dict['description'] = self.description
        _dict['url'] = self.url
        _dict['breadcrumb'] = self.breadcrumb
        _dict['featured_title'] = self.featured_title
        _dict['timestamp'] = self.timestamp
        images_items = []
        if self.images:
            for _item in self.images:
                if _item:
                    images_items.append(_item.to_dict())
            _dict['images'] = images_items
        _dict['table'] = self.table.to_dict() if self.table else None
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
            "xpath": obj.get("xpath"),
            "rectangle": AiModeRectangleInfo.from_dict(obj["rectangle"]) if obj.get("rectangle") is not None else None,
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "domain": obj.get("domain"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "url": obj.get("url"),
            "breadcrumb": obj.get("breadcrumb"),
            "featured_title": obj.get("featured_title"),
            "timestamp": obj.get("timestamp"),
            "images": [AiModeImagesElementInfo.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "table": Table.from_dict(obj["table"]) if obj.get("table") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj