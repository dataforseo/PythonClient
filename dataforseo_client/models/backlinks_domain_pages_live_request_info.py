from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BacklinksDomainPagesLiveRequestInfo(BaseModel):
    """
    BacklinksDomainPagesLiveRequestInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="domain or subdomain. required field. a domain or a subdomain should be specified without https:// and www.. example:. forbes.com")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned pages. optional field. default value: 100. maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned pages. optional field. default value: 0. if you specify the 10 value, the first ten pages in the results array will be omitted and the data will be provided for the successive pages")
    internal_list_limit: Optional[StrictInt] = Field(default=None, description="maximum number of elements within internal arrays. optional field. you can use this field to limit the number of elements within the following arrays:. referring_links_tld. referring_links_types. referring_links_attributes. referring_links_platform_types. referring_links_semantic_locations. default value: 10. maximum value: 1000")
    backlinks_status_type: Optional[StrictStr] = Field(default=None, description="set what backlinks to return and count. optional field. you can use this field to choose what backlinks will be returned and used for aggregated metrics;. possible values:. all – all backlinks will be returned and counted;. live – backlinks found during the last check will be returned and counted;. lost – lost backlinks will be returned and counted;. default value: live")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, not_regex, =, <>, in, not_in, like, not_like, ilike, not_ilike, match, not_match. you can use the % operator with like and not_like to match any string of zero or more characters. example:. ['meta.internal_links_count','>','1']. [['meta.external_links_count','>','2'],. 'and',. ['backlinks','>','10']]. [['first_visited','>','2017-10-23 11:31:45 +00:00'],. 'and',. [['title','like','%seo%'],'or',['referring_domains','>','10']]]. The full list of possible filters is available here.")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. you can use the same values as in the filters array to sort the results. possible sorting types:. asc – results will be sorted in the ascending order. desc – results will be sorted in the descending order. you should use a comma to set up a sorting type. example:. ['page_summary.backlinks,desc']. note that you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['page_summary.backlinks,desc','page_summary.rank,asc']")
    backlinks_filters: Optional[List[Optional[Any]]] = Field(default=None, description="filter the backlinks of your target. optional field. you can use this field to filter the initial backlinks that will be included in the dataset for aggregated metrics for your target. you can filter the backlinks by all fields available in the response of this endpoint. using this parameter, you can include only dofollow backlinks in the response and create a flexible backlinks dataset to calculate the metrics for. example:. 'backlinks_filters': ['dofollow', '=', true]")
    include_subdomains: Optional[StrictBool] = Field(default=None, description="indicates if the subdomains of the target will be included in the search. optional field. if set to false, the subdomains will be ignored. default value: true")
    exclude_internal_backlinks: Optional[StrictBool] = Field(default=None, description="indicates if internal backlinks from subdomains to the target will be excluded from the results. optional field. if set to true, the results will not include data on internal backlinks from subdomains of the same domain as target. if set to false, internal links will be included in the results. default value: true")
    rank_scale: Optional[StrictStr] = Field(default=None, description="defines the scale used for calculating and displaying the rank, domain_from_rank, and page_from_rank values. optional field. you can use this parameter to choose whether rank values are presented on a 0–100 or 0–1000 scale. possible values:. one_hundred — rank values are displayed on a 0–100 scale. one_thousand — rank values are displayed on a 0–1000 scale. default value: one_thousand. learn more about how this parameter works and how ranking metrics are calculated in this Help Center article")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "target", 
        "limit", 
        "offset", 
        "internal_list_limit", 
        "backlinks_status_type", 
        "filters", 
        "order_by", 
        "backlinks_filters", 
        "include_subdomains", 
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
        _dict['limit'] = self.limit
        _dict['offset'] = self.offset
        _dict['internal_list_limit'] = self.internal_list_limit
        _dict['backlinks_status_type'] = self.backlinks_status_type
        _dict['filters'] = self.filters
        _dict['order_by'] = self.order_by
        _dict['backlinks_filters'] = self.backlinks_filters
        _dict['include_subdomains'] = self.include_subdomains
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
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "internal_list_limit": obj.get("internal_list_limit"),
            "backlinks_status_type": obj.get("backlinks_status_type"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "backlinks_filters": obj.get("backlinks_filters"),
            "include_subdomains": obj.get("include_subdomains"),
            "exclude_internal_backlinks": obj.get("exclude_internal_backlinks"),
            "rank_scale": obj.get("rank_scale"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj