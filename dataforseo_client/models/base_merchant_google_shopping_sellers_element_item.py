from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement

from importlib import import_module
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dataforseo_client.models.google_shopping_sellers_shops_list_element_item import GoogleShoppingSellersShopsListElementItem;
    from dataforseo_client.models.google_shopping_sellers_buy_on_google_element_item import GoogleShoppingSellersBuyOnGoogleElementItem;



class BaseMerchantGoogleShoppingSellersElementItem(BaseModel):
    """
    BaseMerchantGoogleShoppingSellersElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements found in Google Shopping SERP")
    position: Optional[StrictStr] = Field(default=None, description="alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="XPath of the element")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    title: Optional[StrictStr] = Field(default=None, description="product title")
    url: Optional[StrictStr] = Field(default=None, description="Google Shopping URL forwarding to the product page on the seller’s website. if you want to obtain a URL of the advertisement forwarding to the product page on the seller’s website, please refer to the Google Shopping Sellers Ad URL endpoint")
    details: Optional[StrictStr] = Field(default=None, description="details and special offers. if there are no details, the value will be null")
    base_price: Optional[StrictFloat] = Field(default=None, description="product price without tax and shipping")
    tax: Optional[StrictFloat] = Field(default=None, description="the amount of tax. tax is specified as the actual amount of money, not as the percentage")
    shipping_price: Optional[StrictFloat] = Field(default=None, description="product shipping price")
    total_price: Optional[StrictFloat] = Field(default=None, description="product price including tax and shipping")
    currency: Optional[StrictStr] = Field(default=None, description="currency in the ISO format. example:. USD")
    seller_name: Optional[StrictStr] = Field(default=None, description="name of the seller. the name of the company that placed a corresponding product on Google Shopping")
    rating: Optional[RatingElement] = Field(default=None, description="shop rating. the shop popularity rate based on product reviews")
    shop_ad_aclk: Optional[StrictStr] = Field(default=None, description="unique ad click referral parameter. using this parameter you can get a URL of the advertisement in Google Shopping Sellers Ad URL")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "domain", 
        "title", 
        "url", 
        "details", 
        "base_price", 
        "tax", 
        "shipping_price", 
        "total_price", 
        "currency", 
        "seller_name", 
        "rating", 
        "shop_ad_aclk", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'shops_list': 'GoogleShoppingSellersShopsListElementItem',
        'buy_on_google': 'GoogleShoppingSellersBuyOnGoogleElementItem',
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
        _dict['domain'] = self.domain
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['details'] = self.details
        _dict['base_price'] = self.base_price
        _dict['tax'] = self.tax
        _dict['shipping_price'] = self.shipping_price
        _dict['total_price'] = self.total_price
        _dict['currency'] = self.currency
        _dict['seller_name'] = self.seller_name
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['shop_ad_aclk'] = self.shop_ad_aclk
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
        GoogleShoppingSellersShopsListElementItem, 
        GoogleShoppingSellersBuyOnGoogleElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'GoogleShoppingSellersShopsListElementItem':
            return import_module("dataforseo_client.models.google_shopping_sellers_shops_list_element_item").GoogleShoppingSellersShopsListElementItem.from_dict(obj)
        if object_type == 'GoogleShoppingSellersBuyOnGoogleElementItem':
            return import_module("dataforseo_client.models.google_shopping_sellers_buy_on_google_element_item").GoogleShoppingSellersBuyOnGoogleElementItem.from_dict(obj)

        return None