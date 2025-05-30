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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.keyword_kpi import KeywordKpi
from typing import Optional, Set
from typing_extensions import Self

class KeywordsDataBingKeywordPerformanceTaskGetResultInfo(BaseModel):
    """
    KeywordsDataBingKeywordPerformanceTaskGetResultInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword in a POST array")
    location_code: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="location code in a POST array if there is no data, then the value is null")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array if there is no data, then the value is null")
    year: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="indicates the year for which the data is provided for example: 2020")
    month: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="indicates the month for which the data is provided for example: 10")
    keyword_kpi: Optional[KeywordKpi] = None
    __properties: ClassVar[List[str]] = ["keyword", "location_code", "language_code", "year", "month", "keyword_kpi"]

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
        """Create an instance of KeywordsDataBingKeywordPerformanceTaskGetResultInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of keyword_kpi
        if self.keyword_kpi:
            _dict['keyword_kpi'] = self.keyword_kpi.to_dict()
        # set to None if keyword (nullable) is None
        # and model_fields_set contains the field
        if self.keyword is None and "keyword" in self.model_fields_set:
            _dict['keyword'] = None

        # set to None if location_code (nullable) is None
        # and model_fields_set contains the field
        if self.location_code is None and "location_code" in self.model_fields_set:
            _dict['location_code'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if year (nullable) is None
        # and model_fields_set contains the field
        if self.year is None and "year" in self.model_fields_set:
            _dict['year'] = None

        # set to None if month (nullable) is None
        # and model_fields_set contains the field
        if self.month is None and "month" in self.model_fields_set:
            _dict['month'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KeywordsDataBingKeywordPerformanceTaskGetResultInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "year": obj.get("year"),
            "month": obj.get("month"),
            "keyword_kpi": KeywordKpi.from_dict(obj["keyword_kpi"]) if obj.get("keyword_kpi") is not None else None
        })
        return _obj


