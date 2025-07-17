from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.gps_coordinates_location_info import GpsCoordinatesLocationInfo
from dataforseo_client.models.hotel_review_info import HotelReviewInfo
from dataforseo_client.models.hotel_price_info import HotelPriceInfo



class BusinessDataGoogleHotelSearchesItem(BaseModel):
    """
    BusinessDataGoogleHotelSearchesItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    hotel_identifier: Optional[StrictStr] = Field(default=None, description="unique identifier of a hotel entity in Google search. example:. CgoI-KWyzenM_MV3EAE")
    title: Optional[StrictStr] = Field(default=None, description="title of the hotel")
    stars: Optional[StrictInt] = Field(default=None, description="hotel class rating. class rating that ranges between 1-5 stars")
    is_paid: Optional[StrictBool] = Field(default=None, description="indicates a paid hotel listing. if true, related hotel_search_item is a paid ad. if false, related hotel_search_item is an organic hotel listing")
    location: Optional[GpsCoordinatesLocationInfo] = Field(default=None, description="GPS coordinates of the hotel’s location")
    reviews: Optional[HotelReviewInfo] = Field(default=None, description="hotel reviews and rating information")
    overview_images: Optional[List[Optional[StrictStr]]] = Field(default=None, description="featured images for a hotel")
    prices: Optional[HotelPriceInfo] = Field(default=None, description="hotel price")
    __properties: ClassVar[List[str]] = [
        "type", 
        "hotel_identifier", 
        "title", 
        "stars", 
        "is_paid", 
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

        _dict['type'] = self.type
        _dict['hotel_identifier'] = self.hotel_identifier
        _dict['title'] = self.title
        _dict['stars'] = self.stars
        _dict['is_paid'] = self.is_paid
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
            "type": obj.get("type"),
            "hotel_identifier": obj.get("hotel_identifier"),
            "title": obj.get("title"),
            "stars": obj.get("stars"),
            "is_paid": obj.get("is_paid"),
            "location": GpsCoordinatesLocationInfo.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "reviews": HotelReviewInfo.from_dict(obj["reviews"]) if obj.get("reviews") is not None else None,
            "overview_images": obj.get("overview_images"),
            "prices": HotelPriceInfo.from_dict(obj["prices"]) if obj.get("prices") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj