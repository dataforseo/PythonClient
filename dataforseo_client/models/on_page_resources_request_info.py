from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class OnPageResourcesRequestInfo(BaseModel):
    """
    OnPageResourcesRequestInfo
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="ID of the task. required field. you can get this ID in the response of the Task POST endpoint. example:. “07131248-1535-0216-1000-17384017ad04”")
    url: Optional[StrictStr] = Field(default=None, description="page URL. optional field. specify this field if you want to get the resources for a specific page. note that to obtain resource’s meta from a particular URL, you should specify the URL in this field;. if you do not indicate a url when setting a task, resource’s meta in the results will be returned based on the data from the page where our crawler first saw the resource")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned resources. optional field. default value: 100. maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned resources. optional field. default value: 0. if you specify the 10 value, the first ten resources in the results array will be omitted and the data will be provided for the successive resources")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, not_regex, <, <=, >, >=, =, <>, in, not_in, like, not_like. you can use the % operator with like and not_like to match any string of zero or more characters. example:. ['resource_type','=','stylesheet']. [['resource_type','=','image'],. 'and',['checks.is_https','=',false]]. [['fetch_timing.duration_time','>',1],'and',[['total_transfer_size','>',100],'or',['checks.high_loading_time','=',true]]]. The full list of possible filters is available by this link.")
    relevant_pages_filters: Optional[List[Optional[StrictStr]]] = Field(default=None, description="filter the resources by relevant pages. optional field. you can use this field to obtain resources from pages matching to the defined parameters. you can apply the same filters here as available for the pages endpoint. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, not_regex, <, <=, >, >=, =, <>, in, not_in, like, not_like. you can use the % operator with like and not_like to match any string of zero or more characters. example:. ['checks.no_image_title','=',true]")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. you can use the same values as in the filters array to sort the results. possible sorting types:. asc – results will be sorted in the ascending order. desc – results will be sorted in the descending order. you should use a comma to set up a sorting type. example:. ['size,desc']. note that you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['size,desc','fetch_timing.fetch_end,desc']")
    search_after_token: Optional[StrictStr] = Field(default=None, description="token for subsequent requests. optional field. provided in the identical filed of the response to each request;. use this parameter to avoid timeouts while trying to obtain over 20,000 results in a single request;. by specifying the unique search_after_token value from the response array, you will get the subsequent results of the initial task;. search_after_token values are unique for each subsequent task ;. Note: if the search_after_token is specified in the request, all other parameters should be identical to the previous request")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "id", 
        "url", 
        "limit", 
        "offset", 
        "filters", 
        "relevant_pages_filters", 
        "order_by", 
        "search_after_token", 
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

        _dict['id'] = self.id
        _dict['url'] = self.url
        _dict['limit'] = self.limit
        _dict['offset'] = self.offset
        _dict['filters'] = self.filters
        _dict['relevant_pages_filters'] = self.relevant_pages_filters
        _dict['order_by'] = self.order_by
        _dict['search_after_token'] = self.search_after_token
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "url": obj.get("url"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "filters": obj.get("filters"),
            "relevant_pages_filters": obj.get("relevant_pages_filters"),
            "order_by": obj.get("order_by"),
            "search_after_token": obj.get("search_after_token"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj