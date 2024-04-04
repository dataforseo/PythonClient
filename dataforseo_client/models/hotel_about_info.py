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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.hotel_amenity_info import HotelAmenityInfo
from dataforseo_client.models.hotel_amenity_item_info import HotelAmenityItemInfo
from dataforseo_client.models.work_time_info import WorkTimeInfo
from typing import Optional, Set
from typing_extensions import Self

class HotelAboutInfo(BaseModel):
    """
    HotelAboutInfo
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="description of the hotel the description of the hotel entity for which the results are collected")
    sub_descriptions: Optional[List[Optional[StrictStr]]] = Field(default=None, description="additional description of the hotel details about the hotel provided in addition to the description")
    check_in_time: Optional[WorkTimeInfo] = None
    check_out_time: Optional[WorkTimeInfo] = None
    full_address: Optional[StrictStr] = Field(default=None, description="full address of the hotel address of the hotel indicated in the standardised format")
    domain: Optional[StrictStr] = Field(default=None, description="hotel domain domain of the hotel’s website")
    url: Optional[StrictStr] = Field(default=None, description="hotel url URL to the hotel’s website indicated in the listing")
    amenities: Optional[List[HotelAmenityInfo]] = Field(default=None, description="hotel amenities information about hotel amenities")
    popular_amenities: Optional[List[HotelAmenityItemInfo]] = Field(default=None, description="hotel amenities information about hotel amenities labelled as “popular”")
    __properties: ClassVar[List[str]] = ["description", "sub_descriptions", "check_in_time", "check_out_time", "full_address", "domain", "url", "amenities", "popular_amenities"]

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
        """Create an instance of HotelAboutInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of check_in_time
        if self.check_in_time:
            _dict['check_in_time'] = self.check_in_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of check_out_time
        if self.check_out_time:
            _dict['check_out_time'] = self.check_out_time.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in amenities (list)
        _items = []
        if self.amenities:
            for _item in self.amenities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['amenities'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in popular_amenities (list)
        _items = []
        if self.popular_amenities:
            for _item in self.popular_amenities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['popular_amenities'] = _items
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if sub_descriptions (nullable) is None
        # and model_fields_set contains the field
        if self.sub_descriptions is None and "sub_descriptions" in self.model_fields_set:
            _dict['sub_descriptions'] = None

        # set to None if full_address (nullable) is None
        # and model_fields_set contains the field
        if self.full_address is None and "full_address" in self.model_fields_set:
            _dict['full_address'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if amenities (nullable) is None
        # and model_fields_set contains the field
        if self.amenities is None and "amenities" in self.model_fields_set:
            _dict['amenities'] = None

        # set to None if popular_amenities (nullable) is None
        # and model_fields_set contains the field
        if self.popular_amenities is None and "popular_amenities" in self.model_fields_set:
            _dict['popular_amenities'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HotelAboutInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "sub_descriptions": obj.get("sub_descriptions"),
            "check_in_time": WorkTimeInfo.from_dict(obj["check_in_time"]) if obj.get("check_in_time") is not None else None,
            "check_out_time": WorkTimeInfo.from_dict(obj["check_out_time"]) if obj.get("check_out_time") is not None else None,
            "full_address": obj.get("full_address"),
            "domain": obj.get("domain"),
            "url": obj.get("url"),
            "amenities": [HotelAmenityInfo.from_dict(_item) for _item in obj["amenities"]] if obj.get("amenities") is not None else None,
            "popular_amenities": [HotelAmenityItemInfo.from_dict(_item) for _item in obj["popular_amenities"]] if obj.get("popular_amenities") is not None else None
        })
        return _obj


