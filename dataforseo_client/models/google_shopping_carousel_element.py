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
from dataforseo_client.models.special_offer_info import SpecialOfferInfo



class GoogleShoppingCarouselElement(BaseModel):
    """
    GoogleShoppingCarouselElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    xpath: Optional[StrictStr] = Field(default=None, description=r"XPath of the element")
    title: Optional[StrictStr] = Field(default=None, description=r"product title")
    tags: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"tags assigned to the product")
    seller: Optional[StrictStr] = Field(default=None, description=r"name of the seller. the name of the company that placed a corresponding product on Google Shopping")
    price: Optional[StrictFloat] = Field(default=None, description=r"product price. example:. 384.99")
    currency: Optional[StrictStr] = Field(default=None, description=r"currency in the ISO format. example:. USD")
    product_rating: Optional[RatingElement] = Field(default=None, description=r"product rating. the product popularity rate based on product reviews")
    product_images: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"URLs to the images of the product. the first URL in the array is the featured image of the product")
    shopping_url: Optional[StrictStr] = Field(default=None, description=r"URL to the product page on Google Shopping")
    product_id: Optional[StrictStr] = Field(default=None, description=r"unique product identifier on Google Shopping. note that there is no full list of possible values as the product_id is a dynamic value assigned by Google. if there are no values, you will get null. example:. 4485466949985702538. learn more about the parameter in this help center guide")
    data_docid: Optional[StrictStr] = Field(default=None, description=r"unique identifier of the SERP data element. note that there is no full list of possible values as the data_docid is a dynamic value assigned by Google. example:. 17363035694596624076")
    gid: Optional[StrictStr] = Field(default=None, description=r"global product identifier on Google Shopping. note that there is no full list of possible values as the gid is a dynamic value assigned by Google. if there are no values, you will get null. example:. 4702526954592161872. learn more about gid parameter in this help center guide")
    delivery_info: Optional[DeliveryInfo] = Field(default=None, description=r"delivery information. delivery information including free and fast delivery date ranges")
    special_offer_info: Optional[SpecialOfferInfo] = Field(default=None, description=r"special offer from the seller. information on the special offer from the seller, including discount and coupon info")
    __properties: ClassVar[List[str]] = [
        "type", 
        "xpath", 
        "title", 
        "tags", 
        "seller", 
        "price", 
        "currency", 
        "product_rating", 
        "product_images", 
        "shopping_url", 
        "product_id", 
        "data_docid", 
        "gid", 
        "delivery_info", 
        "special_offer_info", 
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
        _dict['xpath'] = self.xpath
        _dict['title'] = self.title
        _dict['tags'] = self.tags
        _dict['seller'] = self.seller
        _dict['price'] = self.price
        _dict['currency'] = self.currency
        _dict['product_rating'] = self.product_rating.to_dict() if self.product_rating else None
        _dict['product_images'] = self.product_images
        _dict['shopping_url'] = self.shopping_url
        _dict['product_id'] = self.product_id
        _dict['data_docid'] = self.data_docid
        _dict['gid'] = self.gid
        _dict['delivery_info'] = self.delivery_info.to_dict() if self.delivery_info else None
        _dict['special_offer_info'] = self.special_offer_info.to_dict() if self.special_offer_info else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "xpath": obj.get("xpath"),
            "title": obj.get("title"),
            "tags": obj.get("tags"),
            "seller": obj.get("seller"),
            "price": obj.get("price"),
            "currency": obj.get("currency"),
            "product_rating": RatingElement.from_dict(obj["product_rating"]) if obj.get("product_rating") is not None else None,
            "product_images": obj.get("product_images"),
            "shopping_url": obj.get("shopping_url"),
            "product_id": obj.get("product_id"),
            "data_docid": obj.get("data_docid"),
            "gid": obj.get("gid"),
            "delivery_info": DeliveryInfo.from_dict(obj["delivery_info"]) if obj.get("delivery_info") is not None else None,
            "special_offer_info": SpecialOfferInfo.from_dict(obj["special_offer_info"]) if obj.get("special_offer_info") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj