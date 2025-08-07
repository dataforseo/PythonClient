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
from dataforseo_client.models.about_this_result_element import AboutThisResultElement



class RelatedResult(BaseModel):
    """
    RelatedResult
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    domain: Optional[StrictStr] = Field(default=None, description="domain where a link points")
    title: Optional[StrictStr] = Field(default=None, description="title of the link")
    url: Optional[StrictStr] = Field(default=None, description="reference page URL")
    cache_url: Optional[StrictStr] = Field(default=None, description="cached version of the page")
    related_search_url: Optional[StrictStr] = Field(default=None, description="URL to a similar search. URL to a new search for the same keyword(s) on related sites")
    breadcrumb: Optional[StrictStr] = Field(default=None, description="breadcrumb in SERP")
    website_name: Optional[StrictStr] = Field(default=None, description="name of the website in the ad element")
    is_image: Optional[StrictBool] = Field(default=None, description="indicates whether the element contains an image")
    is_video: Optional[StrictBool] = Field(default=None, description="indicates whether the element contains a video")
    description: Optional[StrictStr] = Field(default=None, description="description of the hotel booking element")
    pre_snippet: Optional[StrictStr] = Field(default=None, description="includes additional information appended before the result description in SERP")
    extended_snippet: Optional[StrictStr] = Field(default=None, description="includes additional information appended after the result description in SERP")
    images: Optional[List[Optional[AiModeImagesElementInfo]]] = Field(default=None, description="images of the component. if there are none, equals null")
    amp_version: Optional[StrictBool] = Field(default=None, description="Accelerated Mobile Pages. indicates whether an item has the Accelerated Mobile Page (AMP) version")
    rating: Optional[RatingElement] = Field(default=None, description="the item’s rating . the popularity rate based on reviews and displayed in SERP")
    price: Optional[PriceInfo] = Field(default=None, description="price of booking a place for the specified dates of stay")
    highlighted: Optional[List[Optional[StrictStr]]] = Field(default=None, description="words highlighted in bold within the results description")
    about_this_result: Optional[AboutThisResultElement] = Field(default=None, description="contains information from the ‘About this result’ panel. ‘About this result’ panel provides additional context about why Google returned this result for the given query;. this feature appears after clicking on the three dots next to most results")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the video was published or indexed. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    __properties: ClassVar[List[str]] = [
        "type", 
        "xpath", 
        "domain", 
        "title", 
        "url", 
        "cache_url", 
        "related_search_url", 
        "breadcrumb", 
        "website_name", 
        "is_image", 
        "is_video", 
        "description", 
        "pre_snippet", 
        "extended_snippet", 
        "images", 
        "amp_version", 
        "rating", 
        "price", 
        "highlighted", 
        "about_this_result", 
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
        _dict['xpath'] = self.xpath
        _dict['domain'] = self.domain
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['cache_url'] = self.cache_url
        _dict['related_search_url'] = self.related_search_url
        _dict['breadcrumb'] = self.breadcrumb
        _dict['website_name'] = self.website_name
        _dict['is_image'] = self.is_image
        _dict['is_video'] = self.is_video
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
        _dict['about_this_result'] = self.about_this_result.to_dict() if self.about_this_result else None
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
            "xpath": obj.get("xpath"),
            "domain": obj.get("domain"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "cache_url": obj.get("cache_url"),
            "related_search_url": obj.get("related_search_url"),
            "breadcrumb": obj.get("breadcrumb"),
            "website_name": obj.get("website_name"),
            "is_image": obj.get("is_image"),
            "is_video": obj.get("is_video"),
            "description": obj.get("description"),
            "pre_snippet": obj.get("pre_snippet"),
            "extended_snippet": obj.get("extended_snippet"),
            "images": [AiModeImagesElementInfo.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "amp_version": obj.get("amp_version"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "highlighted": obj.get("highlighted"),
            "about_this_result": AboutThisResultElement.from_dict(obj["about_this_result"]) if obj.get("about_this_result") is not None else None,
            "timestamp": obj.get("timestamp"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj