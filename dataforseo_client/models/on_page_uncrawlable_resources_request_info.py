from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class OnPageUncrawlableResourcesRequestInfo(BaseModel):
    """
    OnPageUncrawlableResourcesRequestInfo
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description=r"ID of the taskrequired fieldyou can get this ID in the response of the Task POST endpointexample:'07131248-1535-0216-1000-17384017ad04'")
    limit: Optional[StrictInt] = Field(default=None, description=r"the maximum number of returned uncrawlable resourcesoptional fielddefault value: 100maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description=r"offset in the results array of returned uncrawlable resourcesoptional fielddefault value: 0 maximum value: 2000000if you specify the 10 value, the first ten invalid resources in the results array will be omitted and the data will be provided for the successive invalid resources")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"results sorting rulesoptional fieldyou can use the same values as in the filters array to sort the resultspossible sorting types:asc - results will be sorted in the ascending orderdesc - results will be sorted in the descending orderyou should use a comma to set up a sorting typeexample:['meta.content_type,desc']note that you can set no more than three sorting rules in a single requestyou should use a comma to separate several sorting rulesexample:['meta.content_type,asc','fetch_time,desc']")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description=r"array of results filtering parametersoptional fieldyou can add several filters at once (8 filters maximum)you should set a logical operator and, or between the conditionsthe following operators are supported:regex, not_regex, <, <=, >, >=, =, <>, in, not_in, like, not_likeyou can use the % operator with like and not_like to match any string of zero or more charactersexample: [['meta.content_type','=','image/jpeg'],'and',['url','not_like','%/help-center/%']]The full list of possible filters is available by this link.")
    __properties: ClassVar[List[str]] = [
        "id", 
        "limit", 
        "offset", 
        "order_by", 
        "filters", 
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
        _dict['limit'] = self.limit
        _dict['offset'] = self.offset
        _dict['order_by'] = self.order_by
        _dict['filters'] = self.filters
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "order_by": obj.get("order_by"),
            "filters": obj.get("filters"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj