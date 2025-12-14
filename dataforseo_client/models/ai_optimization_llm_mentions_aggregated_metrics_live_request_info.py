from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_ai_optimization_l_lm_mentions_target_element import BaseAiOptimizationLLmMentionsTargetElement



class AiOptimizationLlmMentionsAggregatedMetricsLiveRequestInfo(BaseModel):
    """
    AiOptimizationLlmMentionsAggregatedMetricsLiveRequestInfo
    """ # noqa: E501
    target: Optional[List[Optional[BaseAiOptimizationLLmMentionsTargetElement]]] = Field(default=None, description=r"array of objects containing target entities. required field. you can specify up to 10 entities (objects) in the target field. one target entity can contain either one domain or one keyword and related parameters. examples:. . target array with a domain entity")
    domain: Optional[StrictStr] = Field(default=None, description=r"target domain. required field if you don’t specify keyword. a domain should be specified without https:// and www.")
    search_filter: Optional[StrictStr] = Field(default=None, description=r"target keyword search filter. optional field. possible values:. include, exclude. default value: include")
    search_scope: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"target keyword search scope. optional field. possible values:. any, question, answer, brand_entities, fan_out_queries. default value: any")
    include_subdomains: Optional[StrictBool] = Field(default=None, description=r"indicates if the subdomains of the target domain will be included in the search. optional field. if set to true, the subdomains will be included in the search. default value: false")
    keyword: Optional[StrictStr] = Field(default=None, description=r"target keyword. required field if you don’t specify domain. you can specify up to 2000 characters in the keyword field. all %## will be decoded (plus character ‘+’ will be decoded to a space character). if you need to use the “%” character for your keyword, please specify it as “%25”;. if you need to use the “+” character for your keyword, please specify it as “%2B”. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    match_type: Optional[StrictStr] = Field(default=None, description=r"target keyword match type. optional field. word_match – режим повнотекстового пошуку,  full-text search for terms that match the specified seed keyword with additional words included before, after, or within the seed key phrase.. partial_match – режим пошуку підстроки в слові. possible values:. word_match, partial_match. default value: word_match")
    location_name: Optional[StrictStr] = Field(default=None, description=r"full name of search location. optional field. if you use this field, you don’t need to specify location_code. if you don’t specify this field, the location_code with 2840 value will be used by default;. you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages. Note: chat_gpt data is available for United States only")
    location_code: Optional[StrictInt] = Field(default=None, description=r"search location code. optional field. if you use this field, you don’t need to specify location_name. you can receive the list of available locations of the search engine with their location_code by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages. default value: 2840. Note: chat_gpt data is available for 2840 only")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of search language. optional field. if you use this field, you don’t need to specify language_code;. if you don’t specify this field, the language_code with en value will be used by default;. you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages. Note: chat_gpt data is available for English only")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search language code. optional field. if you use this field, you don’t need to specify language_name;. you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages. default value: en. Note: chat_gpt data is available for en only")
    platform: Optional[StrictStr] = Field(default=None, description=r"target platform. optional field. possible values:. chat_gpt, google. default value: google. Note:chat_gpt data is available for the United States and English only")
    initial_dataset_filters: Optional[List[Optional[Any]]] = Field(default=None, description=r"array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. =, <>, in, not_in, like, not_like, ilike, not_ilike, match, not_match. you can use the % operator with like and not_like to match any string of zero or more characters. example:. ['ai_search_volume','>','1000']. The full list of possible filters is available here.")
    internal_list_limit: Optional[StrictInt] = Field(default=None, description=r"maximum number of elements within internal arrays. optional field. you can use this field to limit the number of elements within the following arrays:. sources_domain. search_results_domain. minimum value: 1. maximum value: 10. default value: 5")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "target", 
        "domain", 
        "search_filter", 
        "search_scope", 
        "include_subdomains", 
        "keyword", 
        "match_type", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "platform", 
        "initial_dataset_filters", 
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

        target_items = []
        if self.target:
            for _item in self.target:
                if _item:
                    target_items.append(_item.to_dict())
            _dict['target'] = target_items
        _dict['domain'] = self.domain
        _dict['search_filter'] = self.search_filter
        _dict['search_scope'] = self.search_scope
        _dict['include_subdomains'] = self.include_subdomains
        _dict['keyword'] = self.keyword
        _dict['match_type'] = self.match_type
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['platform'] = self.platform
        _dict['initial_dataset_filters'] = self.initial_dataset_filters
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
            "target": [BaseAiOptimizationLLmMentionsTargetElement.from_dict(_item) for _item in obj["target"]] if obj.get("target") is not None else None,
            "domain": obj.get("domain"),
            "search_filter": obj.get("search_filter"),
            "search_scope": obj.get("search_scope"),
            "include_subdomains": obj.get("include_subdomains"),
            "keyword": obj.get("keyword"),
            "match_type": obj.get("match_type"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "platform": obj.get("platform"),
            "initial_dataset_filters": obj.get("initial_dataset_filters"),
            "internal_list_limit": obj.get("internal_list_limit"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj