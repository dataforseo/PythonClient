from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_status_endpoints_info import AppendixStatusEndpointsInfo



class AppendixStatusResultInfo(BaseModel):
    """
    AppendixStatusResultInfo
    """ # noqa: E501
    api: Optional[StrictStr] = Field(default=None, description="name of the API. the list of APIs:. serp. keywords_data. appendix. dataforseo_labs. domain_analytics. merchant. on_page. business_data. backlinks. app_data. content_analysis. content_generation")
    status: Optional[StrictStr] = Field(default=None, description="current status. you can find all information about the statuses of our endpoints for the last 60 days here. the list of possible current statuses:. major_outage. partial_outage. long_response_time. long_execution_time. webhook_delay. send_delay")
    endpoints: Optional[List[Optional[AppendixStatusEndpointsInfo]]] = Field(default=None, description="array of objects that contain status information for API endpoints")
    __properties: ClassVar[List[str]] = [
        "api", 
        "status", 
        "endpoints", 
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

        _dict['api'] = self.api
        _dict['status'] = self.status
        endpoints_items = []
        if self.endpoints:
            for _item in self.endpoints:
                if _item:
                    endpoints_items.append(_item.to_dict())
            _dict['endpoints'] = endpoints_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "api": obj.get("api"),
            "status": obj.get("status"),
            "endpoints": [AppendixStatusEndpointsInfo.from_dict(_item) for _item in obj["endpoints"]] if obj.get("endpoints") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj