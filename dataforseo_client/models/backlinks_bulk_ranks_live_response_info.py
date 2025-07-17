from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.backlinks_bulk_ranks_live_task_info import BacklinksBulkRanksLiveTaskInfo
from dataforseo_client.models.base_response_info import BaseResponseInfo



class BacklinksBulkRanksLiveResponseInfo(BaseModel):
    """
    BacklinksBulkRanksLiveResponseInfo
    """ # noqa: E501
    version: Optional[StrictStr] = Field(default=None, description="the current version of the API")
    status_code: Optional[StrictInt] = Field(default=None, description="general status code. you can find the full list of the response codes here")
    status_message: Optional[StrictStr] = Field(default=None, description="general informational message. you can find the full list of general informational messages here")
    time: Optional[StrictStr] = Field(default=None, description="total execution time, seconds")
    cost: Optional[StrictFloat] = Field(default=None, description="total tasks cost, USD")
    tasks_count: Optional[StrictInt] = Field(default=None, description="the number of tasks in the tasks array")
    tasks_error: Optional[StrictInt] = Field(default=None, description="the number of tasks in the tasks array returned with an error")
    tasks: Optional[List[Optional[BacklinksBulkRanksLiveTaskInfo]]] = Field(default=None, description="array of tasks")
    __properties: ClassVar[List[str]] = [
        "version", 
        "status_code", 
        "status_message", 
        "time", 
        "cost", 
        "tasks_count", 
        "tasks_error", 
        "tasks", 
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

        _dict['version'] = self.version
        _dict['status_code'] = self.status_code
        _dict['status_message'] = self.status_message
        _dict['time'] = self.time
        _dict['cost'] = self.cost
        _dict['tasks_count'] = self.tasks_count
        _dict['tasks_error'] = self.tasks_error
        tasks_items = []
        if self.tasks:
            for _item in self.tasks:
                if _item:
                    tasks_items.append(_item.to_dict())
            _dict['tasks'] = tasks_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "version": obj.get("version"),
            "status_code": obj.get("status_code"),
            "status_message": obj.get("status_message"),
            "time": obj.get("time"),
            "cost": obj.get("cost"),
            "tasks_count": obj.get("tasks_count"),
            "tasks_error": obj.get("tasks_error"),
            "tasks": [BacklinksBulkRanksLiveTaskInfo.from_dict(_item) for _item in obj["tasks"]] if obj.get("tasks") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj