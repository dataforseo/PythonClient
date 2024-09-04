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

from pydantic import Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.ad_link_element import AdLinkElement
from dataforseo_client.models.base_serp_element_item import BaseSerpElementItem
from dataforseo_client.models.images_element import ImagesElement
from dataforseo_client.models.price_info import PriceInfo
from dataforseo_client.models.rectangle import Rectangle
from typing import Optional, Set
from typing_extensions import Self

class PaidSerpElementItem(BaseSerpElementItem):
    """
    PaidSerpElementItem
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description="title of the result in SERP")
    domain: Optional[StrictStr] = Field(default=None, description="website domain")
    breadcrumb: Optional[StrictStr] = Field(default=None, description="breadcrumb in SERP")
    is_image: Optional[StrictBool] = Field(default=None, description="indicates whether the element contains an image")
    is_video: Optional[StrictBool] = Field(default=None, description="indicates whether the element contains a video")
    images: Optional[List[ImagesElement]] = Field(default=None, description="images of the element")
    url: Optional[StrictStr] = Field(default=None, description="relevant URL in SERP")
    highlighted: Optional[List[Optional[StrictStr]]] = Field(default=None, description="words highlighted in bold within the results description")
    extra: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="additional information about the result")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    description_rows: Optional[List[Optional[StrictStr]]] = Field(default=None, description="extended description if there is none, equals null")
    links: Optional[List[AdLinkElement]] = Field(default=None, description="sitelinks the links shown below some of Google’s search results if there are none, equals null")
    price: Optional[PriceInfo] = None
    rectangle: Optional[Rectangle] = None
    website_name: Optional[StrictStr] = Field(default=None, description="website name in SERP")
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "position", "xpath", "title", "domain", "breadcrumb", "is_image", "is_video", "images", "url", "highlighted", "extra", "description", "description_rows", "links", "price", "rectangle", "website_name"]

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
        """Create an instance of PaidSerpElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of price
        if self.price:
            _dict['price'] = self.price.to_dict()
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

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if breadcrumb (nullable) is None
        # and model_fields_set contains the field
        if self.breadcrumb is None and "breadcrumb" in self.model_fields_set:
            _dict['breadcrumb'] = None

        # set to None if is_image (nullable) is None
        # and model_fields_set contains the field
        if self.is_image is None and "is_image" in self.model_fields_set:
            _dict['is_image'] = None

        # set to None if is_video (nullable) is None
        # and model_fields_set contains the field
        if self.is_video is None and "is_video" in self.model_fields_set:
            _dict['is_video'] = None

        # set to None if images (nullable) is None
        # and model_fields_set contains the field
        if self.images is None and "images" in self.model_fields_set:
            _dict['images'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if highlighted (nullable) is None
        # and model_fields_set contains the field
        if self.highlighted is None and "highlighted" in self.model_fields_set:
            _dict['highlighted'] = None

        # set to None if extra (nullable) is None
        # and model_fields_set contains the field
        if self.extra is None and "extra" in self.model_fields_set:
            _dict['extra'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if description_rows (nullable) is None
        # and model_fields_set contains the field
        if self.description_rows is None and "description_rows" in self.model_fields_set:
            _dict['description_rows'] = None

        # set to None if links (nullable) is None
        # and model_fields_set contains the field
        if self.links is None and "links" in self.model_fields_set:
            _dict['links'] = None

        # set to None if website_name (nullable) is None
        # and model_fields_set contains the field
        if self.website_name is None and "website_name" in self.model_fields_set:
            _dict['website_name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaidSerpElementItem from a dict"""
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
            "domain": obj.get("domain"),
            "breadcrumb": obj.get("breadcrumb"),
            "is_image": obj.get("is_image"),
            "is_video": obj.get("is_video"),
            "images": [ImagesElement.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "url": obj.get("url"),
            "highlighted": obj.get("highlighted"),
            "extra": obj.get("extra"),
            "description": obj.get("description"),
            "description_rows": obj.get("description_rows"),
            "links": [AdLinkElement.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "rectangle": Rectangle.from_dict(obj["rectangle"]) if obj.get("rectangle") is not None else None,
            "website_name": obj.get("website_name")
        })
        return _obj


