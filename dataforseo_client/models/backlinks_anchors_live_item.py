from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BacklinksAnchorsLiveItem(BaseModel):
    """
    BacklinksAnchorsLiveItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    anchor: Optional[StrictStr] = Field(default=None, description="anchor of the backlink")
    rank: Optional[StrictInt] = Field(default=None, description="rank of the anchor links. rank volume that referring websites pass to the target through links with a particular anchor. rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm. learn more about the metric and how it is calculated in this help center article")
    backlinks: Optional[StrictInt] = Field(default=None, description="indicates the number of backlinks")
    first_seen: Optional[StrictStr] = Field(default=None, description="date and time when our crawler found the backlink with this anchor for the first time. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    lost_date: Optional[StrictStr] = Field(default=None, description="date and time when the last backlink with this anchor was lost. indicates the date and time when our crawler visited the page and it responded with 4xx or 5xx status code or the last backlink was removed. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2017-01-24 13:20:59 +00:00")
    backlinks_spam_score: Optional[StrictInt] = Field(default=None, description="average spam score of all backlinks with this anchor. learn more about how the metric is calculated on this help center page")
    broken_backlinks: Optional[StrictInt] = Field(default=None, description="number of broken backlinks. number of broken backlinks pointing to the target")
    broken_pages: Optional[StrictInt] = Field(default=None, description="number of broken pages. number of pages that respond with 4xx or 5xx status codes where backlinks are pointing to")
    referring_domains: Optional[StrictInt] = Field(default=None, description="indicates the number of referring domains")
    referring_domains_nofollow: Optional[StrictInt] = Field(default=None, description="number of domains pointing at least one nofollow link to the target")
    referring_main_domains: Optional[StrictInt] = Field(default=None, description="indicates the number of referring main domains")
    referring_main_domains_nofollow: Optional[StrictInt] = Field(default=None, description="number of main domains pointing at least one nofollow link to the target")
    referring_ips: Optional[StrictInt] = Field(default=None, description="number of referring IP addresses. number of IP addresses pointing to this page")
    referring_subnets: Optional[StrictInt] = Field(default=None, description="number of referring subnetworks")
    referring_pages: Optional[StrictInt] = Field(default=None, description="indicates the number of pages pointing to target with this anchor")
    referring_pages_nofollow: Optional[StrictInt] = Field(default=None, description="number of referring pages pointing at least one nofollow link to the target with this anchor")
    referring_links_tld: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="top-level domains of the referring links. contains top level domains and referring link count per each")
    referring_links_types: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="types of referring links. indicates the types of the referring links and link count per each type. possible values:. anchor, image, link, meta, canonical, alternate, redirect")
    referring_links_attributes: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="link attributes of the referring links. indicates link attributes of the referring links and link count per each attribute")
    referring_links_platform_types: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="types of referring platforms. indicates referring platform types and and link count per each platform. possible values: cms, blogs, ecommerce, message-boards, wikis, news, organization")
    referring_links_semantic_locations: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="semantic locations of the referring links. indicates semantic elements in HTML where the referring links are located and link count per each semantic location. you can get the full list of semantic elements here. examples:. article, section, summary")
    referring_links_countries: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="ISO country codes of the referring links. indicates ISO country codes of the domains where the referring links are located and the link count per each country")
    __properties: ClassVar[List[str]] = [
        "type", 
        "anchor", 
        "rank", 
        "backlinks", 
        "first_seen", 
        "lost_date", 
        "backlinks_spam_score", 
        "broken_backlinks", 
        "broken_pages", 
        "referring_domains", 
        "referring_domains_nofollow", 
        "referring_main_domains", 
        "referring_main_domains_nofollow", 
        "referring_ips", 
        "referring_subnets", 
        "referring_pages", 
        "referring_pages_nofollow", 
        "referring_links_tld", 
        "referring_links_types", 
        "referring_links_attributes", 
        "referring_links_platform_types", 
        "referring_links_semantic_locations", 
        "referring_links_countries", 
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
        _dict['anchor'] = self.anchor
        _dict['rank'] = self.rank
        _dict['backlinks'] = self.backlinks
        _dict['first_seen'] = self.first_seen
        _dict['lost_date'] = self.lost_date
        _dict['backlinks_spam_score'] = self.backlinks_spam_score
        _dict['broken_backlinks'] = self.broken_backlinks
        _dict['broken_pages'] = self.broken_pages
        _dict['referring_domains'] = self.referring_domains
        _dict['referring_domains_nofollow'] = self.referring_domains_nofollow
        _dict['referring_main_domains'] = self.referring_main_domains
        _dict['referring_main_domains_nofollow'] = self.referring_main_domains_nofollow
        _dict['referring_ips'] = self.referring_ips
        _dict['referring_subnets'] = self.referring_subnets
        _dict['referring_pages'] = self.referring_pages
        _dict['referring_pages_nofollow'] = self.referring_pages_nofollow
        _dict['referring_links_tld'] = self.referring_links_tld
        _dict['referring_links_types'] = self.referring_links_types
        _dict['referring_links_attributes'] = self.referring_links_attributes
        _dict['referring_links_platform_types'] = self.referring_links_platform_types
        _dict['referring_links_semantic_locations'] = self.referring_links_semantic_locations
        _dict['referring_links_countries'] = self.referring_links_countries
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "anchor": obj.get("anchor"),
            "rank": obj.get("rank"),
            "backlinks": obj.get("backlinks"),
            "first_seen": obj.get("first_seen"),
            "lost_date": obj.get("lost_date"),
            "backlinks_spam_score": obj.get("backlinks_spam_score"),
            "broken_backlinks": obj.get("broken_backlinks"),
            "broken_pages": obj.get("broken_pages"),
            "referring_domains": obj.get("referring_domains"),
            "referring_domains_nofollow": obj.get("referring_domains_nofollow"),
            "referring_main_domains": obj.get("referring_main_domains"),
            "referring_main_domains_nofollow": obj.get("referring_main_domains_nofollow"),
            "referring_ips": obj.get("referring_ips"),
            "referring_subnets": obj.get("referring_subnets"),
            "referring_pages": obj.get("referring_pages"),
            "referring_pages_nofollow": obj.get("referring_pages_nofollow"),
            "referring_links_tld": obj.get("referring_links_tld"),
            "referring_links_types": obj.get("referring_links_types"),
            "referring_links_attributes": obj.get("referring_links_attributes"),
            "referring_links_platform_types": obj.get("referring_links_platform_types"),
            "referring_links_semantic_locations": obj.get("referring_links_semantic_locations"),
            "referring_links_countries": obj.get("referring_links_countries"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj