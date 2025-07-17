from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.address_info import AddressInfo
from dataforseo_client.models.work_hours import WorkHours
from dataforseo_client.models.local_justification_info import LocalJustificationInfo
from dataforseo_client.models.base_serp_api_google_maps_element_item import BaseSerpApiGoogleMapsElementItem
from dataforseo_client.models.rating_element import RatingElement



class SerpApiMapsSearchElementItem(BaseSerpApiGoogleMapsElementItem):
    """
    SerpApiMapsSearchElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    domain: Optional[StrictStr] = Field(default=None, description="domain in SERP")
    title: Optional[StrictStr] = Field(default=None, description="title of the element")
    url: Optional[StrictStr] = Field(default=None, description="search URL with refinement parameters")
    rating: Optional[RatingElement] = Field(default=None, description="the element’s rating . the popularity rate based on reviews and displayed in SERP")
    rating_distribution: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="the distribution of ratings of the business entity. the object displays the number of 1-star to 5-star ratings, as reviewed by users")
    original_title: Optional[StrictStr] = Field(default=None, description="original title of the element. original title not translated by Google")
    contact_url: Optional[StrictStr] = Field(default=None, description="URL of the preferred contact page")
    contributor_url: Optional[StrictStr] = Field(default=None, description="URL of the user’s or entity’s Local Guides profile, if available")
    book_online_url: Optional[StrictStr] = Field(default=None, description="URL in the ‘book online’ button of the element. URL directing users to the online booking or order page of the business entity")
    hotel_rating: Optional[StrictFloat] = Field(default=None, description="hotel class rating. class ratings range between 1-5 stars, learn more. if there is no hotel class rating information, the value will be null")
    price_level: Optional[StrictStr] = Field(default=None, description="property price level. can take values: inexpensive, moderate, expensive, very_expensive. if there is no price level information, the value will be null")
    snippet: Optional[StrictStr] = Field(default=None, description="element snippet. contains the address and other information about the local establishment featured in the element")
    address: Optional[StrictStr] = Field(default=None, description="address line. address of the local establishment featured in the element")
    address_info: Optional[AddressInfo] = Field(default=None, description="object containing address components of the local establishment")
    place_id: Optional[StrictStr] = Field(default=None, description="unique place identifier. place id of the local establishment featured in the element")
    phone: Optional[StrictStr] = Field(default=None, description="phone number. phone number of the local establishment featured in the element")
    main_image: Optional[StrictStr] = Field(default=None, description="URL of the main image featured in Google My Business profile")
    total_photos: Optional[StrictInt] = Field(default=None, description="total count of images featured in Google My Business profile")
    category: Optional[StrictStr] = Field(default=None, description="business category. Google My Business general category that best describes the services provided by the business entity")
    additional_categories: Optional[List[Optional[StrictStr]]] = Field(default=None, description="additional business categories. additional Google My Business categories that describe the services provided by the business entity in more detail")
    category_ids: Optional[List[Optional[StrictStr]]] = Field(default=None, description="global category IDs. universal category IDs that do not change based on the selected country")
    work_hours: Optional[WorkHours] = Field(default=None, description="open hours. information about work hours of the local establishment")
    feature_id: Optional[StrictStr] = Field(default=None, description="the unique identifier of the element in SERP")
    cid: Optional[StrictStr] = Field(default=None, description="google-defined client id. unique id of a local establishment;. can be used with Google Reviews API to get a full list of reviews")
    latitude: Optional[StrictFloat] = Field(default=None, description="latitude coordinate of the local establishments in google maps. example:. 'latitude': 51.584091")
    longitude: Optional[StrictFloat] = Field(default=None, description="longitude coordinate of the local establishment in google maps. example:. 'longitude': -0.31365919999999997")
    is_claimed: Optional[StrictBool] = Field(default=None, description="indicates whether ownership of this local establishment is claimed")
    local_justifications: Optional[List[Optional[LocalJustificationInfo]]] = Field(default=None, description="Google local justifications. snippets of text that “justify” why the business is showing up for search query")
    is_directory_item: Optional[StrictBool] = Field(default=None, description="indicates whether this local establishment is a directory")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "domain", 
        "title", 
        "url", 
        "rating", 
        "rating_distribution", 
        "original_title", 
        "contact_url", 
        "contributor_url", 
        "book_online_url", 
        "hotel_rating", 
        "price_level", 
        "snippet", 
        "address", 
        "address_info", 
        "place_id", 
        "phone", 
        "main_image", 
        "total_photos", 
        "category", 
        "additional_categories", 
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
        _dict['original_title'] = self.original_title
        _dict['contact_url'] = self.contact_url
        _dict['contributor_url'] = self.contributor_url
        _dict['book_online_url'] = self.book_online_url
        _dict['hotel_rating'] = self.hotel_rating
        _dict['price_level'] = self.price_level
        _dict['snippet'] = self.snippet
        _dict['address'] = self.address
        _dict['address_info'] = self.address_info.to_dict() if self.address_info else None
        _dict['place_id'] = self.place_id
        _dict['phone'] = self.phone
        _dict['main_image'] = self.main_image
        _dict['total_photos'] = self.total_photos
        _dict['category'] = self.category
        _dict['additional_categories'] = self.additional_categories
        _dict['category_ids'] = self.category_ids
        _dict['work_hours'] = self.work_hours.to_dict() if self.work_hours else None
        _dict['feature_id'] = self.feature_id
        _dict['cid'] = self.cid
        _dict['latitude'] = self.latitude
        _dict['longitude'] = self.longitude
        _dict['is_claimed'] = self.is_claimed
        local_justifications_items = []
        if self.local_justifications:
            for _item in self.local_justifications:
                if _item:
                    local_justifications_items.append(_item.to_dict())
            _dict['local_justifications'] = local_justifications_items
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
            "original_title": obj.get("original_title"),
            "contact_url": obj.get("contact_url"),
            "contributor_url": obj.get("contributor_url"),
            "book_online_url": obj.get("book_online_url"),
            "hotel_rating": obj.get("hotel_rating"),
            "price_level": obj.get("price_level"),
            "snippet": obj.get("snippet"),
            "address": obj.get("address"),
            "address_info": AddressInfo.from_dict(obj["address_info"]) if obj.get("address_info") is not None else None,
            "place_id": obj.get("place_id"),
            "phone": obj.get("phone"),
            "main_image": obj.get("main_image"),
            "total_photos": obj.get("total_photos"),
            "category": obj.get("category"),
            "additional_categories": obj.get("additional_categories"),
            "category_ids": obj.get("category_ids"),
            "work_hours": WorkHours.from_dict(obj["work_hours"]) if obj.get("work_hours") is not None else None,
            "feature_id": obj.get("feature_id"),
            "cid": obj.get("cid"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "is_claimed": obj.get("is_claimed"),
            "local_justifications": [LocalJustificationInfo.from_dict(_item) for _item in obj["local_justifications"]] if obj.get("local_justifications") is not None else None,
            "is_directory_item": obj.get("is_directory_item"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj