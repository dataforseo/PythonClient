from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_ai_optimization_l_lm_mentions_target_element import BaseAiOptimizationLLmMentionsTargetElement



class AiOptimizationLlmMentionsTopMentionedBrandsLiveRequestInfo(BaseModel):
    """
    AiOptimizationLlmMentionsTopMentionedBrandsLiveRequestInfo
    """ # noqa: E501
    target: Optional[List[Optional[BaseAiOptimizationLLmMentionsTargetElement]]] = Field(default=None, description=r"array of objects containing target entities. required field. you can specify up to 10 entities (objects) in the target field. one target entity can contain either one domain or one keyword and related parameters. examples:. target array with a domain entity")
    location_name: Optional[StrictStr] = Field(default=None, description=r"*full name of search location*. optional field. if you use this field, you don't need to specify `location_code`. if you don't specify this field, the `location_code` with `2840` value will be used by default;. you can receive the list of available locations of the search engine with their `location_name` by making a separate request to the `https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages`. Note: `chat_gpt` data is available for `United States` only")
    location_code: Optional[StrictInt] = Field(default=None, description=r"*search location code*. optional field. if you use this field, you don't need to specify `location_name`. you can receive the list of available locations of the search engine with their `location_code` by making a separate request to the `https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages`. default value: `2840`. Note: `chat_gpt` data is available for `2840` only")
    language_name: Optional[StrictStr] = Field(default=None, description=r"*full name of search language*. optional field. if you use this field, you don't need to specify `language_code`;. if you don't specify this field, the `language_code` with `en` value will be used by default;. you can receive the list of available languages of the search engine with their `language_name` by making a separate request to the `https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages`. Note: `chat_gpt` data is available for `English` only")
    language_code: Optional[StrictStr] = Field(default=None, description=r"*search language code*. optional field. if you use this field, you don't need to specify `language_name`;. you can receive the list of available languages of the search engine with their `language_code` by making a separate request to the `https://api.dataforseo.com/v3/ai_optimization/llm_mentions/locations_and_languages`. default value: `en`. Note: `chat_gpt` data is available for `en` only")
    platform: Optional[StrictStr] = Field(default=None, description=r"*target platform*. optional field. possible values:. `chat_gpt`, `google`. **Note:** data specific to brand entities is available for `chat_gpt` only;. **Note #2:**`chat_gpt` data is available for the `United States` and `English` only")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description=r"*array of results filtering parameters*. optional field. **you can add several filters at once (8 filters maximum)**. you should set a logical operator `and`, `or` between the conditions. the following operators are supported:. `=`, `<>`, `in`, `not_in`, `like`, `not_like`, `ilike`, `not_ilike`, `match`, `not_match`. you can use the `%` operator with `like` and `not_like` to match any string of zero or more characters. example:. `['ai_search_volume','>',1000]`. The full list of possible filters is available [here.](/v3/ai_optimization/llm_mentions/filters/)")
    initial_dataset_filters: Optional[List[Optional[Any]]] = Field(default=None, description=r"*array of filter expressions applied before aggregation*. optional field. you can use this array to filter expressions applied to the raw mentions database before aggregation to limit the rows contributing to the result;. **you can add several filters at once (8 filters maximum)**. you should set a logical operator `and`, `or` between the conditions. the following operators are supported:. `=`, `<>`, `in`, `not_in`, `like`, `not_like`, `ilike`, `not_ilike`, `match`, `not_match`. you can use the `%` operator with `like` and `not_like` to match any string of zero or more characters. example:. `['ai_search_volume','>',1000]`. the full list of possible filters is available [here.](/v3/ai_optimization/llm_mentions/filters). learn more about the initial dataset filters in [this help center article.](https://dataforseo.com/help-center/what-are-the-initial-dataset-filters-and-how-do-they-work)")
    limit: Optional[StrictInt] = Field(default=None, description=r"*maximum number of results in the items array*. optional field. you can use this parameter to limit the number of data objects you receive in the `items` array. minimum value: `1`. maximum value: `1000`. default value: `100`")
    internal_list_limit: Optional[StrictInt] = Field(default=None, description=r"*maximum number of elements within internal arrays*. optional field. you can use this field to limit the number of elements within the following arrays:. `sources_domain`, `search_results_domain`, `brand_entities_title`, `brand_entities_category`. minimum value: `1`. maximum value: `10`. default value: `5`")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"*results sorting rules*. optional field. you can use the same values as in the `filters` array to sort the results. possible sorting types:. `asc` - results will be sorted in the ascending order. `desc` - results will be sorted in the descending order. you should use a comma to set up a sorting type. example:. `['ai_search_volume,desc']`. **Note:** you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules")
    offset: Optional[StrictInt] = Field(default=None, description=r"*offset in the results array of the returned mentions data*. optional field. default value: `0`. example: if you specify the `10` value, the first ten mentions objects in the results array will be omitted and the data will be provided for the successive objects;. **Note:** the maximum value is `1000000`")
    include_brands: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"*array of brands to include in the response*. optional field. if specified, only the listed brands will be returned in the `items` array. example:. `'include_brands': ['Audi']`")
    exclude_brands: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"*array of brands to exclude from the response*. optional field. if specified, the listed brands will be omitted from the `items` array. example:. `'exclude_brands': ['Audi']`")
    tag: Optional[StrictStr] = Field(default=None, description=r"*user-defined task identifier*. optional field. *the character limit is 255*. you can use this parameter to identify the task and match it with the result. you will find the specified `tag` value in the `data` object of the response")
    __properties: ClassVar[List[str]] = [
        "target", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "platform", 
        "filters", 
        "initial_dataset_filters", 
        "limit", 
        "internal_list_limit", 
        "order_by", 
        "offset", 
        "include_brands", 
        "exclude_brands", 
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
        _dict['initial_dataset_filters'] = self.initial_dataset_filters
        _dict['limit'] = self.limit
        _dict['internal_list_limit'] = self.internal_list_limit
        _dict['order_by'] = self.order_by
        _dict['offset'] = self.offset
        _dict['include_brands'] = self.include_brands
        _dict['exclude_brands'] = self.exclude_brands
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
            "initial_dataset_filters": obj.get("initial_dataset_filters"),
            "limit": obj.get("limit"),
            "internal_list_limit": obj.get("internal_list_limit"),
            "order_by": obj.get("order_by"),
            "offset": obj.get("offset"),
            "include_brands": obj.get("include_brands"),
            "exclude_brands": obj.get("exclude_brands"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj