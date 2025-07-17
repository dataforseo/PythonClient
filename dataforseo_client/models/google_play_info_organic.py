from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.rating_element import RatingElement
from dataforseo_client.models.price_info import PriceInfo
from dataforseo_client.models.apps_info import AppsInfo



class GooglePlayInfoOrganic(BaseModel):
    """
    GooglePlayInfoOrganic
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank among all the listed apps. absolute position among all apps on the list")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values: left")
    app_id: Optional[StrictStr] = Field(default=None, description="ID of the app")
    title: Optional[StrictStr] = Field(default=None, description="title of the app")
    url: Optional[StrictStr] = Field(default=None, description="URL to the app page on Google Play")
    icon: Optional[StrictStr] = Field(default=None, description="URL to the app icon")
    description: Optional[StrictStr] = Field(default=None, description="description of the app")
    reviews_count: Optional[StrictInt] = Field(default=None, description="the total number of reviews the app has")
    rating: Optional[RatingElement] = Field(default=None, description="average rating of the app")
    price: Optional[PriceInfo] = Field(default=None, description="price of the app")
    is_free: Optional[StrictBool] = Field(default=None, description="indicates whether the app is free")
    main_category: Optional[StrictStr] = Field(default=None, description="main category of the app")
    installs: Optional[StrictStr] = Field(default=None, description="number of installs of the app. approximate number of installs as displayed on the app page")
    installs_count: Optional[StrictInt] = Field(default=None, description="number of installs of the app. the exact number of installs of the app")
    developer: Optional[StrictStr] = Field(default=None, description="name of the app developer")
    developer_id: Optional[StrictStr] = Field(default=None, description="ID of the app developer")
    developer_url: Optional[StrictStr] = Field(default=None, description="URL to the developer page on Google Play")
    developer_email: Optional[StrictStr] = Field(default=None, description="email address of the developer")
    developer_address: Optional[StrictStr] = Field(default=None, description="physical address of the developer")
    developer_website: Optional[StrictStr] = Field(default=None, description="official website of the developer")
    version: Optional[StrictStr] = Field(default=None, description="current version of the app")
    minimum_os_version: Optional[StrictStr] = Field(default=None, description="minimum OS version required to install the app")
    size: Optional[StrictStr] = Field(default=None, description="size of the app")
    released_date: Optional[StrictStr] = Field(default=None, description="date and time when the app was released. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;. example:. 2019-11-15 12:57:46 +00:00")
    last_update_date: Optional[StrictStr] = Field(default=None, description="date and time when the app was last updated. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”;. example:. 2019-11-15 12:57:46 +00:00")
    update_notes: Optional[StrictStr] = Field(default=None, description="update notes. contains the latest update notes from the developer")
    images: Optional[List[Optional[StrictStr]]] = Field(default=None, description="app images. contains URLs to the images published on the app page on Google Play")
    videos: Optional[List[Optional[StrictStr]]] = Field(default=None, description="app videos. contains URLs to the video published on the app page on Google Play")
    similar_apps: Optional[List[Optional[AppsInfo]]] = Field(default=None, description="similar apps. displays apps similar to the app in a POST request")
    more_apps_by_developer: Optional[List[Optional[AppsInfo]]] = Field(default=None, description="similar apps. information about apps built by the same developer")
    genres: Optional[List[Optional[StrictStr]]] = Field(default=None, description="app genres. contains relevant app categories")
    tags: Optional[List[Optional[StrictStr]]] = Field(default=None, description="app tags. contains relevant app tags")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "app_id", 
        "title", 
        "url", 
        "icon", 
        "description", 
        "reviews_count", 
        "rating", 
        "price", 
        "is_free", 
        "main_category", 
        "installs", 
        "installs_count", 
        "developer", 
        "developer_id", 
        "developer_url", 
        "developer_email", 
        "developer_address", 
        "developer_website", 
        "version", 
        "minimum_os_version", 
        "size", 
        "released_date", 
        "last_update_date", 
        "update_notes", 
        "images", 
        "videos", 
        "similar_apps", 
        "more_apps_by_developer", 
        "genres", 
        "tags", 
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
        _dict['app_id'] = self.app_id
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['icon'] = self.icon
        _dict['description'] = self.description
        _dict['reviews_count'] = self.reviews_count
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['price'] = self.price.to_dict() if self.price else None
        _dict['is_free'] = self.is_free
        _dict['main_category'] = self.main_category
        _dict['installs'] = self.installs
        _dict['installs_count'] = self.installs_count
        _dict['developer'] = self.developer
        _dict['developer_id'] = self.developer_id
        _dict['developer_url'] = self.developer_url
        _dict['developer_email'] = self.developer_email
        _dict['developer_address'] = self.developer_address
        _dict['developer_website'] = self.developer_website
        _dict['version'] = self.version
        _dict['minimum_os_version'] = self.minimum_os_version
        _dict['size'] = self.size
        _dict['released_date'] = self.released_date
        _dict['last_update_date'] = self.last_update_date
        _dict['update_notes'] = self.update_notes
        _dict['images'] = self.images
        _dict['videos'] = self.videos
        similar_apps_items = []
        if self.similar_apps:
            for _item in self.similar_apps:
                if _item:
                    similar_apps_items.append(_item.to_dict())
            _dict['similar_apps'] = similar_apps_items
        more_apps_by_developer_items = []
        if self.more_apps_by_developer:
            for _item in self.more_apps_by_developer:
                if _item:
                    more_apps_by_developer_items.append(_item.to_dict())
            _dict['more_apps_by_developer'] = more_apps_by_developer_items
        _dict['genres'] = self.genres
        _dict['tags'] = self.tags
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
            "app_id": obj.get("app_id"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "icon": obj.get("icon"),
            "description": obj.get("description"),
            "reviews_count": obj.get("reviews_count"),
            "rating": RatingElement.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "price": PriceInfo.from_dict(obj["price"]) if obj.get("price") is not None else None,
            "is_free": obj.get("is_free"),
            "main_category": obj.get("main_category"),
            "installs": obj.get("installs"),
            "installs_count": obj.get("installs_count"),
            "developer": obj.get("developer"),
            "developer_id": obj.get("developer_id"),
            "developer_url": obj.get("developer_url"),
            "developer_email": obj.get("developer_email"),
            "developer_address": obj.get("developer_address"),
            "developer_website": obj.get("developer_website"),
            "version": obj.get("version"),
            "minimum_os_version": obj.get("minimum_os_version"),
            "size": obj.get("size"),
            "released_date": obj.get("released_date"),
            "last_update_date": obj.get("last_update_date"),
            "update_notes": obj.get("update_notes"),
            "images": obj.get("images"),
            "videos": obj.get("videos"),
            "similar_apps": [AppsInfo.from_dict(_item) for _item in obj["similar_apps"]] if obj.get("similar_apps") is not None else None,
            "more_apps_by_developer": [AppsInfo.from_dict(_item) for _item in obj["more_apps_by_developer"]] if obj.get("more_apps_by_developer") is not None else None,
            "genres": obj.get("genres"),
            "tags": obj.get("tags"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj