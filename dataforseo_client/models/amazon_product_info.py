from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.amazon_applicable_vouchers_item import AmazonApplicableVouchersItem
from dataforseo_client.models.amazon_product_newer_model_info import AmazonProductNewerModelInfo
from dataforseo_client.models.product_category_info import ProductCategoryInfo
from dataforseo_client.models.base_merchant_amazon_product_information_element_item import BaseMerchantAmazonProductInformationElementItem
from dataforseo_client.models.amazon_review_item import AmazonReviewItem



class AmazonProductInfo(BaseModel):
    """
    AmazonProductInfo
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank. absolute position among all the elements in the response array")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in Amazon SERP. possible values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    title: Optional[StrictStr] = Field(default=None, description="product title")
    details: Optional[StrictStr] = Field(default=None, description="product specs and other details")
    image_url: Optional[StrictStr] = Field(default=None, description="the URL of the product image")
    author: Optional[StrictStr] = Field(default=None, description="product brand name")
    data_asin: Optional[StrictStr] = Field(default=None, description="ASIN of the product received in a POST array")
    parent_asin: Optional[StrictStr] = Field(default=None, description="parent ASIN of the product")
    product_asins: Optional[List[Optional[StrictStr]]] = Field(default=None, description="ASINs of all found product modifications")
    price_from: Optional[StrictFloat] = Field(default=None, description="the lower limit of the product price range. example:. 49.98")
    price_to: Optional[StrictFloat] = Field(default=None, description="the upper limit of the product price range. example:. 384.99")
    currency: Optional[StrictStr] = Field(default=None, description="currency in the ISO format. example:. USD")
    is_amazon_choice: Optional[StrictBool] = Field(default=None, description="“Amazon’s choice” label. if the value is true, the product is marked with the “Amazon’s choice” label")
    rating: Optional[RatingElement] = Field(default=None, description="product rating info")
    is_newer_model_available: Optional[StrictBool] = Field(default=None, description="indicates whether the newer model of the product is available")
    applicable_vouchers: Optional[List[Optional[AmazonApplicableVouchersItem]]] = Field(default=None, description="array of objects containing information about applicable vouchers")
    newer_model: Optional[AmazonProductNewerModelInfo] = Field(default=None, description="information about the newer model of the product")
    categories: Optional[List[Optional[ProductCategoryInfo]]] = Field(default=None, description="contains related product categories")
    product_information: Optional[List[Optional[BaseMerchantAmazonProductInformationElementItem]]] = Field(default=None, description="contains related product information")
    product_images_list: Optional[List[Optional[StrictStr]]] = Field(default=None, description="contains URLs for all images of the product displayed on the left side of the main image")
    product_videos_list: Optional[List[Optional[StrictStr]]] = Field(default=None, description="contains URLs for all videos of the product displayed on the right side of the main video")
    description: Optional[StrictStr] = Field(default=None, description="contains description of the product")
    is_available: Optional[StrictBool] = Field(default=None, description="indicates whether the product is available for ordering. if the value is true, the product can be ordered")
    top_local_reviews: Optional[List[Optional[AmazonReviewItem]]] = Field(default=None, description="array of objects with top reviews from target location. to obtain additional local reviews, you can specify the load_more_local_reviews parameter in Task POST")
    top_global_reviews: Optional[List[Optional[AmazonReviewItem]]] = Field(default=None, description="array of objects with top reviews from around the world")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "title", 
        "details", 
        "image_url", 
        "author", 
        "data_asin", 
        "parent_asin", 
        "product_asins", 
        "price_from", 
        "price_to", 
        "currency", 
        "is_amazon_choice", 
        "rating", 
        "is_newer_model_available", 
        "applicable_vouchers", 
        "newer_model", 
        "categories", 
        "product_information", 
        "product_images_list", 
        "product_videos_list", 
        "description", 
        "is_available", 
        "top_local_reviews", 
        "top_global_reviews", 
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
        _dict['details'] = self.details
        _dict['image_url'] = self.image_url
        _dict['author'] = self.author
        _dict['data_asin'] = self.data_asin
        _dict['parent_asin'] = self.parent_asin
        _dict['product_asins'] = self.product_asins
        _dict['price_from'] = self.price_from
        _dict['price_to'] = self.price_to
        _dict['currency'] = self.currency
        _dict['is_amazon_choice'] = self.is_amazon_choice
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['is_newer_model_available'] = self.is_newer_model_available
        applicable_vouchers_items = []
        if self.applicable_vouchers:
            for _item in self.applicable_vouchers:
                if _item:
                    applicable_vouchers_items.append(_item.to_dict())
            _dict['applicable_vouchers'] = applicable_vouchers_items
        _dict['newer_model'] = self.newer_model.to_dict() if self.newer_model else None
        categories_items = []
        if self.categories:
            for _item in self.categories:
                if _item:
                    categories_items.append(_item.to_dict())
            _dict['categories'] = categories_items
        product_information_items = []
        if self.product_information:
            for _item in self.product_information:
                if _item:
                    product_information_items.append(_item.to_dict())
            _dict['product_information'] = product_information_items
        _dict['product_images_list'] = self.product_images_list
        _dict['product_videos_list'] = self.product_videos_list
        _dict['description'] = self.description
        _dict['is_available'] = self.is_available
        top_local_reviews_items = []
        if self.top_local_reviews:
            for _item in self.top_local_reviews:
                if _item:
                    top_local_reviews_items.append(_item.to_dict())
            _dict['top_local_reviews'] = top_local_reviews_items
        top_global_reviews_items = []
        if self.top_global_reviews:
            for _item in self.top_global_reviews:
                if _item:
                    top_global_reviews_items.append(_item.to_dict())
            _dict['top_global_reviews'] = top_global_reviews_items
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
            "details": obj.get("details"),
            "image_url": obj.get("image_url"),
            "author": obj.get("author"),
            "data_asin": obj.get("data_asin"),
            "parent_asin": obj.get("parent_asin"),
            "product_asins": obj.get("product_asins"),
            "price_from": obj.get("price_from"),
            "price_to": obj.get("price_to"),
            "currency": obj.get("currency"),
            "is_amazon_choice": obj.get("is_amazon_choice"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "is_newer_model_available": obj.get("is_newer_model_available"),
            "applicable_vouchers": [AmazonApplicableVouchersItem.from_dict(_item) for _item in obj["applicable_vouchers"]] if obj.get("applicable_vouchers") is not None else None,
            "newer_model": AmazonProductNewerModelInfo.from_dict(obj["newer_model"]) if obj.get("newer_model") is not None else None,
            "categories": [ProductCategoryInfo.from_dict(_item) for _item in obj["categories"]] if obj.get("categories") is not None else None,
            "product_information": [BaseMerchantAmazonProductInformationElementItem.from_dict(_item) for _item in obj["product_information"]] if obj.get("product_information") is not None else None,
            "product_images_list": obj.get("product_images_list"),
            "product_videos_list": obj.get("product_videos_list"),
            "description": obj.get("description"),
            "is_available": obj.get("is_available"),
            "top_local_reviews": [AmazonReviewItem.from_dict(_item) for _item in obj["top_local_reviews"]] if obj.get("top_local_reviews") is not None else None,
            "top_global_reviews": [AmazonReviewItem.from_dict(_item) for _item in obj["top_global_reviews"]] if obj.get("top_global_reviews") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj