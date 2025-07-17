from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ContentAnalysisPhraseTrendsLiveRequestInfo(BaseModel):
    """
    ContentAnalysisPhraseTrendsLiveRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="target keyword. required field. UTF-8 encoding. the keywords will be converted to a lowercase format;. Note: to match an exact phrase instead of a stand-alone keyword, use double quotes and backslashes;. example:. 'keyword': '\'tesla palo alto\''. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    keyword_fields: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="target keyword fields and target keywords. optional field. use this parameter to filter the dataset by keywords that certain fields should contain;. fields you can specify: title, main_title, previous_title, snippet. you can indicate several fields;. Note: to match an exact phrase instead of a stand-alone keyword, use double quotes and backslashes;. example:. 'keyword_fields': {.     'snippet': '\'logitech mouse\'',.     'main_title': 'sale'. }")
    page_type: Optional[List[Optional[StrictStr]]] = Field(default=None, description="target page types. optional field. use this parameter to filter the dataset by page types. possible values:. 'ecommerce', 'news', 'blogs', 'message-boards', 'organization'")
    search_mode: Optional[StrictStr] = Field(default=None, description="results grouping type. optional field. possible grouping types:. as_is – returns data on all citations for the target keyword. one_per_domain – returns data on one citation of the keyword per domain. default value: as_is")
    internal_list_limit: Optional[StrictInt] = Field(default=None, description="maximum number of elements within internal arrays. optional field. you can use this field to limit the number of elements within the following arrays:. top_domains. text_categories. page_categories. countries. languages. default value: 1. maximum value: 20")
    date_from: Optional[StrictStr] = Field(default=None, description="starting date of the time range. required field. date format: 'yyyy-mm-dd'. example:. '2019-01-15'")
    date_to: Optional[StrictStr] = Field(default=None, description="ending date of the time range. optional field. if you don’t specify this field, today’s date will be used by default. date format: 'yyyy-mm-dd'. example:. '2019-01-15'")
    date_group: Optional[StrictStr] = Field(default=None, description="time range which will be used to group the results. optional field. default value: month. possible values: day, week, month")
    initial_dataset_filters: Optional[List[Optional[Any]]] = Field(default=None, description="initial dataset filtering parameters. optional field. initial filtering parameters that apply to fields in the Search endpoint;. you can add several filters at once (8 filters maximum);. you should set a logical operator and, or between the conditions;. the following operators are supported:. regex, not_regex, <, <=, >, >=, =, <>, in, not_in, like,not_like, has, has_not, match, not_match. you can use the % operator with like and not_like to match any string of zero or more characters;. example:. ['domain','<>', 'logitech.com']. [['domain','<>','logitech.com'],'and',['content_info.connotation_types.negative','>',1000]]. [['domain','<>','logitech.com']],. 'and',. [['content_info.connotation_types.negative','>',1000],. 'or',. ['content_info.text_category','has',10994]]]. for more information about filters, please refer to Content Analysis API – Filters")
    rank_scale: Optional[StrictStr] = Field(default=None, description="defines the scale used for calculating and displaying the rank values. optional field. you can use this parameter to choose whether rank values are presented on a 0–100 or 0–1000 scale. possible values:. one_hundred — rank values are displayed on a 0–100 scale. one_thousand — rank values are displayed on a 0–1000 scale. default value: one_thousand. learn more about how this parameter works in this Help Center article")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "keyword_fields", 
        "page_type", 
        "search_mode", 
        "internal_list_limit", 
        "date_from", 
        "date_to", 
        "date_group", 
        "initial_dataset_filters", 
        "rank_scale", 
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

        _dict['keyword'] = self.keyword
        _dict['keyword_fields'] = self.keyword_fields
        _dict['page_type'] = self.page_type
        _dict['search_mode'] = self.search_mode
        _dict['internal_list_limit'] = self.internal_list_limit
        _dict['date_from'] = self.date_from
        _dict['date_to'] = self.date_to
        _dict['date_group'] = self.date_group
        _dict['initial_dataset_filters'] = self.initial_dataset_filters
        _dict['rank_scale'] = self.rank_scale
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "keyword_fields": obj.get("keyword_fields"),
            "page_type": obj.get("page_type"),
            "search_mode": obj.get("search_mode"),
            "internal_list_limit": obj.get("internal_list_limit"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "date_group": obj.get("date_group"),
            "initial_dataset_filters": obj.get("initial_dataset_filters"),
            "rank_scale": obj.get("rank_scale"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj