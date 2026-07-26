from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AiOptimizationLlmMentionsTimeseriesNewLostLiveItem(BaseModel):
    """
    AiOptimizationLlmMentionsTimeseriesNewLostLiveItem
    """ # noqa: E501
    date: Optional[StrictStr] = Field(default=None, description=r"*date timestamp*.  date format: `'yyyy-mm-dd'`")
    new_mentions: Optional[StrictInt] = Field(default=None, description=r"*new LLM mentions*. indicates the LLM responses that contain the target at the `date_to` timestamp, did not contain it at the `date_from` timestamp")
    lost_mentions: Optional[StrictInt] = Field(default=None, description=r"*lost LLM mentions*. indicates the LLM responses that contained the specified target at the `date_from` timestamp, do not contain it at the `date_to` timestamp")
    new_ai_search_volume: Optional[StrictInt] = Field(default=None, description=r"*ai_search_volume increment*. indicates the increase of `ai_search_volume` values between the current timestamp and the previous one. learn more about this metric [here](https://dataforseo.com/help-center/how-ai-search-volume-metrics-work-in-the-llm-mentions-timeseries-endpoints)")
    lost_ai_search_volume: Optional[StrictInt] = Field(default=None, description=r"*ai_search_volume decrement*. indicates the decrease of `ai_search_volume` values between the current timestamp and the previous one. learn more about this metric [here](https://dataforseo.com/help-center/how-ai-search-volume-metrics-work-in-the-llm-mentions-timeseries-endpoints)")
    __properties: ClassVar[List[str]] = [
        "date", 
        "new_mentions", 
        "lost_mentions", 
        "new_ai_search_volume", 
        "lost_ai_search_volume", 
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
        _dict['new_mentions'] = self.new_mentions
        _dict['lost_mentions'] = self.lost_mentions
        _dict['new_ai_search_volume'] = self.new_ai_search_volume
        _dict['lost_ai_search_volume'] = self.lost_ai_search_volume
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "new_mentions": obj.get("new_mentions"),
            "lost_mentions": obj.get("lost_mentions"),
            "new_ai_search_volume": obj.get("new_ai_search_volume"),
            "lost_ai_search_volume": obj.get("lost_ai_search_volume"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj