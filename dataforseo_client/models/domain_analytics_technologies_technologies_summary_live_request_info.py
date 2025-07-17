from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DomainAnalyticsTechnologiesTechnologiesSummaryLiveRequestInfo(BaseModel):
    """
    DomainAnalyticsTechnologiesTechnologiesSummaryLiveRequestInfo
    """ # noqa: E501
    technology_paths: Optional[List[Optional[StrictStr]]] = Field(default=None, description="target technology paths. required field if you don’t specify groups, technologies and categories. each technology path should be specified as a separate object containing “path” and “name”, where “path” is specified as “$group_id.$category_id” and “name” – as the name of the target technology;. each object with a technology path should be separated with a comma. you can find the full list of technology group ids, category ids and technology names on this page. note: you can specify up to 10 technology paths in this array. example:. [{'path': 'content.cms','name': 'wordpress'}, {'path': 'marketing.crm','name': 'salesforce'}]")
    groups: Optional[List[Optional[StrictStr]]] = Field(default=None, description="ids of the target technology groups. required field if you don’t specify technologies, technology_paths, categories, or keywords. you can find the full list of technology group ids on this page. note: you can specify up to 10 technology groups in this array. example:. ['sales', 'marketing']")
    categories: Optional[List[Optional[StrictStr]]] = Field(default=None, description="ids of the target technology categories. required field if you don’t specify groups, technology_paths, technologies, or keywords. you can find the full list of technology category ids on this page. note: you can specify up to 10 technology categories in this array. example:. ['payment_processors','crm']")
    technologies: Optional[List[Optional[StrictStr]]] = Field(default=None, description="target technologies. required field if you don’t specify groups, technology_paths, categories, or keywords. you can find the full list of technologies you can specify here on this page. note: you can specify up to 10 technologies in this array. example:. ['Google Pay','Salesforce']")
    keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="target keywords in the domain’s title, description or meta keywords. required field if you don’t specify groups, technology_paths, categories, or technologies. you can specify the maximum of 10 keywords;. UTF-8 encoding;. example:. ['seo','software']. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    mode: Optional[StrictStr] = Field(default=None, description="search mode. optional field. possible search mode types:. as_is – search for results exactly matching the specified group ids, category ids, or technology names. entry – search for results matching a part of the specified group ids, category ids, or technology names. default value: as_is")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. <, <=, >, >=, =, <>, in, not_in, like,not_like. you can use the % operator with like and not_like to match any string of zero or more characters. you can use the following parameters to filter the results: domain_rank, last_visited, country_iso_code, language_code, content_language_code. example:. [['country_iso_code','=','US'],. 'and',. ['domain_rank','>',800]]. for more information about filters, please refer to Domain Analytics Technologies API – Filters")
    internal_list_limit: Optional[StrictInt] = Field(default=None, description="maximum number of elements within internal arrays. optional field. you can use this field to limit the number of elements within the following arrays:. countries, languages, content_languages, keywords. default value: 10. minimum value: 1. maximum value: 10000")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "technology_paths", 
        "groups", 
        "categories", 
        "technologies", 
        "keywords", 
        "mode", 
        "filters", 
        "internal_list_limit", 
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

        _dict['technology_paths'] = self.technology_paths
        _dict['groups'] = self.groups
        _dict['categories'] = self.categories
        _dict['technologies'] = self.technologies
        _dict['keywords'] = self.keywords
        _dict['mode'] = self.mode
        _dict['filters'] = self.filters
        _dict['internal_list_limit'] = self.internal_list_limit
        _dict['tag'] = self.tag
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
            "internal_list_limit": obj.get("internal_list_limit"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj