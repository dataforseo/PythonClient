from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.spell_info import SpellInfo
from dataforseo_client.models.ai_mode_images_element_info import AiModeImagesElementInfo
from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.amazon_review_item import AmazonReviewItem



class MerchantAmazonReviewsTaskGetAdvancedResultInfo(BaseModel):
    """
    MerchantAmazonReviewsTaskGetAdvancedResultInfo
    """ # noqa: E501
    asin: Optional[StrictStr] = Field(default=None, description="asin received in a POST array")
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    se_domain: Optional[StrictStr] = Field(default=None, description="search engine domain in a POST array")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to search engine results. you can use it to make sure that we provided accurate results")
    datetime: Optional[StrictStr] = Field(default=None, description="date and time when the result was received. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    spell: Optional[SpellInfo] = Field(default=None, description="autocorrection of the search engine. if the search engine provided results for a keyword that was corrected, we will specify the keyword corrected by the search engine and the type of autocorrection")
    title: Optional[StrictStr] = Field(default=None, description="title of the product on Amazon. the title of the product for which the reviews are collected")
    image: Optional[AiModeImagesElementInfo] = Field(default=None, description="product image data")
    rating: Optional[RatingElement] = Field(default=None, description="rating of the product on Amazon. popularity rate based on reviews and displayed in SERP")
    reviews_count: Optional[StrictInt] = Field(default=None, description="the total number of reviews")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="type of search results in Amazon SERP. contains types of search results (items) found in Amazon SERP;. possible item types:. amazon_review_item")
    items_count: Optional[StrictInt] = Field(default=None, description="the number of reviews items in the results array. you can get more results by using the depth parameter when setting a task")
    items: Optional[List[Optional[AmazonReviewItem]]] = Field(default=None, description="found reviews. you can get more results by using the depth parameter when setting a task")
    __properties: ClassVar[List[str]] = [
        "asin", 
        "type", 
        "se_domain", 
        "location_code", 
        "language_code", 
        "check_url", 
        "datetime", 
        "spell", 
        "title", 
        "image", 
        "rating", 
        "reviews_count", 
        "item_types", 
        "items_count", 
        "items", 
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

        _dict['asin'] = self.asin
        _dict['type'] = self.type
        _dict['se_domain'] = self.se_domain
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['check_url'] = self.check_url
        _dict['datetime'] = self.datetime
        _dict['spell'] = self.spell.to_dict() if self.spell else None
        _dict['title'] = self.title
        _dict['image'] = self.image.to_dict() if self.image else None
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['reviews_count'] = self.reviews_count
        _dict['item_types'] = self.item_types
        _dict['items_count'] = self.items_count
        items_items = []
        if self.items:
            for _item in self.items:
                if _item:
                    items_items.append(_item.to_dict())
            _dict['items'] = items_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "asin": obj.get("asin"),
            "type": obj.get("type"),
            "se_domain": obj.get("se_domain"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "check_url": obj.get("check_url"),
            "datetime": obj.get("datetime"),
            "spell": SpellInfo.from_dict(obj["spell"]) if obj.get("spell") is not None else None,
            "title": obj.get("title"),
            "image": AiModeImagesElementInfo.from_dict(obj["image"]) if obj.get("image") is not None else None,
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "reviews_count": obj.get("reviews_count"),
            "item_types": obj.get("item_types"),
            "items_count": obj.get("items_count"),
            "items": [AmazonReviewItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj