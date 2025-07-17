from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class OnPageTasksReadyResultInfo(BaseModel):
    """
    OnPageTasksReadyResultInfo
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="task identifier of the completed task. unique task identifier in our system in the UUID format")
    target: Optional[StrictStr] = Field(default=None, description="target website specified when setting a task")
    date_posted: Optional[StrictStr] = Field(default=None, description="date when the task was posted (in the UTC format)")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier")
    __properties: ClassVar[List[str]] = [
        "id", 
        "target", 
        "date_posted", 
        "tag", 
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

        _dict['id'] = self.id
        _dict['target'] = self.target
        _dict['date_posted'] = self.date_posted
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "target": obj.get("target"),
            "date_posted": obj.get("date_posted"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj