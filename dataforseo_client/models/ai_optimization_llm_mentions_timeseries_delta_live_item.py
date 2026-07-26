from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AiOptimizationLlmMentionsTimeseriesDeltaLiveItem(BaseModel):
    """
    AiOptimizationLlmMentionsTimeseriesDeltaLiveItem
    """ # noqa: E501
    date: Optional[StrictStr] = Field(default=None, description=r"*date timestamp*.  date format: `'yyyy-mm-dd'`")
    delta_mentions: Optional[StrictInt] = Field(default=None, description=r"*LLM mentions count delta*. the difference in `mentions` between the current timestamp and the previous one")
    delta_ai_search_volume: Optional[StrictInt] = Field(default=None, description=r"*LLM mentions count delta*. the difference in `ai_search_volume` values between the current timestamp and the previous one. learn more about this metric [here](https://dataforseo.com/help-center/how-ai-search-volume-metrics-work-in-the-llm-mentions-timeseries-endpoints)")
    __properties: ClassVar[List[str]] = [
        "date", 
        "delta_mentions", 
        "delta_ai_search_volume", 
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

        _dict['date'] = self.date
        _dict['delta_mentions'] = self.delta_mentions
        _dict['delta_ai_search_volume'] = self.delta_ai_search_volume
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "delta_mentions": obj.get("delta_mentions"),
            "delta_ai_search_volume": obj.get("delta_ai_search_volume"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj