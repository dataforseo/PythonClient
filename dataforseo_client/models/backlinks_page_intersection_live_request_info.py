from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BacklinksPageIntersectionLiveRequestInfo(BaseModel):
    """
    BacklinksPageIntersectionLiveRequestInfo
    """ # noqa: E501
    targets: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="domains, subdomains or webpages to get links for. required field. you can set up to 20 domains, subdomains or webpages. a domain or a subdomain should be specified without https:// and www.. a page should be specified with absolute URL (including http:// or https://). example:. 'targets': {. '1': 'http://planet.postgresql.org/',. '2': 'http://gborg.postgresql.org/'. }")
    exclude_targets: Optional[List[Optional[StrictStr]]] = Field(default=None, description="domains, subdomains or webpages you want to exclude. optional field. you can set up to 10 domains, subdomains or webpages. if you use this array, results will contain the referring pages that link to targets but don’t link to exclude_targets. example:. 'exclude_targets': [. 'bbc.com',. 'https://www.apple.com/iphone/*',. 'https://dataforseo.com/apis/*']")
    backlinks_status_type: Optional[StrictStr] = Field(default=None, description="set what backlinks to return and count. optional field. you can use this field to choose what backlinks will be returned and used for aggregated metrics for your targets;. possible values:. all – all backlinks will be returned and counted;. live – backlinks found during the last check will be returned and counted;. lost – lost backlinks will be returned and counted;. default value: live")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, not_regex, =, <>, in, not_in, like, not_like, ilike, not_ilike, match, not_match. you can use the % operator with like and not_like to match any string of zero or more characters. example:. ['1.rank','>','80']. [['2.page_from_rank','>','55'],. 'and',. ['1.original','=','true']]. [['1.first_seen','>','2017-10-23 11:31:45 +00:00'],. 'and',. [['1.acnhor','like','%seo%'],'or',['1.text_pre','not_like','%seo%']]]. The full list of possible filters is available here.")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. you can use the same values as in the filters array to sort the results. possible sorting types:. asc – results will be sorted in the ascending order. desc – results will be sorted in the descending order. you should use a comma to set up a sorting type. example:. ['rank,desc']. note that you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['domain_from_rank,desc','page_from_rank,asc']")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of the returned backlinks. optional field. default value: 0. if you specify the 10 value, the first ten backlinks in the results array will be omitted and the data will be provided for the successive backlinks")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned backlinks. optional field. default value: 100. maximum value: 1000")
    internal_list_limit: Optional[StrictInt] = Field(default=None, description="maximum number of elements within internal arrays. optional field. you can use this field to limit the number of elements within the following arrays:. attributes. domain_from_platform_type. default value: 10. maximum value: 1000")
    include_subdomains: Optional[StrictBool] = Field(default=None, description="indicates if the subdomains of the targets will be included in the search. optional field. if set to false, the subdomains will be ignored. default value: true")
    include_indirect_links: Optional[StrictBool] = Field(default=None, description="indicates if indirect links to the targets will be included in the results. optional field. if set to true, the results will include data on indirect links pointing to a page that either redirects to a target, or points to a canonical page. if set to false, indirect links will be ignored. default value: true")
    exclude_internal_backlinks: Optional[StrictBool] = Field(default=None, description="indicates if internal backlinks from subdomains to the target will be excluded from the results. optional field. if set to true, the results will not include data on internal backlinks from subdomains of the same domain as target. if set to false, internal links will be included in the result. default value: true")
    intersection_mode: Optional[StrictStr] = Field(default=None, description="indicates whether to intersect backlinks. optional field. use this field to intersect or merge results for the specified URLs. possible values: all, partial. all – results are based on all backlinks;. partial – results are based on the intersecting backlinks only;. default value: all")
    rank_scale: Optional[StrictStr] = Field(default=None, description="defines the scale used for calculating and displaying the rank, domain_from_rank, and page_from_rank values. optional field. you can use this parameter to choose whether rank values are presented on a 0–100 or 0–1000 scale. possible values:. one_hundred — rank values are displayed on a 0–100 scale. one_thousand — rank values are displayed on a 0–1000 scale. default value: one_thousand. learn more about how this parameter works and how ranking metrics are calculated in this Help Center article")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "targets", 
        "exclude_targets", 
        "backlinks_status_type", 
        "filters", 
        "order_by", 
        "offset", 
        "limit", 
        "internal_list_limit", 
        "include_subdomains", 
        "include_indirect_links", 
        "exclude_internal_backlinks", 
        "intersection_mode", 
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

        _dict['targets'] = self.targets
        _dict['exclude_targets'] = self.exclude_targets
        _dict['backlinks_status_type'] = self.backlinks_status_type
        _dict['filters'] = self.filters
        _dict['order_by'] = self.order_by
        _dict['offset'] = self.offset
        _dict['limit'] = self.limit
        _dict['internal_list_limit'] = self.internal_list_limit
        _dict['include_subdomains'] = self.include_subdomains
        _dict['include_indirect_links'] = self.include_indirect_links
        _dict['exclude_internal_backlinks'] = self.exclude_internal_backlinks
        _dict['intersection_mode'] = self.intersection_mode
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
            "targets": obj.get("targets"),
            "exclude_targets": obj.get("exclude_targets"),
            "backlinks_status_type": obj.get("backlinks_status_type"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "offset": obj.get("offset"),
            "limit": obj.get("limit"),
            "internal_list_limit": obj.get("internal_list_limit"),
            "include_subdomains": obj.get("include_subdomains"),
            "include_indirect_links": obj.get("include_indirect_links"),
            "exclude_internal_backlinks": obj.get("exclude_internal_backlinks"),
            "intersection_mode": obj.get("intersection_mode"),
            "rank_scale": obj.get("rank_scale"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj