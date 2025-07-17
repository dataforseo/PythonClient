from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_serp_days_rates_data_info import AppendixSerpDaysRatesDataInfo
from dataforseo_client.models.appendix_business_listings_business_data_limits_rates_data_info import AppendixBusinessListingsBusinessDataLimitsRatesDataInfo



class AppendixAppDataLimitsRatesDataInfo(BaseModel):
    """
    AppendixAppDataLimitsRatesDataInfo
    """ # noqa: E501
    app_info: Optional[AppendixSerpDaysRatesDataInfo] = Field(default=None, description="")
    app_list: Optional[AppendixSerpDaysRatesDataInfo] = Field(default=None, description="")
    app_reviews: Optional[AppendixSerpDaysRatesDataInfo] = Field(default=None, description="")
    app_searches: Optional[AppendixSerpDaysRatesDataInfo] = Field(default=None, description="")
    errors: Optional[StrictFloat] = Field(default=None, description="")
    languages: Optional[StrictFloat] = Field(default=None, description="")
    locations: Optional[StrictFloat] = Field(default=None, description="")
    categories: Optional[StrictFloat] = Field(default=None, description="")
    app_listings: Optional[AppendixBusinessListingsBusinessDataLimitsRatesDataInfo] = Field(default=None, description="")
    tasks_ready: Optional[StrictFloat] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "app_info", 
        "app_list", 
        "app_reviews", 
        "app_searches", 
        "errors", 
        "languages", 
        "locations", 
        "categories", 
        "app_listings", 
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
        _dict['app_list'] = self.app_list.to_dict() if self.app_list else None
        _dict['app_reviews'] = self.app_reviews.to_dict() if self.app_reviews else None
        _dict['app_searches'] = self.app_searches.to_dict() if self.app_searches else None
        _dict['errors'] = self.errors
        _dict['languages'] = self.languages
        _dict['locations'] = self.locations
        _dict['categories'] = self.categories
        _dict['app_listings'] = self.app_listings.to_dict() if self.app_listings else None
        _dict['tasks_ready'] = self.tasks_ready
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app_info": AppendixSerpDaysRatesDataInfo.from_dict(obj["app_info"]) if obj.get("app_info") is not None else None,
            "app_list": AppendixSerpDaysRatesDataInfo.from_dict(obj["app_list"]) if obj.get("app_list") is not None else None,
            "app_reviews": AppendixSerpDaysRatesDataInfo.from_dict(obj["app_reviews"]) if obj.get("app_reviews") is not None else None,
            "app_searches": AppendixSerpDaysRatesDataInfo.from_dict(obj["app_searches"]) if obj.get("app_searches") is not None else None,
            "errors": obj.get("errors"),
            "languages": obj.get("languages"),
            "locations": obj.get("locations"),
            "categories": obj.get("categories"),
            "app_listings": AppendixBusinessListingsBusinessDataLimitsRatesDataInfo.from_dict(obj["app_listings"]) if obj.get("app_listings") is not None else None,
            "tasks_ready": obj.get("tasks_ready"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj