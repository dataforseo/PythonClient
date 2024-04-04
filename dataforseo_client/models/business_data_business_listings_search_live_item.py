# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.address_info import AddressInfo
from dataforseo_client.models.base_local_business_link import BaseLocalBusinessLink
from dataforseo_client.models.business_data_attributes_info import BusinessDataAttributesInfo
from dataforseo_client.models.business_data_contact_info import BusinessDataContactInfo
from dataforseo_client.models.people_also_search import PeopleAlsoSearch
from dataforseo_client.models.popular_times import PopularTimes
from dataforseo_client.models.rating_info import RatingInfo
from dataforseo_client.models.work_info import WorkInfo
from typing import Optional, Set
from typing_extensions import Self

class BusinessDataBusinessListingsSearchLiveItem(BaseModel):
    """
    BusinessDataBusinessListingsSearchLiveItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="title of the element in SERP the name of the business entity for which the results are collected")
    description: Optional[StrictStr] = Field(default=None, description="description of the element in SERP the description of the business entity for which the results are collected")
    category: Optional[StrictStr] = Field(default=None, description="business category Google My Business general category that best describes the services provided by the business entity")
    category_ids: Optional[List[Optional[StrictStr]]] = Field(default=None, description="global category IDs universal category IDs that do not change based on the selected country")
    additional_categories: Optional[List[Optional[StrictStr]]] = Field(default=None, description="additional business categories additional Google My Business categories that describe the services provided by the business entity in more detail")
    cid: Optional[StrictStr] = Field(default=None, description="google-defined client id unique id of a local establishment learn more about the identifier in this help center article")
    feature_id: Optional[StrictStr] = Field(default=None, description="the unique identifier of the element in SERP learn more about the identifier in this help center article")
    address: Optional[StrictStr] = Field(default=None, description="address of the business entity")
    address_info: Optional[AddressInfo] = None
    place_id: Optional[StrictStr] = Field(default=None, description="unique place identifier place id of the local establishment featured in the element learn more about the identifier in this help center article")
    phone: Optional[StrictStr] = Field(default=None, description="phone number of the business entity")
    url: Optional[StrictStr] = Field(default=None, description="absolute url of the business entity")
    domain: Optional[StrictStr] = Field(default=None, description="domain of the business entity")
    logo: Optional[StrictStr] = Field(default=None, description="URL of the logo featured in Google My Business profile")
    main_image: Optional[StrictStr] = Field(default=None, description="URL of the main image featured in Google My Business profile")
    total_photos: Optional[StrictInt] = Field(default=None, description="total count of images featured in Google My Business profile")
    snippet: Optional[StrictStr] = Field(default=None, description="additional information on the business entity")
    latitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="latitude coordinate of the local establishments in google maps example: \"latitude\": 51.584091")
    longitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="longitude coordinate of the local establishment in google maps example: \"longitude\": -0.31365919999999997")
    is_claimed: Optional[StrictBool] = Field(default=None, description="shows whether the entity is verified by its owner on Google Maps")
    attributes: Optional[BusinessDataAttributesInfo] = None
    place_topics: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="keywords mentioned in customer reviews contains most popular keywords related to products/services mentioned in customer reviews of a business entity and the number of reviews mentioning each keyword example:  \"place_topics\": { \"egg roll\": 48, \"birthday\": 33 }")
    rating: Optional[RatingInfo] = None
    rating_distribution: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="the distribution of ratings of the business entity the object displays the number of 1-star to 5-star ratings, as reviewed by users")
    people_also_search: Optional[List[PeopleAlsoSearch]] = Field(default=None, description="related business entities")
    work_time: Optional[WorkInfo] = None
    popular_times: Optional[PopularTimes] = None
    local_business_links: Optional[List[BaseLocalBusinessLink]] = Field(default=None, description="available interactions with the business list of options to interact with the business directly from search results")
    contact_info: Optional[List[BusinessDataContactInfo]] = Field(default=None, description="available contacts of the business list of contacts to interact with the business")
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to search engine results you can use it to make sure that we provided accurate results")
    last_updated_time: Optional[StrictStr] = Field(default=None, description="date and time when the data was last updated in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00” example: 2023-01-26 09:03:15 +00:00")
    __properties: ClassVar[List[str]] = ["type", "title", "description", "category", "category_ids", "additional_categories", "cid", "feature_id", "address", "address_info", "place_id", "phone", "url", "domain", "logo", "main_image", "total_photos", "snippet", "latitude", "longitude", "is_claimed", "attributes", "place_topics", "rating", "rating_distribution", "people_also_search", "work_time", "popular_times", "local_business_links", "contact_info", "check_url", "last_updated_time"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BusinessDataBusinessListingsSearchLiveItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of address_info
        if self.address_info:
            _dict['address_info'] = self.address_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rating
        if self.rating:
            _dict['rating'] = self.rating.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in people_also_search (list)
        _items = []
        if self.people_also_search:
            for _item in self.people_also_search:
                if _item:
                    _items.append(_item.to_dict())
            _dict['people_also_search'] = _items
        # override the default output from pydantic by calling `to_dict()` of work_time
        if self.work_time:
            _dict['work_time'] = self.work_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of popular_times
        if self.popular_times:
            _dict['popular_times'] = self.popular_times.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in local_business_links (list)
        _items = []
        if self.local_business_links:
            for _item in self.local_business_links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['local_business_links'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in contact_info (list)
        _items = []
        if self.contact_info:
            for _item in self.contact_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['contact_info'] = _items
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if category (nullable) is None
        # and model_fields_set contains the field
        if self.category is None and "category" in self.model_fields_set:
            _dict['category'] = None

        # set to None if category_ids (nullable) is None
        # and model_fields_set contains the field
        if self.category_ids is None and "category_ids" in self.model_fields_set:
            _dict['category_ids'] = None

        # set to None if additional_categories (nullable) is None
        # and model_fields_set contains the field
        if self.additional_categories is None and "additional_categories" in self.model_fields_set:
            _dict['additional_categories'] = None

        # set to None if cid (nullable) is None
        # and model_fields_set contains the field
        if self.cid is None and "cid" in self.model_fields_set:
            _dict['cid'] = None

        # set to None if feature_id (nullable) is None
        # and model_fields_set contains the field
        if self.feature_id is None and "feature_id" in self.model_fields_set:
            _dict['feature_id'] = None

        # set to None if address (nullable) is None
        # and model_fields_set contains the field
        if self.address is None and "address" in self.model_fields_set:
            _dict['address'] = None

        # set to None if place_id (nullable) is None
        # and model_fields_set contains the field
        if self.place_id is None and "place_id" in self.model_fields_set:
            _dict['place_id'] = None

        # set to None if phone (nullable) is None
        # and model_fields_set contains the field
        if self.phone is None and "phone" in self.model_fields_set:
            _dict['phone'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if logo (nullable) is None
        # and model_fields_set contains the field
        if self.logo is None and "logo" in self.model_fields_set:
            _dict['logo'] = None

        # set to None if main_image (nullable) is None
        # and model_fields_set contains the field
        if self.main_image is None and "main_image" in self.model_fields_set:
            _dict['main_image'] = None

        # set to None if total_photos (nullable) is None
        # and model_fields_set contains the field
        if self.total_photos is None and "total_photos" in self.model_fields_set:
            _dict['total_photos'] = None

        # set to None if snippet (nullable) is None
        # and model_fields_set contains the field
        if self.snippet is None and "snippet" in self.model_fields_set:
            _dict['snippet'] = None

        # set to None if latitude (nullable) is None
        # and model_fields_set contains the field
        if self.latitude is None and "latitude" in self.model_fields_set:
            _dict['latitude'] = None

        # set to None if longitude (nullable) is None
        # and model_fields_set contains the field
        if self.longitude is None and "longitude" in self.model_fields_set:
            _dict['longitude'] = None

        # set to None if is_claimed (nullable) is None
        # and model_fields_set contains the field
        if self.is_claimed is None and "is_claimed" in self.model_fields_set:
            _dict['is_claimed'] = None

        # set to None if place_topics (nullable) is None
        # and model_fields_set contains the field
        if self.place_topics is None and "place_topics" in self.model_fields_set:
            _dict['place_topics'] = None

        # set to None if rating_distribution (nullable) is None
        # and model_fields_set contains the field
        if self.rating_distribution is None and "rating_distribution" in self.model_fields_set:
            _dict['rating_distribution'] = None

        # set to None if people_also_search (nullable) is None
        # and model_fields_set contains the field
        if self.people_also_search is None and "people_also_search" in self.model_fields_set:
            _dict['people_also_search'] = None

        # set to None if local_business_links (nullable) is None
        # and model_fields_set contains the field
        if self.local_business_links is None and "local_business_links" in self.model_fields_set:
            _dict['local_business_links'] = None

        # set to None if contact_info (nullable) is None
        # and model_fields_set contains the field
        if self.contact_info is None and "contact_info" in self.model_fields_set:
            _dict['contact_info'] = None

        # set to None if check_url (nullable) is None
        # and model_fields_set contains the field
        if self.check_url is None and "check_url" in self.model_fields_set:
            _dict['check_url'] = None

        # set to None if last_updated_time (nullable) is None
        # and model_fields_set contains the field
        if self.last_updated_time is None and "last_updated_time" in self.model_fields_set:
            _dict['last_updated_time'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BusinessDataBusinessListingsSearchLiveItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "title": obj.get("title"),
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
            "rating": RatingInfo.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "rating_distribution": obj.get("rating_distribution"),
            "people_also_search": [PeopleAlsoSearch.from_dict(_item) for _item in obj["people_also_search"]] if obj.get("people_also_search") is not None else None,
            "work_time": WorkInfo.from_dict(obj["work_time"]) if obj.get("work_time") is not None else None,
            "popular_times": PopularTimes.from_dict(obj["popular_times"]) if obj.get("popular_times") is not None else None,
            "local_business_links": [BaseLocalBusinessLink.from_dict(_item) for _item in obj["local_business_links"]] if obj.get("local_business_links") is not None else None,
            "contact_info": [BusinessDataContactInfo.from_dict(_item) for _item in obj["contact_info"]] if obj.get("contact_info") is not None else None,
            "check_url": obj.get("check_url"),
            "last_updated_time": obj.get("last_updated_time")
        })
        return _obj


