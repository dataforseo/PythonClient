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

class SerpErrorsResultInfo(BaseModel):
    """
    SerpErrorsResultInfo
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="id of the task")
    datetime: Optional[StrictStr] = Field(default=None, description="date and time when an error occurred in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    function: Optional[StrictStr] = Field(default=None, description="corresponding API function")
    error_code: Optional[StrictInt] = Field(default=None, description="error code")
    error_message: Optional[StrictStr] = Field(default=None, description="error message or error URL error message (see full list) or URL that caused an error")
    http_url: Optional[StrictStr] = Field(default=None, description="URL that caused an error URL you used for making an API call or pingback/postback URL")
    http_method: Optional[StrictStr] = Field(default=None, description="HTTP method")
    http_code: Optional[StrictInt] = Field(default=None, description="HTTP status code")
    http_time: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="time taken by HTTP request for tasks set with a pingback/postback, this field will show the time it took your server to respond")
    http_response: Optional[StrictStr] = Field(default=None, description="HTTP response server response")
    __properties: ClassVar[List[str]] = ["id", "datetime", "function", "error_code", "error_message", "http_url", "http_method", "http_code", "http_time", "http_response"]

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
        """Create an instance of SerpErrorsResultInfo from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if datetime (nullable) is None
        # and model_fields_set contains the field
        if self.datetime is None and "datetime" in self.model_fields_set:
            _dict['datetime'] = None

        # set to None if function (nullable) is None
        # and model_fields_set contains the field
        if self.function is None and "function" in self.model_fields_set:
            _dict['function'] = None

        # set to None if error_code (nullable) is None
        # and model_fields_set contains the field
        if self.error_code is None and "error_code" in self.model_fields_set:
            _dict['error_code'] = None

        # set to None if error_message (nullable) is None
        # and model_fields_set contains the field
        if self.error_message is None and "error_message" in self.model_fields_set:
            _dict['error_message'] = None

        # set to None if http_url (nullable) is None
        # and model_fields_set contains the field
        if self.http_url is None and "http_url" in self.model_fields_set:
            _dict['http_url'] = None

        # set to None if http_method (nullable) is None
        # and model_fields_set contains the field
        if self.http_method is None and "http_method" in self.model_fields_set:
            _dict['http_method'] = None

        # set to None if http_code (nullable) is None
        # and model_fields_set contains the field
        if self.http_code is None and "http_code" in self.model_fields_set:
            _dict['http_code'] = None

        # set to None if http_time (nullable) is None
        # and model_fields_set contains the field
        if self.http_time is None and "http_time" in self.model_fields_set:
            _dict['http_time'] = None

        # set to None if http_response (nullable) is None
        # and model_fields_set contains the field
        if self.http_response is None and "http_response" in self.model_fields_set:
            _dict['http_response'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SerpErrorsResultInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "datetime": obj.get("datetime"),
            "function": obj.get("function"),
            "error_code": obj.get("error_code"),
            "error_message": obj.get("error_message"),
            "http_url": obj.get("http_url"),
            "http_method": obj.get("http_method"),
            "http_code": obj.get("http_code"),
            "http_time": obj.get("http_time"),
            "http_response": obj.get("http_response")
        })
        return _obj


