from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_ai_optimization_l_lm_mentions_target_element import BaseAiOptimizationLLmMentionsTargetElement



class AiOptimizationLlmMentionsSearchLiveRequestInfo(BaseModel):
    """
    AiOptimizationLlmMentionsSearchLiveRequestInfo
    """ # noqa: E501
    target: Optional[List[Optional[BaseAiOptimizationLLmMentionsTargetElement]]] = Field(default=None, description=r"array of objects containing target entities. required field. you can specify up to 10 entities (objects) in the target field. one target entity can contain either one domain or one keyword and related parameters. examples:. . target array with a domain entity")
    location_name: Optional[StrictStr] = Field(default=None, description=r"full name of search locationoptional fieldif you use this field, you don't need to specify location_codeif you don't specify this field, the location_code with 2840 value will be used by default;you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languagesNote: chat_gpt data is available for United States only")
    location_code: Optional[StrictInt] = Field(default=None, description=r"search location codeoptional fieldif you use this field, you don't need to specify location_nameyou can receive the list of available locations of the search engine with their location_code by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languagesdefault value: 2840Note: chat_gpt data is available for 2840 only")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of search languageoptional fieldif you use this field, you don't need to specify language_code;if you don't specify this field, the language_code with en value will be used by default;you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languagesNote: chat_gpt data is available for English only")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search language codeoptional fieldif you use this field, you don't need to specify language_name;you can receive the list of available languages of the search engine with their language_code_by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languagesdefault value: enNote: chat_gpt data is available for en onlyn")
    platform: Optional[StrictStr] = Field(default=None, description=r"target platformoptional fieldpossible values:chat_gpt, googledefault value: googleNote: the data returned depends on the selected platformNote #2:chat_gpt data is available for the United States and English only")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description=r"array of results filtering parametersoptional fieldyou can add several filters at once (8 filters maximum)you should set a logical operator and, or between the conditionsthe following operators are supported:=, <>, in, not_in, like, not_like, ilike, not_ilike, match, not_matchyou can use the % operator with like and not_like to match any string of zero or more charactersexample:['ai_search_volume','>','1000']The full list of possible filters is available here.")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"results sorting rulesoptional fieldyou can use the same values as in the filters array to sort the resultspossible sorting types:asc - results will be sorted in the ascending orderdesc - results will be sorted in the descending orderyou should use a comma to set up a sorting typeexample:['ai_search_volume,desc']note that you can set no more than three sorting rules in a single requestyou should use a comma to separate several sorting rules")
    offset: Optional[StrictInt] = Field(default=None, description=r"offset in the results array of the returned mentions dataoptional fielddefault value: 0example: if you specify the 10 value, the first ten mentions objects in the results array will be omitted and the data will be provided for the successive objects;Note: the maximum value is 9,000, use the search_after_token if you would like to offset more results")
    search_after_token: Optional[StrictStr] = Field(default=None, description=r"token for subsequent requestsoptional fieldprovided in the identical filed of the response to each request;use this parameter to avoid timeouts while trying to obtain over 20,000 results in a single request;by specifying the unique search_after_token value from the response array, you will get the subsequent results of the initial task;search_after_token values are unique for each subsequent task ;Note: if the search_after_token is specified in the request, all other parameters should be identical to the previous request")
    limit: Optional[StrictInt] = Field(default=None, description=r"the maximum number of returned objectsoptional fielddefault value: 100maximum value: 1000")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "target", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "platform", 
        "filters", 
        "order_by", 
        "offset", 
        "search_after_token", 
        "limit", 
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
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['platform'] = self.platform
        _dict['filters'] = self.filters
        _dict['order_by'] = self.order_by
        _dict['offset'] = self.offset
        _dict['search_after_token'] = self.search_after_token
        _dict['limit'] = self.limit
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
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "platform": obj.get("platform"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "offset": obj.get("offset"),
            "search_after_token": obj.get("search_after_token"),
            "limit": obj.get("limit"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj