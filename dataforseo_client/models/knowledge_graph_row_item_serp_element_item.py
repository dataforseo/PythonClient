from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.link_element import LinkElement
from dataforseo_client.models.base_serp_api_element_item import BaseSerpApiElementItem
from dataforseo_client.models.rectangle_info import RectangleInfo



class KnowledgeGraphRowItemSerpElementItem(BaseSerpApiElementItem):
    """
    KnowledgeGraphRowItemSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    rectangle: Optional[RectangleInfo] = Field(default=None, description="rectangle parameters. contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP. equals null if calculate_rectangles in the POST request is not set to true")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values;. positions of elements with different type values are omitted from rank_group;. always equals 0 for desktop")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP. always equals 0 for desktop")
    title: Optional[StrictStr] = Field(default=None, description="reference page title")
    data_attrid: Optional[StrictStr] = Field(default=None, description="google defined data attribute ID. example:. action:listen_artist")
    text: Optional[StrictStr] = Field(default=None, description="reference text. text snippet from the page that was used to generate the ai_overview_element")
    links: Optional[List[Optional[LinkElement]]] = Field(default=None, description="link of the element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "xpath", 
        "rectangle", 
        "rank_group", 
        "rank_absolute", 
        "title", 
        "data_attrid", 
        "text", 
        "links", 
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
        _dict['title'] = self.title
        _dict['data_attrid'] = self.data_attrid
        _dict['text'] = self.text
        links_items = []
        if self.links:
            for _item in self.links:
                if _item:
                    links_items.append(_item.to_dict())
            _dict['links'] = links_items
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
            "rectangle": RectangleInfo.from_dict(obj["rectangle"]) if obj.get("rectangle") is not None else None,
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "title": obj.get("title"),
            "data_attrid": obj.get("data_attrid"),
            "text": obj.get("text"),
            "links": [LinkElement.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj