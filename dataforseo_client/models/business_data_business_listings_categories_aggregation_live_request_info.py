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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class BusinessDataBusinessListingsCategoriesAggregationLiveRequestInfo(BaseModel):
    """
    BusinessDataBusinessListingsCategoriesAggregationLiveRequestInfo
    """ # noqa: E501
    categories: Optional[List[StrictStr]] = Field(default=None, description="business categories optional field the categories you specify are used to search for business listings; if you don’t use this field, we will return business listings found in the specified location; you can specify up to 10 categories")
    description: Optional[StrictStr] = Field(default=None, description="description of the element in SERP optional field the description of the business entity for which the results are collected; can contain up to 200 characters")
    title: Optional[StrictStr] = Field(default=None, description="title of the element in SERP optional field the name of the business entity for which the results are collected; can contain up to 200 characters")
    is_claimed: Optional[StrictBool] = Field(default=None, description="indicates whether the business is verified by its owner on Google Maps optional field")
    location_coordinate: Optional[StrictStr] = Field(default=None, description="GPS coordinates of a location optional field location_coordinate parameter should be specified in the “latitude,longitude,radius” format the maximum number of decimal digits for “latitude” and “longitude”: 7 the minimum value for “radius”: 1 the maximum value for “radius”: 100000 example: 53.476225,-2.243572,200")
    initial_dataset_filters: Optional[List[Optional[Dict[str, Any]]]] = Field(default=None, description="array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, <, <=, >, >=, =, <>, in, not_in, like, not_like you can use the % operator with like and not_like to match any string of zero or more characters example: [\"rating.value\",\">\",3] you can receive the list of available filters by making a separate request to https://api.dataforseo.com/v3/business_data/business_listings/available_filters")
    internal_list_limit: Optional[StrictInt] = Field(default=None, description="maximum number of elements within internal arrays optional field you can use this field to limit the number of elements within the aggregated categories default value: 10")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned businesses optional field default value: 100 maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="the maximum number of returned businesses optional field")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = ["categories", "description", "title", "is_claimed", "location_coordinate", "initial_dataset_filters", "internal_list_limit", "limit", "offset", "tag"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BusinessDataBusinessListingsCategoriesAggregationLiveRequestInfo from a JSON string"""
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
        # set to None if categories (nullable) is None
        # and model_fields_set contains the field
        if self.categories is None and "categories" in self.model_fields_set:
            _dict['categories'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if is_claimed (nullable) is None
        # and model_fields_set contains the field
        if self.is_claimed is None and "is_claimed" in self.model_fields_set:
            _dict['is_claimed'] = None

        # set to None if location_coordinate (nullable) is None
        # and model_fields_set contains the field
        if self.location_coordinate is None and "location_coordinate" in self.model_fields_set:
            _dict['location_coordinate'] = None

        # set to None if initial_dataset_filters (nullable) is None
        # and model_fields_set contains the field
        if self.initial_dataset_filters is None and "initial_dataset_filters" in self.model_fields_set:
            _dict['initial_dataset_filters'] = None

        # set to None if internal_list_limit (nullable) is None
        # and model_fields_set contains the field
        if self.internal_list_limit is None and "internal_list_limit" in self.model_fields_set:
            _dict['internal_list_limit'] = None

        # set to None if limit (nullable) is None
        # and model_fields_set contains the field
        if self.limit is None and "limit" in self.model_fields_set:
            _dict['limit'] = None

        # set to None if offset (nullable) is None
        # and model_fields_set contains the field
        if self.offset is None and "offset" in self.model_fields_set:
            _dict['offset'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BusinessDataBusinessListingsCategoriesAggregationLiveRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "categories": obj.get("categories"),
            "description": obj.get("description"),
            "title": obj.get("title"),
            "is_claimed": obj.get("is_claimed"),
            "location_coordinate": obj.get("location_coordinate"),
            "initial_dataset_filters": obj.get("initial_dataset_filters"),
            "internal_list_limit": obj.get("internal_list_limit"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "tag": obj.get("tag")
        })
        return _obj


