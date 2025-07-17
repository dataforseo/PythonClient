from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.table import Table
from dataforseo_client.models.rank_changes import RankChanges
from dataforseo_client.models.backlinks_info import BacklinksInfo
from dataforseo_client.models.rank_info import RankInfo
from dataforseo_client.models.base_dataforseo_labs_api_element_item import BaseDataforseoLabsApiElementItem



class DataLabsFeaturedSnippetSerpElementItem(BaseDataforseoLabsApiElementItem):
    """
    DataLabsFeaturedSnippetSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    domain: Optional[StrictStr] = Field(default=None, description="subdomain in SERP")
    title: Optional[StrictStr] = Field(default=None, description="title of the result in SERP")
    featured_title: Optional[StrictStr] = Field(default=None, description="the title of the featured snippets source page")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    url: Optional[StrictStr] = Field(default=None, description="relevant URL in SERP")
    table: Optional[Table] = Field(default=None, description="results table. if there are none, equals null")
    main_domain: Optional[StrictStr] = Field(default=None, description="primary domain name in SERP")
    relative_url: Optional[StrictStr] = Field(default=None, description="URL in SERP that does not specify the HTTPs protocol and domain name")
    etv: Optional[StrictFloat] = Field(default=None, description="estimated traffic volume. estimated paid monthly traffic to the domain. calculated as the product of CTR (click-through-rate) and search volume values of all keywords in the category that the domain ranks for. learn more about how the metric is calculated in this help center article")
    estimated_paid_traffic_cost: Optional[StrictFloat] = Field(default=None, description="estimated cost of monthly search traffic. represents the estimated cost of paid monthly traffic (USD) based on etv and cpc values of all keywords in the category that the domain ranks for. learn more about how the metric is calculated in this help center article")
    clickstream_etv: Optional[StrictFloat] = Field(default=None, description="estimated traffic volume based on clickstream data. calculated as the product of click-through-rate and clickstream search volume values of all keywords the domain ranks for. to retrieve results for this field, the parameter include_clickstream_data must be set to true. learn more about how the metric is calculated in this help center article")
    rank_changes: Optional[RankChanges] = Field(default=None, description="changes in rankings. contains information about the ranking changes of the SERP element since the previous_updated_time")
    backlinks_info: Optional[BacklinksInfo] = Field(default=None, description="backlinks information for the target website")
    rank_info: Optional[RankInfo] = Field(default=None, description="page and domain rank information")
    __properties: ClassVar[List[str]] = [
        "type", 
        "se_type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "domain", 
        "title", 
        "featured_title", 
        "description", 
        "url", 
        "table", 
        "main_domain", 
        "relative_url", 
        "etv", 
        "estimated_paid_traffic_cost", 
        "clickstream_etv", 
        "rank_changes", 
        "backlinks_info", 
        "rank_info", 
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

        _dict['type'] = self.type
        _dict['se_type'] = self.se_type
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
        _dict['domain'] = self.domain
        _dict['title'] = self.title
        _dict['featured_title'] = self.featured_title
        _dict['description'] = self.description
        _dict['url'] = self.url
        _dict['table'] = self.table.to_dict() if self.table else None
        _dict['main_domain'] = self.main_domain
        _dict['relative_url'] = self.relative_url
        _dict['etv'] = self.etv
        _dict['estimated_paid_traffic_cost'] = self.estimated_paid_traffic_cost
        _dict['clickstream_etv'] = self.clickstream_etv
        _dict['rank_changes'] = self.rank_changes.to_dict() if self.rank_changes else None
        _dict['backlinks_info'] = self.backlinks_info.to_dict() if self.backlinks_info else None
        _dict['rank_info'] = self.rank_info.to_dict() if self.rank_info else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "se_type": obj.get("se_type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "domain": obj.get("domain"),
            "title": obj.get("title"),
            "featured_title": obj.get("featured_title"),
            "description": obj.get("description"),
            "url": obj.get("url"),
            "table": Table.from_dict(obj["table"]) if obj.get("table") is not None else None,
            "main_domain": obj.get("main_domain"),
            "relative_url": obj.get("relative_url"),
            "etv": obj.get("etv"),
            "estimated_paid_traffic_cost": obj.get("estimated_paid_traffic_cost"),
            "clickstream_etv": obj.get("clickstream_etv"),
            "rank_changes": RankChanges.from_dict(obj["rank_changes"]) if obj.get("rank_changes") is not None else None,
            "backlinks_info": BacklinksInfo.from_dict(obj["backlinks_info"]) if obj.get("backlinks_info") is not None else None,
            "rank_info": RankInfo.from_dict(obj["rank_info"]) if obj.get("rank_info") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj