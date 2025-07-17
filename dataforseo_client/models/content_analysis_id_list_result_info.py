from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ContentAnalysisIdListResultInfo(BaseModel):
    """
    ContentAnalysisIdListResultInfo
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="id of the task")
    url: Optional[StrictStr] = Field(default=None, description="URL of the task. URL you used for making an API call")
    datetime_posted: Optional[StrictStr] = Field(default=None, description="date and time when the task was made. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2023-01-15 12:57:46 +00:00")
    datetime_done: Optional[StrictStr] = Field(default=None, description="date and time when the task was completed. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2023-01-15 12:57:46 +00:00")
    status: Optional[StrictStr] = Field(default=None, description="informational message of the task. you can find the full list of general informational messages here")
    cost: Optional[StrictFloat] = Field(default=None, description="cost of the task, USD")
    metadata: Optional[Dict[str, Optional[Any]]] = Field(default=None, description="contains parameters you specified in the POST request")
    __properties: ClassVar[List[str]] = [
        "id", 
        "url", 
        "datetime_posted", 
        "datetime_done", 
        "status", 
        "cost", 
        "metadata", 
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
        _dict['url'] = self.url
        _dict['datetime_posted'] = self.datetime_posted
        _dict['datetime_done'] = self.datetime_done
        _dict['status'] = self.status
        _dict['cost'] = self.cost
        _dict['metadata'] = self.metadata
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "url": obj.get("url"),
            "datetime_posted": obj.get("datetime_posted"),
            "datetime_done": obj.get("datetime_done"),
            "status": obj.get("status"),
            "cost": obj.get("cost"),
            "metadata": obj.get("metadata"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj