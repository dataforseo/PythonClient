from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_optimization_item import AiOptimizationItem



class AiOptimizationGeminiLlmResponsesTaskGetResultInfo(BaseModel):
    """
    AiOptimizationGeminiLlmResponsesTaskGetResultInfo
    """ # noqa: E501
    model_name: Optional[StrictStr] = Field(default=None, description=r"name of the AI model used")
    input_tokens: Optional[StrictInt] = Field(default=None, description=r"number of tokens in the input. total count of tokens processed")
    output_tokens: Optional[StrictInt] = Field(default=None, description=r"number of tokens in the output. total count of tokens generated in the AI response")
    web_search: Optional[StrictBool] = Field(default=None, description=r"indicates if web search was used")
    money_spent: Optional[StrictFloat] = Field(default=None, description=r"cost of AI tokens, USD. the price charged by the third-party AI model provider for according to its Pricing")
    datetime: Optional[StrictStr] = Field(default=None, description=r"date and time when the result was received. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    items: Optional[List[Optional[AiOptimizationItem]]] = Field(default=None, description=r"array of response items. contains structured AI response data")
    fan_out_queries: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"array of fan-out queries. contains related search queries derived from the main query to provide a more comprehensive response")
    __properties: ClassVar[List[str]] = [
        "model_name", 
        "input_tokens", 
        "output_tokens", 
        "web_search", 
        "money_spent", 
        "datetime", 
        "items", 
        "fan_out_queries", 
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

        _dict['model_name'] = self.model_name
        _dict['input_tokens'] = self.input_tokens
        _dict['output_tokens'] = self.output_tokens
        _dict['web_search'] = self.web_search
        _dict['money_spent'] = self.money_spent
        _dict['datetime'] = self.datetime
        items_items = []
        if self.items:
            for _item in self.items:
                if _item:
                    items_items.append(_item.to_dict())
            _dict['items'] = items_items
        _dict['fan_out_queries'] = self.fan_out_queries
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "model_name": obj.get("model_name"),
            "input_tokens": obj.get("input_tokens"),
            "output_tokens": obj.get("output_tokens"),
            "web_search": obj.get("web_search"),
            "money_spent": obj.get("money_spent"),
            "datetime": obj.get("datetime"),
            "items": [AiOptimizationItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "fan_out_queries": obj.get("fan_out_queries"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj