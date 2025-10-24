from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.shopping_specification import ShoppingSpecification
from dataforseo_client.models.product_seller import ProductSeller
from dataforseo_client.models.product_variation import ProductVariation



class ProductInfoElement(BaseModel):
    """
    ProductInfoElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description=r"position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description=r"absolute rank on the product specification page. absolute position among all the elements found on the product specification page")
    position: Optional[StrictStr] = Field(default=None, description=r"alignment of the element on the product specification page. can take the following values:. right, left")
    product_id: Optional[StrictStr] = Field(default=None, description=r"product_id received in a POST array. ilearn more about the parameter in this help center guide")
    title: Optional[StrictStr] = Field(default=None, description=r"title of the product")
    description: Optional[StrictStr] = Field(default=None, description=r"description of the product")
    url: Optional[StrictStr] = Field(default=None, description=r"product url. url of the product on Google Shopping")
    images: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"product images. contains urls to product images")
    features: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"product features. contains snippets with the description of product features")
    rating: Optional[RatingElement] = Field(default=None, description=r"product rating . the popularity rate based on reviews")
    seller_reviews_count: Optional[StrictInt] = Field(default=None, description=r"number of seller reviews. number of reviews on the product seller’s account")
    data_docid: Optional[StrictStr] = Field(default=None, description=r"unique identifier of the SERP data element. note that there is no full list of possible values as the data_docid is a dynamic value assigned by Google. example:. 17363035694596624076")
    gid: Optional[StrictStr] = Field(default=None, description=r"global product identifier on Google Shopping. note that there is no full list of possible values as the gid is a dynamic value assigned by Google. if there are no values, you will get null. example:. 4702526954592161872. learn more about gid in this help center guide")
    specifications: Optional[List[Optional[ShoppingSpecification]]] = Field(default=None, description=r"product specifications. contains all product attributes and related data listed on the product specification page")
    sellers: Optional[List[Optional[ProductSeller]]] = Field(default=None, description=r"sellers of the product. number of reviews on the product seller’s account")
    variations: Optional[List[Optional[ProductVariation]]] = Field(default=None, description=r"variations of the product. contains brief information about different product variations")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "product_id", 
        "title", 
        "description", 
        "url", 
        "images", 
        "features", 
        "rating", 
        "seller_reviews_count", 
        "data_docid", 
        "gid", 
        "specifications", 
        "sellers", 
        "variations", 
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
        _dict['product_id'] = self.product_id
        _dict['title'] = self.title
        _dict['description'] = self.description
        _dict['url'] = self.url
        _dict['images'] = self.images
        _dict['features'] = self.features
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['seller_reviews_count'] = self.seller_reviews_count
        _dict['data_docid'] = self.data_docid
        _dict['gid'] = self.gid
        specifications_items = []
        if self.specifications:
            for _item in self.specifications:
                if _item:
                    specifications_items.append(_item.to_dict())
            _dict['specifications'] = specifications_items
        sellers_items = []
        if self.sellers:
            for _item in self.sellers:
                if _item:
                    sellers_items.append(_item.to_dict())
            _dict['sellers'] = sellers_items
        variations_items = []
        if self.variations:
            for _item in self.variations:
                if _item:
                    variations_items.append(_item.to_dict())
            _dict['variations'] = variations_items
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
            "product_id": obj.get("product_id"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "url": obj.get("url"),
            "images": obj.get("images"),
            "features": obj.get("features"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "seller_reviews_count": obj.get("seller_reviews_count"),
            "data_docid": obj.get("data_docid"),
            "gid": obj.get("gid"),
            "specifications": [ShoppingSpecification.from_dict(_item) for _item in obj["specifications"]] if obj.get("specifications") is not None else None,
            "sellers": [ProductSeller.from_dict(_item) for _item in obj["sellers"]] if obj.get("sellers") is not None else None,
            "variations": [ProductVariation.from_dict(_item) for _item in obj["variations"]] if obj.get("variations") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj