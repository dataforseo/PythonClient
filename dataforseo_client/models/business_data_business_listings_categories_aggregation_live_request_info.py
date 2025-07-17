from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BusinessDataBusinessListingsCategoriesAggregationLiveRequestInfo(BaseModel):
    """
    BusinessDataBusinessListingsCategoriesAggregationLiveRequestInfo
    """ # noqa: E501
    categories: Optional[List[Optional[StrictStr]]] = Field(default=None, description="business categories. optional field. the categories you specify are used to search for business listings;. if you don’t use this field, we will return business listings found in the specified location;. you can specify up to 10 categories")
    description: Optional[StrictStr] = Field(default=None, description="description of the element in SERP. optional field. the description of the business entity for which the results are collected;. can contain up to 200 characters")
    title: Optional[StrictStr] = Field(default=None, description="title of the element in SERP. optional field. the name of the business entity for which the results are collected;. can contain up to 200 characters")
    is_claimed: Optional[StrictBool] = Field(default=None, description="indicates whether the business is verified by its owner on Google Maps. optional field")
    location_coordinate: Optional[StrictStr] = Field(default=None, description="GPS coordinates of a location. optional field. location_coordinate parameter should be specified in the “latitude,longitude,radius” format. the maximum number of decimal digits for “latitude” and “longitude”: 7. the minimum value for “radius”: 1. the maximum value for “radius”: 100000. example:. 53.476225,-2.243572,200")
    initial_dataset_filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, not_regex, <, <=, >, >=, =, <>, in, not_in, like, not_like, match, not_match. you can use the % operator with like and not_like to match any string of zero or more characters. example:. ['rating.value','>',3]. you can receive the list of available filters by making a separate request to https://api.dataforseo.com/v3/business_data/business_listings/available_filters")
    internal_list_limit: Optional[StrictInt] = Field(default=None, description="maximum number of elements within internal arrays. optional field. you can use this field to limit the number of elements within the aggregated categories. default value: 10")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned businesses. optional field. default value: 100. maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="the maximum number of returned businesses. optional field")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "categories", 
        "description", 
        "title", 
        "is_claimed", 
        "location_coordinate", 
        "initial_dataset_filters", 
        "internal_list_limit", 
        "limit", 
        "offset", 
        "tag", 
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

        _dict['categories'] = self.categories
        _dict['description'] = self.description
        _dict['title'] = self.title
        _dict['is_claimed'] = self.is_claimed
        _dict['location_coordinate'] = self.location_coordinate
        _dict['initial_dataset_filters'] = self.initial_dataset_filters
        _dict['internal_list_limit'] = self.internal_list_limit
        _dict['limit'] = self.limit
        _dict['offset'] = self.offset
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
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
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj