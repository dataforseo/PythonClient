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
from dataforseo_client.models.avg_backlinks_info import AvgBacklinksInfo
from dataforseo_client.models.clickstream_keyword_info import ClickstreamKeywordInfo
from dataforseo_client.models.keyword_info import KeywordInfo
from dataforseo_client.models.keyword_info_normalized_with_info import KeywordInfoNormalizedWithInfo
from dataforseo_client.models.keyword_properties import KeywordProperties
from dataforseo_client.models.search_intent_info import SearchIntentInfo
from dataforseo_client.models.serp_info import SerpInfo
from typing import Optional, Set
from typing_extensions import Self

class KeywordDataInfo(BaseModel):
    """
    KeywordDataInfo
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    keyword: Optional[StrictStr] = Field(default=None, description="returned keyword idea")
    location_code: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    keyword_info: Optional[KeywordInfo] = None
    keyword_info_normalized_with_bing: Optional[KeywordInfoNormalizedWithInfo] = None
    keyword_info_normalized_with_clickstream: Optional[KeywordInfoNormalizedWithInfo] = None
    clickstream_keyword_info: Optional[ClickstreamKeywordInfo] = None
    keyword_properties: Optional[KeywordProperties] = None
    serp_info: Optional[SerpInfo] = None
    avg_backlinks_info: Optional[AvgBacklinksInfo] = None
    search_intent_info: Optional[SearchIntentInfo] = None
    __properties: ClassVar[List[str]] = ["se_type", "keyword", "location_code", "language_code", "keyword_info", "keyword_info_normalized_with_bing", "keyword_info_normalized_with_clickstream", "clickstream_keyword_info", "keyword_properties", "serp_info", "avg_backlinks_info", "search_intent_info"]

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
        """Create an instance of KeywordDataInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of keyword_info
        if self.keyword_info:
            _dict['keyword_info'] = self.keyword_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keyword_info_normalized_with_bing
        if self.keyword_info_normalized_with_bing:
            _dict['keyword_info_normalized_with_bing'] = self.keyword_info_normalized_with_bing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keyword_info_normalized_with_clickstream
        if self.keyword_info_normalized_with_clickstream:
            _dict['keyword_info_normalized_with_clickstream'] = self.keyword_info_normalized_with_clickstream.to_dict()
        # override the default output from pydantic by calling `to_dict()` of clickstream_keyword_info
        if self.clickstream_keyword_info:
            _dict['clickstream_keyword_info'] = self.clickstream_keyword_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of keyword_properties
        if self.keyword_properties:
            _dict['keyword_properties'] = self.keyword_properties.to_dict()
        # override the default output from pydantic by calling `to_dict()` of serp_info
        if self.serp_info:
            _dict['serp_info'] = self.serp_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of avg_backlinks_info
        if self.avg_backlinks_info:
            _dict['avg_backlinks_info'] = self.avg_backlinks_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of search_intent_info
        if self.search_intent_info:
            _dict['search_intent_info'] = self.search_intent_info.to_dict()
        # set to None if se_type (nullable) is None
        # and model_fields_set contains the field
        if self.se_type is None and "se_type" in self.model_fields_set:
            _dict['se_type'] = None

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

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KeywordDataInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "keyword": obj.get("keyword"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "keyword_info": KeywordInfo.from_dict(obj["keyword_info"]) if obj.get("keyword_info") is not None else None,
            "keyword_info_normalized_with_bing": KeywordInfoNormalizedWithInfo.from_dict(obj["keyword_info_normalized_with_bing"]) if obj.get("keyword_info_normalized_with_bing") is not None else None,
            "keyword_info_normalized_with_clickstream": KeywordInfoNormalizedWithInfo.from_dict(obj["keyword_info_normalized_with_clickstream"]) if obj.get("keyword_info_normalized_with_clickstream") is not None else None,
            "clickstream_keyword_info": ClickstreamKeywordInfo.from_dict(obj["clickstream_keyword_info"]) if obj.get("clickstream_keyword_info") is not None else None,
            "keyword_properties": KeywordProperties.from_dict(obj["keyword_properties"]) if obj.get("keyword_properties") is not None else None,
            "serp_info": SerpInfo.from_dict(obj["serp_info"]) if obj.get("serp_info") is not None else None,
            "avg_backlinks_info": AvgBacklinksInfo.from_dict(obj["avg_backlinks_info"]) if obj.get("avg_backlinks_info") is not None else None,
            "search_intent_info": SearchIntentInfo.from_dict(obj["search_intent_info"]) if obj.get("search_intent_info") is not None else None
        })
        return _obj


