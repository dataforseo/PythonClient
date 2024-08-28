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

from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class KeywordsDataGoogleTrendsExploreLiveRequestInfo(BaseModel):
    """
    KeywordsDataGoogleTrendsExploreLiveRequestInfo
    """ # noqa: E501
    keywords: Optional[List[StrictStr]] = Field(default=None, description="keywords optional field if keywords are not specified, the results will not contain keyword-related data; The maximum number of keywords you can specify: 5 Note: comma symbols (,) in the specified keywords will be unset and ignored")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location optional field if you don’t use this field, you will recieve global results if you use this field, you don’t need to specify location_code you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_trends/locations example: United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code optional field if you don’t use this field, you will recieve global results if you use this field, you don’t need to specify location_name you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_trends/locations example: 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language optional field default value: English if you use this field, you don’t need to specify language_code you can receive the list of available languages of the search engine with their language_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_trends/languages example: English")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code optional field default value: en if you use this field, you don’t need to specify language_name you can receive the list of available languages of the search engine with their language_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_trends/languages example: en")
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    category_code: Optional[StrictInt] = Field(default=None, description="google trends search category optional field if you don’t specify this field, the 0 value will be applied by default and the search will be carried out across all available categories you can receive the list of available categories with their category_code by making a separate request to the https://api.dataforseo.com/v3/keywords_data/google_trends/categories")
    date_from: Optional[StrictStr] = Field(default=None, description="starting date of the time range optional field if you don’t specify this field, the current day and month of the preceding year will be used by default minimal value for the web type: 2004-01-01 minimal value for other types: 2008-01-01 date format: \"yyyy-mm-dd\" example: \"2019-01-15\"")
    date_to: Optional[StrictStr] = Field(default=None, description="ending date of the time range optional field if you don’t specify this field, the today’s date will be used by default date format: \"yyyy-mm-dd\" example: \"2019-01-15\"")
    time_range: Optional[StrictStr] = Field(default=None, description="preset time ranges optional field if you specify date_from or date_to parameters, this field will be ignored when setting a task possible values for all type parameters: past_hour, past_4_hours, past_day, past_7_days, past_30_days, past_90_days, past_12_months, past_5_years possible values for web only: 2004_present possible values for news, youtube, images, froogle: 2008_present")
    item_types: Optional[List[StrictStr]] = Field(default=None, description="types of items returned optional field to speed up the execution of the request, specify one item at a time; possible values: \"google_trends_graph\", \"google_trends_map\", \"google_trends_topics_list\",\"google_trends_queries_list\" default value: \"google_trends_graph\"")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = ["keywords", "location_name", "location_code", "language_name", "language_code", "type", "category_code", "date_from", "date_to", "time_range", "item_types", "tag"]

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
        """Create an instance of KeywordsDataGoogleTrendsExploreLiveRequestInfo from a JSON string"""
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
        # set to None if keywords (nullable) is None
        # and model_fields_set contains the field
        if self.keywords is None and "keywords" in self.model_fields_set:
            _dict['keywords'] = None

        # set to None if location_name (nullable) is None
        # and model_fields_set contains the field
        if self.location_name is None and "location_name" in self.model_fields_set:
            _dict['location_name'] = None

        # set to None if location_code (nullable) is None
        # and model_fields_set contains the field
        if self.location_code is None and "location_code" in self.model_fields_set:
            _dict['location_code'] = None

        # set to None if language_name (nullable) is None
        # and model_fields_set contains the field
        if self.language_name is None and "language_name" in self.model_fields_set:
            _dict['language_name'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if category_code (nullable) is None
        # and model_fields_set contains the field
        if self.category_code is None and "category_code" in self.model_fields_set:
            _dict['category_code'] = None

        # set to None if date_from (nullable) is None
        # and model_fields_set contains the field
        if self.date_from is None and "date_from" in self.model_fields_set:
            _dict['date_from'] = None

        # set to None if date_to (nullable) is None
        # and model_fields_set contains the field
        if self.date_to is None and "date_to" in self.model_fields_set:
            _dict['date_to'] = None

        # set to None if time_range (nullable) is None
        # and model_fields_set contains the field
        if self.time_range is None and "time_range" in self.model_fields_set:
            _dict['time_range'] = None

        # set to None if item_types (nullable) is None
        # and model_fields_set contains the field
        if self.item_types is None and "item_types" in self.model_fields_set:
            _dict['item_types'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KeywordsDataGoogleTrendsExploreLiveRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keywords": obj.get("keywords"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "type": obj.get("type"),
            "category_code": obj.get("category_code"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "time_range": obj.get("time_range"),
            "item_types": obj.get("item_types"),
            "tag": obj.get("tag")
        })
        return _obj


