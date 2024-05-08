# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.target_info import TargetInfo
from typing import Optional, Set
from typing_extensions import Self

class BacklinksSummaryLiveResultInfo(BaseModel):
    """
    BacklinksSummaryLiveResultInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="target in a POST array")
    first_seen: Optional[StrictStr] = Field(default=None, description="date and time when our crawler found the backlink for the target for the first time in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    lost_date: Optional[StrictStr] = Field(default=None, description="date and time when the backlink was lost indicates the date and time when our crawler visited the target and it responded with a 4xx or 5xx status code or when its last backlink was removed in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    rank: Optional[StrictInt] = Field(default=None, description="target rank learn more about the metric and how it is calculated in this help center article")
    backlinks: Optional[StrictInt] = Field(default=None, description="indicates the number of backlinks")
    backlinks_spam_score: Optional[StrictInt] = Field(default=None, description="spam score of the backlinks displays the total spam score of all backlinks pointing to the target domain, subdomain, or webpage; to learn more about how the metric is calculated, refer to this Help Center page")
    crawled_pages: Optional[StrictInt] = Field(default=None, description="number of crawled pages for the target")
    info: Optional[TargetInfo] = None
    internal_links_count: Optional[StrictInt] = Field(default=None, description="number of internal links calculated as the sum of internal links on the pages of the specified target")
    external_links_count: Optional[StrictInt] = Field(default=None, description="number of external links on the page calculated as the sum of external links on the pages of the specified target")
    broken_backlinks: Optional[StrictInt] = Field(default=None, description="number of broken backlinks number of broken backlinks pointing to the target")
    broken_pages: Optional[StrictInt] = Field(default=None, description="number of broken pages number of pages on the target that respond with 4xx or 5xx status codes note that the number of broken pages includes pages on the target discovered by following external links, but it may also include pages discovered by following the target’s sitemap")
    referring_domains: Optional[StrictInt] = Field(default=None, description="indicates the number of referring domains referring domains include subdomains that are counted as separate domains for this metric")
    referring_domains_nofollow: Optional[StrictInt] = Field(default=None, description="number of domains pointing at least one nofollow link to the target")
    referring_main_domains: Optional[StrictInt] = Field(default=None, description="indicates the number of referring main domains")
    referring_main_domains_nofollow: Optional[StrictInt] = Field(default=None, description="number of main domains pointing at least one nofollow link to the target")
    referring_ips: Optional[StrictInt] = Field(default=None, description="number of referring IP addresses number of IP addresses pointing to this page")
    referring_subnets: Optional[StrictInt] = Field(default=None, description="number of referring subnetworks")
    referring_pages: Optional[StrictInt] = Field(default=None, description="indicates the number of pages pointing to the target")
    referring_links_tld: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="top-level domains of the referring links contains top level domains and referring link count per each")
    referring_links_types: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="types of referring links indicates the types of the referring links and link count per each type possible values: anchor, image, link, meta, canonical, alternate, redirect")
    referring_links_attributes: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="link attributes of the referring links indicates link attributes of the referring links and link count per each attribute example values: nofollow, noopener, noreferrer, external, ugc, sponsored")
    referring_links_platform_types: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="types of referring platforms indicates referring platform types and and link count per each platform example values: cms, blogs, unknown, ecommerce, message-boards")
    referring_links_semantic_locations: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="semantic locations of the referring links indicates semantic elements in HTML where the referring links are located and link count per each semantic location you can get the full list of semantic elements here example values: article, section, summary, \"\"")
    referring_links_countries: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="ISO country codes of the referring links indicates ISO country codes of the domains where the referring links are located and the link count per each country")
    referring_pages_nofollow: Optional[StrictInt] = Field(default=None, description="number of referring pages pointing at least one nofollow link to the target")
    __properties: ClassVar[List[str]] = ["target", "first_seen", "lost_date", "rank", "backlinks", "backlinks_spam_score", "crawled_pages", "info", "internal_links_count", "external_links_count", "broken_backlinks", "broken_pages", "referring_domains", "referring_domains_nofollow", "referring_main_domains", "referring_main_domains_nofollow", "referring_ips", "referring_subnets", "referring_pages", "referring_links_tld", "referring_links_types", "referring_links_attributes", "referring_links_platform_types", "referring_links_semantic_locations", "referring_links_countries", "referring_pages_nofollow"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BacklinksSummaryLiveResultInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of info
        if self.info:
            _dict['info'] = self.info.to_dict()
        # set to None if target (nullable) is None
        # and model_fields_set contains the field
        if self.target is None and "target" in self.model_fields_set:
            _dict['target'] = None

        # set to None if first_seen (nullable) is None
        # and model_fields_set contains the field
        if self.first_seen is None and "first_seen" in self.model_fields_set:
            _dict['first_seen'] = None

        # set to None if lost_date (nullable) is None
        # and model_fields_set contains the field
        if self.lost_date is None and "lost_date" in self.model_fields_set:
            _dict['lost_date'] = None

        # set to None if rank (nullable) is None
        # and model_fields_set contains the field
        if self.rank is None and "rank" in self.model_fields_set:
            _dict['rank'] = None

        # set to None if backlinks (nullable) is None
        # and model_fields_set contains the field
        if self.backlinks is None and "backlinks" in self.model_fields_set:
            _dict['backlinks'] = None

        # set to None if backlinks_spam_score (nullable) is None
        # and model_fields_set contains the field
        if self.backlinks_spam_score is None and "backlinks_spam_score" in self.model_fields_set:
            _dict['backlinks_spam_score'] = None

        # set to None if crawled_pages (nullable) is None
        # and model_fields_set contains the field
        if self.crawled_pages is None and "crawled_pages" in self.model_fields_set:
            _dict['crawled_pages'] = None

        # set to None if internal_links_count (nullable) is None
        # and model_fields_set contains the field
        if self.internal_links_count is None and "internal_links_count" in self.model_fields_set:
            _dict['internal_links_count'] = None

        # set to None if external_links_count (nullable) is None
        # and model_fields_set contains the field
        if self.external_links_count is None and "external_links_count" in self.model_fields_set:
            _dict['external_links_count'] = None

        # set to None if broken_backlinks (nullable) is None
        # and model_fields_set contains the field
        if self.broken_backlinks is None and "broken_backlinks" in self.model_fields_set:
            _dict['broken_backlinks'] = None

        # set to None if broken_pages (nullable) is None
        # and model_fields_set contains the field
        if self.broken_pages is None and "broken_pages" in self.model_fields_set:
            _dict['broken_pages'] = None

        # set to None if referring_domains (nullable) is None
        # and model_fields_set contains the field
        if self.referring_domains is None and "referring_domains" in self.model_fields_set:
            _dict['referring_domains'] = None

        # set to None if referring_domains_nofollow (nullable) is None
        # and model_fields_set contains the field
        if self.referring_domains_nofollow is None and "referring_domains_nofollow" in self.model_fields_set:
            _dict['referring_domains_nofollow'] = None

        # set to None if referring_main_domains (nullable) is None
        # and model_fields_set contains the field
        if self.referring_main_domains is None and "referring_main_domains" in self.model_fields_set:
            _dict['referring_main_domains'] = None

        # set to None if referring_main_domains_nofollow (nullable) is None
        # and model_fields_set contains the field
        if self.referring_main_domains_nofollow is None and "referring_main_domains_nofollow" in self.model_fields_set:
            _dict['referring_main_domains_nofollow'] = None

        # set to None if referring_ips (nullable) is None
        # and model_fields_set contains the field
        if self.referring_ips is None and "referring_ips" in self.model_fields_set:
            _dict['referring_ips'] = None

        # set to None if referring_subnets (nullable) is None
        # and model_fields_set contains the field
        if self.referring_subnets is None and "referring_subnets" in self.model_fields_set:
            _dict['referring_subnets'] = None

        # set to None if referring_pages (nullable) is None
        # and model_fields_set contains the field
        if self.referring_pages is None and "referring_pages" in self.model_fields_set:
            _dict['referring_pages'] = None

        # set to None if referring_links_tld (nullable) is None
        # and model_fields_set contains the field
        if self.referring_links_tld is None and "referring_links_tld" in self.model_fields_set:
            _dict['referring_links_tld'] = None

        # set to None if referring_links_types (nullable) is None
        # and model_fields_set contains the field
        if self.referring_links_types is None and "referring_links_types" in self.model_fields_set:
            _dict['referring_links_types'] = None

        # set to None if referring_links_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.referring_links_attributes is None and "referring_links_attributes" in self.model_fields_set:
            _dict['referring_links_attributes'] = None

        # set to None if referring_links_platform_types (nullable) is None
        # and model_fields_set contains the field
        if self.referring_links_platform_types is None and "referring_links_platform_types" in self.model_fields_set:
            _dict['referring_links_platform_types'] = None

        # set to None if referring_links_semantic_locations (nullable) is None
        # and model_fields_set contains the field
        if self.referring_links_semantic_locations is None and "referring_links_semantic_locations" in self.model_fields_set:
            _dict['referring_links_semantic_locations'] = None

        # set to None if referring_links_countries (nullable) is None
        # and model_fields_set contains the field
        if self.referring_links_countries is None and "referring_links_countries" in self.model_fields_set:
            _dict['referring_links_countries'] = None

        # set to None if referring_pages_nofollow (nullable) is None
        # and model_fields_set contains the field
        if self.referring_pages_nofollow is None and "referring_pages_nofollow" in self.model_fields_set:
            _dict['referring_pages_nofollow'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BacklinksSummaryLiveResultInfo from a dict"""
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
            "referring_links_tld": obj.get("referring_links_tld"),
            "referring_links_types": obj.get("referring_links_types"),
            "referring_links_attributes": obj.get("referring_links_attributes"),
            "referring_links_platform_types": obj.get("referring_links_platform_types"),
            "referring_links_semantic_locations": obj.get("referring_links_semantic_locations"),
            "referring_links_countries": obj.get("referring_links_countries"),
            "referring_pages_nofollow": obj.get("referring_pages_nofollow")
        })
        return _obj

