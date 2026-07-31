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
from dataforseo_client.models.about_this_result_element import AboutThisResultElement



class RelatedResult(BaseModel):
    """
    RelatedResult
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    page: Optional[StrictInt] = Field(default=None, description=r"search results page number. indicates the number of the SERP page on which the element is located")
    xpath: Optional[StrictStr] = Field(default=None, description=r"the XPath of the element")
    domain: Optional[StrictStr] = Field(default=None, description=r"website domain")
    title: Optional[StrictStr] = Field(default=None, description=r"title of a given link element")
    url: Optional[StrictStr] = Field(default=None, description=r"URL")
    cache_url: Optional[StrictStr] = Field(default=None, description=r"cached version of the page")
    related_search_url: Optional[StrictStr] = Field(default=None, description=r"URL to a similar search. URL to a new search for the same keyword(s) on related sites")
    breadcrumb: Optional[StrictStr] = Field(default=None, description=r"breadcrumb in SERP")
    website_name: Optional[StrictStr] = Field(default=None, description=r"name of the website in the ad element")
    is_image: Optional[StrictBool] = Field(default=None, description=r"indicates whether the element contains an image. Note: this check no longer appears in SERP")
    is_video: Optional[StrictBool] = Field(default=None, description=r"indicates whether the element contains a video. Note: this check no longer appears in SERP")
    checks: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"array of properties detected for the SERP element. lists the properties that are true for this element. each value in the array represents a detected property. example:. if is_image is present in the array, the element contains an image. possible values in the array:. is_image, is_video, is_featured_snippet, amp_version, is_malicious, is_web_story, is_highly_cited. equals null if none of the properties are detected for the element. learn more about the checks array in this Help Center article")
    description: Optional[StrictStr] = Field(default=None, description=r"description of the results element in SERP")
    pre_snippet: Optional[StrictStr] = Field(default=None, description=r"includes additional information appended before the result description in SERP")
    extended_snippet: Optional[StrictStr] = Field(default=None, description=r"includes additional information appended after the result description in SERP")
    images: Optional[List[Optional[AiModeImagesElementInfo]]] = Field(default=None, description=r"images of the component. if there are none, equals null")
    amp_version: Optional[StrictBool] = Field(default=None, description=r"Accelerated Mobile Pages. indicates whether an item has the Accelerated Mobile Page (AMP) version")
    rating: Optional[RatingInfo] = Field(default=None, description=r"the item’s rating . the popularity rate based on reviews and displayed in SERP;. if there is none, equals null")
    price: Optional[PriceInfo] = Field(default=None, description=r"price of booking a place for the specified dates of stay")
    highlighted: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"words highlighted in bold within the results description")
    about_this_result: Optional[AboutThisResultElement] = Field(default=None, description=r"contains information from the ‘About this result’ panel. Note: this object is deprecated and always returns null", deprecated=True)
    timestamp: Optional[StrictStr] = Field(default=None, description=r"date and time when the result was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    __properties: ClassVar[List[str]] = [
        "type", 
        "page", 
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
        "checks", 
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
        _dict['page'] = self.page
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
            "page": obj.get("page"),
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
            "checks": obj.get("checks"),
            "description": obj.get("description"),
            "pre_snippet": obj.get("pre_snippet"),
            "extended_snippet": obj.get("extended_snippet"),
            "images": [AiModeImagesElementInfo.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "amp_version": obj.get("amp_version"),
            "rating": RatingInfo.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "highlighted": obj.get("highlighted"),
            "about_this_result": AboutThisResultElement.from_dict(obj["about_this_result"]) if obj.get("about_this_result") is not None else None,
            "timestamp": obj.get("timestamp"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj