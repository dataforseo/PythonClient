from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_business_listings_business_data_price_data import AppendixBusinessListingsBusinessDataPriceData
from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo
from dataforseo_client.models.appendix_google_business_data_price_data import AppendixGoogleBusinessDataPriceData
from dataforseo_client.models.appendix_social_media_business_data_price_data import AppendixSocialMediaBusinessDataPriceData
from dataforseo_client.models.appendix_tr_business_data_price_data_info import AppendixTrBusinessDataPriceDataInfo



class AppendixBusinessDataPriceData(BaseModel):
    """
    AppendixBusinessDataPriceData
    """ # noqa: E501
    business_listings: Optional[AppendixBusinessListingsBusinessDataPriceData] = Field(default=None, description="")
    errors: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    google: Optional[AppendixGoogleBusinessDataPriceData] = Field(default=None, description="")
    social_media: Optional[AppendixSocialMediaBusinessDataPriceData] = Field(default=None, description="")
    languages: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    locations: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    tripadvisor: Optional[AppendixTrBusinessDataPriceDataInfo] = Field(default=None, description="")
    trustpilot: Optional[AppendixTrBusinessDataPriceDataInfo] = Field(default=None, description="")
    yelp: Optional[AppendixTrBusinessDataPriceDataInfo] = Field(default=None, description="")
    tasks_ready: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "business_listings", 
        "errors", 
        "google", 
        "social_media", 
        "languages", 
        "locations", 
        "tripadvisor", 
        "trustpilot", 
        "yelp", 
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

        _dict['business_listings'] = self.business_listings.to_dict() if self.business_listings else None
        _dict['errors'] = self.errors.to_dict() if self.errors else None
        _dict['google'] = self.google.to_dict() if self.google else None
        _dict['social_media'] = self.social_media.to_dict() if self.social_media else None
        _dict['languages'] = self.languages.to_dict() if self.languages else None
        _dict['locations'] = self.locations.to_dict() if self.locations else None
        _dict['tripadvisor'] = self.tripadvisor.to_dict() if self.tripadvisor else None
        _dict['trustpilot'] = self.trustpilot.to_dict() if self.trustpilot else None
        _dict['yelp'] = self.yelp.to_dict() if self.yelp else None
        _dict['tasks_ready'] = self.tasks_ready.to_dict() if self.tasks_ready else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "business_listings": AppendixBusinessListingsBusinessDataPriceData.from_dict(obj["business_listings"]) if obj.get("business_listings") is not None else None,
            "errors": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["errors"]) if obj.get("errors") is not None else None,
            "google": AppendixGoogleBusinessDataPriceData.from_dict(obj["google"]) if obj.get("google") is not None else None,
            "social_media": AppendixSocialMediaBusinessDataPriceData.from_dict(obj["social_media"]) if obj.get("social_media") is not None else None,
            "languages": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["languages"]) if obj.get("languages") is not None else None,
            "locations": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["locations"]) if obj.get("locations") is not None else None,
            "tripadvisor": AppendixTrBusinessDataPriceDataInfo.from_dict(obj["tripadvisor"]) if obj.get("tripadvisor") is not None else None,
            "trustpilot": AppendixTrBusinessDataPriceDataInfo.from_dict(obj["trustpilot"]) if obj.get("trustpilot") is not None else None,
            "yelp": AppendixTrBusinessDataPriceDataInfo.from_dict(obj["yelp"]) if obj.get("yelp") is not None else None,
            "tasks_ready": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["tasks_ready"]) if obj.get("tasks_ready") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj