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

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.about_this_result_element import AboutThisResultElement
from dataforseo_client.models.base_serp_element_item import BaseSerpElementItem
from dataforseo_client.models.faq_box import FaqBox
from dataforseo_client.models.images_element import ImagesElement
from dataforseo_client.models.link_element import LinkElement
from dataforseo_client.models.price_info import PriceInfo
from dataforseo_client.models.rating_info import RatingInfo
from dataforseo_client.models.rectangle import Rectangle
from dataforseo_client.models.related_result import RelatedResult
from typing import Optional, Set
from typing_extensions import Self

class OrganicSerpElementItem(BaseSerpElementItem):
    """
    OrganicSerpElementItem
    """ # noqa: E501
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP can take the following values: left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    domain: Optional[StrictStr] = Field(default=None, description="website domain")
    title: Optional[StrictStr] = Field(default=None, description="title of the result in SERP")
    url: Optional[StrictStr] = Field(default=None, description="relevant URL in SERP")
    cache_url: Optional[StrictStr] = Field(default=None, description="cached version of the page")
    related_search_url: Optional[StrictStr] = Field(default=None, description="URL to a similar search URL to a new search for the same keyword(s) on related sites")
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
    images: Optional[List[ImagesElement]] = Field(default=None, description="images of the element")
    amp_version: Optional[StrictBool] = Field(default=None, description="Accelerated Mobile Pages indicates whether an item has the Accelerated Mobile Page (AMP) version")
    rating: Optional[RatingInfo] = None
    price: Optional[PriceInfo] = None
    highlighted: Optional[List[Optional[StrictStr]]] = Field(default=None, description="words highlighted in bold within the results description")
    links: Optional[List[LinkElement]] = Field(default=None, description="sitelinks the links shown below some of Google’s search results if there are none, equals null")
    faq: Optional[FaqBox] = None
    extended_people_also_search: Optional[List[Optional[StrictStr]]] = Field(default=None, description="extension of the organic element extension of the organic result containing related search queries Note: extension appears in SERP upon clicking on the result and then bouncing back to search results")
    about_this_result: Optional[AboutThisResultElement] = None
    related_result: Optional[List[RelatedResult]] = Field(default=None, description="related result from the same domain related result from the same domain appears as a part of the main result snippet; you can derive the related_result snippets as \"type\": \"organic\" results by setting the group_organic_results parameter to false in the POST request")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    rectangle: Optional[Rectangle] = None
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "position", "xpath", "domain", "title", "url", "cache_url", "related_search_url", "breadcrumb", "website_name", "is_image", "is_video", "is_featured_snippet", "is_malicious", "is_web_story", "description", "pre_snippet", "extended_snippet", "images", "amp_version", "rating", "price", "highlighted", "links", "faq", "extended_people_also_search", "about_this_result", "related_result", "timestamp", "rectangle"]

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
        """Create an instance of OrganicSerpElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of rating
        if self.rating:
            _dict['rating'] = self.rating.to_dict()
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of faq
        if self.faq:
            _dict['faq'] = self.faq.to_dict()
        # override the default output from pydantic by calling `to_dict()` of about_this_result
        if self.about_this_result:
            _dict['about_this_result'] = self.about_this_result.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in related_result (list)
        _items = []
        if self.related_result:
            for _item in self.related_result:
                if _item:
                    _items.append(_item.to_dict())
            _dict['related_result'] = _items
        # override the default output from pydantic by calling `to_dict()` of rectangle
        if self.rectangle:
            _dict['rectangle'] = self.rectangle.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if rank_group (nullable) is None
        # and model_fields_set contains the field
        if self.rank_group is None and "rank_group" in self.model_fields_set:
            _dict['rank_group'] = None

        # set to None if rank_absolute (nullable) is None
        # and model_fields_set contains the field
        if self.rank_absolute is None and "rank_absolute" in self.model_fields_set:
            _dict['rank_absolute'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if xpath (nullable) is None
        # and model_fields_set contains the field
        if self.xpath is None and "xpath" in self.model_fields_set:
            _dict['xpath'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if cache_url (nullable) is None
        # and model_fields_set contains the field
        if self.cache_url is None and "cache_url" in self.model_fields_set:
            _dict['cache_url'] = None

        # set to None if related_search_url (nullable) is None
        # and model_fields_set contains the field
        if self.related_search_url is None and "related_search_url" in self.model_fields_set:
            _dict['related_search_url'] = None

        # set to None if breadcrumb (nullable) is None
        # and model_fields_set contains the field
        if self.breadcrumb is None and "breadcrumb" in self.model_fields_set:
            _dict['breadcrumb'] = None

        # set to None if website_name (nullable) is None
        # and model_fields_set contains the field
        if self.website_name is None and "website_name" in self.model_fields_set:
            _dict['website_name'] = None

        # set to None if is_image (nullable) is None
        # and model_fields_set contains the field
        if self.is_image is None and "is_image" in self.model_fields_set:
            _dict['is_image'] = None

        # set to None if is_video (nullable) is None
        # and model_fields_set contains the field
        if self.is_video is None and "is_video" in self.model_fields_set:
            _dict['is_video'] = None

        # set to None if is_featured_snippet (nullable) is None
        # and model_fields_set contains the field
        if self.is_featured_snippet is None and "is_featured_snippet" in self.model_fields_set:
            _dict['is_featured_snippet'] = None

        # set to None if is_malicious (nullable) is None
        # and model_fields_set contains the field
        if self.is_malicious is None and "is_malicious" in self.model_fields_set:
            _dict['is_malicious'] = None

        # set to None if is_web_story (nullable) is None
        # and model_fields_set contains the field
        if self.is_web_story is None and "is_web_story" in self.model_fields_set:
            _dict['is_web_story'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if pre_snippet (nullable) is None
        # and model_fields_set contains the field
        if self.pre_snippet is None and "pre_snippet" in self.model_fields_set:
            _dict['pre_snippet'] = None

        # set to None if extended_snippet (nullable) is None
        # and model_fields_set contains the field
        if self.extended_snippet is None and "extended_snippet" in self.model_fields_set:
            _dict['extended_snippet'] = None

        # set to None if images (nullable) is None
        # and model_fields_set contains the field
        if self.images is None and "images" in self.model_fields_set:
            _dict['images'] = None

        # set to None if amp_version (nullable) is None
        # and model_fields_set contains the field
        if self.amp_version is None and "amp_version" in self.model_fields_set:
            _dict['amp_version'] = None

        # set to None if highlighted (nullable) is None
        # and model_fields_set contains the field
        if self.highlighted is None and "highlighted" in self.model_fields_set:
            _dict['highlighted'] = None

        # set to None if links (nullable) is None
        # and model_fields_set contains the field
        if self.links is None and "links" in self.model_fields_set:
            _dict['links'] = None

        # set to None if extended_people_also_search (nullable) is None
        # and model_fields_set contains the field
        if self.extended_people_also_search is None and "extended_people_also_search" in self.model_fields_set:
            _dict['extended_people_also_search'] = None

        # set to None if related_result (nullable) is None
        # and model_fields_set contains the field
        if self.related_result is None and "related_result" in self.model_fields_set:
            _dict['related_result'] = None

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrganicSerpElementItem from a dict"""
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
            "domain": obj.get("domain"),
            "title": obj.get("title"),
            "url": obj.get("url"),
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
            "images": [ImagesElement.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
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
            "rectangle": Rectangle.from_dict(obj["rectangle"]) if obj.get("rectangle") is not None else None
        })
        return _obj

