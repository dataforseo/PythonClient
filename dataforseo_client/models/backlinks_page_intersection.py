from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.backlinks_redirect_info import BacklinksRedirectInfo



class BacklinksPageIntersection(BaseModel):
    """
    BacklinksPageIntersection
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    domain_from: Optional[StrictStr] = Field(default=None, description="domain referring to the target domain or webpage")
    url_from: Optional[StrictStr] = Field(default=None, description="URL of the page where the backlink is found")
    url_from_https: Optional[StrictBool] = Field(default=None, description="indicates whether the referring URL is secured with HTTPS. if true, the referring URL is secured with HTTPS")
    domain_to: Optional[StrictStr] = Field(default=None, description="domain the backlink is pointing to")
    url_to: Optional[StrictStr] = Field(default=None, description="URL the backlink is pointing to")
    url_to_https: Optional[StrictBool] = Field(default=None, description="indicates if the URL the backlink is pointing to is secured with HTTPS. if true, the URL is secured with HTTPS")
    tld_from: Optional[StrictStr] = Field(default=None, description="top-level domain of the referring URL")
    is_new: Optional[StrictBool] = Field(default=None, description="indicates whether the backlink is new. if true, the backlink was found on the page last time our crawler visited it")
    is_lost: Optional[StrictBool] = Field(default=None, description="indicates whether the backlink was removed. if true, the backlink or the entire page was removed")
    backlink_spam_score: Optional[StrictInt] = Field(default=None, description="spam score of the backlink. learn more about how the metric is calculated on this help center page")
    rank: Optional[StrictInt] = Field(default=None, description="backlink rank. rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm. learn more about the metric and how it is calculated in this help center article")
    page_from_rank: Optional[StrictInt] = Field(default=None, description="page rank of the referring page. page_from_rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm. learn more about the metric and how it is calculated in this help center article")
    domain_from_rank: Optional[StrictInt] = Field(default=None, description="domain rank of the referring domain. indicates the rank of the domain at the time our crawler last saw the backlink;. domain_from_rank is calculated based on the method for node ranking in a linked database – a principle used in the original Google PageRank algorithm. learn more about the metric and how it is calculated in this help center article")
    domain_from_platform_type: Optional[List[Optional[StrictStr]]] = Field(default=None, description="platform types of the referring domain. possible values: cms, blogs, ecommerce, message-boards, wikis, news, organization")
    domain_from_is_ip: Optional[StrictBool] = Field(default=None, description="indicates if the domain is IP. if true, the domain functions as an IP address and does not have a domain name")
    domain_from_ip: Optional[StrictStr] = Field(default=None, description="IP address of the referring domain")
    domain_from_country: Optional[StrictStr] = Field(default=None, description="ISO country code of the referring domain")
    page_from_external_links: Optional[StrictInt] = Field(default=None, description="number of external links found on the referring page")
    page_from_internal_links: Optional[StrictInt] = Field(default=None, description="number of internal links found on the referring page")
    page_from_size: Optional[StrictInt] = Field(default=None, description="size of the referring page, in bytes. example:. 63357")
    page_from_encoding: Optional[StrictStr] = Field(default=None, description="character encoding of the referring page. example:. utf-8")
    page_from_language: Optional[StrictStr] = Field(default=None, description="language of the referring page. in ISO 639-1 format. example:. en")
    page_from_title: Optional[StrictStr] = Field(default=None, description="title of the referring page")
    page_from_status_code: Optional[StrictInt] = Field(default=None, description="HTTP status code returned by the referring page. example:. 200")
    first_seen: Optional[StrictStr] = Field(default=None, description="date and time when our crawler found the backlink for the first time. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    prev_seen: Optional[StrictStr] = Field(default=None, description="previous to the most recent date when our crawler visited the backlink. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    last_seen: Optional[StrictStr] = Field(default=None, description="most recent date when our crawler visited the backlink. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    item_type: Optional[StrictStr] = Field(default=None, description="link type. possible values:. anchor, image, link, meta, canonical, alternate, redirect")
    attributes: Optional[List[Optional[StrictStr]]] = Field(default=None, description="link attributes of the referring links. example:. nofollow")
    dofollow: Optional[StrictBool] = Field(default=None, description="indicates whether the backlink is dofollow. if false, the backlink is nofollow")
    original: Optional[StrictBool] = Field(default=None, description="indicates whether the backlink was present on the referring page when our crawler first visited it")
    alt: Optional[StrictStr] = Field(default=None, description="alternative text of the image. this field will be null if backlink type is not image")
    anchor: Optional[StrictStr] = Field(default=None, description="anchor text of the backlink")
    text_pre: Optional[StrictStr] = Field(default=None, description="text snippet before the anchor text")
    text_post: Optional[StrictStr] = Field(default=None, description="snippet after the anchor text")
    semantic_location: Optional[StrictStr] = Field(default=None, description="indicates semantic element in HTML where the backlink is found. you can get the full list of semantic elements here. examples:. article, section, summary")
    links_count: Optional[StrictInt] = Field(default=None, description="number of identical backlinks found on the referring page")
    group_count: Optional[StrictInt] = Field(default=None, description="indicates total number of backlinks from this domain. for example, if mode is set to one_per_domain, this field will indicate the total number of backlinks coming from this domain")
    is_broken: Optional[StrictBool] = Field(default=None, description="indicates whether the backlink is broken. if true, the backlink is pointing to a page responding with a 4xx or 5xx status code")
    url_to_status_code: Optional[StrictInt] = Field(default=None, description="status code of the referenced page. if the value is null, our crawler hasn’t yet visited the webpage the link is pointing to. example:. 200")
    url_to_spam_score: Optional[StrictInt] = Field(default=None, description="spam score of the referenced page. if the value is null, our crawler hasn’t yet visited the webpage the link is pointing to. learn more about how the metric is calculated on this help center page")
    url_to_redirect_target: Optional[StrictStr] = Field(default=None, description="target url of the redirect. target page the redirect is pointing to")
    is_indirect_link: Optional[StrictBool] = Field(default=None, description="indicates whether the backlink is an indirect link. if true, the backlink is an indirect link pointing to a page that either redirects to url_to, or points to a canonical page")
    indirect_link_path: Optional[List[Optional[BacklinksRedirectInfo]]] = Field(default=None, description="indirect link path. indicates a URL or a sequence of URLs that lead to url_to")
    __properties: ClassVar[List[str]] = [
        "type", 
        "domain_from", 
        "url_from", 
        "url_from_https", 
        "domain_to", 
        "url_to", 
        "url_to_https", 
        "tld_from", 
        "is_new", 
        "is_lost", 
        "backlink_spam_score", 
        "rank", 
        "page_from_rank", 
        "domain_from_rank", 
        "domain_from_platform_type", 
        "domain_from_is_ip", 
        "domain_from_ip", 
        "domain_from_country", 
        "page_from_external_links", 
        "page_from_internal_links", 
        "page_from_size", 
        "page_from_encoding", 
        "page_from_language", 
        "page_from_title", 
        "page_from_status_code", 
        "first_seen", 
        "prev_seen", 
        "last_seen", 
        "item_type", 
        "attributes", 
        "dofollow", 
        "original", 
        "alt", 
        "anchor", 
        "text_pre", 
        "text_post", 
        "semantic_location", 
        "links_count", 
        "group_count", 
        "is_broken", 
        "url_to_status_code", 
        "url_to_spam_score", 
        "url_to_redirect_target", 
        "is_indirect_link", 
        "indirect_link_path", 
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
        _dict['domain_from'] = self.domain_from
        _dict['url_from'] = self.url_from
        _dict['url_from_https'] = self.url_from_https
        _dict['domain_to'] = self.domain_to
        _dict['url_to'] = self.url_to
        _dict['url_to_https'] = self.url_to_https
        _dict['tld_from'] = self.tld_from
        _dict['is_new'] = self.is_new
        _dict['is_lost'] = self.is_lost
        _dict['backlink_spam_score'] = self.backlink_spam_score
        _dict['rank'] = self.rank
        _dict['page_from_rank'] = self.page_from_rank
        _dict['domain_from_rank'] = self.domain_from_rank
        _dict['domain_from_platform_type'] = self.domain_from_platform_type
        _dict['domain_from_is_ip'] = self.domain_from_is_ip
        _dict['domain_from_ip'] = self.domain_from_ip
        _dict['domain_from_country'] = self.domain_from_country
        _dict['page_from_external_links'] = self.page_from_external_links
        _dict['page_from_internal_links'] = self.page_from_internal_links
        _dict['page_from_size'] = self.page_from_size
        _dict['page_from_encoding'] = self.page_from_encoding
        _dict['page_from_language'] = self.page_from_language
        _dict['page_from_title'] = self.page_from_title
        _dict['page_from_status_code'] = self.page_from_status_code
        _dict['first_seen'] = self.first_seen
        _dict['prev_seen'] = self.prev_seen
        _dict['last_seen'] = self.last_seen
        _dict['item_type'] = self.item_type
        _dict['attributes'] = self.attributes
        _dict['dofollow'] = self.dofollow
        _dict['original'] = self.original
        _dict['alt'] = self.alt
        _dict['anchor'] = self.anchor
        _dict['text_pre'] = self.text_pre
        _dict['text_post'] = self.text_post
        _dict['semantic_location'] = self.semantic_location
        _dict['links_count'] = self.links_count
        _dict['group_count'] = self.group_count
        _dict['is_broken'] = self.is_broken
        _dict['url_to_status_code'] = self.url_to_status_code
        _dict['url_to_spam_score'] = self.url_to_spam_score
        _dict['url_to_redirect_target'] = self.url_to_redirect_target
        _dict['is_indirect_link'] = self.is_indirect_link
        indirect_link_path_items = []
        if self.indirect_link_path:
            for _item in self.indirect_link_path:
                if _item:
                    indirect_link_path_items.append(_item.to_dict())
            _dict['indirect_link_path'] = indirect_link_path_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "domain_from": obj.get("domain_from"),
            "url_from": obj.get("url_from"),
            "url_from_https": obj.get("url_from_https"),
            "domain_to": obj.get("domain_to"),
            "url_to": obj.get("url_to"),
            "url_to_https": obj.get("url_to_https"),
            "tld_from": obj.get("tld_from"),
            "is_new": obj.get("is_new"),
            "is_lost": obj.get("is_lost"),
            "backlink_spam_score": obj.get("backlink_spam_score"),
            "rank": obj.get("rank"),
            "page_from_rank": obj.get("page_from_rank"),
            "domain_from_rank": obj.get("domain_from_rank"),
            "domain_from_platform_type": obj.get("domain_from_platform_type"),
            "domain_from_is_ip": obj.get("domain_from_is_ip"),
            "domain_from_ip": obj.get("domain_from_ip"),
            "domain_from_country": obj.get("domain_from_country"),
            "page_from_external_links": obj.get("page_from_external_links"),
            "page_from_internal_links": obj.get("page_from_internal_links"),
            "page_from_size": obj.get("page_from_size"),
            "page_from_encoding": obj.get("page_from_encoding"),
            "page_from_language": obj.get("page_from_language"),
            "page_from_title": obj.get("page_from_title"),
            "page_from_status_code": obj.get("page_from_status_code"),
            "first_seen": obj.get("first_seen"),
            "prev_seen": obj.get("prev_seen"),
            "last_seen": obj.get("last_seen"),
            "item_type": obj.get("item_type"),
            "attributes": obj.get("attributes"),
            "dofollow": obj.get("dofollow"),
            "original": obj.get("original"),
            "alt": obj.get("alt"),
            "anchor": obj.get("anchor"),
            "text_pre": obj.get("text_pre"),
            "text_post": obj.get("text_post"),
            "semantic_location": obj.get("semantic_location"),
            "links_count": obj.get("links_count"),
            "group_count": obj.get("group_count"),
            "is_broken": obj.get("is_broken"),
            "url_to_status_code": obj.get("url_to_status_code"),
            "url_to_spam_score": obj.get("url_to_spam_score"),
            "url_to_redirect_target": obj.get("url_to_redirect_target"),
            "is_indirect_link": obj.get("is_indirect_link"),
            "indirect_link_path": [BacklinksRedirectInfo.from_dict(_item) for _item in obj["indirect_link_path"]] if obj.get("indirect_link_path") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj