from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_google_merchant_price_data import AppendixGoogleMerchantPriceData
from dataforseo_client.models.appendix_amazon_merchant_price_data import AppendixAmazonMerchantPriceData
from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo
from dataforseo_client.models.appendix_product_google_merchant_price_data_info import AppendixProductGoogleMerchantPriceDataInfo



class AppendixMerchantPriceData(BaseModel):
    """
    AppendixMerchantPriceData
    """ # noqa: E501
    google: Optional[AppendixGoogleMerchantPriceData] = Field(default=None, description="")
    amazon: Optional[AppendixAmazonMerchantPriceData] = Field(default=None, description="")
    errors: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    languages: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    locations: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    reviews: Optional[AppendixProductGoogleMerchantPriceDataInfo] = Field(default=None, description="")
    tasks_ready: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "google", 
        "amazon", 
        "errors", 
        "languages", 
        "locations", 
        "reviews", 
        "tasks_ready", 
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

        _dict['google'] = self.google.to_dict() if self.google else None
        _dict['amazon'] = self.amazon.to_dict() if self.amazon else None
        _dict['errors'] = self.errors.to_dict() if self.errors else None
        _dict['languages'] = self.languages.to_dict() if self.languages else None
        _dict['locations'] = self.locations.to_dict() if self.locations else None
        _dict['reviews'] = self.reviews.to_dict() if self.reviews else None
        _dict['tasks_ready'] = self.tasks_ready.to_dict() if self.tasks_ready else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "google": AppendixGoogleMerchantPriceData.from_dict(obj["google"]) if obj.get("google") is not None else None,
            "amazon": AppendixAmazonMerchantPriceData.from_dict(obj["amazon"]) if obj.get("amazon") is not None else None,
            "errors": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["errors"]) if obj.get("errors") is not None else None,
            "languages": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["languages"]) if obj.get("languages") is not None else None,
            "locations": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["locations"]) if obj.get("locations") is not None else None,
            "reviews": AppendixProductGoogleMerchantPriceDataInfo.from_dict(obj["reviews"]) if obj.get("reviews") is not None else None,
            "tasks_ready": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["tasks_ready"]) if obj.get("tasks_ready") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj