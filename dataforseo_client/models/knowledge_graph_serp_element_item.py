from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_serp_api_knowledge_graph_element_item import BaseSerpApiKnowledgeGraphElementItem
from dataforseo_client.models.base_serp_api_element_item import BaseSerpApiElementItem
from dataforseo_client.models.ai_mode_rectangle_info import AiModeRectangleInfo



class KnowledgeGraphSerpElementItem(BaseSerpApiElementItem):
    """
    KnowledgeGraphSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    rectangle: Optional[AiModeRectangleInfo] = Field(default=None, description="rectangle parameters. contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP. equals null if calculate_rectangles in the POST request is not set to true")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    title: Optional[StrictStr] = Field(default=None, description="title of the result in SERP")
    subtitle: Optional[StrictStr] = Field(default=None, description="subtitle of the item")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    card_id: Optional[StrictStr] = Field(default=None, description="card id")
    url: Optional[StrictStr] = Field(default=None, description="relevant URL in SERP")
    image_url: Optional[StrictStr] = Field(default=None, description="URL of the image. the URL leading to the image on the original resource or DataForSEO storage (in case the original source is not available)")
    logo_url: Optional[StrictStr] = Field(default=None, description="URL of the logo from knowledge graph")
    cid: Optional[StrictStr] = Field(default=None, description="google-defined client id. unique id of a local establishment;. can be used with Google Reviews API to get a full list of reviews")
    items: Optional[List[Optional[BaseSerpApiKnowledgeGraphElementItem]]] = Field(default=None, description="contains results featured in the ‘hotels_pack’ element of SERP")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "xpath", 
        "rectangle", 
        "rank_group", 
        "rank_absolute", 
        "title", 
        "subtitle", 
        "description", 
        "card_id", 
        "url", 
        "image_url", 
        "logo_url", 
        "cid", 
        "items", 
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
        _dict['subtitle'] = self.subtitle
        _dict['description'] = self.description
        _dict['card_id'] = self.card_id
        _dict['url'] = self.url
        _dict['image_url'] = self.image_url
        _dict['logo_url'] = self.logo_url
        _dict['cid'] = self.cid
        items_items = []
        if self.items:
            for _item in self.items:
                if _item:
                    items_items.append(_item.to_dict())
            _dict['items'] = items_items
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
            "title": obj.get("title"),
            "subtitle": obj.get("subtitle"),
            "description": obj.get("description"),
            "card_id": obj.get("card_id"),
            "url": obj.get("url"),
            "image_url": obj.get("image_url"),
            "logo_url": obj.get("logo_url"),
            "cid": obj.get("cid"),
            "items": [BaseSerpApiKnowledgeGraphElementItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj