from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AppendixStatusEndpointsInfo(BaseModel):
    """
    AppendixStatusEndpointsInfo
    """ # noqa: E501
    endpoint: Optional[StrictStr] = Field(default=None, description="name of the endpoint. the list of possible endpoints:. task_get. task_post. live. postback/pingback")
    status: Optional[StrictStr] = Field(default=None, description="current status. you can find all information about your API statuses for the last 60 days here. the list of possible current statuses:. major_outage. partial_outage. long_response_time. long_execution_time. webhook_delay. send_delay")
    __properties: ClassVar[List[str]] = [
        "endpoint", 
        "status", 
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

        _dict['endpoint'] = self.endpoint
        _dict['status'] = self.status
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "endpoint": obj.get("endpoint"),
            "status": obj.get("status"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj