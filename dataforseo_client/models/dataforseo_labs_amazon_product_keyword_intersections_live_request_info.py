from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsAmazonProductKeywordIntersectionsLiveRequestInfo(BaseModel):
    """
    DataforseoLabsAmazonProductKeywordIntersectionsLiveRequestInfo
    """ # noqa: E501
    asins: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="asins of target products. required field. product IDs of the products for which you need to find keyword intersections;. specify the ASINs as in the following example:. 'asins': {. '1': '019005476X',. '2': '0190074442'. }. the maximum number of ASINs you can specify in this object is 20;. learn more about the parameter on this help center page")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location. required field if don’t specify location_code. you can receive the list of available locations with their location_name by making a separate request to. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;. Note: this endpoint currently supports the US, Egypt, Saudi Arabia, and the United Arab Emirates locations only;. example:. United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="location code. required field if don’t specify location_name. you can receive the list of available locations with their location_code by making a separate request to. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;. Note: this endpoint currently supports the US, Egypt, Saudi Arabia, and the United Arab Emirates locations only;. example:. 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of the language. required field if don’t specify language_code. you can receive the list of available languages with their language_name by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="language code. required field if don’t specify language_name. you can receive the list of available languages with their language_code by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. en")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of products in the results array. optional field. default value: 100;. maximum value: 1000")
    intersection_mode: Optional[StrictStr] = Field(default=None, description="mode for finding asin intersections. optional field. possible values: union, intersect;. default value: intersect;. learn more about the parameter in this help center guide")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, not_regex, <, <=, >, >=, =, <>, in, not_in, ilike, not_ilike, like, not_like, match, not_match. you can use the % operator with like and not_like, as well as ilike and not_ilike to match any string of zero or more characters. example:. ['avg_position','<', 10]. for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. you can use the same values as in the filters array to sort the results. possible sorting types:. asc – results will be sorted in the ascending order. desc – results will be sorted in the descending order. you should use a comma to set up a sorting parameter. example:. ['sum_position,desc']. note that you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['intersections,desc','avg_position,asc']. default rule:. ['intersections,desc']")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned keywords. optional field. default value: 0. if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "asins", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "limit", 
        "intersection_mode", 
        "filters", 
        "order_by", 
        "offset", 
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

        _dict['asins'] = self.asins
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['limit'] = self.limit
        _dict['intersection_mode'] = self.intersection_mode
        _dict['filters'] = self.filters
        _dict['order_by'] = self.order_by
        _dict['offset'] = self.offset
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "asins": obj.get("asins"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "limit": obj.get("limit"),
            "intersection_mode": obj.get("intersection_mode"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "offset": obj.get("offset"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj