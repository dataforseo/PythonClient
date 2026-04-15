from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_ai_optimization_l_lm_mentions_target_element import BaseAiOptimizationLLmMentionsTargetElement



class AiOptimizationLlmMentionsTopDomainsLiveRequestInfo(BaseModel):
    """
    AiOptimizationLlmMentionsTopDomainsLiveRequestInfo
    """ # noqa: E501
    target: Optional[List[Optional[BaseAiOptimizationLLmMentionsTargetElement]]] = Field(default=None, description=r"array of objects containing target entities. required field. you can specify up to 10 entities (objects) in the target field. one target entity can contain either one domain or one keyword and related parameters. examples:. . target array with a domain entity")
    domain_entity: Optional[Any] = Field(default=None, description=r"domain entity in the target arrayexample:{'domain': 'en.wikipedia.org', 'search_filter': 'exclude', 'search_scope': ['sources']}")
    domain: Optional[StrictStr] = Field(default=None, description=r"target domainrequired field if you don't specify keywordyou can specify up to 63 characters in the domain field;a domain should be specified without https:// and www.")
    search_filter: Optional[StrictStr] = Field(default=None, description=r"target keyword search filteroptional fieldpossible values:include, excludedefault value: include")
    search_scope: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"target keyword search scopeoptional fieldpossible values:any, question, answer, brand_entities, fan_out_queriesdefault value: any")
    include_subdomains: Optional[StrictBool] = Field(default=None, description=r"indicates if the subdomains of the target domain will be included in the searchoptional fieldif set to true, the subdomains will be included in the searchdefault value: false")
    keyword_entity: Optional[Any] = Field(default=None, description=r"keyword entity in the target arrayexample:{'keyword': 'bmw', 'search_filter': 'include', 'search_scope': ['question'], 'match_type ': 'partial_match'}")
    keyword: Optional[StrictStr] = Field(default=None, description=r"target keywordrequired field if you don't specify domainyou can specify up to 250 characters in the keyword fieldall %## will be decoded (plus character ‘+’ will be decoded to a space character)if you need to use the “%” character for your keyword, please specify it as “%25”;if you need to use the “+” character for your keyword, please specify it as “%2B”learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    match_type: Optional[StrictStr] = Field(default=None, description=r"target keyword match typeoptional fieldpossible values:word_match, partial_matchword_match - full-text search for terms that match the specified seed keyword with additional words included before, after, or within the seed key phrase.partial_match - searches for any occurrence of the keyword or its parts within the contentdefault value: word_match")
    location_name: Optional[StrictStr] = Field(default=None, description=r"full name of search locationoptional fieldif you use this field, you don't need to specify location_codeif you don't specify this field, the location_code with 2840 value will be used by default;you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languagesNote: chat_gpt data is available for United States only")
    location_code: Optional[StrictInt] = Field(default=None, description=r"search location codeoptional fieldif you use this field, you don't need to specify location_nameyou can receive the list of available locations of the search engine with their location_code by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languagesdefault value: 2840Note: chat_gpt data is available for 2840 only")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of search languageoptional fieldif you use this field, you don't need to specify language_code;if you don't specify this field, the language_code with en value will be used by default;you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languagesNote: chat_gpt data is available for English only")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search language codeoptional fieldif you use this field, you don't need to specify language_name;you can receive the list of available languages of the search engine with their language_code_by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languagesdefault value: enNote: chat_gpt data is available for en onlyn")
    platform: Optional[StrictStr] = Field(default=None, description=r"target platformoptional fieldpossible values:chat_gpt, googledefault value: googleNote: the data returned depends on the selected platformNote #2:chat_gpt data is available for the United States and English only")
    links_scope: Optional[StrictStr] = Field(default=None, description=r"links source scopeoptional fieldthis parameter specifies which links will be used to extract domains and aggregation datapossible values: sources, search_resultsdefault value: sources")
    initial_dataset_filters: Optional[List[Optional[Any]]] = Field(default=None, description=r"array of filter expressions applied before aggregationoptional fieldyou can use this array to filter expressions applied to the raw mentions database before aggregation to limit the rows contributing to the result;you can add several filters at once (8 filters maximum)you should set a logical operator and, or between the conditionsthe following operators are supported:=, <>, in, not_in, like, not_like, ilike, not_ilike, match, not_matchyou can use the % operator with like and not_like to match any string of zero or more charactersexample:['ai_search_volume','>','1000']The full list of possible filters is available here.")
    items_list_limit: Optional[StrictInt] = Field(default=None, description=r"maximum number of results in the items arrayoptional fieldyou can use this parameter to limit the number of data objects you receive in the items arrayminimum value: 1maximum value: 10default value: 5")
    internal_list_limit: Optional[StrictInt] = Field(default=None, description=r"maximum number of elements within internal arraysoptional fieldyou can use this field to limit the number of elements within the following arrays:sources_domainsearch_results_domainminimum value: 1maximum value: 10default value: 5")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "target", 
        "domain_entity", 
        "domain", 
        "search_filter", 
        "search_scope", 
        "include_subdomains", 
        "keyword_entity", 
        "keyword", 
        "match_type", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "platform", 
        "links_scope", 
        "initial_dataset_filters", 
        "items_list_limit", 
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
        _dict['domain_entity'] = self.domain_entity
        _dict['domain'] = self.domain
        _dict['search_filter'] = self.search_filter
        _dict['search_scope'] = self.search_scope
        _dict['include_subdomains'] = self.include_subdomains
        _dict['keyword_entity'] = self.keyword_entity
        _dict['keyword'] = self.keyword
        _dict['match_type'] = self.match_type
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['platform'] = self.platform
        _dict['links_scope'] = self.links_scope
        _dict['initial_dataset_filters'] = self.initial_dataset_filters
        _dict['items_list_limit'] = self.items_list_limit
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
            "domain_entity": obj.get("domain_entity"),
            "domain": obj.get("domain"),
            "search_filter": obj.get("search_filter"),
            "search_scope": obj.get("search_scope"),
            "include_subdomains": obj.get("include_subdomains"),
            "keyword_entity": obj.get("keyword_entity"),
            "keyword": obj.get("keyword"),
            "match_type": obj.get("match_type"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "platform": obj.get("platform"),
            "links_scope": obj.get("links_scope"),
            "initial_dataset_filters": obj.get("initial_dataset_filters"),
            "items_list_limit": obj.get("items_list_limit"),
            "internal_list_limit": obj.get("internal_list_limit"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj