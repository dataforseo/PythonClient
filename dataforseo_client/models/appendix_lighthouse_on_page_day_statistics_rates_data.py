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

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class AppendixLighthouseOnPageDayStatisticsRatesData(BaseModel):
    """
    AppendixLighthouseOnPageDayStatisticsRatesData
    """ # noqa: E501
    task_post: Optional[Union[StrictFloat, StrictInt]] = None
    tasks_ready: Optional[Union[StrictFloat, StrictInt]] = None
    task_get: Optional[Union[StrictFloat, StrictInt]] = None
    live: Optional[Union[StrictFloat, StrictInt]] = None
    audits: Optional[Union[StrictFloat, StrictInt]] = None
    languages: Optional[Union[StrictFloat, StrictInt]] = None
    versions: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["task_post", "tasks_ready", "task_get", "live", "audits", "languages", "versions"]

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
        """Create an instance of AppendixLighthouseOnPageDayStatisticsRatesData from a JSON string"""
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
        # set to None if task_post (nullable) is None
        # and model_fields_set contains the field
        if self.task_post is None and "task_post" in self.model_fields_set:
            _dict['task_post'] = None

        # set to None if tasks_ready (nullable) is None
        # and model_fields_set contains the field
        if self.tasks_ready is None and "tasks_ready" in self.model_fields_set:
            _dict['tasks_ready'] = None

        # set to None if task_get (nullable) is None
        # and model_fields_set contains the field
        if self.task_get is None and "task_get" in self.model_fields_set:
            _dict['task_get'] = None

        # set to None if live (nullable) is None
        # and model_fields_set contains the field
        if self.live is None and "live" in self.model_fields_set:
            _dict['live'] = None

        # set to None if audits (nullable) is None
        # and model_fields_set contains the field
        if self.audits is None and "audits" in self.model_fields_set:
            _dict['audits'] = None

        # set to None if languages (nullable) is None
        # and model_fields_set contains the field
        if self.languages is None and "languages" in self.model_fields_set:
            _dict['languages'] = None

        # set to None if versions (nullable) is None
        # and model_fields_set contains the field
        if self.versions is None and "versions" in self.model_fields_set:
            _dict['versions'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppendixLighthouseOnPageDayStatisticsRatesData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "task_post": obj.get("task_post"),
            "tasks_ready": obj.get("tasks_ready"),
            "task_get": obj.get("task_get"),
            "live": obj.get("live"),
            "audits": obj.get("audits"),
            "languages": obj.get("languages"),
            "versions": obj.get("versions")
        })
        return _obj


