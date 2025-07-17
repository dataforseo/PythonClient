from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.hotel_about_info import HotelAboutInfo
from dataforseo_client.models.hotel_location_info import HotelLocationInfo
from dataforseo_client.models.hotel_review_info import HotelReviewInfo
from dataforseo_client.models.hotel_price_info import HotelPriceInfo



class BusinessDataGoogleHotelInfoLiveAdvancedResultInfo(BaseModel):
    """
    BusinessDataGoogleHotelInfoLiveAdvancedResultInfo
    """ # noqa: E501
    hotel_identifier: Optional[StrictStr] = Field(default=None, description="identifier received in a POST array. this field will contain the hotel_identifier parameter specified when setting a task;. example:. CgoI-KWyzenM_MV3EAE")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to search engine results. you can use it to make sure that we provided accurate results")
    datetime: Optional[StrictStr] = Field(default=None, description="date and time when the result was received. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    title: Optional[StrictStr] = Field(default=None, description="hotel title. the title of the hotel entity for which the results are collected")
    stars: Optional[StrictInt] = Field(default=None, description="hotel class rating. class rating that ranges between 1-5 stars and displayed after review ratings in hotel summary")
    stars_description: Optional[StrictStr] = Field(default=None, description="hotel class rating. class rating that ranges between 1-5 stars and displayed after review ratings in the hotel summary")
    address: Optional[StrictStr] = Field(default=None, description="hotel address. physical address of the hotel")
    phone: Optional[StrictStr] = Field(default=None, description="hotel phone number. contact phone number of the hotel")
    about: Optional[HotelAboutInfo] = Field(default=None, description="information about the hotel")
    location: Optional[HotelLocationInfo] = Field(default=None, description="information about the hotel location. information about the location where the hotel is located")
    reviews: Optional[HotelReviewInfo] = Field(default=None, description="hotel reviews by criteria. information about reviews of the hotel entity")
    overview_images: Optional[List[Optional[StrictStr]]] = Field(default=None, description="images displayed in the hotel overview. array containing URLs to images displayed in the hotel overview")
    prices: Optional[HotelPriceInfo] = Field(default=None, description="pricing details of the hotel entity. contains information about the hotel’s prices")
    __properties: ClassVar[List[str]] = [
        "hotel_identifier", 
        "location_code", 
        "language_code", 
        "check_url", 
        "datetime", 
        "title", 
        "stars", 
        "stars_description", 
        "address", 
        "phone", 
        "about", 
        "location", 
        "reviews", 
        "overview_images", 
        "prices", 
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

        _dict['hotel_identifier'] = self.hotel_identifier
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['check_url'] = self.check_url
        _dict['datetime'] = self.datetime
        _dict['title'] = self.title
        _dict['stars'] = self.stars
        _dict['stars_description'] = self.stars_description
        _dict['address'] = self.address
        _dict['phone'] = self.phone
        _dict['about'] = self.about.to_dict() if self.about else None
        _dict['location'] = self.location.to_dict() if self.location else None
        _dict['reviews'] = self.reviews.to_dict() if self.reviews else None
        _dict['overview_images'] = self.overview_images
        _dict['prices'] = self.prices.to_dict() if self.prices else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hotel_identifier": obj.get("hotel_identifier"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "check_url": obj.get("check_url"),
            "datetime": obj.get("datetime"),
            "title": obj.get("title"),
            "stars": obj.get("stars"),
            "stars_description": obj.get("stars_description"),
            "address": obj.get("address"),
            "phone": obj.get("phone"),
            "about": HotelAboutInfo.from_dict(obj["about"]) if obj.get("about") is not None else None,
            "location": HotelLocationInfo.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "reviews": HotelReviewInfo.from_dict(obj["reviews"]) if obj.get("reviews") is not None else None,
            "overview_images": obj.get("overview_images"),
            "prices": HotelPriceInfo.from_dict(obj["prices"]) if obj.get("prices") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj