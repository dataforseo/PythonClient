from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsBingSerpCompetitorsLiveRequestInfo(BaseModel):
    """
    DataforseoLabsBingSerpCompetitorsLiveRequestInfo
    """ # noqa: E501
    keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="keywords array. required field. the results will be based on the keywords you specify in this array. UTF-8 encoding;. the keywords will be converted to lowercase format;. you can specify the maximum of 200 keywords. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location. required field if you don’t specify location_code. Note: it is required to specify either location_name or location_code. you can receive the list of available locations with location_name parameters by making a separate request to. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;. Note: this endpoint currently supports the US location only;. example:. United States")
    location_code: Optional[StrictInt] = Field(default=None, description="unique location identifier. required field if you don’t specify location_name. Note: it is required to specify either location_name or location_code. you can receive the list of available locations with their location_code parameters by making a separate request to. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;. Note: this endpoint currently supports the US location only;. example:. 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of the language. required field if you don’t specify language_code. Note: it is required to specify either language_name or language_code. you can receive the list of available languages with their language_name parameters by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="unique language identifier. required field if you don’t specify language_name. Note: it is required to specify either language_name or language_code. you can receive the list of available languages with their language_code parameters by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. en")
    include_subdomains: Optional[StrictBool] = Field(default=None, description="indicates if the subdomains will be included in the search. optional field. if set to false, the subdomains will be ignored. default value: true")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="search results type. indicates type of search results included in the response. optional field. possible values:. ['organic', 'paid', 'featured_snippet', 'local_pack']. default value:. ['organic', 'paid', 'featured_snippet', 'local_pack']")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned domains. optional field. default value: 100. maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned domains. optional field. default value: 0. if you specify the 10 value, the first ten domains in the results array will be omitted and the data will be provided for the successive domains")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, not_regex, <, <=, >, >=, =, <>, in, not_in, ilike, not_ilike, like, not_like, match, not_match. you can use the % operator with like and not_like, as well as ilike and not_ilike to match any string of zero or more characters. example:. ['median_position','in',[1,10]]. [['median_position','in',[1,10]],'and',['domain','not_like','%wikipedia.org%']]. [['domain','not_like','%wikipedia.org%'],. 'and',. [['relevant_serp_items','>',0],'or',['median_position','in',[1,10]]]]. for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. you can use the same values as in the filters array to sort the results. possible sorting types:. asc – results will be sorted in the ascending order. desc – results will be sorted in the descending order. the comma is used as a separator. example:. ['avg_position,asc']. default rule:. ['rating,desc']. note that you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['avg_position,asc','etv,desc']")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "keywords", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "include_subdomains", 
        "item_types", 
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

        _dict['keywords'] = self.keywords
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['include_subdomains'] = self.include_subdomains
        _dict['item_types'] = self.item_types
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
            "keywords": obj.get("keywords"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "include_subdomains": obj.get("include_subdomains"),
            "item_types": obj.get("item_types"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj