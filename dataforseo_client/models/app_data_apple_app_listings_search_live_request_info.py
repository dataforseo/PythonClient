from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AppDataAppleAppListingsSearchLiveRequestInfo(BaseModel):
    """
    AppDataAppleAppListingsSearchLiveRequestInfo
    """ # noqa: E501
    categories: Optional[List[Optional[StrictStr]]] = Field(default=None, description="app categories. optional field. the categories you specify are used to search for app listings;. you can get the full list of available app listing categories by this link. you can specify up to 10 categories")
    description: Optional[StrictStr] = Field(default=None, description="keyword in the app’s description. optional field. keywords that occur in the description of the app;. can contain up to 200 characters")
    title: Optional[StrictStr] = Field(default=None, description="keyword in the app’s title. optional field. keywords that occur in the title of the app;. can contain up to 200 characters")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, not_regex, <, <=, >, >=, =, <>, in, not_in, like, not_like. you can use the % operator with like and not_like to match any string of zero or more characters. example:. ['rating.value','>',3]. you can receive the list of available filters by making a separate request to https://api.dataforseo.com/v3/app_data/apple/app_listings/available_filters")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. you can use the same values as in the filters array to sort the results. possible sorting types:. asc – results will be sorted in the ascending order. desc – results will be sorted in the descending order. you should use a comma to set up a sorting parameter. example:. ['item.rating.value,desc']. note that you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['item.rating.value,desc','item.rating.value,desc']")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned apps. optional field. default value: 100. maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned apps. optional field. default value: 0. if you specify the 10 value, the first ten entities in the results array will be omitted and the data will be provided for the successive entities")
    offset_token: Optional[StrictStr] = Field(default=None, description="token for subsequent requests. optional field. provided in the identical filed of the response to each request;. use this parameter to avoid timeouts while trying to obtain over 100,000 results in a single request;. by specifying the unique offset_token value from the response array, you will get the subsequent results of the initial task;. offset_token values are unique for each subsequent task. Note: if the offset_token is specified in the request, all other parameters should be identical to the previous request")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "categories", 
        "description", 
        "title", 
        "filters", 
        "order_by", 
        "limit", 
        "offset", 
        "offset_token", 
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

        _dict['categories'] = self.categories
        _dict['description'] = self.description
        _dict['title'] = self.title
        _dict['filters'] = self.filters
        _dict['order_by'] = self.order_by
        _dict['limit'] = self.limit
        _dict['offset'] = self.offset
        _dict['offset_token'] = self.offset_token
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "categories": obj.get("categories"),
            "description": obj.get("description"),
            "title": obj.get("title"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "offset_token": obj.get("offset_token"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj