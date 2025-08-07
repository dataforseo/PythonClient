from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AiOptimizationGeminiLlmResponsesModelsResultInfo(BaseModel):
    """
    AiOptimizationGeminiLlmResponsesModelsResultInfo
    """ # noqa: E501
    model_name: Optional[StrictStr] = Field(default=None, description="name of the AI model")
    web_search_supported: Optional[StrictBool] = Field(default=None, description="web search support for the AI model. if true, the web_search parameter can be set with the AI model")
    task_post_supported: Optional[StrictBool] = Field(default=None, description="indicates if Standard (POST-GET) data retrieval is supported. if true, you can use the Standard (POST-GET) data retrieval method with the AI model")
    __properties: ClassVar[List[str]] = [
        "model_name", 
        "web_search_supported", 
        "task_post_supported", 
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
        _dict['web_search_supported'] = self.web_search_supported
        _dict['task_post_supported'] = self.task_post_supported
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "model_name": obj.get("model_name"),
            "web_search_supported": obj.get("web_search_supported"),
            "task_post_supported": obj.get("task_post_supported"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj