from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.table import Table
from dataforseo_client.models.graph import Graph
from dataforseo_client.models.base_serp_api_element_item import BaseSerpApiElementItem
from dataforseo_client.models.ai_mode_rectangle_info import AiModeRectangleInfo



class CurrencyBoxSerpElementItem(BaseSerpApiElementItem):
    """
    CurrencyBoxSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    rectangle: Optional[AiModeRectangleInfo] = Field(default=None, description="rectangle parameters. contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP. equals null if calculate_rectangles in the POST request is not set to true")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values;. positions of elements with different type values are omitted from rank_group;. always equals 0 for desktop")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP. always equals 0 for desktop")
    value: Optional[StrictFloat] = Field(default=None, description="the value of the rating")
    converted_value: Optional[StrictFloat] = Field(default=None, description="value converted to a requested currency. indicates the exact value based on Google Fincance data at the time when our API pulled the results. note that exchange rates displayed in the currency_box element may be delayed according to the Google Finance disclaimer")
    currency: Optional[StrictStr] = Field(default=None, description="currency of the listed price. ISO code of the currency applied to the price")
    converted_currency: Optional[StrictStr] = Field(default=None, description="converted currency")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the result was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    table: Optional[Table] = Field(default=None, description="table present in the element. the header and content of the table present in the element")
    graph: Optional[Graph] = Field(default=None, description="contains data provided in the graph of the element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "xpath", 
        "rectangle", 
        "rank_group", 
        "rank_absolute", 
        "value", 
        "converted_value", 
        "currency", 
        "converted_currency", 
        "timestamp", 
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
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
        _dict['rectangle'] = self.rectangle.to_dict() if self.rectangle else None
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['value'] = self.value
        _dict['converted_value'] = self.converted_value
        _dict['currency'] = self.currency
        _dict['converted_currency'] = self.converted_currency
        _dict['timestamp'] = self.timestamp
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
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "rectangle": AiModeRectangleInfo.from_dict(obj["rectangle"]) if obj.get("rectangle") is not None else None,
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "value": obj.get("value"),
            "converted_value": obj.get("converted_value"),
            "currency": obj.get("currency"),
            "converted_currency": obj.get("converted_currency"),
            "timestamp": obj.get("timestamp"),
            "table": Table.from_dict(obj["table"]) if obj.get("table") is not None else None,
            "graph": Graph.from_dict(obj["graph"]) if obj.get("graph") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj