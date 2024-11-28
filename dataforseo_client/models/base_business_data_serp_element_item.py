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
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dataforseo_client.models.google_business_info_business_data_serp_element_item import GoogleBusinessInfoBusinessDataSerpElementItem
    from dataforseo_client.models.google_business_post_business_data_serp_element_item import GoogleBusinessPostBusinessDataSerpElementItem
    from dataforseo_client.models.google_reviews_search_business_data_serp_element_item import GoogleReviewsSearchBusinessDataSerpElementItem
    from dataforseo_client.models.maps_search_business_data_serp_element_item import MapsSearchBusinessDataSerpElementItem
    from dataforseo_client.models.tripadvisor_review_search_business_data_serp_element_item import TripadvisorReviewSearchBusinessDataSerpElementItem
    from dataforseo_client.models.tripadvisor_search_organic_business_data_serp_element_item import TripadvisorSearchOrganicBusinessDataSerpElementItem
    from dataforseo_client.models.trustpilot_review_search_business_data_serp_element_item import TrustpilotReviewSearchBusinessDataSerpElementItem
    from dataforseo_client.models.trustpilot_search_organic_business_data_serp_element_item import TrustpilotSearchOrganicBusinessDataSerpElementItem

class BaseBusinessDataSerpElementItem(BaseModel):
    """
    BaseBusinessDataSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values positions of elements with different type values are omitted from the rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank among all the elements")
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'google_business_info': 'GoogleBusinessInfoBusinessDataSerpElementItem','google_business_post': 'GoogleBusinessPostBusinessDataSerpElementItem','google_reviews_search': 'GoogleReviewsSearchBusinessDataSerpElementItem','maps_search': 'MapsSearchBusinessDataSerpElementItem','tripadvisor_review_search': 'TripadvisorReviewSearchBusinessDataSerpElementItem','tripadvisor_search_organic': 'TripadvisorSearchOrganicBusinessDataSerpElementItem','trustpilot_review_search': 'TrustpilotReviewSearchBusinessDataSerpElementItem','trustpilot_search_organic': 'TrustpilotSearchOrganicBusinessDataSerpElementItem'
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
    def from_json(cls, json_str: str) -> Optional[Union[GoogleBusinessInfoBusinessDataSerpElementItem, GoogleBusinessPostBusinessDataSerpElementItem, GoogleReviewsSearchBusinessDataSerpElementItem, MapsSearchBusinessDataSerpElementItem, TripadvisorReviewSearchBusinessDataSerpElementItem, TripadvisorSearchOrganicBusinessDataSerpElementItem, TrustpilotReviewSearchBusinessDataSerpElementItem, TrustpilotSearchOrganicBusinessDataSerpElementItem]]:
        """Create an instance of BaseBusinessDataSerpElementItem from a JSON string"""
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

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[GoogleBusinessInfoBusinessDataSerpElementItem, GoogleBusinessPostBusinessDataSerpElementItem, GoogleReviewsSearchBusinessDataSerpElementItem, MapsSearchBusinessDataSerpElementItem, TripadvisorReviewSearchBusinessDataSerpElementItem, TripadvisorSearchOrganicBusinessDataSerpElementItem, TrustpilotReviewSearchBusinessDataSerpElementItem, TrustpilotSearchOrganicBusinessDataSerpElementItem]]:
        """Create an instance of BaseBusinessDataSerpElementItem from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'GoogleBusinessInfoBusinessDataSerpElementItem':
            return import_module("dataforseo_client.models.google_business_info_business_data_serp_element_item").GoogleBusinessInfoBusinessDataSerpElementItem.from_dict(obj)
        if object_type ==  'GoogleBusinessPostBusinessDataSerpElementItem':
            return import_module("dataforseo_client.models.google_business_post_business_data_serp_element_item").GoogleBusinessPostBusinessDataSerpElementItem.from_dict(obj)
        if object_type ==  'GoogleReviewsSearchBusinessDataSerpElementItem':
            return import_module("dataforseo_client.models.google_reviews_search_business_data_serp_element_item").GoogleReviewsSearchBusinessDataSerpElementItem.from_dict(obj)
        if object_type ==  'MapsSearchBusinessDataSerpElementItem':
            return import_module("dataforseo_client.models.maps_search_business_data_serp_element_item").MapsSearchBusinessDataSerpElementItem.from_dict(obj)
        if object_type ==  'TripadvisorReviewSearchBusinessDataSerpElementItem':
            return import_module("dataforseo_client.models.tripadvisor_review_search_business_data_serp_element_item").TripadvisorReviewSearchBusinessDataSerpElementItem.from_dict(obj)
        if object_type ==  'TripadvisorSearchOrganicBusinessDataSerpElementItem':
            return import_module("dataforseo_client.models.tripadvisor_search_organic_business_data_serp_element_item").TripadvisorSearchOrganicBusinessDataSerpElementItem.from_dict(obj)
        if object_type ==  'TrustpilotReviewSearchBusinessDataSerpElementItem':
            return import_module("dataforseo_client.models.trustpilot_review_search_business_data_serp_element_item").TrustpilotReviewSearchBusinessDataSerpElementItem.from_dict(obj)
        if object_type ==  'TrustpilotSearchOrganicBusinessDataSerpElementItem':
            return import_module("dataforseo_client.models.trustpilot_search_organic_business_data_serp_element_item").TrustpilotSearchOrganicBusinessDataSerpElementItem.from_dict(obj)

        raise ValueError("BaseBusinessDataSerpElementItem failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


