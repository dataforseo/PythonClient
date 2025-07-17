from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.html_content_info import HtmlContentInfo
from dataforseo_client.models.hunspell_info import HunspellInfo
from dataforseo_client.models.on_page_resource_issue_info import OnPageResourceIssueInfo



class PageMetaInfo(BaseModel):
    """
    PageMetaInfo
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description="page title")
    charset: Optional[StrictInt] = Field(default=None, description="code page. example: 65001")
    follow: Optional[StrictBool] = Field(default=None, description="indicates whether a page’s ‘meta robots’ allows crawlers to follow the links on the page. if false, the page’s ‘meta robots’ tag contains “nofollow” parameter instructing crawlers not to follow the links on the page")
    generator: Optional[StrictStr] = Field(default=None, description="meta tag generator")
    htags: Optional[Dict[str, Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="HTML header tags")
    description: Optional[StrictStr] = Field(default=None, description="content of the meta description tag")
    favicon: Optional[StrictStr] = Field(default=None, description="favicon of the page")
    meta_keywords: Optional[StrictStr] = Field(default=None, description="content of the keywords meta tag")
    canonical: Optional[StrictStr] = Field(default=None, description="canonical page")
    internal_links_count: Optional[StrictInt] = Field(default=None, description="number of internal links on the page")
    external_links_count: Optional[StrictInt] = Field(default=None, description="number of external links on the page")
    inbound_links_count: Optional[StrictInt] = Field(default=None, description="number of internal links pointing at the page")
    images_count: Optional[StrictInt] = Field(default=None, description="number of images on the page")
    images_size: Optional[StrictInt] = Field(default=None, description="total size of images on the page measured in bytes")
    scripts_count: Optional[StrictInt] = Field(default=None, description="number of scripts on the page")
    scripts_size: Optional[StrictInt] = Field(default=None, description="total size of scripts on the page measured in bytes")
    stylesheets_count: Optional[StrictInt] = Field(default=None, description="number of stylesheets on the page")
    stylesheets_size: Optional[StrictInt] = Field(default=None, description="total size of stylesheets on the page measured in bytes")
    title_length: Optional[StrictInt] = Field(default=None, description="length of the title tag in characters")
    description_length: Optional[StrictInt] = Field(default=None, description="length of the description tag in characters")
    render_blocking_scripts_count: Optional[StrictInt] = Field(default=None, description="number of scripts on the page that block page rendering")
    render_blocking_stylesheets_count: Optional[StrictInt] = Field(default=None, description="number of CSS styles on the page that block page rendering")
    cumulative_layout_shift: Optional[StrictFloat] = Field(default=None, description="Core Web Vitals metric measuring the layout stability of the page. measures the sum total of all individual layout shift scores for every unexpected layout shift that occurs during the entire lifespan of the page. Learn more.")
    meta_title: Optional[StrictStr] = Field(default=None, description="meta title of the page. meta tag in the head section of an HTML document that defines the title of a page")
    content: Optional[HtmlContentInfo] = Field(default=None, description="overall information about content of the page")
    deprecated_tags: Optional[List[Optional[StrictStr]]] = Field(default=None, description="deprecated tags on the page")
    duplicate_meta_tags: Optional[List[Optional[StrictStr]]] = Field(default=None, description="duplicate meta tags on the page")
    spell: Optional[HunspellInfo] = Field(default=None, description="spellcheck. hunspell spellcheck errors")
    social_media_tags: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="object of social media tags found on the page. contains social media tags and their content. supported tags include but are not limited to Open Graph and Twitter card")
    broken_html: Optional[OnPageResourceIssueInfo] = Field(default=None, description="resource errors and warnings")
    __properties: ClassVar[List[str]] = [
        "title", 
        "charset", 
        "follow", 
        "generator", 
        "htags", 
        "description", 
        "favicon", 
        "meta_keywords", 
        "canonical", 
        "internal_links_count", 
        "external_links_count", 
        "inbound_links_count", 
        "images_count", 
        "images_size", 
        "scripts_count", 
        "scripts_size", 
        "stylesheets_count", 
        "stylesheets_size", 
        "title_length", 
        "description_length", 
        "render_blocking_scripts_count", 
        "render_blocking_stylesheets_count", 
        "cumulative_layout_shift", 
        "meta_title", 
        "content", 
        "deprecated_tags", 
        "duplicate_meta_tags", 
        "spell", 
        "social_media_tags", 
        "broken_html", 
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
        _dict['charset'] = self.charset
        _dict['follow'] = self.follow
        _dict['generator'] = self.generator
        _dict['htags'] = self.htags
        _dict['description'] = self.description
        _dict['favicon'] = self.favicon
        _dict['meta_keywords'] = self.meta_keywords
        _dict['canonical'] = self.canonical
        _dict['internal_links_count'] = self.internal_links_count
        _dict['external_links_count'] = self.external_links_count
        _dict['inbound_links_count'] = self.inbound_links_count
        _dict['images_count'] = self.images_count
        _dict['images_size'] = self.images_size
        _dict['scripts_count'] = self.scripts_count
        _dict['scripts_size'] = self.scripts_size
        _dict['stylesheets_count'] = self.stylesheets_count
        _dict['stylesheets_size'] = self.stylesheets_size
        _dict['title_length'] = self.title_length
        _dict['description_length'] = self.description_length
        _dict['render_blocking_scripts_count'] = self.render_blocking_scripts_count
        _dict['render_blocking_stylesheets_count'] = self.render_blocking_stylesheets_count
        _dict['cumulative_layout_shift'] = self.cumulative_layout_shift
        _dict['meta_title'] = self.meta_title
        _dict['content'] = self.content.to_dict() if self.content else None
        _dict['deprecated_tags'] = self.deprecated_tags
        _dict['duplicate_meta_tags'] = self.duplicate_meta_tags
        _dict['spell'] = self.spell.to_dict() if self.spell else None
        _dict['social_media_tags'] = self.social_media_tags
        _dict['broken_html'] = self.broken_html.to_dict() if self.broken_html else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "charset": obj.get("charset"),
            "follow": obj.get("follow"),
            "generator": obj.get("generator"),
            "htags": obj.get("htags"),
            "description": obj.get("description"),
            "favicon": obj.get("favicon"),
            "meta_keywords": obj.get("meta_keywords"),
            "canonical": obj.get("canonical"),
            "internal_links_count": obj.get("internal_links_count"),
            "external_links_count": obj.get("external_links_count"),
            "inbound_links_count": obj.get("inbound_links_count"),
            "images_count": obj.get("images_count"),
            "images_size": obj.get("images_size"),
            "scripts_count": obj.get("scripts_count"),
            "scripts_size": obj.get("scripts_size"),
            "stylesheets_count": obj.get("stylesheets_count"),
            "stylesheets_size": obj.get("stylesheets_size"),
            "title_length": obj.get("title_length"),
            "description_length": obj.get("description_length"),
            "render_blocking_scripts_count": obj.get("render_blocking_scripts_count"),
            "render_blocking_stylesheets_count": obj.get("render_blocking_stylesheets_count"),
            "cumulative_layout_shift": obj.get("cumulative_layout_shift"),
            "meta_title": obj.get("meta_title"),
            "content": HtmlContentInfo.from_dict(obj["content"]) if obj.get("content") is not None else None,
            "deprecated_tags": obj.get("deprecated_tags"),
            "duplicate_meta_tags": obj.get("duplicate_meta_tags"),
            "spell": HunspellInfo.from_dict(obj["spell"]) if obj.get("spell") is not None else None,
            "social_media_tags": obj.get("social_media_tags"),
            "broken_html": OnPageResourceIssueInfo.from_dict(obj["broken_html"]) if obj.get("broken_html") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj