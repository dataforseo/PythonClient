from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_a_keywords_data_price_data_info import AppendixAKeywordsDataPriceDataInfo
from dataforseo_client.models.appendix_hotel_info_google_business_data_price_data import AppendixHotelInfoGoogleBusinessDataPriceData
from dataforseo_client.models.appendix_google_business_data_price_data_info import AppendixGoogleBusinessDataPriceDataInfo



class AppendixGoogleBusinessDataPriceData(BaseModel):
    """
    AppendixGoogleBusinessDataPriceData
    """ # noqa: E501
    extended_reviews: Optional[AppendixAKeywordsDataPriceDataInfo] = Field(default=None, description="")
    hotel_info: Optional[AppendixHotelInfoGoogleBusinessDataPriceData] = Field(default=None, description="")
    hotel_searches: Optional[AppendixGoogleBusinessDataPriceDataInfo] = Field(default=None, description="")
    my_business_info: Optional[AppendixGoogleBusinessDataPriceDataInfo] = Field(default=None, description="")
    my_business_updates: Optional[AppendixGoogleBusinessDataPriceDataInfo] = Field(default=None, description="")
    questions_and_answers: Optional[AppendixGoogleBusinessDataPriceDataInfo] = Field(default=None, description="")
    reviews: Optional[AppendixGoogleBusinessDataPriceDataInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "extended_reviews", 
        "hotel_info", 
        "hotel_searches", 
        "my_business_info", 
        "my_business_updates", 
        "questions_and_answers", 
        "reviews", 
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

        _dict['extended_reviews'] = self.extended_reviews.to_dict() if self.extended_reviews else None
        _dict['hotel_info'] = self.hotel_info.to_dict() if self.hotel_info else None
        _dict['hotel_searches'] = self.hotel_searches.to_dict() if self.hotel_searches else None
        _dict['my_business_info'] = self.my_business_info.to_dict() if self.my_business_info else None
        _dict['my_business_updates'] = self.my_business_updates.to_dict() if self.my_business_updates else None
        _dict['questions_and_answers'] = self.questions_and_answers.to_dict() if self.questions_and_answers else None
        _dict['reviews'] = self.reviews.to_dict() if self.reviews else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "extended_reviews": AppendixAKeywordsDataPriceDataInfo.from_dict(obj["extended_reviews"]) if obj.get("extended_reviews") is not None else None,
            "hotel_info": AppendixHotelInfoGoogleBusinessDataPriceData.from_dict(obj["hotel_info"]) if obj.get("hotel_info") is not None else None,
            "hotel_searches": AppendixGoogleBusinessDataPriceDataInfo.from_dict(obj["hotel_searches"]) if obj.get("hotel_searches") is not None else None,
            "my_business_info": AppendixGoogleBusinessDataPriceDataInfo.from_dict(obj["my_business_info"]) if obj.get("my_business_info") is not None else None,
            "my_business_updates": AppendixGoogleBusinessDataPriceDataInfo.from_dict(obj["my_business_updates"]) if obj.get("my_business_updates") is not None else None,
            "questions_and_answers": AppendixGoogleBusinessDataPriceDataInfo.from_dict(obj["questions_and_answers"]) if obj.get("questions_and_answers") is not None else None,
            "reviews": AppendixGoogleBusinessDataPriceDataInfo.from_dict(obj["reviews"]) if obj.get("reviews") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj