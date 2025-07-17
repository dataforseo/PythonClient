from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.target_info import TargetInfo



class BacklinksSummaryLiveResultInfo(BaseModel):
    """
    BacklinksSummaryLiveResultInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="target in a POST array")
    first_seen: Optional[StrictStr] = Field(default=None, description="date and time when our crawler found the backlink for the target for the first time. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    lost_date: Optional[StrictStr] = Field(default=None, description="date and time when the backlink was lost. indicates the date and time when our crawler visited the target and it responded with a 4xx or 5xx status code or when its last backlink was removed. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    rank: Optional[StrictInt] = Field(default=None, description="target rank. learn more about the metric and how it is calculated in this help center article")
    backlinks: Optional[StrictInt] = Field(default=None, description="indicates the number of backlinks")
    backlinks_spam_score: Optional[StrictInt] = Field(default=None, description="spam score of the backlinks. displays the total spam score of all backlinks pointing to the target domain, subdomain, or webpage;. to learn more about how the metric is calculated, refer to this Help Center page")
    crawled_pages: Optional[StrictInt] = Field(default=None, description="number of crawled pages for the target")
    info: Optional[TargetInfo] = Field(default=None, description="information about the target")
    internal_links_count: Optional[StrictInt] = Field(default=None, description="number of internal links. calculated as the sum of internal links on the pages of the specified target")
    external_links_count: Optional[StrictInt] = Field(default=None, description="number of external links on the page. calculated as the sum of external links on the pages of the specified target")
    broken_backlinks: Optional[StrictInt] = Field(default=None, description="number of broken backlinks. number of broken backlinks pointing to the target")
    broken_pages: Optional[StrictInt] = Field(default=None, description="number of broken pages. number of pages on the target that respond with 4xx or 5xx status codes. note that the number of broken pages includes pages on the target discovered by following external links, but it may also include pages discovered by following the target’s sitemap")
    referring_domains: Optional[StrictInt] = Field(default=None, description="indicates the number of referring domains. referring domains include subdomains that are counted as separate domains for this metric")
    referring_domains_nofollow: Optional[StrictInt] = Field(default=None, description="number of domains pointing at least one nofollow link to the target")
    referring_main_domains: Optional[StrictInt] = Field(default=None, description="indicates the number of referring main domains")
    referring_main_domains_nofollow: Optional[StrictInt] = Field(default=None, description="number of main domains pointing at least one nofollow link to the target")
    referring_ips: Optional[StrictInt] = Field(default=None, description="number of referring IP addresses. number of IP addresses pointing to this page")
    referring_subnets: Optional[StrictInt] = Field(default=None, description="number of referring subnetworks")
    referring_pages: Optional[StrictInt] = Field(default=None, description="indicates the number of pages pointing to the target")
    referring_pages_nofollow: Optional[StrictInt] = Field(default=None, description="number of referring pages pointing at least one nofollow link to the target")
    referring_links_tld: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="top-level domains of the referring links. contains top level domains and referring link count per each")
    referring_links_types: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="types of referring links. indicates the types of the referring links and link count per each type. possible values:. anchor, image, link, meta, canonical, alternate, redirect")
    referring_links_attributes: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="link attributes of the referring links. indicates link attributes of the referring links and link count per each attribute. example values:. nofollow, noopener, noreferrer, external, ugc, sponsored")
    referring_links_platform_types: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="types of referring platforms. indicates referring platform types and and link count per each platform. possible values: cms, blogs, ecommerce, message-boards, wikis, news, organization")
    referring_links_semantic_locations: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="semantic locations of the referring links. indicates semantic elements in HTML where the referring links are located and link count per each semantic location. you can get the full list of semantic elements here. example values:. article, section, summary, ''")
    referring_links_countries: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="ISO country codes of the referring links. indicates ISO country codes of the domains where the referring links are located and the link count per each country")
    __properties: ClassVar[List[str]] = [
        "target", 
        "first_seen", 
        "lost_date", 
        "rank", 
        "backlinks", 
        "backlinks_spam_score", 
        "crawled_pages", 
        "info", 
        "internal_links_count", 
        "external_links_count", 
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

        _dict['target'] = self.target
        _dict['first_seen'] = self.first_seen
        _dict['lost_date'] = self.lost_date
        _dict['rank'] = self.rank
        _dict['backlinks'] = self.backlinks
        _dict['backlinks_spam_score'] = self.backlinks_spam_score
        _dict['crawled_pages'] = self.crawled_pages
        _dict['info'] = self.info.to_dict() if self.info else None
        _dict['internal_links_count'] = self.internal_links_count
        _dict['external_links_count'] = self.external_links_count
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
            "target": obj.get("target"),
            "first_seen": obj.get("first_seen"),
            "lost_date": obj.get("lost_date"),
            "rank": obj.get("rank"),
            "backlinks": obj.get("backlinks"),
            "backlinks_spam_score": obj.get("backlinks_spam_score"),
            "crawled_pages": obj.get("crawled_pages"),
            "info": TargetInfo.from_dict(obj["info"]) if obj.get("info") is not None else None,
            "internal_links_count": obj.get("internal_links_count"),
            "external_links_count": obj.get("external_links_count"),
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