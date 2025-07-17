from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DomainAnalyticsWhoisOverviewLiveRequestInfo(BaseModel):
    """
    DomainAnalyticsWhoisOverviewLiveRequestInfo
    """ # noqa: E501
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned domains. optional field. default value: 100. maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned items. optional field. default value: 0. if you specify the 10 value, the first ten items in the results array will be omitted and the data will be provided for the successive items")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, <, <=, >, >=, =, <>, in, not_in, like, not_like. you can use the % operator with like and not_like to match any string of zero or more characters. examples:. ['expiration_datetime', '<', '2021-02-15 01:00:00 +00:00']. [['expiration_datetime', '<', '2021-02-15 01:00:00 +00:00'],.  'and', . ['domain', 'like', '%seo%']]. . for more information about filters, please refer to Filters Page or this help center guide")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. you can use the same values as in the filters array to sort the results. possible sorting types:. asc - results will be sorted in the ascending order. desc - results will be sorted in the descending order. the comma is used as a separator. example:. ['metrics.organic.pos_1,desc']. default rule:. ['metrics.organic.count,desc']. note that you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['expiration_datetime,asc','metrics.organic.etv,desc','metrics.organic.pos_1,desc']")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "limit", 
        "offset", 
        "filters", 
        "order_by", 
        "tag", 
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
        _dict['filters'] = self.filters
        _dict['order_by'] = self.order_by
        _dict['tag'] = self.tag
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
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj