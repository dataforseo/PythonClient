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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AppDataGoogleLocationsResultInfo(BaseModel):
    """
    AppDataGoogleLocationsResultInfo
    """ # noqa: E501
    location_code: Optional[StrictInt] = Field(default=None, description="location code")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location")
    location_name_parent: Optional[StrictStr] = Field(default=None, description="the name of the superordinate location example: \"location_code\": 1006473, \"location_name\": \"Altrincham,England,United Kingdom\", \"location_name_parent\": \"England,United Kingdom\", where location_name_parent corresponds to: \"location_code\": 20339, \"location_name\": \"England,United Kingdom\"")
    country_iso_code: Optional[StrictStr] = Field(default=None, description="ISO country code of the location")
    location_type: Optional[StrictStr] = Field(default=None, description="location type")
    __properties: ClassVar[List[str]] = ["location_code", "location_name", "location_name_parent", "country_iso_code", "location_type"]

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
        """Create an instance of AppDataGoogleLocationsResultInfo from a JSON string"""
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
        # set to None if location_code (nullable) is None
        # and model_fields_set contains the field
        if self.location_code is None and "location_code" in self.model_fields_set:
            _dict['location_code'] = None

        # set to None if location_name (nullable) is None
        # and model_fields_set contains the field
        if self.location_name is None and "location_name" in self.model_fields_set:
            _dict['location_name'] = None

        # set to None if location_name_parent (nullable) is None
        # and model_fields_set contains the field
        if self.location_name_parent is None and "location_name_parent" in self.model_fields_set:
            _dict['location_name_parent'] = None

        # set to None if country_iso_code (nullable) is None
        # and model_fields_set contains the field
        if self.country_iso_code is None and "country_iso_code" in self.model_fields_set:
            _dict['country_iso_code'] = None

        # set to None if location_type (nullable) is None
        # and model_fields_set contains the field
        if self.location_type is None and "location_type" in self.model_fields_set:
            _dict['location_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppDataGoogleLocationsResultInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "location_code": obj.get("location_code"),
            "location_name": obj.get("location_name"),
            "location_name_parent": obj.get("location_name_parent"),
            "country_iso_code": obj.get("country_iso_code"),
            "location_type": obj.get("location_type")
        })
        return _obj


