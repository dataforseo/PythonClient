from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BacklinksBacklinksLiveRequestInfo(BaseModel):
    """
    BacklinksBacklinksLiveRequestInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="domain, subdomain or webpage to get backlinks for. required field. a domain or a subdomain should be specified without https:// and www.. a page should be specified with absolute URL (including http:// or https://)")
    mode: Optional[StrictStr] = Field(default=None, description="results grouping type. optional field. possible grouping types:. as_is – returns all backlinks. one_per_domain – returns one backlink per domain. one_per_anchor – returns one backlink per anchor. default value: as_is")
    custom_mode: Optional[Dict[str, Optional[Any]]] = Field(default=None, description="detailed results grouping type. optional field. use this object to get a specific number of backlinks per field. if you use custom_mode, then mode will be ignored. example:. 'custom_mode': {'field': 'domain', 'value': 100}")
    field: Optional[StrictStr] = Field(default=None, description="response field. required field if you choose to specify custom_mode. possible values:. anchor. domain_from. domain_from_country. tld_from. page_from_encoding. page_from_language. item_type. page_from_status_code. semantic_location")
    value: Optional[StrictInt] = Field(default=None, description="number of backlinks to return per field. required field if you choose to specify custom_mode. can be set from 1 to 1000")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. =, <>, in, not_in, like, not_like, ilike, not_ilike, regex, not_regex, match, not_match. you can use the % operator with like and not_like to match any string of zero or more characters. example:. ['rank','>','80']. [['page_from_rank','>','55'],. 'and',. ['dofollow','=',true]]. [['first_seen','>','2017-10-23 11:31:45 +00:00'],. 'and',. [['anchor','like','%seo%'],'or',['text_pre','like','%seo%']]]. The full list of possible filters is available here.")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. you can use the same values as in the filters array to sort the results. possible sorting types:. asc – results will be sorted in the ascending order. desc – results will be sorted in the descending order. you should use a comma to set up a sorting type. example:. ['rank,desc']. note that you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['domain_from_rank,desc','page_from_rank,asc']")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of the returned backlinks. optional field. default value: 0. if you specify the 10 value, the first ten backlinks in the results array will be omitted and the data will be provided for the successive backlinks;. Note: the maximum value is 20,000, use the search_after_token if you would like to offset more results")
    search_after_token: Optional[StrictStr] = Field(default=None, description="token for subsequent requests. optional field. provided in the identical filed of the response to each request;. use this parameter to avoid timeouts while trying to obtain over 20,000 results in a single request;. by specifying the unique search_after_token value from the response array, you will get the subsequent results of the initial task;. search_after_token values are unique for each subsequent task ;. Note: if the search_after_token is specified in the request, all other parameters should be identical to the previous request")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned backlinks. optional field. default value: 100. maximum value: 1000")
    backlinks_status_type: Optional[StrictStr] = Field(default=None, description="set what backlinks to return and count. optional field. you can use this field to choose what backlinks will be returned and used for aggregated metrics for your target;. possible values:. all – all backlinks will be returned and counted;. live – backlinks found during the last check will be returned and counted;. lost – lost backlinks will be returned and counted;. default value: live")
    include_subdomains: Optional[StrictBool] = Field(default=None, description="indicates if the subdomains of the target will be included in the search. optional field. if set to false, the subdomains will be ignored. default value: true")
    include_indirect_links: Optional[StrictBool] = Field(default=None, description="indicates if indirect links to the target will be included in the results. optional field. if set to true, the results will include data on indirect links pointing to a page that either redirects to the target, or points to a canonical page. if set to false, indirect links will be ignored. default value: true")
    exclude_internal_backlinks: Optional[StrictBool] = Field(default=None, description="indicates if internal backlinks from subdomains to the target will be excluded from the results. optional field. if set to true, the results will not include data on internal backlinks from subdomains of the same domain as target. if set to false, internal links will be included in the results. default value: true")
    rank_scale: Optional[StrictStr] = Field(default=None, description="defines the scale used for calculating and displaying the rank, domain_from_rank, and page_from_rank values. optional field. you can use this parameter to choose whether rank values are presented on a 0–100 or 0–1000 scale. possible values:. one_hundred — rank values are displayed on a 0–100 scale. one_thousand — rank values are displayed on a 0–1000 scale. default value: one_thousand. learn more about how this parameter works and how ranking metrics are calculated in this Help Center article")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "target", 
        "mode", 
        "custom_mode", 
        "field", 
        "value", 
        "filters", 
        "order_by", 
        "offset", 
        "search_after_token", 
        "limit", 
        "backlinks_status_type", 
        "include_subdomains", 
        "include_indirect_links", 
        "exclude_internal_backlinks", 
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

        _dict['target'] = self.target
        _dict['mode'] = self.mode
        _dict['custom_mode'] = self.custom_mode
        _dict['field'] = self.field
        _dict['value'] = self.value
        _dict['filters'] = self.filters
        _dict['order_by'] = self.order_by
        _dict['offset'] = self.offset
        _dict['search_after_token'] = self.search_after_token
        _dict['limit'] = self.limit
        _dict['backlinks_status_type'] = self.backlinks_status_type
        _dict['include_subdomains'] = self.include_subdomains
        _dict['include_indirect_links'] = self.include_indirect_links
        _dict['exclude_internal_backlinks'] = self.exclude_internal_backlinks
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
            "target": obj.get("target"),
            "mode": obj.get("mode"),
            "custom_mode": obj.get("custom_mode"),
            "field": obj.get("field"),
            "value": obj.get("value"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "offset": obj.get("offset"),
            "search_after_token": obj.get("search_after_token"),
            "limit": obj.get("limit"),
            "backlinks_status_type": obj.get("backlinks_status_type"),
            "include_subdomains": obj.get("include_subdomains"),
            "include_indirect_links": obj.get("include_indirect_links"),
            "exclude_internal_backlinks": obj.get("exclude_internal_backlinks"),
            "rank_scale": obj.get("rank_scale"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj