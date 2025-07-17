from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BacklinksPageMeta(BaseModel):
    """
    BacklinksPageMeta
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description="page title")
    canonical: Optional[StrictStr] = Field(default=None, description="canonical page")
    internal_links_count: Optional[StrictInt] = Field(default=None, description="number of internal links on the page")
    external_links_count: Optional[StrictInt] = Field(default=None, description="number of external links on the page")
    images_count: Optional[StrictInt] = Field(default=None, description="number of images on the page")
    words_count: Optional[StrictInt] = Field(default=None, description="number of words on the page")
    page_spam_score: Optional[StrictInt] = Field(default=None, description="spam score of the page. learn more about how the metric is calculated on this help center page")
    social_media_tags: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="array of social media tags found on the page. contains social media tags and their content. supported tags include but are not limited to Open Graph and Twitter card")
    h_1: Optional[List[Optional[StrictStr]]] = Field(default=None, description="h1 tag. content of h1 tags")
    h_2: Optional[List[Optional[StrictStr]]] = Field(default=None, description="h2 tag. content of h2 tags")
    h_3: Optional[List[Optional[StrictStr]]] = Field(default=None, description="h3 tag. content of h3 tags")
    images_alt: Optional[List[Optional[StrictStr]]] = Field(default=None, description="content of alt tags")
    powered_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="CMS details")
    language: Optional[StrictStr] = Field(default=None, description="page content language. example:. en")
    charset: Optional[StrictStr] = Field(default=None, description="character encoding. examples:. utf-8")
    platform_type: Optional[List[Optional[StrictStr]]] = Field(default=None, description="type of a platform")
    technologies: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="website technologies")
    __properties: ClassVar[List[str]] = [
        "title", 
        "canonical", 
        "internal_links_count", 
        "external_links_count", 
        "images_count", 
        "words_count", 
        "page_spam_score", 
        "social_media_tags", 
        "h1", 
        "h2", 
        "h3", 
        "images_alt", 
        "powered_by", 
        "language", 
        "charset", 
        "platform_type", 
        "technologies", 
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

        _dict['title'] = self.title
        _dict['canonical'] = self.canonical
        _dict['internal_links_count'] = self.internal_links_count
        _dict['external_links_count'] = self.external_links_count
        _dict['images_count'] = self.images_count
        _dict['words_count'] = self.words_count
        _dict['page_spam_score'] = self.page_spam_score
        _dict['social_media_tags'] = self.social_media_tags
        _dict['h1'] = self.h_1
        _dict['h2'] = self.h_2
        _dict['h3'] = self.h_3
        _dict['images_alt'] = self.images_alt
        _dict['powered_by'] = self.powered_by
        _dict['language'] = self.language
        _dict['charset'] = self.charset
        _dict['platform_type'] = self.platform_type
        _dict['technologies'] = self.technologies
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "canonical": obj.get("canonical"),
            "internal_links_count": obj.get("internal_links_count"),
            "external_links_count": obj.get("external_links_count"),
            "images_count": obj.get("images_count"),
            "words_count": obj.get("words_count"),
            "page_spam_score": obj.get("page_spam_score"),
            "social_media_tags": obj.get("social_media_tags"),
            "h_1": obj.get("h1"),
            "h_2": obj.get("h2"),
            "h_3": obj.get("h3"),
            "images_alt": obj.get("images_alt"),
            "powered_by": obj.get("powered_by"),
            "language": obj.get("language"),
            "charset": obj.get("charset"),
            "platform_type": obj.get("platform_type"),
            "technologies": obj.get("technologies"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj