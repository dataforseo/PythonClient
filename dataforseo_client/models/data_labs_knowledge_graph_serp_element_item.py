from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_dataforseo_labs_knowledge_graph_element_item import BaseDataforseoLabsKnowledgeGraphElementItem
from dataforseo_client.models.base_dataforseo_labs_api_element_item import BaseDataforseoLabsApiElementItem



class DataLabsKnowledgeGraphSerpElementItem(BaseDataforseoLabsApiElementItem):
    """
    DataLabsKnowledgeGraphSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    title: Optional[StrictStr] = Field(default=None, description="title of the result in SERP")
    sub_title: Optional[StrictStr] = Field(default=None, description="subtitle of the item")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    card_id: Optional[StrictStr] = Field(default=None, description="card id")
    url: Optional[StrictStr] = Field(default=None, description="sitelink URL")
    image_url: Optional[StrictStr] = Field(default=None, description="URL of the image")
    logo_url: Optional[StrictStr] = Field(default=None, description="URL of the logo from knowledge graph")
    cid: Optional[StrictStr] = Field(default=None, description="google-defined client id")
    items: Optional[List[Optional[BaseDataforseoLabsKnowledgeGraphElementItem]]] = Field(default=None, description="elements of search results found in SERP")
    __properties: ClassVar[List[str]] = [
        "type", 
        "se_type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "title", 
        "sub_title", 
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
        _dict['se_type'] = self.se_type
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
        _dict['title'] = self.title
        _dict['sub_title'] = self.sub_title
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
            "se_type": obj.get("se_type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "title": obj.get("title"),
            "sub_title": obj.get("sub_title"),
            "description": obj.get("description"),
            "card_id": obj.get("card_id"),
            "url": obj.get("url"),
            "image_url": obj.get("image_url"),
            "logo_url": obj.get("logo_url"),
            "cid": obj.get("cid"),
            "items": [BaseDataforseoLabsKnowledgeGraphElementItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj