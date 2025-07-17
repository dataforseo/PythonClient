from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BacklinksSummaryLiveRequestInfo(BaseModel):
    """
    BacklinksSummaryLiveRequestInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="domain, subdomain or webpage to get data for. required field. a domain or a subdomain should be specified without https:// and www.. a page should be specified with absolute URL (including http:// or https://)")
    include_subdomains: Optional[StrictBool] = Field(default=None, description="indicates if the subdomains of the target will be included in the search. optional field. if set to false, the subdomains will be ignored. default value: true")
    include_indirect_links: Optional[StrictBool] = Field(default=None, description="indicates if indirect links to the target will be included in the results. optional field. if set to true, the results will include data on indirect links pointing to a page that either redirects to the target, or points to a canonical page. if set to false, indirect links will be ignored. default value: true")
    exclude_internal_backlinks: Optional[StrictBool] = Field(default=None, description="indicates if internal backlinks from subdomains to the target will be excluded from the results. optional field. if set to true, the results will not include data on internal backlinks from subdomains of the same domain as target. if set to false, internal links will be included in the results. default value: true")
    internal_list_limit: Optional[StrictInt] = Field(default=None, description="maximum number of elements within internal arrays. optional field. you can use this field to limit the number of elements within the following arrays:. referring_links_tld. referring_links_types. referring_links_attributes. referring_links_platform_types. referring_links_semantic_locations. default value: 10. maximum value: 1000")
    backlinks_status_type: Optional[StrictStr] = Field(default=None, description="set what backlinks to return and count. optional field. you can use this field to choose what backlinks will be returned and used for aggregated metrics for your target;. possible values:. all – all backlinks will be returned and counted;. live – backlinks found during the last check will be returned and counted;. lost – lost backlinks will be returned and counted;. default value: live")
    backlinks_filters: Optional[List[Optional[Any]]] = Field(default=None, description="filter the backlinks of your target. optional field. you can use this field to filter the initial backlinks that will be included in the dataset for aggregated metrics for your target. you can filter the backlinks by all fields available in the response of this endpoint. using this parameter, you can include only dofollow backlinks in the response and create a flexible backlinks dataset to calculate the metrics for. example:. 'backlinks_filters': ['dofollow', '=', true]")
    rank_scale: Optional[StrictStr] = Field(default=None, description="defines the scale used for calculating and displaying the rank, domain_from_rank, and page_from_rank values. optional field. you can use this parameter to choose whether rank values are presented on a 0–100 or 0–1000 scale. possible values:. one_hundred — rank values are displayed on a 0–100 scale. one_thousand — rank values are displayed on a 0–1000 scale. default value: one_thousand. learn more about how this parameter works and how ranking metrics are calculated in this Help Center article")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "target", 
        "include_subdomains", 
        "include_indirect_links", 
        "exclude_internal_backlinks", 
        "internal_list_limit", 
        "backlinks_status_type", 
        "backlinks_filters", 
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
        _dict['include_subdomains'] = self.include_subdomains
        _dict['include_indirect_links'] = self.include_indirect_links
        _dict['exclude_internal_backlinks'] = self.exclude_internal_backlinks
        _dict['internal_list_limit'] = self.internal_list_limit
        _dict['backlinks_status_type'] = self.backlinks_status_type
        _dict['backlinks_filters'] = self.backlinks_filters
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
            "include_subdomains": obj.get("include_subdomains"),
            "include_indirect_links": obj.get("include_indirect_links"),
            "exclude_internal_backlinks": obj.get("exclude_internal_backlinks"),
            "internal_list_limit": obj.get("internal_list_limit"),
            "backlinks_status_type": obj.get("backlinks_status_type"),
            "backlinks_filters": obj.get("backlinks_filters"),
            "rank_scale": obj.get("rank_scale"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj