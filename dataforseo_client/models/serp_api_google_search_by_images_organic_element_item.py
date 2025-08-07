from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_mode_images_element_info import AiModeImagesElementInfo
from dataforseo_client.models.rating_element import RatingElement
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
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    title: Optional[StrictStr] = Field(default=None, description="title of the element")
    url: Optional[StrictStr] = Field(default=None, description="search URL with refinement parameters")
    rectangle: Optional[AiModeRectangleInfo] = Field(default=None, description="rectangle parameters. contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP. equals null if calculate_rectangles in the POST request is not set to true")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    cache_url: Optional[StrictStr] = Field(default=None, description="cached version of the page")
    related_search_url: Optional[StrictStr] = Field(default=None, description="URL to a similar search. URL to a new search for the same keyword(s) on related sites")
    breadcrumb: Optional[StrictStr] = Field(default=None, description="breadcrumb in SERP")
    website_name: Optional[StrictStr] = Field(default=None, description="name of the website in SERP")
    is_image: Optional[StrictBool] = Field(default=None, description="indicates whether the element contains an image")
    is_video: Optional[StrictBool] = Field(default=None, description="indicates whether the element contains a video")
    is_featured_snippet: Optional[StrictBool] = Field(default=None, description="indicates whether the element is a featured_snippet")
    is_malicious: Optional[StrictBool] = Field(default=None, description="indicates whether the element is marked as malicious")
    is_web_story: Optional[StrictBool] = Field(default=None, description="indicates whether the element is marked as Google web story")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    pre_snippet: Optional[StrictStr] = Field(default=None, description="includes additional information appended before the result description in SERP")
    extended_snippet: Optional[StrictStr] = Field(default=None, description="includes additional information appended after the result description in SERP")
    images: Optional[List[Optional[AiModeImagesElementInfo]]] = Field(default=None, description="images of the element")
    amp_version: Optional[StrictBool] = Field(default=None, description="Accelerated Mobile Pages. indicates whether an item has the Accelerated Mobile Page (AMP) version")
    rating: Optional[RatingElement] = Field(default=None, description="the item’s rating . the popularity rate based on reviews and displayed in SERP")
    price: Optional[PriceInfo] = Field(default=None, description="pricing details. contains the pricing details of the product or service featured in the result")
    highlighted: Optional[List[Optional[StrictStr]]] = Field(default=None, description="words highlighted in bold within the results description")
    links: Optional[List[Optional[LinkElement]]] = Field(default=None, description="sitelinks. the links shown below some of Google’s search results. if there are none, equals null")
    faq: Optional[FaqBox] = Field(default=None, description="frequently asked questions. questions and answers extension shown below some of Google’s search results. if there are none, equals null")
    extended_people_also_search: Optional[List[Optional[StrictStr]]] = Field(default=None, description="extension of the organic element. extension of the organic result containing related search queries. Note: extension appears in SERP upon clicking on the result and then bouncing back to search results")
    about_this_result: Optional[AboutThisResultElement] = Field(default=None, description="contains information from the ‘About this result’ panel. ‘About this result’ panel provides additional context about why Google returned this result for the given query;. this feature appears after clicking on the three dots next to most results")
    related_result: Optional[List[Optional[RelatedResult]]] = Field(default=None, description="related result from the same domain. related result from the same domain appears as a part of the main result snippet;. you can derive the related_result snippets as 'type': 'organic' results by setting the group_organic_results parameter to false in the POST request")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the result was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
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
            "description": obj.get("description"),
            "pre_snippet": obj.get("pre_snippet"),
            "extended_snippet": obj.get("extended_snippet"),
            "images": [AiModeImagesElementInfo.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "amp_version": obj.get("amp_version"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
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