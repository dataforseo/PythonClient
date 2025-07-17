from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class PageMetrics(BaseModel):
    """
    PageMetrics
    """ # noqa: E501
    links_external: Optional[StrictInt] = Field(default=None, description="number of external links. the number of links pointing to other websites")
    links_internal: Optional[StrictInt] = Field(default=None, description="number of internal links. the number of links pointing to other pages within the target website")
    duplicate_title: Optional[StrictInt] = Field(default=None, description="number of pages with duplicate titles")
    duplicate_description: Optional[StrictInt] = Field(default=None, description="number of pages with duplicate descriptions")
    duplicate_content: Optional[StrictInt] = Field(default=None, description="number of pages with duplicate content")
    broken_links: Optional[StrictInt] = Field(default=None, description="number of broken links. number of broken links across all crawled pages on a target website")
    broken_resources: Optional[StrictInt] = Field(default=None, description="number of broken resources. the number of images and other resources with broken links")
    links_relation_conflict: Optional[StrictInt] = Field(default=None, description="number of links present on the target website that may have a conflict. for example, if 'links_relation_conflict': 2, the target website is referring to the same source by at least one internal link with the rel='nofollow' attribute and by at least one dofollow link")
    redirect_loop: Optional[StrictInt] = Field(default=None, description="number of redirect chains that start and end at the same URL. number of redirect chains where the destination URL redirects back to the original URL")
    onpage_score: Optional[StrictFloat] = Field(default=None, description="shows how website is optimized on a 100-point scale. this field shows how website is optimized considering critical on-page issues and warnings detected;. 100 is the highest possible score that means website does not have any critical on-page issues and important warnings;. note that this value depends on the number of crawled pages;. learn more about how the metric is calculated in this help center article")
    non_indexable: Optional[StrictInt] = Field(default=None, description="number of non-indexable pages. number of pages that are blocked from being indexed by Google and other search engines by robots.txt, HTTP headers, or meta tags settings;. you can receive a list of non-indexable URLs using this endpoint")
    checks: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="page-specific on-page check-ups")
    __properties: ClassVar[List[str]] = [
        "links_external", 
        "links_internal", 
        "duplicate_title", 
        "duplicate_description", 
        "duplicate_content", 
        "broken_links", 
        "broken_resources", 
        "links_relation_conflict", 
        "redirect_loop", 
        "onpage_score", 
        "non_indexable", 
        "checks", 
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

        _dict['links_external'] = self.links_external
        _dict['links_internal'] = self.links_internal
        _dict['duplicate_title'] = self.duplicate_title
        _dict['duplicate_description'] = self.duplicate_description
        _dict['duplicate_content'] = self.duplicate_content
        _dict['broken_links'] = self.broken_links
        _dict['broken_resources'] = self.broken_resources
        _dict['links_relation_conflict'] = self.links_relation_conflict
        _dict['redirect_loop'] = self.redirect_loop
        _dict['onpage_score'] = self.onpage_score
        _dict['non_indexable'] = self.non_indexable
        _dict['checks'] = self.checks
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "links_external": obj.get("links_external"),
            "links_internal": obj.get("links_internal"),
            "duplicate_title": obj.get("duplicate_title"),
            "duplicate_description": obj.get("duplicate_description"),
            "duplicate_content": obj.get("duplicate_content"),
            "broken_links": obj.get("broken_links"),
            "broken_resources": obj.get("broken_resources"),
            "links_relation_conflict": obj.get("links_relation_conflict"),
            "redirect_loop": obj.get("redirect_loop"),
            "onpage_score": obj.get("onpage_score"),
            "non_indexable": obj.get("non_indexable"),
            "checks": obj.get("checks"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj