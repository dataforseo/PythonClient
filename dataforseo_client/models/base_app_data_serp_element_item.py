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

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.rating_info import RatingInfo
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dataforseo_client.models.data_app_app_store_info_organic_serp_element_item import DataAppAppStoreInfoOrganicSerpElementItem
    from dataforseo_client.models.data_app_app_store_reviews_search_serp_element_item import DataAppAppStoreReviewsSearchSerpElementItem
    from dataforseo_client.models.data_app_app_store_search_organic_serp_element_item import DataAppAppStoreSearchOrganicSerpElementItem
    from dataforseo_client.models.data_app_google_play_info_organic_serp_element_item import DataAppGooglePlayInfoOrganicSerpElementItem
    from dataforseo_client.models.data_app_google_play_reviews_search_serp_element_item import DataAppGooglePlayReviewsSearchSerpElementItem
    from dataforseo_client.models.data_app_google_play_search_organic_serp_element_item import DataAppGooglePlaySearchOrganicSerpElementItem

class BaseAppDataSerpElementItem(BaseModel):
    """
    BaseAppDataSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP can take the following values: left, right")
    title: Optional[StrictStr] = Field(default=None, description="title of the app")
    rating: Optional[RatingInfo] = None
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "position", "title", "rating"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'app_store_info_organic': 'DataAppAppStoreInfoOrganicSerpElementItem','app_store_reviews_search': 'DataAppAppStoreReviewsSearchSerpElementItem','app_store_search_organic': 'DataAppAppStoreSearchOrganicSerpElementItem','google_play_info_organic': 'DataAppGooglePlayInfoOrganicSerpElementItem','google_play_reviews_search': 'DataAppGooglePlayReviewsSearchSerpElementItem','google_play_search_organic': 'DataAppGooglePlaySearchOrganicSerpElementItem'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[DataAppAppStoreInfoOrganicSerpElementItem, DataAppAppStoreReviewsSearchSerpElementItem, DataAppAppStoreSearchOrganicSerpElementItem, DataAppGooglePlayInfoOrganicSerpElementItem, DataAppGooglePlayReviewsSearchSerpElementItem, DataAppGooglePlaySearchOrganicSerpElementItem]]:
        """Create an instance of BaseAppDataSerpElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rating
        if self.rating:
            _dict['rating'] = self.rating.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if rank_group (nullable) is None
        # and model_fields_set contains the field
        if self.rank_group is None and "rank_group" in self.model_fields_set:
            _dict['rank_group'] = None

        # set to None if rank_absolute (nullable) is None
        # and model_fields_set contains the field
        if self.rank_absolute is None and "rank_absolute" in self.model_fields_set:
            _dict['rank_absolute'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[DataAppAppStoreInfoOrganicSerpElementItem, DataAppAppStoreReviewsSearchSerpElementItem, DataAppAppStoreSearchOrganicSerpElementItem, DataAppGooglePlayInfoOrganicSerpElementItem, DataAppGooglePlayReviewsSearchSerpElementItem, DataAppGooglePlaySearchOrganicSerpElementItem]]:
        """Create an instance of BaseAppDataSerpElementItem from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'DataAppAppStoreInfoOrganicSerpElementItem':
            return import_module("dataforseo_client.models.data_app_app_store_info_organic_serp_element_item").DataAppAppStoreInfoOrganicSerpElementItem.from_dict(obj)
        if object_type ==  'DataAppAppStoreReviewsSearchSerpElementItem':
            return import_module("dataforseo_client.models.data_app_app_store_reviews_search_serp_element_item").DataAppAppStoreReviewsSearchSerpElementItem.from_dict(obj)
        if object_type ==  'DataAppAppStoreSearchOrganicSerpElementItem':
            return import_module("dataforseo_client.models.data_app_app_store_search_organic_serp_element_item").DataAppAppStoreSearchOrganicSerpElementItem.from_dict(obj)
        if object_type ==  'DataAppGooglePlayInfoOrganicSerpElementItem':
            return import_module("dataforseo_client.models.data_app_google_play_info_organic_serp_element_item").DataAppGooglePlayInfoOrganicSerpElementItem.from_dict(obj)
        if object_type ==  'DataAppGooglePlayReviewsSearchSerpElementItem':
            return import_module("dataforseo_client.models.data_app_google_play_reviews_search_serp_element_item").DataAppGooglePlayReviewsSearchSerpElementItem.from_dict(obj)
        if object_type ==  'DataAppGooglePlaySearchOrganicSerpElementItem':
            return import_module("dataforseo_client.models.data_app_google_play_search_organic_serp_element_item").DataAppGooglePlaySearchOrganicSerpElementItem.from_dict(obj)

        raise ValueError("BaseAppDataSerpElementItem failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


