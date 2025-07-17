from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_merchant_google_shopping_products_element_item import BaseMerchantGoogleShoppingProductsElementItem



class GoogleShoppingPaidElementItem(BaseMerchantGoogleShoppingProductsElementItem):
    """
    GoogleShoppingPaidElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements found in Google Shopping SERP")
    position: Optional[StrictStr] = Field(default=None, description="alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="XPath of the element")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    title: Optional[StrictStr] = Field(default=None, description="product title")
    description: Optional[StrictStr] = Field(default=None, description="description of the product in Google Shopping SERP")
    url: Optional[StrictStr] = Field(default=None, description="URL to the product page on the seller’s website")
    shop_ad_aclk: Optional[StrictStr] = Field(default=None, description="unique ad click referral parameter. using this parameter you can get a URL of the advertisement in Google Shopping Sellers Ad URL")
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
        "shop_ad_aclk", 
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
        _dict['shop_ad_aclk'] = self.shop_ad_aclk
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
            "shop_ad_aclk": obj.get("shop_ad_aclk"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj