from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_ai_optimization_l_lm_mentions_target_element import BaseAiOptimizationLLmMentionsTargetElement



class AiOptimizationLLmMentionsCrossAggregateMetricsTargetInfo(BaseModel):
    """
    AiOptimizationLLmMentionsCrossAggregateMetricsTargetInfo
    """ # noqa: E501
    target: Optional[List[Optional[BaseAiOptimizationLLmMentionsTargetElement]]] = Field(default=None, description=r"")
    aggregation_key: Optional[StrictStr] = Field(default=None, description=r"")
    __properties: ClassVar[List[str]] = [
        "target", 
        "aggregation_key", 
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

        target_items = []
        if self.target:
            for _item in self.target:
                if _item:
                    target_items.append(_item.to_dict())
            _dict['target'] = target_items
        _dict['aggregation_key'] = self.aggregation_key
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "target": [BaseAiOptimizationLLmMentionsTargetElement.from_dict(_item) for _item in obj["target"]] if obj.get("target") is not None else None,
            "aggregation_key": obj.get("aggregation_key"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj