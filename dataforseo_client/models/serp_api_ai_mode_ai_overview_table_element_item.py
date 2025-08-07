from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_mode_table_info import AiModeTableInfo
from dataforseo_client.models.base_serp_api_ai_mode_ai_overview_element_item import BaseSerpApiAiModeAiOverviewElementItem



class SerpApiAiModeAiOverviewTableElementItem(BaseSerpApiAiModeAiOverviewElementItem):
    """
    SerpApiAiModeAiOverviewTableElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    markdown: Optional[StrictStr] = Field(default=None, description="text of the component in the markdwon format")
    table: Optional[AiModeTableInfo] = Field(default=None, description="table present in the element. the header and content of the table present in the element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "markdown", 
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
        _dict['markdown'] = self.markdown
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
            "markdown": obj.get("markdown"),
            "table": AiModeTableInfo.from_dict(obj["table"]) if obj.get("table") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj