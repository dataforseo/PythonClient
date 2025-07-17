from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.price_info import PriceInfo
from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.amazon_delivery_info import AmazonDeliveryInfo

from importlib import import_module
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dataforseo_client.models.merchant_amazon_seller_main_item_serp_element_item import MerchantAmazonSellerMainItemSerpElementItem;
    from dataforseo_client.models.merchant_amazon_seller_item_serp_element_item import MerchantAmazonSellerItemSerpElementItem;



class BaseMerchantAmazonSellersElementItem(BaseModel):
    """
    BaseMerchantAmazonSellersElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements found in Amazon Sellers SERP")
    position: Optional[StrictStr] = Field(default=None, description="alignment of the element in SERP. possible values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="XPath of the element")
    seller_name: Optional[StrictStr] = Field(default=None, description="business name of the seller")
    seller_url: Optional[StrictStr] = Field(default=None, description="url forwarding to the seller’s page on Amazon")
    ships_from: Optional[StrictStr] = Field(default=None, description="sender company name")
    price: Optional[PriceInfo] = Field(default=None, description="product pricing details. if there are no details, the value will be null")
    rating: Optional[RatingElement] = Field(default=None, description="seller rating details. seller popularity rate based on customer reviews")
    condition: Optional[StrictStr] = Field(default=None, description="product condition. condition of the product offered by the seller")
    condition_description: Optional[StrictStr] = Field(default=None, description="product condition details. expanded details on the condition of the product offered by the seller")
    delivery_info: Optional[AmazonDeliveryInfo] = Field(default=None, description="delivery information. delivery information including free and fast delivery date ranges")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "seller_name", 
        "seller_url", 
        "ships_from", 
        "price", 
        "rating", 
        "condition", 
        "condition_description", 
        "delivery_info", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'amazon_seller_main_item': 'MerchantAmazonSellerMainItemSerpElementItem',
        'amazon_seller_item': 'MerchantAmazonSellerItemSerpElementItem',
    }

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
        _dict['seller_name'] = self.seller_name
        _dict['seller_url'] = self.seller_url
        _dict['ships_from'] = self.ships_from
        _dict['price'] = self.price.to_dict() if self.price else None
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['condition'] = self.condition
        _dict['condition_description'] = self.condition_description
        _dict['delivery_info'] = self.delivery_info.to_dict() if self.delivery_info else None
        return _dict


    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None
    
    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[
        MerchantAmazonSellerMainItemSerpElementItem, 
        MerchantAmazonSellerItemSerpElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'MerchantAmazonSellerMainItemSerpElementItem':
            return import_module("dataforseo_client.models.merchant_amazon_seller_main_item_serp_element_item").MerchantAmazonSellerMainItemSerpElementItem.from_dict(obj)
        if object_type == 'MerchantAmazonSellerItemSerpElementItem':
            return import_module("dataforseo_client.models.merchant_amazon_seller_item_serp_element_item").MerchantAmazonSellerItemSerpElementItem.from_dict(obj)

        raise ValueError("BaseSerpElementItem failed to lookup discriminator value from " +
                         json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                         ", mapping: " + json.dumps(cls.__discriminator_value_class_map))