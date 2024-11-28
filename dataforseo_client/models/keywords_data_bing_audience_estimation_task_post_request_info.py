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
from typing import Optional, Set
from typing_extensions import Self

class KeywordsDataBingAudienceEstimationTaskPostRequestInfo(BaseModel):
    """
    KeywordsDataBingAudienceEstimationTaskPostRequestInfo
    """ # noqa: E501
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/locations example: London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/locations example: 2840")
    location_coordinate: Optional[StrictStr] = Field(default=None, description="GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude,radius (in km)” format the data will be provided for the country the specified coordinates belong to example: 29.6821525,-82.4098881,100")
    age: Optional[List[StrictStr]] = Field(default=None, description="selection of age ranges for targeting possible values: eighteen_to_twenty_four, fifty_to_sixty_four, sixty_five_and_above, thirteen_to_seventeen, thirty_five_to_forty_nine, twenty_five_to_thirty_four, unknown, zero_to_twelve")
    bid: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="desired bid setting value in USD maximum value: 1000")
    daily_budget: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="daily campaign budget value in USD maximum value: 10000")
    gender: Optional[List[StrictStr]] = Field(default=None, description="gender to target possible values: male, female, unknown")
    industry: Optional[List[StrictStr]] = Field(default=None, description="industry of LinkedIn profile targeting if you use this field, you can receive the list of available industry names  with industry_id by making a separate request to the https://api.dataforseo.com/v3/keywords_data/bing/audience_estimation/industries example: 806301758")
    job_function: Optional[List[StrictStr]] = Field(default=None, description="job function of LinkedIn profile targeting if you use this field, you can receive the list of available job function names  with job_function_id by making a separate request to the https://api.dataforseo.com/v3/keywords_data/bing/audience_estimation/job_functions example: 806300451")
    __properties: ClassVar[List[str]] = ["location_name", "location_code", "location_coordinate", "age", "bid", "daily_budget", "gender", "industry", "job_function"]

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
        """Create an instance of KeywordsDataBingAudienceEstimationTaskPostRequestInfo from a JSON string"""
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
        # set to None if location_name (nullable) is None
        # and model_fields_set contains the field
        if self.location_name is None and "location_name" in self.model_fields_set:
            _dict['location_name'] = None

        # set to None if location_code (nullable) is None
        # and model_fields_set contains the field
        if self.location_code is None and "location_code" in self.model_fields_set:
            _dict['location_code'] = None

        # set to None if location_coordinate (nullable) is None
        # and model_fields_set contains the field
        if self.location_coordinate is None and "location_coordinate" in self.model_fields_set:
            _dict['location_coordinate'] = None

        # set to None if age (nullable) is None
        # and model_fields_set contains the field
        if self.age is None and "age" in self.model_fields_set:
            _dict['age'] = None

        # set to None if bid (nullable) is None
        # and model_fields_set contains the field
        if self.bid is None and "bid" in self.model_fields_set:
            _dict['bid'] = None

        # set to None if daily_budget (nullable) is None
        # and model_fields_set contains the field
        if self.daily_budget is None and "daily_budget" in self.model_fields_set:
            _dict['daily_budget'] = None

        # set to None if gender (nullable) is None
        # and model_fields_set contains the field
        if self.gender is None and "gender" in self.model_fields_set:
            _dict['gender'] = None

        # set to None if industry (nullable) is None
        # and model_fields_set contains the field
        if self.industry is None and "industry" in self.model_fields_set:
            _dict['industry'] = None

        # set to None if job_function (nullable) is None
        # and model_fields_set contains the field
        if self.job_function is None and "job_function" in self.model_fields_set:
            _dict['job_function'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KeywordsDataBingAudienceEstimationTaskPostRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "location_coordinate": obj.get("location_coordinate"),
            "age": obj.get("age"),
            "bid": obj.get("bid"),
            "daily_budget": obj.get("daily_budget"),
            "gender": obj.get("gender"),
            "industry": obj.get("industry"),
            "job_function": obj.get("job_function")
        })
        return _obj


