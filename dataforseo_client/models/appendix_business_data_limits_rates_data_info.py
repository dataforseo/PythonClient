from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_business_data_google_info import AppendixBusinessDataGoogleInfo
from dataforseo_client.models.appendix_business_data_day_limits_rates_data_info import AppendixBusinessDataDayLimitsRatesDataInfo
from dataforseo_client.models.appendix_social_media_business_data_limits_rates_data_info import AppendixSocialMediaBusinessDataLimitsRatesDataInfo
from dataforseo_client.models.appendix_business_listings_business_data_limits_rates_data_info import AppendixBusinessListingsBusinessDataLimitsRatesDataInfo



class AppendixBusinessDataLimitsRatesDataInfo(BaseModel):
    """
    AppendixBusinessDataLimitsRatesDataInfo
    """ # noqa: E501
    google: Optional[AppendixBusinessDataGoogleInfo] = Field(default=None, description="")
    locations: Optional[StrictFloat] = Field(default=None, description="")
    languages: Optional[StrictFloat] = Field(default=None, description="")
    errors: Optional[StrictFloat] = Field(default=None, description="")
    yelp: Optional[AppendixBusinessDataDayLimitsRatesDataInfo] = Field(default=None, description="")
    social_media: Optional[AppendixSocialMediaBusinessDataLimitsRatesDataInfo] = Field(default=None, description="")
    tripadvisor: Optional[AppendixBusinessDataDayLimitsRatesDataInfo] = Field(default=None, description="")
    trustpilot: Optional[AppendixBusinessDataDayLimitsRatesDataInfo] = Field(default=None, description="")
    business_listings: Optional[AppendixBusinessListingsBusinessDataLimitsRatesDataInfo] = Field(default=None, description="")
    tasks_ready: Optional[StrictFloat] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "google", 
        "locations", 
        "languages", 
        "errors", 
        "yelp", 
        "social_media", 
        "tripadvisor", 
        "trustpilot", 
        "business_listings", 
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
        _dict['locations'] = self.locations
        _dict['languages'] = self.languages
        _dict['errors'] = self.errors
        _dict['yelp'] = self.yelp.to_dict() if self.yelp else None
        _dict['social_media'] = self.social_media.to_dict() if self.social_media else None
        _dict['tripadvisor'] = self.tripadvisor.to_dict() if self.tripadvisor else None
        _dict['trustpilot'] = self.trustpilot.to_dict() if self.trustpilot else None
        _dict['business_listings'] = self.business_listings.to_dict() if self.business_listings else None
        _dict['tasks_ready'] = self.tasks_ready
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "google": AppendixBusinessDataGoogleInfo.from_dict(obj["google"]) if obj.get("google") is not None else None,
            "locations": obj.get("locations"),
            "languages": obj.get("languages"),
            "errors": obj.get("errors"),
            "yelp": AppendixBusinessDataDayLimitsRatesDataInfo.from_dict(obj["yelp"]) if obj.get("yelp") is not None else None,
            "social_media": AppendixSocialMediaBusinessDataLimitsRatesDataInfo.from_dict(obj["social_media"]) if obj.get("social_media") is not None else None,
            "tripadvisor": AppendixBusinessDataDayLimitsRatesDataInfo.from_dict(obj["tripadvisor"]) if obj.get("tripadvisor") is not None else None,
            "trustpilot": AppendixBusinessDataDayLimitsRatesDataInfo.from_dict(obj["trustpilot"]) if obj.get("trustpilot") is not None else None,
            "business_listings": AppendixBusinessListingsBusinessDataLimitsRatesDataInfo.from_dict(obj["business_listings"]) if obj.get("business_listings") is not None else None,
            "tasks_ready": obj.get("tasks_ready"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj