from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_merchant_google_info import AppendixMerchantGoogleInfo
from dataforseo_client.models.appendix_merchant_amazon_info import AppendixMerchantAmazonInfo
from dataforseo_client.models.appendix_serp_days_rates_data_info import AppendixSerpDaysRatesDataInfo



class AppendixMerchantLimitsRatesDataInfo(BaseModel):
    """
    AppendixMerchantLimitsRatesDataInfo
    """ # noqa: E501
    google: Optional[AppendixMerchantGoogleInfo] = Field(default=None, description="")
    amazon: Optional[AppendixMerchantAmazonInfo] = Field(default=None, description="")
    locations: Optional[StrictFloat] = Field(default=None, description="")
    languages: Optional[StrictFloat] = Field(default=None, description="")
    errors: Optional[StrictFloat] = Field(default=None, description="")
    reviews: Optional[AppendixSerpDaysRatesDataInfo] = Field(default=None, description="")
    tasks_ready: Optional[StrictFloat] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "google", 
        "amazon", 
        "locations", 
        "languages", 
        "errors", 
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
        _dict['locations'] = self.locations
        _dict['languages'] = self.languages
        _dict['errors'] = self.errors
        _dict['reviews'] = self.reviews.to_dict() if self.reviews else None
        _dict['tasks_ready'] = self.tasks_ready
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "google": AppendixMerchantGoogleInfo.from_dict(obj["google"]) if obj.get("google") is not None else None,
            "amazon": AppendixMerchantAmazonInfo.from_dict(obj["amazon"]) if obj.get("amazon") is not None else None,
            "locations": obj.get("locations"),
            "languages": obj.get("languages"),
            "errors": obj.get("errors"),
            "reviews": AppendixSerpDaysRatesDataInfo.from_dict(obj["reviews"]) if obj.get("reviews") is not None else None,
            "tasks_ready": obj.get("tasks_ready"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj