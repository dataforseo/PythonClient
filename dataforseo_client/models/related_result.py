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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.about_this_result_element import AboutThisResultElement
from dataforseo_client.models.images_element import ImagesElement
from dataforseo_client.models.price_info import PriceInfo
from dataforseo_client.models.rating_info import RatingInfo
from typing import Optional, Set
from typing_extensions import Self

class RelatedResult(BaseModel):
    """
    RelatedResult
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    domain: Optional[StrictStr] = Field(default=None, description="domain where a link points")
    title: Optional[StrictStr] = Field(default=None, description="title of a given link element")
    url: Optional[StrictStr] = Field(default=None, description="reference page URL")
    cache_url: Optional[StrictStr] = Field(default=None, description="cached version of the page")
    related_search_url: Optional[StrictStr] = Field(default=None, description="URL to a similar search URL to a new search for the same keyword(s) on related sites")
    breadcrumb: Optional[StrictStr] = Field(default=None, description="breadcrumb in SERP")
    website_name: Optional[StrictStr] = Field(default=None, description="name of the website in SERP")
    is_image: Optional[StrictBool] = Field(default=None, description="indicates whether the element contains an image")
    is_video: Optional[StrictBool] = Field(default=None, description="indicates whether the element contains a video")
    description: Optional[StrictStr] = Field(default=None, description="description of the hotel booking element")
    pre_snippet: Optional[StrictStr] = Field(default=None, description="includes additional information appended before the result description in SERP")
    extended_snippet: Optional[StrictStr] = Field(default=None, description="includes additional information appended after the result description in SERP")
    images: Optional[List[ImagesElement]] = Field(default=None, description="images of the element")
    amp_version: Optional[StrictBool] = Field(default=None, description="Accelerated Mobile Pages indicates whether an item has the Accelerated Mobile Page (AMP) version")
    rating: Optional[RatingInfo] = None
    price: Optional[PriceInfo] = None
    highlighted: Optional[List[Optional[StrictStr]]] = Field(default=None, description="words highlighted in bold within the results description")
    about_this_result: Optional[AboutThisResultElement] = None
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the result was published in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2019-11-15 12:57:46 +00:00")
    __properties: ClassVar[List[str]] = ["type", "xpath", "domain", "title", "url", "cache_url", "related_search_url", "breadcrumb", "website_name", "is_image", "is_video", "description", "pre_snippet", "extended_snippet", "images", "amp_version", "rating", "price", "highlighted", "about_this_result", "timestamp"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of RelatedResult from a JSON string"""
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
            for _item_images in self.images:
                if _item_images:
                    _items.append(_item_images.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of rating
        if self.rating:
            _dict['rating'] = self.rating.to_dict()
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
        # override the default output from pydantic by calling `to_dict()` of about_this_result
        if self.about_this_result:
            _dict['about_this_result'] = self.about_this_result.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

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

        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RelatedResult from a dict"""
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
            "images": [ImagesElement.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "amp_version": obj.get("amp_version"),
            "rating": RatingInfo.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "highlighted": obj.get("highlighted"),
            "about_this_result": AboutThisResultElement.from_dict(obj["about_this_result"]) if obj.get("about_this_result") is not None else None,
            "timestamp": obj.get("timestamp")
        })
        return _obj


