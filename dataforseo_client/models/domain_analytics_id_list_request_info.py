from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DomainAnalyticsIdListRequestInfo(BaseModel):
    """
    DomainAnalyticsIdListRequestInfo
    """ # noqa: E501
    datetime_from: Optional[StrictStr] = Field(default=None, description="start time for filtering results. required field. if include_metadata is set to true, maximum value: a month from current datetime;. if include_metadata is set to false, maximum value: six months from current datetime;. must be specified in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2023-01-15 12:57:46 +00:00")
    datetime_to: Optional[StrictStr] = Field(default=None, description="finish time for filtering results. required field. maximum value: current datetime;. must be specified in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2023-01-31 13:57:46 +00:00")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned task IDs. optional field. default value: 1000. maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned task IDs. optional field. default value: 0. if you specify the 10 value, the first ten tasks in the results array will be omitted")
    sort: Optional[StrictStr] = Field(default=None, description="sorting by task execution time. optional field. possible values: 'asc', 'desc'. default value: 'asc'")
    include_metadata: Optional[StrictBool] = Field(default=None, description="include task metadata in the respond. optional field. default value: false")
    __properties: ClassVar[List[str]] = [
        "datetime_from", 
        "datetime_to", 
        "limit", 
        "offset", 
        "sort", 
        "include_metadata", 
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

        _dict['datetime_from'] = self.datetime_from
        _dict['datetime_to'] = self.datetime_to
        _dict['limit'] = self.limit
        _dict['offset'] = self.offset
        _dict['sort'] = self.sort
        _dict['include_metadata'] = self.include_metadata
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "datetime_from": obj.get("datetime_from"),
            "datetime_to": obj.get("datetime_to"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "sort": obj.get("sort"),
            "include_metadata": obj.get("include_metadata"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj