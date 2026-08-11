from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_mode_images_element_info import AiModeImagesElementInfo
from dataforseo_client.models.rating_info import RatingInfo
from dataforseo_client.models.price_info import PriceInfo
from dataforseo_client.models.link_element import LinkElement
from dataforseo_client.models.faq_box import FaqBox
from dataforseo_client.models.about_this_result_element import AboutThisResultElement
from dataforseo_client.models.related_result import RelatedResult
from dataforseo_client.models.base_serp_api_google_search_by_images_element_item import BaseSerpApiGoogleSearchByImagesElementItem
from dataforseo_client.models.ai_mode_rectangle_info import AiModeRectangleInfo



class SerpApiGoogleSearchByImagesOrganicElementItem(BaseSerpApiGoogleSearchByImagesElementItem):
    """
    SerpApiGoogleSearchByImagesOrganicElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description=r"")
    rank_absolute: Optional[StrictInt] = Field(default=None, description=r"")
    page: Optional[StrictInt] = Field(default=None, description=r"")
    position: Optional[StrictStr] = Field(default=None, description=r"")
    xpath: Optional[StrictStr] = Field(default=None, description=r"*the [XPath](https://en.wikipedia.org/wiki/XPath) of the element*")
    title: Optional[StrictStr] = Field(default=None, description=r"*title of the element*")
    url: Optional[StrictStr] = Field(default=None, description=r"*search URL with refinement parameters*")
    rectangle: Optional[AiModeRectangleInfo] = Field(default=None, description=r"")
    domain: Optional[StrictStr] = Field(default=None, description=r"*domain in SERP*")
    cache_url: Optional[StrictStr] = Field(default=None, description=r"")
    related_search_url: Optional[StrictStr] = Field(default=None, description=r"")
    breadcrumb: Optional[StrictStr] = Field(default=None, description=r"")
    website_name: Optional[StrictStr] = Field(default=None, description=r"name of the website in SERP")
    is_image: Optional[StrictBool] = Field(default=None, description=r"")
    is_video: Optional[StrictBool] = Field(default=None, description=r"")
    is_featured_snippet: Optional[StrictBool] = Field(default=None, description=r"")
    is_malicious: Optional[StrictBool] = Field(default=None, description=r"")
    is_web_story: Optional[StrictBool] = Field(default=None, description=r"")
    checks: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"")
    description: Optional[StrictStr] = Field(default=None, description=r"")
    pre_snippet: Optional[StrictStr] = Field(default=None, description=r"")
    extended_snippet: Optional[StrictStr] = Field(default=None, description=r"")
    images: Optional[List[Optional[AiModeImagesElementInfo]]] = Field(default=None, description=r"")
    amp_version: Optional[StrictBool] = Field(default=None, description=r"")
    rating: Optional[RatingInfo] = Field(default=None, description=r"")
    price: Optional[PriceInfo] = Field(default=None, description=r"")
    highlighted: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"")
    links: Optional[List[Optional[LinkElement]]] = Field(default=None, description=r"")
    faq: Optional[FaqBox] = Field(default=None, description=r"", deprecated=True)
    extended_people_also_search: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"")
    about_this_result: Optional[AboutThisResultElement] = Field(default=None, description=r"", deprecated=True)
    related_result: Optional[List[Optional[RelatedResult]]] = Field(default=None, description=r"")
    timestamp: Optional[StrictStr] = Field(default=None, description=r"")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "page", 
        "position", 
        "xpath", 
        "title", 
        "url", 
        "rectangle", 
        "domain", 
        "cache_url", 
        "related_search_url", 
        "breadcrumb", 
        "website_name", 
        "is_image", 
        "is_video", 
        "is_featured_snippet", 
        "is_malicious", 
        "is_web_story", 
        "checks", 
        "description", 
        "pre_snippet", 
        "extended_snippet", 
        "images", 
        "amp_version", 
        "rating", 
        "price", 
        "highlighted", 
        "links", 
        "faq", 
        "extended_people_also_search", 
        "about_this_result", 
        "related_result", 
        "timestamp", 
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
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['page'] = self.page
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['rectangle'] = self.rectangle.to_dict() if self.rectangle else None
        _dict['domain'] = self.domain
        _dict['cache_url'] = self.cache_url
        _dict['related_search_url'] = self.related_search_url
        _dict['breadcrumb'] = self.breadcrumb
        _dict['website_name'] = self.website_name
        _dict['is_image'] = self.is_image
        _dict['is_video'] = self.is_video
        _dict['is_featured_snippet'] = self.is_featured_snippet
        _dict['is_malicious'] = self.is_malicious
        _dict['is_web_story'] = self.is_web_story
        _dict['checks'] = self.checks
        _dict['description'] = self.description
        _dict['pre_snippet'] = self.pre_snippet
        _dict['extended_snippet'] = self.extended_snippet
        images_items = []
        if self.images:
            for _item in self.images:
                if _item:
                    images_items.append(_item.to_dict())
            _dict['images'] = images_items
        _dict['amp_version'] = self.amp_version
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['price'] = self.price.to_dict() if self.price else None
        _dict['highlighted'] = self.highlighted
        links_items = []
        if self.links:
            for _item in self.links:
                if _item:
                    links_items.append(_item.to_dict())
            _dict['links'] = links_items
        _dict['faq'] = self.faq.to_dict() if self.faq else None
        _dict['extended_people_also_search'] = self.extended_people_also_search
        _dict['about_this_result'] = self.about_this_result.to_dict() if self.about_this_result else None
        related_result_items = []
        if self.related_result:
            for _item in self.related_result:
                if _item:
                    related_result_items.append(_item.to_dict())
            _dict['related_result'] = related_result_items
        _dict['timestamp'] = self.timestamp
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "page": obj.get("page"),
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "rectangle": AiModeRectangleInfo.from_dict(obj["rectangle"]) if obj.get("rectangle") is not None else None,
            "domain": obj.get("domain"),
            "cache_url": obj.get("cache_url"),
            "related_search_url": obj.get("related_search_url"),
            "breadcrumb": obj.get("breadcrumb"),
            "website_name": obj.get("website_name"),
            "is_image": obj.get("is_image"),
            "is_video": obj.get("is_video"),
            "is_featured_snippet": obj.get("is_featured_snippet"),
            "is_malicious": obj.get("is_malicious"),
            "is_web_story": obj.get("is_web_story"),
            "checks": obj.get("checks"),
            "description": obj.get("description"),
            "pre_snippet": obj.get("pre_snippet"),
            "extended_snippet": obj.get("extended_snippet"),
            "images": [AiModeImagesElementInfo.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "amp_version": obj.get("amp_version"),
            "rating": RatingInfo.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "highlighted": obj.get("highlighted"),
            "links": [LinkElement.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "faq": FaqBox.from_dict(obj["faq"]) if obj.get("faq") is not None else None,
            "extended_people_also_search": obj.get("extended_people_also_search"),
            "about_this_result": AboutThisResultElement.from_dict(obj["about_this_result"]) if obj.get("about_this_result") is not None else None,
            "related_result": [RelatedResult.from_dict(_item) for _item in obj["related_result"]] if obj.get("related_result") is not None else None,
            "timestamp": obj.get("timestamp"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj