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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SearchVolumeHistoryItemInfo(BaseModel):
    """
    device type = desktop contains historical search volume data for searches made from desktop devices
    """ # noqa: E501
    year: Optional[StrictInt] = Field(default=None, description="year")
    month: Optional[StrictInt] = Field(default=None, description="month")
    day: Optional[StrictInt] = Field(default=None, description="day of the month")
    search_volume: Optional[StrictInt] = Field(default=None, description="search volume rate")
    __properties: ClassVar[List[str]] = ["year", "month", "day", "search_volume"]

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
        """Create an instance of SearchVolumeHistoryItemInfo from a JSON string"""
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
        # set to None if year (nullable) is None
        # and model_fields_set contains the field
        if self.year is None and "year" in self.model_fields_set:
            _dict['year'] = None

        # set to None if month (nullable) is None
        # and model_fields_set contains the field
        if self.month is None and "month" in self.model_fields_set:
            _dict['month'] = None

        # set to None if day (nullable) is None
        # and model_fields_set contains the field
        if self.day is None and "day" in self.model_fields_set:
            _dict['day'] = None

        # set to None if search_volume (nullable) is None
        # and model_fields_set contains the field
        if self.search_volume is None and "search_volume" in self.model_fields_set:
            _dict['search_volume'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SearchVolumeHistoryItemInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "year": obj.get("year"),
            "month": obj.get("month"),
            "day": obj.get("day"),
            "search_volume": obj.get("search_volume")
        })
        return _obj


