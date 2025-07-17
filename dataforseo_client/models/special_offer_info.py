from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SpecialOfferInfo(BaseModel):
    """
    SpecialOfferInfo
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description="product title")
    sub_title: Optional[StrictStr] = Field(default=None, description="subtitle of the special offer")
    fixed_discount: Optional[StrictFloat] = Field(default=None, description="amount of the fixed discount")
    fixed_discount_currency: Optional[StrictStr] = Field(default=None, description="currency of the fixed discount")
    percentage_discount: Optional[StrictFloat] = Field(default=None, description="percentage of the discount")
    coupon_code: Optional[StrictStr] = Field(default=None, description="code of coupon discount")
    coupon_info: Optional[StrictStr] = Field(default=None, description="information on coupon discount")
    url: Optional[StrictStr] = Field(default=None, description="URL to the product page on the seller’s website")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    __properties: ClassVar[List[str]] = [
        "title", 
        "sub_title", 
        "fixed_discount", 
        "fixed_discount_currency", 
        "percentage_discount", 
        "coupon_code", 
        "coupon_info", 
        "url", 
        "domain", 
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

        _dict['title'] = self.title
        _dict['sub_title'] = self.sub_title
        _dict['fixed_discount'] = self.fixed_discount
        _dict['fixed_discount_currency'] = self.fixed_discount_currency
        _dict['percentage_discount'] = self.percentage_discount
        _dict['coupon_code'] = self.coupon_code
        _dict['coupon_info'] = self.coupon_info
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "sub_title": obj.get("sub_title"),
            "fixed_discount": obj.get("fixed_discount"),
            "fixed_discount_currency": obj.get("fixed_discount_currency"),
            "percentage_discount": obj.get("percentage_discount"),
            "coupon_code": obj.get("coupon_code"),
            "coupon_info": obj.get("coupon_info"),
            "url": obj.get("url"),
            "domain": obj.get("domain"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj