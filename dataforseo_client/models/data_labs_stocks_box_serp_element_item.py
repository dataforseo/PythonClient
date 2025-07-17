from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.price_info import PriceInfo
from dataforseo_client.models.table import Table
from dataforseo_client.models.graph import Graph
from dataforseo_client.models.base_dataforseo_labs_api_element_item import BaseDataforseoLabsApiElementItem



class DataLabsStocksBoxSerpElementItem(BaseDataforseoLabsApiElementItem):
    """
    DataLabsStocksBoxSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    title: Optional[StrictStr] = Field(default=None, description="title of the result in SERP")
    source: Optional[StrictStr] = Field(default=None, description="source of the element. indicates the source of the video")
    snippet: Optional[StrictStr] = Field(default=None, description="snippet of the element")
    price: Optional[PriceInfo] = Field(default=None, description="price of the shopping element")
    url: Optional[StrictStr] = Field(default=None, description="sitelink URL")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    table: Optional[Table] = Field(default=None, description="table element")
    graph: Optional[Graph] = Field(default=None, description="contains data provided in the graph of the element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "se_type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "title", 
        "source", 
        "snippet", 
        "price", 
        "url", 
        "domain", 
        "table", 
        "graph", 
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
        _dict['source'] = self.source
        _dict['snippet'] = self.snippet
        _dict['price'] = self.price.to_dict() if self.price else None
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        _dict['table'] = self.table.to_dict() if self.table else None
        _dict['graph'] = self.graph.to_dict() if self.graph else None
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
            "source": obj.get("source"),
            "snippet": obj.get("snippet"),
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "table": Table.from_dict(obj["table"]) if obj.get("table") is not None else None,
            "graph": Graph.from_dict(obj["graph"]) if obj.get("graph") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj