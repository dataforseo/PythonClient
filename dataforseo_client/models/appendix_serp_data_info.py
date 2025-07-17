from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_function_type_info import AppendixFunctionTypeInfo
from dataforseo_client.models.appendix_jobs_serp_limits_rates_data_info import AppendixJobsSerpLimitsRatesDataInfo



class AppendixSerpDataInfo(BaseModel):
    """
    AppendixSerpDataInfo
    """ # noqa: E501
    task_post: Optional[StrictFloat] = Field(default=None, description="")
    task_get: Optional[AppendixFunctionTypeInfo] = Field(default=None, description="")
    tasks_ready: Optional[StrictFloat] = Field(default=None, description="")
    locations: Optional[StrictFloat] = Field(default=None, description="")
    languages: Optional[StrictFloat] = Field(default=None, description="")
    live: Optional[AppendixFunctionTypeInfo] = Field(default=None, description="")
    errors: Optional[StrictFloat] = Field(default=None, description="")
    tasks_fixed: Optional[StrictFloat] = Field(default=None, description="")
    jobs: Optional[AppendixJobsSerpLimitsRatesDataInfo] = Field(default=None, description="")
    screenshot: Optional[StrictFloat] = Field(default=None, description="")
    tasks_ready_queue: Optional[StrictFloat] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "task_post", 
        "task_get", 
        "tasks_ready", 
        "locations", 
        "languages", 
        "live", 
        "errors", 
        "tasks_fixed", 
        "jobs", 
        "screenshot", 
        "tasks_ready_queue", 
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

        _dict['task_post'] = self.task_post
        _dict['task_get'] = self.task_get.to_dict() if self.task_get else None
        _dict['tasks_ready'] = self.tasks_ready
        _dict['locations'] = self.locations
        _dict['languages'] = self.languages
        _dict['live'] = self.live.to_dict() if self.live else None
        _dict['errors'] = self.errors
        _dict['tasks_fixed'] = self.tasks_fixed
        _dict['jobs'] = self.jobs.to_dict() if self.jobs else None
        _dict['screenshot'] = self.screenshot
        _dict['tasks_ready_queue'] = self.tasks_ready_queue
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "task_post": obj.get("task_post"),
            "task_get": AppendixFunctionTypeInfo.from_dict(obj["task_get"]) if obj.get("task_get") is not None else None,
            "tasks_ready": obj.get("tasks_ready"),
            "locations": obj.get("locations"),
            "languages": obj.get("languages"),
            "live": AppendixFunctionTypeInfo.from_dict(obj["live"]) if obj.get("live") is not None else None,
            "errors": obj.get("errors"),
            "tasks_fixed": obj.get("tasks_fixed"),
            "jobs": AppendixJobsSerpLimitsRatesDataInfo.from_dict(obj["jobs"]) if obj.get("jobs") is not None else None,
            "screenshot": obj.get("screenshot"),
            "tasks_ready_queue": obj.get("tasks_ready_queue"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj