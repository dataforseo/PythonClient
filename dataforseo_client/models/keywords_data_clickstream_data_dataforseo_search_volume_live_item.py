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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.monthly_searches import MonthlySearches
from typing import Optional, Set
from typing_extensions import Self

class KeywordsDataClickstreamDataDataforseoSearchVolumeLiveItem(BaseModel):
    """
    KeywordsDataClickstreamDataDataforseoSearchVolumeLiveItem
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword provided in the POST array")
    use_clickstream: Optional[StrictBool] = Field(default=None, description="indicates if the use_clickstream parameter is active possible values: true, false")
    search_volume: Optional[StrictInt] = Field(default=None, description="current search volume rate of a keyword")
    monthly_searches: Optional[List[MonthlySearches]] = Field(default=None, description="monthly search volume rates array of objects with search volume rates in a certain month of a year")
    __properties: ClassVar[List[str]] = ["keyword", "use_clickstream", "search_volume", "monthly_searches"]

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
        """Create an instance of KeywordsDataClickstreamDataDataforseoSearchVolumeLiveItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in monthly_searches (list)
        _items = []
        if self.monthly_searches:
            for _item in self.monthly_searches:
                if _item:
                    _items.append(_item.to_dict())
            _dict['monthly_searches'] = _items
        # set to None if keyword (nullable) is None
        # and model_fields_set contains the field
        if self.keyword is None and "keyword" in self.model_fields_set:
            _dict['keyword'] = None

        # set to None if use_clickstream (nullable) is None
        # and model_fields_set contains the field
        if self.use_clickstream is None and "use_clickstream" in self.model_fields_set:
            _dict['use_clickstream'] = None

        # set to None if search_volume (nullable) is None
        # and model_fields_set contains the field
        if self.search_volume is None and "search_volume" in self.model_fields_set:
            _dict['search_volume'] = None

        # set to None if monthly_searches (nullable) is None
        # and model_fields_set contains the field
        if self.monthly_searches is None and "monthly_searches" in self.model_fields_set:
            _dict['monthly_searches'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KeywordsDataClickstreamDataDataforseoSearchVolumeLiveItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "use_clickstream": obj.get("use_clickstream"),
            "search_volume": obj.get("search_volume"),
            "monthly_searches": [MonthlySearches.from_dict(_item) for _item in obj["monthly_searches"]] if obj.get("monthly_searches") is not None else None
        })
        return _obj

