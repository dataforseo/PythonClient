from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsBingDomainIntersectionLiveRequestInfo(BaseModel):
    """
    DataforseoLabsBingDomainIntersectionLiveRequestInfo
    """ # noqa: E501
    target_1: Optional[StrictStr] = Field(default=None, description="domain. required field. the domain name of the first target website. the domain should be specified without https:// and www.")
    target_2: Optional[StrictStr] = Field(default=None, description="domain. required field. the domain name of the second target website. the domain should be specified without https:// and www.")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location. required field if you don’t specify location_code. Note: it is required to specify either location_name or location_code. you can receive the list of available locations with their location_name by making a separate request to. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;. Note: this endpoint currently supports the US location only;. example:. United States")
    location_code: Optional[StrictInt] = Field(default=None, description="location code. required field if you don’t specify location_name. Note: it is required to specify either location_name or location_code. you can receive the list of available locations with their location_code by making a separate request to. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;. Note: this endpoint currently supports the US location only;. example:. 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of the language. required field if you don’t specify language_code. Note: it is required to specify either language_name or language_code. you can receive the list of available languages with their language_name by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="language code. required field if you don’t specify language_name. Note: it is required to specify either language_name or language_code. you can receive the list of available languages with their language_code by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. en")
    intersections: Optional[StrictBool] = Field(default=None, description="domain intersections in SERP. optional field. if you set intersections to true, you will get the keywords for which both target domains specified as target1 and target2 have results within the same SERP; the corresponding SERP elements for both domains will be provided in the results array. Note: this endpoint will not provide results if the number of intersecting keywords exceeds 10 million. if you specify intersections: false, you will get the keywords for which the domain specified as target1 has results in SERP, and the domain specified as target2 doesn’t;. thus, the corresponding SERP elements and other data will be provided for the domain specified as target1only. default value: true")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="search results type. indicates type of search results included in the response. optional field. possible values:. ['organic', 'paid', 'featured_snippet', 'local_pack']. default value:. ['organic', 'paid']")
    include_serp_info: Optional[StrictBool] = Field(default=None, description="include data from SERP for each keyword. optional field. if set to true, we will return a serp_info array containing SERP data (number of search results, relevant URL, and SERP features) for every keyword in the response. default value: false")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned keywords. optional field. default value: 100. maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the items array of returned keywords. optional field. default value: 0. if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, not_regex, <, <=, >, >=, =, <>, in, not_in, ilike, not_ilike, like, not_like, match, not_match. you can use the % operator with like and not_like, as well as ilike and not_ilike to match any string of zero or more characters. example:. ['keyword_data.keyword_info.search_volume','in',[100,1000]]. [['first_domain_serp_element.etv','>',0],'and',['first_domain_serp_element.description','like','%goat%']]. [['keyword_data.keyword_info.search_volume','>',100],. 'and',. [['first_domain_serp_element.description','like','%goat%'],. 'or',. ['second_domain_serp_element.type','=','organic']]]. for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. you can use the same values as in the filters array to sort the results. possible sorting types:. asc – results will be sorted in the ascending order. desc – results will be sorted in the descending order. you should use a comma to set up a sorting parameter. example:. ['keyword_data.keyword_info.competition,desc']. default rule:. ['keyword_data.keyword_info.search_volume,desc']. note that you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['keyword_data.keyword_info.search_volume,desc','keyword_data.keyword_info.cpc,desc']")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "target1", 
        "target2", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "intersections", 
        "item_types", 
        "include_serp_info", 
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

        _dict['target1'] = self.target_1
        _dict['target2'] = self.target_2
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['intersections'] = self.intersections
        _dict['item_types'] = self.item_types
        _dict['include_serp_info'] = self.include_serp_info
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
            "target_1": obj.get("target1"),
            "target_2": obj.get("target2"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "intersections": obj.get("intersections"),
            "item_types": obj.get("item_types"),
            "include_serp_info": obj.get("include_serp_info"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj