from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.address_info import AddressInfo
from dataforseo_client.models.business_data_attributes_info import BusinessDataAttributesInfo
from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.people_also_search import PeopleAlsoSearch
from dataforseo_client.models.business_work_hours_info import BusinessWorkHoursInfo



class ItemsGoogleBusinessInfo(BaseModel):
    """
    ItemsGoogleBusinessInfo
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank among all the elements")
    position: Optional[StrictStr] = Field(default=None, description="the alignment in SERP")
    title: Optional[StrictStr] = Field(default=None, description="title of the element in SERP. the name of the business entity for which the results are collected")
    original_title: Optional[StrictStr] = Field(default=None, description="original title of the element. original title not translated by Google")
    description: Optional[StrictStr] = Field(default=None, description="description of the element in SERP. the description of the business entity for which the results are collected")
    category: Optional[StrictStr] = Field(default=None, description="business category. Google My Business general category that best describes the services provided by the business entity")
    category_ids: Optional[List[Optional[StrictStr]]] = Field(default=None, description="global category IDs. universal category IDs that do not change based on the selected country")
    additional_categories: Optional[List[Optional[StrictStr]]] = Field(default=None, description="additional business categories. additional Google My Business categories that describe the services provided by the business entity in more detail")
    cid: Optional[StrictStr] = Field(default=None, description="google-defined client id. unique id of a local establishment;. can be used with Google Reviews API to get a full list of reviews. learn more about the identifier in this help center article")
    feature_id: Optional[StrictStr] = Field(default=None, description="the unique identifier of the element in SERP. learn more about the identifier in this help center article")
    address: Optional[StrictStr] = Field(default=None, description="address of the business entity")
    address_info: Optional[AddressInfo] = Field(default=None, description="object containing address components of the business entity")
    place_id: Optional[StrictStr] = Field(default=None, description="unique place identifier. place id of the local establishment featured in the element. learn more about the identifier in this help center article")
    phone: Optional[StrictStr] = Field(default=None, description="phone number of the business entity")
    url: Optional[StrictStr] = Field(default=None, description="absolute url of the business entity")
    contact_url: Optional[StrictStr] = Field(default=None, description="URL of the preferred contact page")
    contributor_url: Optional[StrictStr] = Field(default=None, description="URL of the user’s or entity’s Local Guides profile, if available")
    book_online_url: Optional[StrictStr] = Field(default=None, description="URL in the ‘book online’ button of the element. URL directing users to the online booking or order page of the business entity")
    domain: Optional[StrictStr] = Field(default=None, description="domain of the business entity")
    logo: Optional[StrictStr] = Field(default=None, description="URL of the logo featured in Google My Business profile")
    main_image: Optional[StrictStr] = Field(default=None, description="URL of the main image featured in Google My Business profile")
    total_photos: Optional[StrictInt] = Field(default=None, description="total count of images featured in Google My Business profile")
    snippet: Optional[StrictStr] = Field(default=None, description="additional information on the business entity")
    latitude: Optional[StrictFloat] = Field(default=None, description="latitude coordinate of the local establishments in google maps. example:. 'latitude': 51.584091")
    longitude: Optional[StrictFloat] = Field(default=None, description="longitude coordinate of the local establishment in google maps. example:. 'longitude': -0.31365919999999997")
    is_claimed: Optional[StrictBool] = Field(default=None, description="shows whether the entity is verified by its owner on Google Maps")
    attributes: Optional[BusinessDataAttributesInfo] = Field(default=None, description="service details in a form of user-reviewed checks;. service details of a business entity displayed in a form of checks and based on user feedback and business category")
    place_topics: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="keywords mentioned in customer reviews. contains most popular keywords related to products/services mentioned in customer reviews of a business entity and the number of reviews mentioning each keyword. example: . 'place_topics': {. 'egg roll': 48,. 'birthday': 33. }")
    rating: Optional[RatingElement] = Field(default=None, description="the element’s rating . the popularity rate based on reviews and displayed in SERP")
    hotel_rating: Optional[StrictStr] = Field(default=None, description="hotel class rating. class ratings range between 1-5 stars, learn more. if there is no hotel class rating information, the value will be null")
    price_level: Optional[StrictStr] = Field(default=None, description="property price level. can take values: inexpensive, moderate, expensive, very_expensive. if there is no price level information, the value will be null")
    rating_distribution: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="the distribution of ratings of the business entity. the object displays the number of 1-star to 5-star ratings, as reviewed by users")
    people_also_search: Optional[List[Optional[PeopleAlsoSearch]]] = Field(default=None, description="related business entities")
    work_time: Optional[BusinessWorkHoursInfo] = Field(default=None, description="work time details. information related to operational hours of the business entity")
    popular_times: Optional[Any] = Field(default=None, description="popular times. information related to busy hours of the business entity")
    local_business_links: Optional[Any] = Field(default=None, description="available interactions with the business. list of options to interact with the business directly from search results")
    is_directory_item: Optional[StrictBool] = Field(default=None, description="business establishment is a part of the directory. indicates whether the business establishment is a part of the directory;. if true, the item is a part of the larger directory of businesses with the same address (e.g., a mall or a business centre);. note: if the business establishment is a parent item in the directory, the value will be null")
    directory: Optional[Any] = Field(default=None, description="items of the directory. includes information about businesses that are located within the target business establishment and have the same address")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "title", 
        "original_title", 
        "description", 
        "category", 
        "category_ids", 
        "additional_categories", 
        "cid", 
        "feature_id", 
        "address", 
        "address_info", 
        "place_id", 
        "phone", 
        "url", 
        "contact_url", 
        "contributor_url", 
        "book_online_url", 
        "domain", 
        "logo", 
        "main_image", 
        "total_photos", 
        "snippet", 
        "latitude", 
        "longitude", 
        "is_claimed", 
        "attributes", 
        "place_topics", 
        "rating", 
        "hotel_rating", 
        "price_level", 
        "rating_distribution", 
        "people_also_search", 
        "work_time", 
        "popular_times", 
        "local_business_links", 
        "is_directory_item", 
        "directory", 
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
        _dict['position'] = self.position
        _dict['title'] = self.title
        _dict['original_title'] = self.original_title
        _dict['description'] = self.description
        _dict['category'] = self.category
        _dict['category_ids'] = self.category_ids
        _dict['additional_categories'] = self.additional_categories
        _dict['cid'] = self.cid
        _dict['feature_id'] = self.feature_id
        _dict['address'] = self.address
        _dict['address_info'] = self.address_info.to_dict() if self.address_info else None
        _dict['place_id'] = self.place_id
        _dict['phone'] = self.phone
        _dict['url'] = self.url
        _dict['contact_url'] = self.contact_url
        _dict['contributor_url'] = self.contributor_url
        _dict['book_online_url'] = self.book_online_url
        _dict['domain'] = self.domain
        _dict['logo'] = self.logo
        _dict['main_image'] = self.main_image
        _dict['total_photos'] = self.total_photos
        _dict['snippet'] = self.snippet
        _dict['latitude'] = self.latitude
        _dict['longitude'] = self.longitude
        _dict['is_claimed'] = self.is_claimed
        _dict['attributes'] = self.attributes.to_dict() if self.attributes else None
        _dict['place_topics'] = self.place_topics
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['hotel_rating'] = self.hotel_rating
        _dict['price_level'] = self.price_level
        _dict['rating_distribution'] = self.rating_distribution
        people_also_search_items = []
        if self.people_also_search:
            for _item in self.people_also_search:
                if _item:
                    people_also_search_items.append(_item.to_dict())
            _dict['people_also_search'] = people_also_search_items
        _dict['work_time'] = self.work_time.to_dict() if self.work_time else None
        _dict['popular_times'] = self.popular_times
        _dict['local_business_links'] = self.local_business_links
        _dict['is_directory_item'] = self.is_directory_item
        _dict['directory'] = self.directory
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
            "position": obj.get("position"),
            "title": obj.get("title"),
            "original_title": obj.get("original_title"),
            "description": obj.get("description"),
            "category": obj.get("category"),
            "category_ids": obj.get("category_ids"),
            "additional_categories": obj.get("additional_categories"),
            "cid": obj.get("cid"),
            "feature_id": obj.get("feature_id"),
            "address": obj.get("address"),
            "address_info": AddressInfo.from_dict(obj["address_info"]) if obj.get("address_info") is not None else None,
            "place_id": obj.get("place_id"),
            "phone": obj.get("phone"),
            "url": obj.get("url"),
            "contact_url": obj.get("contact_url"),
            "contributor_url": obj.get("contributor_url"),
            "book_online_url": obj.get("book_online_url"),
            "domain": obj.get("domain"),
            "logo": obj.get("logo"),
            "main_image": obj.get("main_image"),
            "total_photos": obj.get("total_photos"),
            "snippet": obj.get("snippet"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "is_claimed": obj.get("is_claimed"),
            "attributes": BusinessDataAttributesInfo.from_dict(obj["attributes"]) if obj.get("attributes") is not None else None,
            "place_topics": obj.get("place_topics"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "hotel_rating": obj.get("hotel_rating"),
            "price_level": obj.get("price_level"),
            "rating_distribution": obj.get("rating_distribution"),
            "people_also_search": [PeopleAlsoSearch.from_dict(_item) for _item in obj["people_also_search"]] if obj.get("people_also_search") is not None else None,
            "work_time": BusinessWorkHoursInfo.from_dict(obj["work_time"]) if obj.get("work_time") is not None else None,
            "popular_times": obj.get("popular_times"),
            "local_business_links": obj.get("local_business_links"),
            "is_directory_item": obj.get("is_directory_item"),
            "directory": obj.get("directory"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj