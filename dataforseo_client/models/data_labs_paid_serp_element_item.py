from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ad_link_element import AdLinkElement
from dataforseo_client.models.rank_changes import RankChanges
from dataforseo_client.models.backlinks_info import BacklinksInfo
from dataforseo_client.models.rank_info import RankInfo
from dataforseo_client.models.base_dataforseo_labs_api_element_item import BaseDataforseoLabsApiElementItem



class DataLabsPaidSerpElementItem(BaseDataforseoLabsApiElementItem):
    """
    DataLabsPaidSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    title: Optional[StrictStr] = Field(default=None, description="title of the result in SERP")
    domain: Optional[StrictStr] = Field(default=None, description="subdomain in SERP")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    breadcrumb: Optional[StrictStr] = Field(default=None, description="breadcrumb in SERP")
    url: Optional[StrictStr] = Field(default=None, description="relevant URL in SERP")
    highlighted: Optional[List[Optional[StrictStr]]] = Field(default=None, description="words highlighted in bold within the results description")
    extra: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    description_rows: Optional[List[Optional[StrictStr]]] = Field(default=None, description="extended description. if there is none, equals null")
    links: Optional[List[Optional[AdLinkElement]]] = Field(default=None, description="sitelinks. the links shown below some of Google’s search results. if there are none, equals null")
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
        "title", 
        "domain", 
        "description", 
        "breadcrumb", 
        "url", 
        "highlighted", 
        "extra", 
        "description_rows", 
        "links", 
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
        _dict['title'] = self.title
        _dict['domain'] = self.domain
        _dict['description'] = self.description
        _dict['breadcrumb'] = self.breadcrumb
        _dict['url'] = self.url
        _dict['highlighted'] = self.highlighted
        _dict['extra'] = self.extra
        _dict['description_rows'] = self.description_rows
        links_items = []
        if self.links:
            for _item in self.links:
                if _item:
                    links_items.append(_item.to_dict())
            _dict['links'] = links_items
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
            "title": obj.get("title"),
            "domain": obj.get("domain"),
            "description": obj.get("description"),
            "breadcrumb": obj.get("breadcrumb"),
            "url": obj.get("url"),
            "highlighted": obj.get("highlighted"),
            "extra": obj.get("extra"),
            "description_rows": obj.get("description_rows"),
            "links": [AdLinkElement.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
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