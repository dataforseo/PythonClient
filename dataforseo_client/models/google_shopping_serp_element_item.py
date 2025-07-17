from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.delivery_info import DeliveryInfo
from dataforseo_client.models.stores_count_info import StoresCountInfo
from dataforseo_client.models.base_merchant_google_shopping_products_element_item import BaseMerchantGoogleShoppingProductsElementItem



class GoogleShoppingSerpElementItem(BaseMerchantGoogleShoppingProductsElementItem):
    """
    GoogleShoppingSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements found in Google Shopping SERP")
    position: Optional[StrictStr] = Field(default=None, description="alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="XPath of the element")
    domain: Optional[StrictStr] = Field(default=None, description="domain of the URL. domain of the URL where a special offer is posted")
    title: Optional[StrictStr] = Field(default=None, description="title of the element")
    description: Optional[StrictStr] = Field(default=None, description="description of the product in Google Shopping SERP")
    url: Optional[StrictStr] = Field(default=None, description="URL pointing at special offer page. URL where a special offer is posted")
    shopping_url: Optional[StrictStr] = Field(default=None, description="URL to the product page on Google Shopping")
    tags: Optional[List[Optional[StrictStr]]] = Field(default=None, description="tags assigned to the product")
    price: Optional[StrictFloat] = Field(default=None, description="product price. example:. 384.99")
    price_multiplier: Optional[StrictInt] = Field(default=None, description="price multiplier for instalment plan. indicates the number of months covered by the monthly payment for the product")
    old_price: Optional[StrictFloat] = Field(default=None, description="product old price. displayed if the product price has been changed. example:. 499")
    currency: Optional[StrictStr] = Field(default=None, description="currency in the ISO format. example:. USD")
    product_id: Optional[StrictStr] = Field(default=None, description="unique product identifier on Google Shopping. note that there is no full list of possible values as the product_id is a dynamic value assigned by Google. if there are no values, you will get null. example:. 4485466949985702538. learn more about the parameter in this help center guide")
    data_docid: Optional[StrictStr] = Field(default=None, description="unique identifier of the SERP data element. note that there is no full list of possible values as the data_docid is a dynamic value assigned by Google. example:. 17363035694596624076")
    seller: Optional[StrictStr] = Field(default=None, description="name of the seller. the name of the company that placed a corresponding product on Google Shopping")
    additional_specifications: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="object containing additional url parameters. you can get more details about the product by using this object in the POST request to the Google Shopping Product Specification and Google Shopping Sellers endpoint")
    reviews_count: Optional[StrictInt] = Field(default=None, description="number of product reviews. indicates the number of reviews left by users on Google Shopping. if there are no values, you will get null")
    is_best_match: Optional[StrictBool] = Field(default=None, description="“best match” label. if the value is true, the product is marked with the “best match” label. if there are no values, you will get null")
    product_rating: Optional[RatingElement] = Field(default=None, description="product rating. the product popularity rate based on product reviews")
    shop_rating: Optional[RatingElement] = Field(default=None, description="shop rating. the popularity rate of the seller based on user reviews")
    product_images: Optional[List[Optional[StrictStr]]] = Field(default=None, description="URLs to the images of the product. the first URL in the array is the featured image of the product")
    shop_ad_aclk: Optional[StrictStr] = Field(default=None, description="unique ad click referral parameter. using this parameter you can get a URL of the advertisement in Google Shopping Sellers Ad URL")
    delivery_info: Optional[DeliveryInfo] = Field(default=None, description="delivery information. delivery information including free and fast delivery date ranges")
    stores_count_info: Optional[StoresCountInfo] = Field(default=None, description="stores count information. contains information about the number of stores that offer the same product")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "domain", 
        "title", 
        "description", 
        "url", 
        "shopping_url", 
        "tags", 
        "price", 
        "price_multiplier", 
        "old_price", 
        "currency", 
        "product_id", 
        "data_docid", 
        "seller", 
        "additional_specifications", 
        "reviews_count", 
        "is_best_match", 
        "product_rating", 
        "shop_rating", 
        "product_images", 
        "shop_ad_aclk", 
        "delivery_info", 
        "stores_count_info", 
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
        _dict['domain'] = self.domain
        _dict['title'] = self.title
        _dict['description'] = self.description
        _dict['url'] = self.url
        _dict['shopping_url'] = self.shopping_url
        _dict['tags'] = self.tags
        _dict['price'] = self.price
        _dict['price_multiplier'] = self.price_multiplier
        _dict['old_price'] = self.old_price
        _dict['currency'] = self.currency
        _dict['product_id'] = self.product_id
        _dict['data_docid'] = self.data_docid
        _dict['seller'] = self.seller
        _dict['additional_specifications'] = self.additional_specifications
        _dict['reviews_count'] = self.reviews_count
        _dict['is_best_match'] = self.is_best_match
        _dict['product_rating'] = self.product_rating.to_dict() if self.product_rating else None
        _dict['shop_rating'] = self.shop_rating.to_dict() if self.shop_rating else None
        _dict['product_images'] = self.product_images
        _dict['shop_ad_aclk'] = self.shop_ad_aclk
        _dict['delivery_info'] = self.delivery_info.to_dict() if self.delivery_info else None
        _dict['stores_count_info'] = self.stores_count_info.to_dict() if self.stores_count_info else None
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
            "domain": obj.get("domain"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "url": obj.get("url"),
            "shopping_url": obj.get("shopping_url"),
            "tags": obj.get("tags"),
            "price": obj.get("price"),
            "price_multiplier": obj.get("price_multiplier"),
            "old_price": obj.get("old_price"),
            "currency": obj.get("currency"),
            "product_id": obj.get("product_id"),
            "data_docid": obj.get("data_docid"),
            "seller": obj.get("seller"),
            "additional_specifications": obj.get("additional_specifications"),
            "reviews_count": obj.get("reviews_count"),
            "is_best_match": obj.get("is_best_match"),
            "product_rating": RatingElement.from_dict(obj["product_rating"]) if obj.get("product_rating") is not None else None,
            "shop_rating": RatingElement.from_dict(obj["shop_rating"]) if obj.get("shop_rating") is not None else None,
            "product_images": obj.get("product_images"),
            "shop_ad_aclk": obj.get("shop_ad_aclk"),
            "delivery_info": DeliveryInfo.from_dict(obj["delivery_info"]) if obj.get("delivery_info") is not None else None,
            "stores_count_info": StoresCountInfo.from_dict(obj["stores_count_info"]) if obj.get("stores_count_info") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj