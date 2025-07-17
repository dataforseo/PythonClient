from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_product_google_merchant_price_data_info import AppendixProductGoogleMerchantPriceDataInfo
from dataforseo_client.models.appendix_app_listings_app_data_price_data import AppendixAppListingsAppDataPriceData
from dataforseo_client.models.appendix_price_data_info import AppendixPriceDataInfo
from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo



class AppendixAppDataPriceData(BaseModel):
    """
    AppendixAppDataPriceData
    """ # noqa: E501
    app_info: Optional[AppendixProductGoogleMerchantPriceDataInfo] = Field(default=None, description="")
    app_listings: Optional[AppendixAppListingsAppDataPriceData] = Field(default=None, description="")
    app_list: Optional[AppendixProductGoogleMerchantPriceDataInfo] = Field(default=None, description="")
    app_reviews: Optional[AppendixPriceDataInfo] = Field(default=None, description="")
    app_searches: Optional[AppendixProductGoogleMerchantPriceDataInfo] = Field(default=None, description="")
    categories: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    errors: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    languages: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    locations: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    tasks_ready: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "app_info", 
        "app_listings", 
        "app_list", 
        "app_reviews", 
        "app_searches", 
        "categories", 
        "errors", 
        "languages", 
        "locations", 
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

        _dict['app_info'] = self.app_info.to_dict() if self.app_info else None
        _dict['app_listings'] = self.app_listings.to_dict() if self.app_listings else None
        _dict['app_list'] = self.app_list.to_dict() if self.app_list else None
        _dict['app_reviews'] = self.app_reviews.to_dict() if self.app_reviews else None
        _dict['app_searches'] = self.app_searches.to_dict() if self.app_searches else None
        _dict['categories'] = self.categories.to_dict() if self.categories else None
        _dict['errors'] = self.errors.to_dict() if self.errors else None
        _dict['languages'] = self.languages.to_dict() if self.languages else None
        _dict['locations'] = self.locations.to_dict() if self.locations else None
        _dict['tasks_ready'] = self.tasks_ready.to_dict() if self.tasks_ready else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app_info": AppendixProductGoogleMerchantPriceDataInfo.from_dict(obj["app_info"]) if obj.get("app_info") is not None else None,
            "app_listings": AppendixAppListingsAppDataPriceData.from_dict(obj["app_listings"]) if obj.get("app_listings") is not None else None,
            "app_list": AppendixProductGoogleMerchantPriceDataInfo.from_dict(obj["app_list"]) if obj.get("app_list") is not None else None,
            "app_reviews": AppendixPriceDataInfo.from_dict(obj["app_reviews"]) if obj.get("app_reviews") is not None else None,
            "app_searches": AppendixProductGoogleMerchantPriceDataInfo.from_dict(obj["app_searches"]) if obj.get("app_searches") is not None else None,
            "categories": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["categories"]) if obj.get("categories") is not None else None,
            "errors": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["errors"]) if obj.get("errors") is not None else None,
            "languages": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["languages"]) if obj.get("languages") is not None else None,
            "locations": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["locations"]) if obj.get("locations") is not None else None,
            "tasks_ready": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["tasks_ready"]) if obj.get("tasks_ready") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj