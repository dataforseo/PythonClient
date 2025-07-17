from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ContentAnalysisSentimentAnalysisLiveRequestInfo(BaseModel):
    """
    ContentAnalysisSentimentAnalysisLiveRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="target keyword. required field. UTF-8 encoding. the keywords will be converted to a lowercase format;. Note: to match an exact phrase instead of a stand-alone keyword, use double quotes and backslashes;. example:. 'keyword': '\'tesla palo alto\''. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    keyword_fields: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="target keyword fields and target keywords. optional field. use this parameter to filter the dataset by keywords that certain fields should contain;. fields you can specify: title, main_title, previous_title, snippet. you can indicate several fields;. Note: to match an exact phrase instead of a stand-alone keyword, use double quotes and backslashes;. example:. 'keyword_fields': {.     'snippet': '\'logitech mouse\'',.     'main_title': 'sale'. }")
    page_type: Optional[List[Optional[StrictStr]]] = Field(default=None, description="target page types. optional field. use this parameter to filter the dataset by page types. possible values:. 'ecommerce', 'news', 'blogs', 'message-boards', 'organization'")
    internal_list_limit: Optional[StrictInt] = Field(default=None, description="maximum number of elements within internal arrays. optional field. you can use this field to limit the number of elements within the following arrays:. top_domains. text_categories. page_categories. countries. languages. default value: 1. maximum value: 20")
    positive_connotation_threshold: Optional[StrictFloat] = Field(default=None, description="positive connotation threshold. optional field. specified as the probability index threshold for positive sentiment related to the citation content. if you specify this field, connotation_types object in the response will only contain data on citations with positive sentiment probability more than or equal to the specified value. possible values: from 0 to 1. default value: 0.4")
    sentiments_connotation_threshold: Optional[StrictFloat] = Field(default=None, description="sentiment connotation threshold. optional field. specified as the probability index threshold for sentiment connotations related to the citation content. if you specify this field, sentiment_connotations object in the response will only contain data on citations where the probability per each sentiment is more than or equal to the specified value. possible values: from 0 to 1. default value: 0.4")
    initial_dataset_filters: Optional[List[Optional[Any]]] = Field(default=None, description="initial dataset filtering parameters. optional field. initial filtering parameters that apply to fields in the Search endpoint. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, not_regex, <, <=, >, >=, =, <>, in, not_in, like,not_like, has, has_not, match, not_match. you can use the % operator with like and not_like to match any string of zero or more characters. example:. ['domain','<>', 'logitech.com']. [['domain','<>','logitech.com'],'and',['content_info.connotation_types.negative','>',1000]]. [['domain','<>','logitech.com']],. 'and',. [['content_info.connotation_types.negative','>',1000],. 'or',. ['content_info.text_category','has',10994]]]. for more information about filters, please refer to Content Analysis API – Filters")
    rank_scale: Optional[StrictStr] = Field(default=None, description="defines the scale used for calculating and displaying the rank values. optional field. you can use this parameter to choose whether rank values are presented on a 0–100 or 0–1000 scale. possible values:. one_hundred — rank values are displayed on a 0–100 scale. one_thousand — rank values are displayed on a 0–1000 scale. default value: one_thousand. learn more about how this parameter works in this Help Center article")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "keyword_fields", 
        "page_type", 
        "internal_list_limit", 
        "positive_connotation_threshold", 
        "sentiments_connotation_threshold", 
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
        _dict['internal_list_limit'] = self.internal_list_limit
        _dict['positive_connotation_threshold'] = self.positive_connotation_threshold
        _dict['sentiments_connotation_threshold'] = self.sentiments_connotation_threshold
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
            "internal_list_limit": obj.get("internal_list_limit"),
            "positive_connotation_threshold": obj.get("positive_connotation_threshold"),
            "sentiments_connotation_threshold": obj.get("sentiments_connotation_threshold"),
            "initial_dataset_filters": obj.get("initial_dataset_filters"),
            "rank_scale": obj.get("rank_scale"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj