from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_product_google_merchant_price_data_info import AppendixProductGoogleMerchantPriceDataInfo



class AppendixAmazonMerchantPriceData(BaseModel):
    """
    AppendixAmazonMerchantPriceData
    """ # noqa: E501
    asin: Optional[AppendixProductGoogleMerchantPriceDataInfo] = Field(default=None, description="")
    products: Optional[AppendixProductGoogleMerchantPriceDataInfo] = Field(default=None, description="")
    sellers: Optional[AppendixProductGoogleMerchantPriceDataInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "asin", 
        "products", 
        "sellers", 
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

        _dict['asin'] = self.asin.to_dict() if self.asin else None
        _dict['products'] = self.products.to_dict() if self.products else None
        _dict['sellers'] = self.sellers.to_dict() if self.sellers else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "asin": AppendixProductGoogleMerchantPriceDataInfo.from_dict(obj["asin"]) if obj.get("asin") is not None else None,
            "products": AppendixProductGoogleMerchantPriceDataInfo.from_dict(obj["products"]) if obj.get("products") is not None else None,
            "sellers": AppendixProductGoogleMerchantPriceDataInfo.from_dict(obj["sellers"]) if obj.get("sellers") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj