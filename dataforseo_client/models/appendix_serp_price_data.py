from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo
from dataforseo_client.models.appendix_a_keywords_data_price_data_info import AppendixAKeywordsDataPriceDataInfo
from dataforseo_client.models.appendix_serp_price_data_info import AppendixSerpPriceDataInfo



class AppendixSerpPriceData(BaseModel):
    """
    AppendixSerpPriceData
    """ # noqa: E501
    tasks_fixed: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    errors: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    jobs: Optional[AppendixAKeywordsDataPriceDataInfo] = Field(default=None, description="")
    languages: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    live: Optional[AppendixSerpPriceDataInfo] = Field(default=None, description="")
    locations: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    screenshot: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    task_get: Optional[AppendixSerpPriceDataInfo] = Field(default=None, description="")
    task_post: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    tasks_ready: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "tasks_fixed", 
        "errors", 
        "jobs", 
        "languages", 
        "live", 
        "locations", 
        "screenshot", 
        "task_get", 
        "task_post", 
        "tasks_ready", 
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

        _dict['tasks_fixed'] = self.tasks_fixed.to_dict() if self.tasks_fixed else None
        _dict['errors'] = self.errors.to_dict() if self.errors else None
        _dict['jobs'] = self.jobs.to_dict() if self.jobs else None
        _dict['languages'] = self.languages.to_dict() if self.languages else None
        _dict['live'] = self.live.to_dict() if self.live else None
        _dict['locations'] = self.locations.to_dict() if self.locations else None
        _dict['screenshot'] = self.screenshot.to_dict() if self.screenshot else None
        _dict['task_get'] = self.task_get.to_dict() if self.task_get else None
        _dict['task_post'] = self.task_post.to_dict() if self.task_post else None
        _dict['tasks_ready'] = self.tasks_ready.to_dict() if self.tasks_ready else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tasks_fixed": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["tasks_fixed"]) if obj.get("tasks_fixed") is not None else None,
            "errors": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["errors"]) if obj.get("errors") is not None else None,
            "jobs": AppendixAKeywordsDataPriceDataInfo.from_dict(obj["jobs"]) if obj.get("jobs") is not None else None,
            "languages": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["languages"]) if obj.get("languages") is not None else None,
            "live": AppendixSerpPriceDataInfo.from_dict(obj["live"]) if obj.get("live") is not None else None,
            "locations": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["locations"]) if obj.get("locations") is not None else None,
            "screenshot": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["screenshot"]) if obj.get("screenshot") is not None else None,
            "task_get": AppendixSerpPriceDataInfo.from_dict(obj["task_get"]) if obj.get("task_get") is not None else None,
            "task_post": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["task_post"]) if obj.get("task_post") is not None else None,
            "tasks_ready": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["tasks_ready"]) if obj.get("tasks_ready") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj