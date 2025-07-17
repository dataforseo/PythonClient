from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DomainAnalyticsTechnologiesAggregationTechnologiesLiveRequestInfo(BaseModel):
    """
    DomainAnalyticsTechnologiesAggregationTechnologiesLiveRequestInfo
    """ # noqa: E501
    group: Optional[StrictStr] = Field(default=None, description="id of the target technology group. required field if you don’t specify technology, category  or keyword. at least one field (group, category, keyword, technology) must be set. you can find the full list of technology group ids on this page. example:. 'marketing'")
    category: Optional[StrictStr] = Field(default=None, description="id of the target technology category. required field if you don’t specify group, keyword or technology. at least one field (group, category, keyword, technology) must be set. you can find the full list of technology category ids on this page. example:. 'crm'")
    technology: Optional[StrictStr] = Field(default=None, description="target technology. required field if you don’t specify group, keyword or category. at least one field (group, category, keyword, technology) must be set. you can find the full list of technologies on this page. example:. 'Salesforce'")
    keyword: Optional[StrictStr] = Field(default=None, description="target keyword in the domain’s meta keywords. required field if you don’t specify group, category or technology. at least one field (group, category, keyword, technology) must be set. UTF-8 encoding. example:. 'seo'. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    mode: Optional[StrictStr] = Field(default=None, description="search mode. optional field. possible search mode types:. as_is – search for results exactly matching the specified group ids, category ids, or technology names. entry – search for results matching a part of the specified group ids, category ids, or technology names. default value: as_is")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. <, <=, >, >=, =, <>, in, not_in, like,not_like. you can use the % operator with like and not_like to match any string of zero or more characters. you can use the following parameters to filter the results: domain_rank, last_visited, country_iso_code, language_code, content_language_code. Note: all filtering parameters are taken from the domain_technology_item of the domain_technologies endpoint;. example:. [['country_iso_code','=','US'],. 'and',. ['domain_rank','>',800]]for more information about filters, please refer to Domain Analytics Technologies API – Filters")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. you can use the following values to sort the results: groups_count, categories_count, technologies_count. possible sorting types:. asc – results will be sorted in the ascending order. desc – results will be sorted in the descending order. you should use a comma to set up a sorting type. example:. ['groups_count,desc']. note that you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['groups_count,desc','technologies_count,desc']. default value:. ['groups_count,desc','categories_count,desc','technologies_count,desc']")
    internal_groups_list_limit: Optional[StrictInt] = Field(default=None, description="maximum number of returned technology groups. optional field. you can use this field to limit the number of items with identical 'group' in the results. default value: 5. minimum value: 1. maximum value: 10000")
    internal_categories_list_limit: Optional[StrictInt] = Field(default=None, description="maximum number of returned technology categories within the same group. optional field. you can use this field to limit the number of items with identical 'category' in the results. default value: 5. minimum value: 1. maximum value: 10000")
    internal_technologies_list_limit: Optional[StrictInt] = Field(default=None, description="maximum number of returned technologies within the same category. optional field. you can use this field to limit the number of items with identical 'technology' in the results. default value: 10. minimum value: 1. maximum value: 10000")
    internal_list_limit: Optional[StrictInt] = Field(default=None, description="maximum number of items with identical 'category', 'group', and 'technology'. optional field. if you use this field, the values specified in internal_groups_list_limit, internal_categories_list_limit and internal_technologies_list_limit will be ignored;. you can use this field to limit the number of items with identical 'category', 'group', or 'technology'. default value: 10. minimum value: 1. maximum value: 10000")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned technologies. optional field. default value: 100. maximum value: 10000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned domains. optional field. default value: 0. maximum value: 9999. if you specify the 10 value, the first ten technologies in the results array will be omitted and the data will be provided for the successive technologies")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "group", 
        "category", 
        "technology", 
        "keyword", 
        "mode", 
        "filters", 
        "order_by", 
        "internal_groups_list_limit", 
        "internal_categories_list_limit", 
        "internal_technologies_list_limit", 
        "internal_list_limit", 
        "limit", 
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

        _dict['group'] = self.group
        _dict['category'] = self.category
        _dict['technology'] = self.technology
        _dict['keyword'] = self.keyword
        _dict['mode'] = self.mode
        _dict['filters'] = self.filters
        _dict['order_by'] = self.order_by
        _dict['internal_groups_list_limit'] = self.internal_groups_list_limit
        _dict['internal_categories_list_limit'] = self.internal_categories_list_limit
        _dict['internal_technologies_list_limit'] = self.internal_technologies_list_limit
        _dict['internal_list_limit'] = self.internal_list_limit
        _dict['limit'] = self.limit
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
            "group": obj.get("group"),
            "category": obj.get("category"),
            "technology": obj.get("technology"),
            "keyword": obj.get("keyword"),
            "mode": obj.get("mode"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "internal_groups_list_limit": obj.get("internal_groups_list_limit"),
            "internal_categories_list_limit": obj.get("internal_categories_list_limit"),
            "internal_technologies_list_limit": obj.get("internal_technologies_list_limit"),
            "internal_list_limit": obj.get("internal_list_limit"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj