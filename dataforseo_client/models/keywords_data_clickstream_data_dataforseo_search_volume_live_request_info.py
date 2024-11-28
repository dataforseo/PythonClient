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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class KeywordsDataClickstreamDataDataforseoSearchVolumeLiveRequestInfo(BaseModel):
    """
    KeywordsDataClickstreamDataDataforseoSearchVolumeLiveRequestInfo
    """ # noqa: E501
    keywords: Optional[List[StrictStr]] = Field(default=None, description="target keywords required field UTF-8 encoding maximum number of keywords you can specify in this array: 1000 the keywords will be converted to lowercase format Note: certain symbols and characters (e.g., UTF symbols, emojis) are not allowed to learn more about which symbols and characters can be used, please refer to this article learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location required field if you don’t specify location_code  you can receive the list of available locations with location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/clickstream_data/locations_and_languages example: London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code required field if you don’t specify location_name if you use this field, you can receive the list of available locations with location_code by making a separate request to the https://api.dataforseo.com/v3/keywords_data/clickstream_data/locations_and_languages example: 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language required field if don’t specify language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/keywords_data/clickstream_data/locations_and_languages example: English")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code required field if don’t specify language_name you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/keywords_data/clickstream_data/locations_and_languages example: en")
    use_clickstream: Optional[StrictBool] = Field(default=None, description="use clickstream data to provide results optional field if set to true, you will get DataForSEO search volume values based on clickstream data; if set to false, Bing search volume data will be used to calculate DataForSEO search volume; default value: true; Note: some locations may not be available for calculating Bing search volume, in this case search volume will be calculated based on clickstream data even if you set this parameter to false")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = ["keywords", "location_name", "location_code", "language_name", "language_code", "use_clickstream", "tag"]

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
        """Create an instance of KeywordsDataClickstreamDataDataforseoSearchVolumeLiveRequestInfo from a JSON string"""
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

        # set to None if language_name (nullable) is None
        # and model_fields_set contains the field
        if self.language_name is None and "language_name" in self.model_fields_set:
            _dict['language_name'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if use_clickstream (nullable) is None
        # and model_fields_set contains the field
        if self.use_clickstream is None and "use_clickstream" in self.model_fields_set:
            _dict['use_clickstream'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KeywordsDataClickstreamDataDataforseoSearchVolumeLiveRequestInfo from a dict"""
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
            "use_clickstream": obj.get("use_clickstream"),
            "tag": obj.get("tag")
        })
        return _obj


