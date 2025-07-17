from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.base_merchant_google_shopping_sellers_element_item import BaseMerchantGoogleShoppingSellersElementItem



class MerchantGoogleSellersTaskGetAdvancedResultInfo(BaseModel):
    """
    MerchantGoogleSellersTaskGetAdvancedResultInfo
    """ # noqa: E501
    product_id: Optional[StrictStr] = Field(default=None, description="product_id received in a POST array. learn more about the parameter in this help center guide")
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    se_domain: Optional[StrictStr] = Field(default=None, description="search engine domain in a POST array")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to Google Shopping results. you can use it to make sure that we provided accurate results")
    datetime: Optional[StrictStr] = Field(default=None, description="date and time when the result was received. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    title: Optional[StrictStr] = Field(default=None, description="title of the product")
    url: Optional[StrictStr] = Field(default=None, description="URL to the product page")
    image_url: Optional[StrictStr] = Field(default=None, description="URL to the product image")
    rating: Optional[RatingElement] = Field(default=None, description="product rating. the product popularity rate based on product reviews")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="types of search results found in Google Shopping SERP. contains types of all search results (items) found in the returned SERP. possible item types:. shops_list, buy_on_google")
    items_count: Optional[StrictInt] = Field(default=None, description="the number of results returned in the items array")
    items: Optional[List[Optional[BaseMerchantGoogleShoppingSellersElementItem]]] = Field(default=None, description="items in SERP")
    __properties: ClassVar[List[str]] = [
        "product_id", 
        "type", 
        "se_domain", 
        "location_code", 
        "language_code", 
        "check_url", 
        "datetime", 
        "title", 
        "url", 
        "image_url", 
        "rating", 
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

        _dict['product_id'] = self.product_id
        _dict['type'] = self.type
        _dict['se_domain'] = self.se_domain
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['check_url'] = self.check_url
        _dict['datetime'] = self.datetime
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['image_url'] = self.image_url
        _dict['rating'] = self.rating.to_dict() if self.rating else None
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
            "product_id": obj.get("product_id"),
            "type": obj.get("type"),
            "se_domain": obj.get("se_domain"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "check_url": obj.get("check_url"),
            "datetime": obj.get("datetime"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "image_url": obj.get("image_url"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "item_types": obj.get("item_types"),
            "items_count": obj.get("items_count"),
            "items": [BaseMerchantGoogleShoppingSellersElementItem.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj