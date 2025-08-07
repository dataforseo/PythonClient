from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class JobsElement(BaseModel):
    """
    JobsElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="title of a given link element")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    location: Optional[StrictStr] = Field(default=None, description="location for which the job vacancy is posted")
    author: Optional[StrictStr] = Field(default=None, description="author")
    job_posted_time: Optional[StrictStr] = Field(default=None, description="the time when the job was posted")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the result was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    contract_type: Optional[StrictStr] = Field(default=None, description="contract type")
    salary: Optional[StrictStr] = Field(default=None, description="salary")
    url: Optional[StrictStr] = Field(default=None, description="URL")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "description", 
        "location", 
        "author", 
        "job_posted_time", 
        "timestamp", 
        "contract_type", 
        "salary", 
        "url", 
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
        _dict['title'] = self.title
        _dict['description'] = self.description
        _dict['location'] = self.location
        _dict['author'] = self.author
        _dict['job_posted_time'] = self.job_posted_time
        _dict['timestamp'] = self.timestamp
        _dict['contract_type'] = self.contract_type
        _dict['salary'] = self.salary
        _dict['url'] = self.url
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "location": obj.get("location"),
            "author": obj.get("author"),
            "job_posted_time": obj.get("job_posted_time"),
            "timestamp": obj.get("timestamp"),
            "contract_type": obj.get("contract_type"),
            "salary": obj.get("salary"),
            "url": obj.get("url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj