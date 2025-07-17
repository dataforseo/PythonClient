from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ContentAnalysisSearchLiveRequestInfo(BaseModel):
    """
    ContentAnalysisSearchLiveRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="target keyword. required field. UTF-8 encoding. the keywords will be converted to a lowercase format;. Note: to match an exact phrase instead of a stand-alone keyword, use double quotes and backslashes;. example:. 'keyword': '\'tesla palo alto\''. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    keyword_fields: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="target keyword fields and target keywords. optional field. use this parameter to filter the dataset by keywords that certain fields should contain;. fields you can specify: title, main_title, previous_title, snippet. you can indicate several fields;. Note: to match an exact phrase instead of a stand-alone keyword, use double quotes and backslashes;. example:. 'keyword_fields': {.     'snippet': '\'logitech mouse\'',.     'main_title': 'sale'. }")
    page_type: Optional[List[Optional[StrictStr]]] = Field(default=None, description="target page types. optional field. use this parameter to filter the dataset by page types. possible values:. 'ecommerce', 'news', 'blogs', 'message-boards', 'organization'")
    search_mode: Optional[StrictStr] = Field(default=None, description="results grouping type. optional field. possible grouping types:. as_is – returns all citations for the target keyword. one_per_domain – returns one citation of the keyword per domain. default value: as_is")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned citations. optional field. default value: 100. maximum value: 1000")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, not_regex, <, <=, >, >=, =, <>, in, not_in, like,not_like, match, not_match. you can use the % operator with like and not_like to match any string of zero or more characters. example:. ['country','=', 'US']. [['domain_rank','>',800],'and',['content_info.connotation_types.negative','>',0.9]]. [['domain_rank','>',800],. 'and',. [['page_types','has','ecommerce'],. 'or',. ['content_info.text_category','has',10994]]]. for more information about filters, please refer to Content Analysis API – Filters")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. you can use the same values as in the filters array to sort the results. possible sorting types:. asc – results will be sorted in the ascending order. desc – results will be sorted in the descending order. you should use a comma to set up a sorting type. example:. ['content_info.sentiment_connotations.anger,desc']. default rule:. ['content_info.sentiment_connotations.anger,desc']. note that you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['content_info.sentiment_connotations.anger,desc','keyword_data.keyword_info.cpc,desc']")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned citations. optional field. default value: 0. if you specify the 10 value, the first ten citations in the results array will be omitted and the data will be provided for the successive citations")
    offset_token: Optional[StrictStr] = Field(default=None, description="offset token for subsequent requests. optional field. provided in the identical field of the response to each request;. use this parameter to avoid timeouts while trying to obtain over 10,000 results in a single request;. by specifying the unique offset_token value from the response array, you will get the subsequent results of the initial task;. offset_token values are unique for each subsequent task. Note: if the offset_token is specified in the request, all other parameters except limit will not be taken into account when processing a task")
    rank_scale: Optional[StrictStr] = Field(default=None, description="defines the scale used for calculating and displaying the domain_rank, and url_rank values. optional field. you can use this parameter to choose whether rank values are presented on a 0–100 or 0–1000 scale. possible values:. one_hundred — rank values are displayed on a 0–100 scale. one_thousand — rank values are displayed on a 0–1000 scale. default value: one_thousand. learn more about how this parameter works in this Help Center article")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "keyword_fields", 
        "page_type", 
        "search_mode", 
        "limit", 
        "filters", 
        "order_by", 
        "offset", 
        "offset_token", 
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
        _dict['limit'] = self.limit
        _dict['filters'] = self.filters
        _dict['order_by'] = self.order_by
        _dict['offset'] = self.offset
        _dict['offset_token'] = self.offset_token
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
            "limit": obj.get("limit"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "offset": obj.get("offset"),
            "offset_token": obj.get("offset_token"),
            "rank_scale": obj.get("rank_scale"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj