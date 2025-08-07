from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_mode_images_element_info import AiModeImagesElementInfo
from dataforseo_client.models.ad_link_element import AdLinkElement
from dataforseo_client.models.price_info import PriceInfo
from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.base_serp_api_element_item import BaseSerpApiElementItem
from dataforseo_client.models.ai_mode_rectangle_info import AiModeRectangleInfo



class PaidSerpElementItem(BaseSerpApiElementItem):
    """
    PaidSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    rectangle: Optional[AiModeRectangleInfo] = Field(default=None, description="rectangle parameters. contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP. equals null if calculate_rectangles in the POST request is not set to true")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements found in SERP. note values are returned in the ascending order, with values corresponding to advanced SERP features omitted from the results;. to get all items (including SERP features and rich snippets) with their positions, please refer to the Google Organiс Advanced SERP endpoint")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    title: Optional[StrictStr] = Field(default=None, description="title of the results element in SERP")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    url: Optional[StrictStr] = Field(default=None, description="relevant URL in SERP")
    breadcrumb: Optional[StrictStr] = Field(default=None, description="breadcrumb in SERP")
    website_name: Optional[StrictStr] = Field(default=None, description="name of the website in SERP")
    is_image: Optional[StrictBool] = Field(default=None, description="indicates whether the element contains an image")
    is_video: Optional[StrictBool] = Field(default=None, description="indicates whether the element contains a video")
    images: Optional[List[Optional[AiModeImagesElementInfo]]] = Field(default=None, description="images of the element. if there are none, equals null")
    highlighted: Optional[List[Optional[StrictStr]]] = Field(default=None, description="words highlighted in bold within the results description")
    extra: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="additional information about the result")
    description_rows: Optional[List[Optional[StrictStr]]] = Field(default=None, description="extended description. if there is none, equals null")
    links: Optional[List[Optional[AdLinkElement]]] = Field(default=None, description="sitelinks. the links shown below some of Google’s search results. if there are none, equals null")
    price: Optional[PriceInfo] = Field(default=None, description="pricing details. contains the pricing details of the product or service featured in the result")
    rating: Optional[RatingElement] = Field(default=None, description="the item’s rating . the popularity rate based on reviews and displayed in SERP")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "xpath", 
        "rectangle", 
        "rank_group", 
        "rank_absolute", 
        "domain", 
        "title", 
        "description", 
        "url", 
        "breadcrumb", 
        "website_name", 
        "is_image", 
        "is_video", 
        "images", 
        "highlighted", 
        "extra", 
        "description_rows", 
        "links", 
        "price", 
        "rating", 
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
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
        _dict['rectangle'] = self.rectangle.to_dict() if self.rectangle else None
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['domain'] = self.domain
        _dict['title'] = self.title
        _dict['description'] = self.description
        _dict['url'] = self.url
        _dict['breadcrumb'] = self.breadcrumb
        _dict['website_name'] = self.website_name
        _dict['is_image'] = self.is_image
        _dict['is_video'] = self.is_video
        images_items = []
        if self.images:
            for _item in self.images:
                if _item:
                    images_items.append(_item.to_dict())
            _dict['images'] = images_items
        _dict['highlighted'] = self.highlighted
        _dict['extra'] = self.extra
        _dict['description_rows'] = self.description_rows
        links_items = []
        if self.links:
            for _item in self.links:
                if _item:
                    links_items.append(_item.to_dict())
            _dict['links'] = links_items
        _dict['price'] = self.price.to_dict() if self.price else None
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "rectangle": AiModeRectangleInfo.from_dict(obj["rectangle"]) if obj.get("rectangle") is not None else None,
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "domain": obj.get("domain"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "url": obj.get("url"),
            "breadcrumb": obj.get("breadcrumb"),
            "website_name": obj.get("website_name"),
            "is_image": obj.get("is_image"),
            "is_video": obj.get("is_video"),
            "images": [AiModeImagesElementInfo.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "highlighted": obj.get("highlighted"),
            "extra": obj.get("extra"),
            "description_rows": obj.get("description_rows"),
            "links": [AdLinkElement.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj