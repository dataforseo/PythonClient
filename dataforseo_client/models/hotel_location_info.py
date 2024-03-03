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

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.location_chain import LocationChain
from typing import Optional, Set
from typing_extensions import Self

class HotelLocationInfo(BaseModel):
    """
    HotelLocationInfo
    """ # noqa: E501
    neighborhood: Optional[StrictStr] = Field(default=None, description="name of the neighborhood where the hotel is located")
    neighborhood_description: Optional[StrictStr] = Field(default=None, description="description of the neighborhood where the hotel is located")
    maps_url: Optional[StrictStr] = Field(default=None, description="url to the location of the hotel in google maps")
    overall_score: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="overall score of the hotel location indicates the overall score of the hotel’s location in the range from 1 to 5; calculated based on data from the hotel’s proximity to nearby things to do and restaurants, transportation, and airports; note that the criteria are not weighted equally in the overall score")
    score_by_categories: Optional[Dict[str, Optional[Union[StrictFloat, StrictInt]]]] = Field(default=None, description="category scores of the hotel location the scores of the hotel’s location tied to the categories that indicate the proximity to nearby things to do, restaurants, transportation, and airports;")
    latitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="hotel latitude latitude coordinates of the hotel’s location example: 39.4806397")
    longitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="hotel longitude latitude coordinates of the hotel’s location example: -106.0512973")
    location_chain: Optional[List[LocationChain]] = Field(default=None, description="elements of the location chain additional parameters of each element of the location chain")
    __properties: ClassVar[List[str]] = ["neighborhood", "neighborhood_description", "maps_url", "overall_score", "score_by_categories", "latitude", "longitude", "location_chain"]

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
        """Create an instance of HotelLocationInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in location_chain (list)
        _items = []
        if self.location_chain:
            for _item in self.location_chain:
                if _item:
                    _items.append(_item.to_dict())
            _dict['location_chain'] = _items
        # set to None if neighborhood (nullable) is None
        # and model_fields_set contains the field
        if self.neighborhood is None and "neighborhood" in self.model_fields_set:
            _dict['neighborhood'] = None

        # set to None if neighborhood_description (nullable) is None
        # and model_fields_set contains the field
        if self.neighborhood_description is None and "neighborhood_description" in self.model_fields_set:
            _dict['neighborhood_description'] = None

        # set to None if maps_url (nullable) is None
        # and model_fields_set contains the field
        if self.maps_url is None and "maps_url" in self.model_fields_set:
            _dict['maps_url'] = None

        # set to None if overall_score (nullable) is None
        # and model_fields_set contains the field
        if self.overall_score is None and "overall_score" in self.model_fields_set:
            _dict['overall_score'] = None

        # set to None if score_by_categories (nullable) is None
        # and model_fields_set contains the field
        if self.score_by_categories is None and "score_by_categories" in self.model_fields_set:
            _dict['score_by_categories'] = None

        # set to None if latitude (nullable) is None
        # and model_fields_set contains the field
        if self.latitude is None and "latitude" in self.model_fields_set:
            _dict['latitude'] = None

        # set to None if longitude (nullable) is None
        # and model_fields_set contains the field
        if self.longitude is None and "longitude" in self.model_fields_set:
            _dict['longitude'] = None

        # set to None if location_chain (nullable) is None
        # and model_fields_set contains the field
        if self.location_chain is None and "location_chain" in self.model_fields_set:
            _dict['location_chain'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HotelLocationInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "neighborhood": obj.get("neighborhood"),
            "neighborhood_description": obj.get("neighborhood_description"),
            "maps_url": obj.get("maps_url"),
            "overall_score": obj.get("overall_score"),
            "score_by_categories": obj.get("score_by_categories"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "location_chain": [LocationChain.from_dict(_item) for _item in obj["location_chain"]] if obj.get("location_chain") is not None else None
        })
        return _obj


