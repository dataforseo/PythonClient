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

class KeywordsDataGoogleAdsSearchVolumeTaskPostRequestInfo(BaseModel):
    """
    KeywordsDataGoogleAdsSearchVolumeTaskPostRequestInfo
    """ # noqa: E501
    keywords: Optional[List[StrictStr]] = Field(default=None, description="keywords required field The maximum number of keywords you can specify: 1000 The maximum number of characters for each keyword: 80 The maximum number of words for each keyword phrase: 10 the keywords you specify will be converted to a lowercase format Note #1: Google Ads may return no data for certain groups of keywords; Note #2: Google Ads provides combined search volume values for groups of similar keywords to obtain search volume for similar keywords, we recommend submitting such keywords in separate requests; Note #3: Google Ads doesn’t allow using certain symbols and characters (e.g., UTF symbols, emojis), so you can’t use them when setting a task; to learn more about which symbols and characters can be used, please refer to this article learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location optional field if you do not indicate the location, you will receive worldwide results, i.e., for all available locations; if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/locations example: London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code optional field if you do not indicate the location, you will receive worldwide results, i.e., for all available locations; if you use this field, you don’t need to specify location_name or location_coordinate; you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/locations example: 2840")
    location_coordinate: Optional[StrictStr] = Field(default=None, description="GPS coordinates of a location optional field if you do not indicate the location, you will receive worldwide results, i.e., for all available locations; if you use this field, you don’t need to specify location_name or location_code; location_coordinate parameter should be specified in the “latitude,longitude” format; the data will be provided for the country the specified coordinates belong to; example: 52.6178549,-155.352142")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language optional field you can receive the list of available languages of the search engine with their language_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/languages example: English")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code optional field you can receive the list of available languages of the search engine with their language_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/google_ads/languages example: en")
    search_partners: Optional[StrictBool] = Field(default=None, description="include Google search partners optional field if you specify true, the results will be delivered for owned, operated, and syndicated networks across Google and partner sites that host Google search; default value: false – results are returned for Google search sites")
    date_from: Optional[StrictStr] = Field(default=None, description="starting date of the time range optional field date format: \"yyyy-mm-dd\" minimal value: 4 years from the current date by default, data is returned for the past 12 months; Note: the indicated date cannot be greater than that specified in date_to and/or yesterday’s date;if Status endpoint returns false in the actual_data field, date_from can be set to the month before last and prior; if Status endpoint returns true in the actual_data field, date_from can be set to the last month and prior")
    date_to: Optional[StrictStr] = Field(default=None, description="ending date of the time range optional field Note: the indicated date cannot be greater than the past month, Google Ads does not return data on the current month; if you don’t specify this field, yesterday’s date will be used by default date format: \"yyyy-mm-dd\" example: \"2022-11-30\"")
    include_adult_keywords: Optional[StrictBool] = Field(default=None, description="include keywords associated with adult content optional field if set to true, adult keywords will be included in the response default value: false note that the API may return no data for such keywords due to Google Ads restrictions")
    sort_by: Optional[StrictStr] = Field(default=None, description="results sorting parameters optional field use these parameters to sort the results by relevance, search_volume, competition_index, low_top_of_page_bid, or high_top_of_page_bid in the descending order default value: relevance")
    postback_url: Optional[StrictStr] = Field(default=None, description="return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id=$id http://your-server.com/postbackscript?id=$id&tag=$tag Note: special character in postback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center")
    pingback_url: Optional[StrictStr] = Field(default=None, description="notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request example: http://your-server.com/pingscript?id=$id http://your-server.com/pingscript?id=$id&tag=$tag Note: special character in pingback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data array of the response")
    __properties: ClassVar[List[str]] = ["keywords", "location_name", "location_code", "location_coordinate", "language_name", "language_code", "search_partners", "date_from", "date_to", "include_adult_keywords", "sort_by", "postback_url", "pingback_url", "tag"]

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
        """Create an instance of KeywordsDataGoogleAdsSearchVolumeTaskPostRequestInfo from a JSON string"""
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

        # set to None if language_name (nullable) is None
        # and model_fields_set contains the field
        if self.language_name is None and "language_name" in self.model_fields_set:
            _dict['language_name'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if search_partners (nullable) is None
        # and model_fields_set contains the field
        if self.search_partners is None and "search_partners" in self.model_fields_set:
            _dict['search_partners'] = None

        # set to None if date_from (nullable) is None
        # and model_fields_set contains the field
        if self.date_from is None and "date_from" in self.model_fields_set:
            _dict['date_from'] = None

        # set to None if date_to (nullable) is None
        # and model_fields_set contains the field
        if self.date_to is None and "date_to" in self.model_fields_set:
            _dict['date_to'] = None

        # set to None if include_adult_keywords (nullable) is None
        # and model_fields_set contains the field
        if self.include_adult_keywords is None and "include_adult_keywords" in self.model_fields_set:
            _dict['include_adult_keywords'] = None

        # set to None if sort_by (nullable) is None
        # and model_fields_set contains the field
        if self.sort_by is None and "sort_by" in self.model_fields_set:
            _dict['sort_by'] = None

        # set to None if postback_url (nullable) is None
        # and model_fields_set contains the field
        if self.postback_url is None and "postback_url" in self.model_fields_set:
            _dict['postback_url'] = None

        # set to None if pingback_url (nullable) is None
        # and model_fields_set contains the field
        if self.pingback_url is None and "pingback_url" in self.model_fields_set:
            _dict['pingback_url'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KeywordsDataGoogleAdsSearchVolumeTaskPostRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keywords": obj.get("keywords"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "location_coordinate": obj.get("location_coordinate"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "search_partners": obj.get("search_partners"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "include_adult_keywords": obj.get("include_adult_keywords"),
            "sort_by": obj.get("sort_by"),
            "postback_url": obj.get("postback_url"),
            "pingback_url": obj.get("pingback_url"),
            "tag": obj.get("tag")
        })
        return _obj


