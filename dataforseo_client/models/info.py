from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class Info(BaseModel):
    """
    Info
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description=r"")
    description: Optional[StrictStr] = Field(default=None, description=r"")
    category: Optional[StrictStr] = Field(default=None, description=r"")
    category_ids: Optional[StrictStr] = Field(default=None, description=r"")
    additional_categories: Optional[StrictStr] = Field(default=None, description=r"")
    cid: Optional[StrictStr] = Field(default=None, description=r"")
    feature_id: Optional[StrictStr] = Field(default=None, description=r"")
    address: Optional[StrictStr] = Field(default=None, description=r"")
    address_info_borough: Optional[StrictStr] = Field(default=None, description=r"")
    address_info_address: Optional[StrictStr] = Field(default=None, description=r"")
    address_info_city: Optional[StrictStr] = Field(default=None, description=r"")
    address_info_zip: Optional[StrictStr] = Field(default=None, description=r"")
    address_info_region: Optional[StrictStr] = Field(default=None, description=r"")
    address_info_country_code: Optional[StrictStr] = Field(default=None, description=r"")
    place_id: Optional[StrictStr] = Field(default=None, description=r"")
    phone: Optional[StrictStr] = Field(default=None, description=r"")
    url: Optional[StrictStr] = Field(default=None, description=r"")
    domain: Optional[StrictStr] = Field(default=None, description=r"")
    logo: Optional[StrictStr] = Field(default=None, description=r"")
    main_image: Optional[StrictStr] = Field(default=None, description=r"")
    total_photos: Optional[StrictStr] = Field(default=None, description=r"")
    snippet: Optional[StrictStr] = Field(default=None, description=r"")
    latitude: Optional[StrictStr] = Field(default=None, description=r"")
    longitude: Optional[StrictStr] = Field(default=None, description=r"")
    is_claimed: Optional[StrictStr] = Field(default=None, description=r"")
    rating_rating_type: Optional[StrictStr] = Field(default=None, description=r"")
    rating_value: Optional[StrictStr] = Field(default=None, description=r"")
    rating_votes_count: Optional[StrictStr] = Field(default=None, description=r"")
    rating_rating_max: Optional[StrictInt] = Field(default=None, description=r"the maximum value for a rating_type")
    rating_distribution_1: Optional[StrictStr] = Field(default=None, description=r"")
    rating_distribution_2: Optional[StrictStr] = Field(default=None, description=r"")
    rating_distribution_3: Optional[StrictStr] = Field(default=None, description=r"")
    rating_distribution_4: Optional[StrictStr] = Field(default=None, description=r"")
    rating_distribution_5: Optional[StrictStr] = Field(default=None, description=r"")
    work_time_work_hours_current_status: Optional[StrictStr] = Field(default=None, description=r"")
    check_url: Optional[StrictStr] = Field(default=None, description=r"")
    last_updated_time: Optional[StrictStr] = Field(default=None, description=r"")
    price_level: Optional[StrictStr] = Field(default=None, description=r"")
    hotel_rating: Optional[StrictStr] = Field(default=None, description=r"")
    contact_info_type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    first_seen: Optional[StrictStr] = Field(default=None, description=r"")
    __properties: ClassVar[List[str]] = [
        "title", 
        "description", 
        "category", 
        "category_ids", 
        "additional_categories", 
        "cid", 
        "feature_id", 
        "address", 
        "address_info.borough", 
        "address_info.address", 
        "address_info.city", 
        "address_info.zip", 
        "address_info.region", 
        "address_info.country_code", 
        "place_id", 
        "phone", 
        "url", 
        "domain", 
        "logo", 
        "main_image", 
        "total_photos", 
        "snippet", 
        "latitude", 
        "longitude", 
        "is_claimed", 
        "rating.rating_type", 
        "rating.value", 
        "rating.votes_count", 
        "rating.rating_max", 
        "rating_distribution.1", 
        "rating_distribution.2", 
        "rating_distribution.3", 
        "rating_distribution.4", 
        "rating_distribution.5", 
        "work_time.work_hours.current_status", 
        "check_url", 
        "last_updated_time", 
        "price_level", 
        "hotel_rating", 
        "contact_info.type", 
        "first_seen", 
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

        _dict['title'] = self.title
        _dict['description'] = self.description
        _dict['category'] = self.category
        _dict['category_ids'] = self.category_ids
        _dict['additional_categories'] = self.additional_categories
        _dict['cid'] = self.cid
        _dict['feature_id'] = self.feature_id
        _dict['address'] = self.address
        _dict['address_info.borough'] = self.address_info_borough
        _dict['address_info.address'] = self.address_info_address
        _dict['address_info.city'] = self.address_info_city
        _dict['address_info.zip'] = self.address_info_zip
        _dict['address_info.region'] = self.address_info_region
        _dict['address_info.country_code'] = self.address_info_country_code
        _dict['place_id'] = self.place_id
        _dict['phone'] = self.phone
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        _dict['logo'] = self.logo
        _dict['main_image'] = self.main_image
        _dict['total_photos'] = self.total_photos
        _dict['snippet'] = self.snippet
        _dict['latitude'] = self.latitude
        _dict['longitude'] = self.longitude
        _dict['is_claimed'] = self.is_claimed
        _dict['rating.rating_type'] = self.rating_rating_type
        _dict['rating.value'] = self.rating_value
        _dict['rating.votes_count'] = self.rating_votes_count
        _dict['rating.rating_max'] = self.rating_rating_max
        _dict['rating_distribution.1'] = self.rating_distribution_1
        _dict['rating_distribution.2'] = self.rating_distribution_2
        _dict['rating_distribution.3'] = self.rating_distribution_3
        _dict['rating_distribution.4'] = self.rating_distribution_4
        _dict['rating_distribution.5'] = self.rating_distribution_5
        _dict['work_time.work_hours.current_status'] = self.work_time_work_hours_current_status
        _dict['check_url'] = self.check_url
        _dict['last_updated_time'] = self.last_updated_time
        _dict['price_level'] = self.price_level
        _dict['hotel_rating'] = self.hotel_rating
        _dict['contact_info.type'] = self.contact_info_type
        _dict['first_seen'] = self.first_seen
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "description": obj.get("description"),
            "category": obj.get("category"),
            "category_ids": obj.get("category_ids"),
            "additional_categories": obj.get("additional_categories"),
            "cid": obj.get("cid"),
            "feature_id": obj.get("feature_id"),
            "address": obj.get("address"),
            "address_info_borough": obj.get("address_info.borough"),
            "address_info_address": obj.get("address_info.address"),
            "address_info_city": obj.get("address_info.city"),
            "address_info_zip": obj.get("address_info.zip"),
            "address_info_region": obj.get("address_info.region"),
            "address_info_country_code": obj.get("address_info.country_code"),
            "place_id": obj.get("place_id"),
            "phone": obj.get("phone"),
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "logo": obj.get("logo"),
            "main_image": obj.get("main_image"),
            "total_photos": obj.get("total_photos"),
            "snippet": obj.get("snippet"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "is_claimed": obj.get("is_claimed"),
            "rating_rating_type": obj.get("rating.rating_type"),
            "rating_value": obj.get("rating.value"),
            "rating_votes_count": obj.get("rating.votes_count"),
            "rating_rating_max": obj.get("rating.rating_max"),
            "rating_distribution_1": obj.get("rating_distribution.1"),
            "rating_distribution_2": obj.get("rating_distribution.2"),
            "rating_distribution_3": obj.get("rating_distribution.3"),
            "rating_distribution_4": obj.get("rating_distribution.4"),
            "rating_distribution_5": obj.get("rating_distribution.5"),
            "work_time_work_hours_current_status": obj.get("work_time.work_hours.current_status"),
            "check_url": obj.get("check_url"),
            "last_updated_time": obj.get("last_updated_time"),
            "price_level": obj.get("price_level"),
            "hotel_rating": obj.get("hotel_rating"),
            "contact_info_type": obj.get("contact_info.type"),
            "first_seen": obj.get("first_seen"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj