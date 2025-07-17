from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo



class AppendixAKeywordsDataPriceDataInfo(BaseModel):
    """
    AppendixAKeywordsDataPriceDataInfo
    """ # noqa: E501
    task_get: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    task_post: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "task_get", 
        "task_post", 
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

        _dict['task_get'] = self.task_get.to_dict() if self.task_get else None
        _dict['task_post'] = self.task_post.to_dict() if self.task_post else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "task_get": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["task_get"]) if obj.get("task_get") is not None else None,
            "task_post": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["task_post"]) if obj.get("task_post") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj