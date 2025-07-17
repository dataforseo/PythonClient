from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class KeywordsDataErrorsResultInfo(BaseModel):
    """
    KeywordsDataErrorsResultInfo
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="id of the task")
    datetime: Optional[StrictStr] = Field(default=None, description="date and time when an error occurred. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    function: Optional[StrictStr] = Field(default=None, description="corresponding API function")
    error_code: Optional[StrictInt] = Field(default=None, description="error code")
    error_message: Optional[StrictStr] = Field(default=None, description="error message or error URL. error message (see full list) or URL that caused an error")
    http_url: Optional[StrictStr] = Field(default=None, description="URL that caused an error. URL you used for making an API call or pingback/postback URL")
    http_method: Optional[StrictStr] = Field(default=None, description="HTTP method")
    http_code: Optional[StrictInt] = Field(default=None, description="HTTP status code")
    http_time: Optional[StrictFloat] = Field(default=None, description="time taken by HTTP request. for tasks set with a pingback/postback, this field will show the time it took your server to respond")
    http_response: Optional[StrictStr] = Field(default=None, description="HTTP response. server response")
    __properties: ClassVar[List[str]] = [
        "id", 
        "datetime", 
        "function", 
        "error_code", 
        "error_message", 
        "http_url", 
        "http_method", 
        "http_code", 
        "http_time", 
        "http_response", 
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
        _dict['datetime'] = self.datetime
        _dict['function'] = self.function
        _dict['error_code'] = self.error_code
        _dict['error_message'] = self.error_message
        _dict['http_url'] = self.http_url
        _dict['http_method'] = self.http_method
        _dict['http_code'] = self.http_code
        _dict['http_time'] = self.http_time
        _dict['http_response'] = self.http_response
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
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
            "http_response": obj.get("http_response"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj