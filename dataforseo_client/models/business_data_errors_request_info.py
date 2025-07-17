from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BusinessDataErrorsRequestInfo(BaseModel):
    """
    BusinessDataErrorsRequestInfo
    """ # noqa: E501
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned tasks that responded with an error. optional field. default value: 1000. maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned tasks. optional field. default value: 0. if you specify the 10 value, the first ten tasks in the results array will be omitted and the data will be provided for the successive tasks")
    filtered_function: Optional[StrictStr] = Field(default=None, description="return tasks with a certain function. use this field to obtain a list of tasks that returned an error filtered by a certain function. you can filter the results by the values you receive in the function fields of the API response. i.e., once you receive unfiltered results, you can call this API again to filter them by function. example: hotel_searches/task_post, postback_url, pingback_url")
    datetime_from: Optional[StrictStr] = Field(default=None, description="start time for filtering results. optional field. allows filtering results by the datetime parameter within the range of the last 7 days;. must be specified in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2021-11-15 12:57:46 +00:00")
    datetime_to: Optional[StrictStr] = Field(default=None, description="finish time for filtering results. optional field. allows filtering results by the datetime parameter within the range of the last 7 days;. must be specified in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2021-11-15 13:57:46 +00:00")
    __properties: ClassVar[List[str]] = [
        "limit", 
        "offset", 
        "filtered_function", 
        "datetime_from", 
        "datetime_to", 
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

        _dict['limit'] = self.limit
        _dict['offset'] = self.offset
        _dict['filtered_function'] = self.filtered_function
        _dict['datetime_from'] = self.datetime_from
        _dict['datetime_to'] = self.datetime_to
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "filtered_function": obj.get("filtered_function"),
            "datetime_from": obj.get("datetime_from"),
            "datetime_to": obj.get("datetime_to"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj