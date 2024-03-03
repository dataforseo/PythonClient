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
from dataforseo_client.models.base_app_data_serp_element_item import BaseAppDataSerpElementItem
from dataforseo_client.models.keyword_data import KeywordData
from typing import Optional, Set
from typing_extensions import Self

class DataforseoLabsleAppIntersectionLiveItem(BaseModel):
    """
    DataforseoLabsleAppIntersectionLiveItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    keyword_data: Optional[KeywordData] = None
    intersection_result: Optional[Dict[str, BaseAppDataSerpElementItem]] = Field(default=None, description="contains SERP data for the returned keyword data will be provided in separate arrays for each app ID you specified in the app_ids object when setting a task; depending on the number of specified app IDs, it can contain from 1 to 20 arrays named respectively")
    __properties: ClassVar[List[str]] = ["se_type", "keyword_data", "intersection_result"]

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
        """Create an instance of DataforseoLabsleAppIntersectionLiveItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of keyword_data
        if self.keyword_data:
            _dict['keyword_data'] = self.keyword_data.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in intersection_result (dict)
        _field_dict = {}
        if self.intersection_result:
            for _key in self.intersection_result:
                if self.intersection_result[_key]:
                    _field_dict[_key] = self.intersection_result[_key].to_dict()
            _dict['intersection_result'] = _field_dict
        # set to None if se_type (nullable) is None
        # and model_fields_set contains the field
        if self.se_type is None and "se_type" in self.model_fields_set:
            _dict['se_type'] = None

        # set to None if intersection_result (nullable) is None
        # and model_fields_set contains the field
        if self.intersection_result is None and "intersection_result" in self.model_fields_set:
            _dict['intersection_result'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataforseoLabsleAppIntersectionLiveItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "keyword_data": KeywordData.from_dict(obj["keyword_data"]) if obj.get("keyword_data") is not None else None,
            "intersection_result": dict(
                (_k, BaseAppDataSerpElementItem.from_dict(_v))
                for _k, _v in obj["intersection_result"].items()
            )
            if obj.get("intersection_result") is not None
            else None
        })
        return _obj


