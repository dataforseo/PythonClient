from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo(BaseModel):
    """
    DomainAnalyticsTechnologiesDomainsByTechnologyLiveRequestInfo
    """ # noqa: E501
    technology_paths: Optional[List[Optional[StrictStr]]] = Field(default=None, description="target technology paths. required field if you don’t specify groups, technologies, keywords or categories. at least one field (technology_paths, groups, technologies, keywords or categories) must be set;. each technology path should be specified as a separate object containing “path” and “name”, where “path” is specified as “$group_id.$category_id” and “name” – as the name of the target technology;. each object with a technology path should be separated with a comma. you can find the full list of technology group ids, category ids and technology names on this page. note: you can specify up to 10 technology paths in this array. example:. [{'path': 'content.cms','name': 'wordpress'}, {'path': 'marketing.crm','name': 'salesforce'}]")
    groups: Optional[List[Optional[StrictStr]]] = Field(default=None, description="ids of the target technology groups. required field if you don’t specify technologies, technology_paths, keywords or categories. you can find the full list of technology group ids on this page. note: you can specify up to 10 technology groups in this array. example:. ['sales', 'marketing']")
    categories: Optional[List[Optional[StrictStr]]] = Field(default=None, description="ids of the target technology categories. required field if you don’t specify groups, technology_paths, keywords or technologies. you can find the full list of technology category ids on this page. note: you can specify up to 10 technology categories in this array. example:. ['payment_processors','crm']")
    technologies: Optional[List[Optional[StrictStr]]] = Field(default=None, description="target technologies. required field if you don’t specify groups, technology_paths, keywords or categories. you can find the full list of technologies you can specify here on this page. note: you can specify up to 10 technologies in this array. example:. ['Google Pay','Salesforce']")
    keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="target keywords in the domain’s title, description or meta keywords. required field if you don’t specify groups, technology_paths, technologies or categories. optional field. you can specify the maximum of 10 keywords;. UTF-8 encoding;. example:. ['seo','software']. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    mode: Optional[StrictStr] = Field(default=None, description="search mode. optional field. possible search mode types:. as_is – search for results exactly matching the specified group ids, category ids, or technology names. entry – search for results matching a part of the specified group ids, category ids, or technology names. default value: as_is")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. <, <=, >, >=, =, <>, in, not_in, like, not_like. you can use the % operator with like and not_like to match any string of zero or more characters. example:. ['country_iso_code','=','US']. [['country_iso_code','=','US'],. 'and',. ['domain_rank','>',100]]. [['domain_rank','>',100],. 'and',. [['country_iso_code','=','US'],'or',['country_iso_code','=','CA']]]. for more information about filters, please refer to Domain Analytics Technologies API – Filters")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. available fields:. domain_rank, domain, last_visited, country_iso_code, language_code, content_language_code. possible sorting types:. asc – results will be sorted in the ascending order. desc – results will be sorted in the descending order. you should use a comma to set up a sorting type. example:. ['last_visited,desc']. default rule:. ['domain_rank,desc']. note that you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['last_visited,desc','domain_rank,desc']")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned domains. optional field. default value: 100. maximum value: 10000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned domains. optional field. default value: 0. if you specify the 10 value, the first ten domains in the results array will be omitted and the data will be provided for the successive domains;. Note: the maximum value is 9999, the sum of limit and offset must not exceed 10000;. use the offset_token if you would like to offset more results")
    offset_token: Optional[StrictStr] = Field(default=None, description="token for subsequent requests. optional field. provided in the identical filed of the response to each request;. use this parameter to avoid timeouts while trying to obtain over 100,000 results in a single request;. by specifying the unique offset_token value from the response array, you will get the subsequent results of the initial task;. offset_token values are unique for each subsequent task. Note: if the offset_token is specified in the request, all other parameters should be identical to the previous request")
    __properties: ClassVar[List[str]] = [
        "technology_paths", 
        "groups", 
        "categories", 
        "technologies", 
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

        _dict['technology_paths'] = self.technology_paths
        _dict['groups'] = self.groups
        _dict['categories'] = self.categories
        _dict['technologies'] = self.technologies
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
            "technology_paths": obj.get("technology_paths"),
            "groups": obj.get("groups"),
            "categories": obj.get("categories"),
            "technologies": obj.get("technologies"),
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