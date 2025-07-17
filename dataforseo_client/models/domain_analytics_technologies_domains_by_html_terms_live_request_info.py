from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveRequestInfo(BaseModel):
    """
    DomainAnalyticsTechnologiesDomainsByHtmlTermsLiveRequestInfo
    """ # noqa: E501
    search_terms: Optional[List[Optional[StrictStr]]] = Field(default=None, description="target search terms. required field. specify target HTML elements, tags, attributes, their content or all of the above. if you specify more than one search term, you will receive only the domains containing all of the specified terms in the HTML code of their homepage. maximum number of search terms you can specify: 10. example:. ['data-attrid']")
    keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="target keywords in the domain’s title, description or meta keywords. optional field. UTF-8 encoding. maximum number of keywords you can specify: 10. example:. ['seo','software']. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    mode: Optional[StrictStr] = Field(default=None, description="search mode. optional field. possible search mode types:. strict_entry – search for results exactly matching the order, intervals and separators in the specified search terms. entry – search for results ignoring the order, intervals and separators in the specified search terms. default value: entry")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. <, <=, >, >=, =, <>, in, not_in, like, not_like. you can use the % operator with like and not_like to match any string of zero or more characters. example:. ['domain','like','%seo%']. [['country_iso_code','=','US'],. 'and',. ['domain_rank','>',100]]. [['domain_rank','>',100],. 'and',. [['country_iso_code','=','US'],'or',['country_iso_code','=','CA']]]. for more information about filters, please refer to Domain Analytics Technologies API – Filters")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. available fields:. domain_rank, domain, last_visited, country_iso_code, language_code, content_language_code. possible sorting types:. asc – results will be sorted in the ascending order. desc – results will be sorted in the descending order. you should use a comma to set up a sorting type. example:. ['last_visited,desc']. default rule:. ['domain_rank,desc']. note that you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['last_visited,desc','domain_rank,desc']")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned domains. optional field. default value: 100. maximum value: 10000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned domains. optional field. default value: 0. if you specify the 10 value, the first ten domains in the results array will be omitted and the data will be provided for the successive domains;. Note: the maximum value is 9999, the sum of limit and offset must not exceed 10000;. use the offset_token if you would like to offset more results")
    offset_token: Optional[StrictStr] = Field(default=None, description="token for subsequent requests. optional field. provided in the identical filed of the response to each request;. use this parameter to avoid timeouts while trying to obtain over 100,000 results in a single request;. by specifying the unique offset_token value from the response array, you will get the subsequent results of the initial task;. offset_token values are unique for each subsequent task. Note: if the offset_token is specified in the request, all other parameters should be identical to the previous request")
    __properties: ClassVar[List[str]] = [
        "search_terms", 
        "keywords", 
        "mode", 
        "filters", 
        "order_by", 
        "limit", 
        "offset", 
        "offset_token", 
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

        _dict['search_terms'] = self.search_terms
        _dict['keywords'] = self.keywords
        _dict['mode'] = self.mode
        _dict['filters'] = self.filters
        _dict['order_by'] = self.order_by
        _dict['limit'] = self.limit
        _dict['offset'] = self.offset
        _dict['offset_token'] = self.offset_token
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "search_terms": obj.get("search_terms"),
            "keywords": obj.get("keywords"),
            "mode": obj.get("mode"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "offset_token": obj.get("offset_token"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj