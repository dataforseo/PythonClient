# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class BaseResponseInfo(BaseModel):
    """
    BaseResponseInfo
    """ # noqa: E501
    version: Optional[StrictStr] = Field(default=None, description="the current version of the API")
    status_code: Optional[StrictInt] = Field(default=None, description="general status code you can find the full list of the response codes here")
    status_message: Optional[StrictStr] = Field(default=None, description="general informational message you can find the full list of general informational messages here")
    time: Optional[StrictStr] = Field(default=None, description="total execution time, seconds")
    cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="total tasks cost, USD")
    tasks_count: Optional[StrictInt] = Field(default=None, description="the number of tasks in the tasks array")
    tasks_error: Optional[StrictInt] = Field(default=None, description="the number of tasks in the tasks array returned with an error")
    __properties: ClassVar[List[str]] = ["version", "status_code", "status_message", "time", "cost", "tasks_count", "tasks_error"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BaseResponseInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        # set to None if status_code (nullable) is None
        # and model_fields_set contains the field
        if self.status_code is None and "status_code" in self.model_fields_set:
            _dict['status_code'] = None

        # set to None if status_message (nullable) is None
        # and model_fields_set contains the field
        if self.status_message is None and "status_message" in self.model_fields_set:
            _dict['status_message'] = None

        # set to None if time (nullable) is None
        # and model_fields_set contains the field
        if self.time is None and "time" in self.model_fields_set:
            _dict['time'] = None

        # set to None if cost (nullable) is None
        # and model_fields_set contains the field
        if self.cost is None and "cost" in self.model_fields_set:
            _dict['cost'] = None

        # set to None if tasks_count (nullable) is None
        # and model_fields_set contains the field
        if self.tasks_count is None and "tasks_count" in self.model_fields_set:
            _dict['tasks_count'] = None

        # set to None if tasks_error (nullable) is None
        # and model_fields_set contains the field
        if self.tasks_error is None and "tasks_error" in self.model_fields_set:
            _dict['tasks_error'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BaseResponseInfo from a dict"""
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
            "tasks_error": obj.get("tasks_error")
        })
        return _obj


