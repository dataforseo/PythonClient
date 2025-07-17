from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.address_info import AddressInfo
from dataforseo_client.models.business_work_hours_info import BusinessWorkHoursInfo



class MapsSearch(BaseModel):
    """
    MapsSearch
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from the rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank among all the elements")
    domain: Optional[StrictStr] = Field(default=None, description="domain of the business entity")
    title: Optional[StrictStr] = Field(default=None, description="directory title. can take the following values: At this place, Directory")
    url: Optional[StrictStr] = Field(default=None, description="URL to view the menu")
    rating: Optional[RatingElement] = Field(default=None, description="the element’s rating . the popularity rate based on reviews and displayed in SERP")
    rating_distribution: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="the distribution of ratings of the business entity. the object displays the number of 1-star to 5-star ratings, as reviewed by users")
    snippet: Optional[StrictStr] = Field(default=None, description="additional information about the business entity")
    address: Optional[StrictStr] = Field(default=None, description="address of the business entity")
    address_info: Optional[AddressInfo] = Field(default=None, description="object containing address components of the business entity")
    place_id: Optional[StrictStr] = Field(default=None, description="unique place identifier. place id of the local establishment featured in the element. learn more about the identifier in this help center article")
    phone: Optional[StrictStr] = Field(default=None, description="phone number of the business entity")
    main_image: Optional[StrictStr] = Field(default=None, description="URL of the main image featured in Google My Business profile")
    total_photos: Optional[StrictStr] = Field(default=None, description="total count of images featured in Google My Business profile")
    category: Optional[StrictStr] = Field(default=None, description="business category. Google My Business general category that best describes the services provided by the business entity")
    additional_categories: Optional[List[Optional[StrictStr]]] = Field(default=None, description="additional business categories. additional Google My Business categories that describe the services provided by the business entity in more detail")
    price_level: Optional[StrictStr] = Field(default=None, description="property price level. can take values: inexpensive, moderate, expensive, very_expensive. if there is no price level information, the value will be null")
    hotel_rating: Optional[StrictStr] = Field(default=None, description="hotel class rating. class ratings range between 1-5 stars, learn more. if there is no hotel class rating information, the value will be null")
    category_ids: Optional[List[Optional[StrictStr]]] = Field(default=None, description="global category IDs. universal category IDs that do not change based on the selected country")
    work_hours: Optional[BusinessWorkHoursInfo] = Field(default=None, description="open hours. information about work hours of the local establishment")
    feature_id: Optional[StrictStr] = Field(default=None, description="the unique identifier of the element in SERP. learn more about the identifier in this help center article")
    cid: Optional[StrictStr] = Field(default=None, description="google-defined client id. unique id of a local establishment;. can be used with Google Reviews API to get a full list of reviews. learn more about the identifier in this help center article")
    latitude: Optional[StrictFloat] = Field(default=None, description="latitude coordinate of the local establishments in google maps. example:. 'latitude': 51.584091")
    longitude: Optional[StrictFloat] = Field(default=None, description="longitude coordinate of the local establishment in google maps. example:. 'longitude': -0.31365919999999997")
    is_claimed: Optional[StrictBool] = Field(default=None, description="shows whether the entity is verified by its owner on Google Maps")
    local_justifications: Optional[List[Optional[StrictStr]]] = Field(default=None, description="Google local justifications. snippets of text that “justify” why the business is showing up for search query")
    is_directory_item: Optional[StrictBool] = Field(default=None, description="business establishment is a part of the directory. indicates whether the business establishment is a part of the directory;. if true, the item is a part of the larger directory of businesses with the same address (e.g., a mall or a business centre);. note: if the business establishment is a parent item in the directory, the value will be null")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "domain", 
        "title", 
        "url", 
        "rating", 
        "rating_distribution", 
        "snippet", 
        "address", 
        "address_info", 
        "place_id", 
        "phone", 
        "main_image", 
        "total_photos", 
        "category", 
        "additional_categories", 
        "price_level", 
        "hotel_rating", 
        "category_ids", 
        "work_hours", 
        "feature_id", 
        "cid", 
        "latitude", 
        "longitude", 
        "is_claimed", 
        "local_justifications", 
        "is_directory_item", 
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
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['domain'] = self.domain
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['rating_distribution'] = self.rating_distribution
        _dict['snippet'] = self.snippet
        _dict['address'] = self.address
        _dict['address_info'] = self.address_info.to_dict() if self.address_info else None
        _dict['place_id'] = self.place_id
        _dict['phone'] = self.phone
        _dict['main_image'] = self.main_image
        _dict['total_photos'] = self.total_photos
        _dict['category'] = self.category
        _dict['additional_categories'] = self.additional_categories
        _dict['price_level'] = self.price_level
        _dict['hotel_rating'] = self.hotel_rating
        _dict['category_ids'] = self.category_ids
        _dict['work_hours'] = self.work_hours.to_dict() if self.work_hours else None
        _dict['feature_id'] = self.feature_id
        _dict['cid'] = self.cid
        _dict['latitude'] = self.latitude
        _dict['longitude'] = self.longitude
        _dict['is_claimed'] = self.is_claimed
        _dict['local_justifications'] = self.local_justifications
        _dict['is_directory_item'] = self.is_directory_item
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "domain": obj.get("domain"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "rating_distribution": obj.get("rating_distribution"),
            "snippet": obj.get("snippet"),
            "address": obj.get("address"),
            "address_info": AddressInfo.from_dict(obj["address_info"]) if obj.get("address_info") is not None else None,
            "place_id": obj.get("place_id"),
            "phone": obj.get("phone"),
            "main_image": obj.get("main_image"),
            "total_photos": obj.get("total_photos"),
            "category": obj.get("category"),
            "additional_categories": obj.get("additional_categories"),
            "price_level": obj.get("price_level"),
            "hotel_rating": obj.get("hotel_rating"),
            "category_ids": obj.get("category_ids"),
            "work_hours": BusinessWorkHoursInfo.from_dict(obj["work_hours"]) if obj.get("work_hours") is not None else None,
            "feature_id": obj.get("feature_id"),
            "cid": obj.get("cid"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "is_claimed": obj.get("is_claimed"),
            "local_justifications": obj.get("local_justifications"),
            "is_directory_item": obj.get("is_directory_item"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj