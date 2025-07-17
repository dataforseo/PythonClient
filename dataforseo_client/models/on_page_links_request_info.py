from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class OnPageLinksRequestInfo(BaseModel):
    """
    OnPageLinksRequestInfo
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="ID of the task. required field. you can get this ID in the response of the Task POST endpoint. example:. “07131248-1535-0216-1000-17384017ad04”")
    page_from: Optional[StrictStr] = Field(default=None, description="relative page URL. optional field. if you use this field, the API response will contain only links from the specified page. note that in this field you can specify relative URLs only")
    page_to: Optional[StrictStr] = Field(default=None, description="relative page URL. optional field. if you use this field, the API response will contain only internal links pointing to the specified page. note that in this field you can specify relative URLs only")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned links. optional field. default value: 100. maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned links. optional field. default value: 0. if you specify the 10 value, the first ten links in the results array will be omitted and the data will be provided for the successive links")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, not_regex, =, <>, in, not_in, like, not_like. you can use the % operator with like and not_like to match any string of zero or more characters. example:. ['direction','=','external']. [['domain_to','<>','example.com'],. 'and',. ['link_from','not_like','%example.com/blog%']]. [['direction','=','external'],. 'and',. [['link_from','like','%example.com/blog%'],'or',['link_from','like','%example.com/help%']]]. The full list of possible filters is available by this link.")
    search_after_token: Optional[StrictStr] = Field(default=None, description="token for subsequent requests. optional field. provided in the identical filed of the response to each request;. use this parameter to avoid timeouts while trying to obtain over 20,000 results in a single request;. by specifying the unique search_after_token value from the response array, you will get the subsequent results of the initial task;. search_after_token values are unique for each subsequent task ;. Note: if the search_after_token is specified in the request, all other parameters should be identical to the previous request")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "id", 
        "page_from", 
        "page_to", 
        "limit", 
        "offset", 
        "filters", 
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
        _dict['page_from'] = self.page_from
        _dict['page_to'] = self.page_to
        _dict['limit'] = self.limit
        _dict['offset'] = self.offset
        _dict['filters'] = self.filters
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
            "page_from": obj.get("page_from"),
            "page_to": obj.get("page_to"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "filters": obj.get("filters"),
            "search_after_token": obj.get("search_after_token"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj