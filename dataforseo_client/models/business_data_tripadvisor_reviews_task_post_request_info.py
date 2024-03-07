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

class BusinessDataTripadvisorReviewsTaskPostRequestInfo(BaseModel):
    """
    BusinessDataTripadvisorReviewsTaskPostRequestInfo
    """ # noqa: E501
    url_path: Optional[StrictStr] = Field(default=None, description="URL path of the business entity required field if you do not specify keyword URL path to the Tripadvisor page of the business entity; can be found in the URL of the business entity on Tripadvisor example: Hotel_Review-g60763-d23462501-Reviews-Margaritaville_Times_Square-New_York_City_New_York.html https://www.tripadvisor.com/Hotel_Review-g60763-d23462501-Reviews-Margaritaville_Times_Square-New_York_City_New_York.html")
    keyword: Optional[StrictStr] = Field(default=None, description="keyword required field if you do not specify url_path the keyword you specify should indicate a name of an existing business or prominent place on Tripadvisor; you can specify up to 700 symbols in the keyword filed; all %## will be decoded (plus symbol ‘+’ will be decoded to a space character); if you need to use the “%” symbol for your keyword, please specify it as “%25”")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location required field if you don’t specify location_code or url_path you can receive the list of available locations with location_name by making a separate request to the https://api.dataforseo.com/v3/business_data/tripadvisor/locations example: London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code required field if you don’t specify location_name or url_path you can receive the list of available locations with location_code by making a separate request to the https://api.dataforseo.com/v3/business_data/tripadvisor/locations example: 1003854")
    priority: Optional[StrictInt] = Field(default=None, description="task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page.")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language optional field if you use this field, your account will be charged for one extra request you can receive the list of available languages with language_name by making a separate request to the https://api.dataforseo.com/v3/business_data/tripadvisor/languages example: English You will be additionally charged for setting a language parameter in this endpoint. The cost can be calculated on the Pricing page.")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code optional field if you use this field, your account will be charged for one extra request you can receive the list of available languages with language_code by making a separate request to the https://api.dataforseo.com/v3/business_data/tripadvisor/languages example: en You will be additionally charged for setting a language parameter in this endpoint. The cost can be calculated on the Pricing page.")
    depth: Optional[StrictInt] = Field(default=None, description="parsing depth optional field number of reviews in SERP we strongly recommend setting the parsing depth in the multiples of ten, because our systems processes ten reviews in a row default value: 10")
    ratings: Optional[List[StrictStr]] = Field(default=None, description="Tripadvisor traveler rating for a place of interest optional field rating based on the written reviews by a traveler after they visited a place. possible values: excellent, very_good, average, poor, terrible you can specify several values at once")
    visit_type: Optional[List[StrictStr]] = Field(default=None, description="filter by type of travelers who left a review optional field possible values: families, couples, solo, business, friends you can specify several values at once")
    months: Optional[List[StrictStr]] = Field(default=None, description="filter by months when a traveler made a visit optional field possible values: january, february, march, april, may, april, june, july, august, september, october, november, december you can specify several values at once")
    search_reviews_keyword: Optional[StrictStr] = Field(default=None, description="search reviews containing a specified keyword example: dessert")
    sort_by: Optional[StrictStr] = Field(default=None, description="results sorting parameters optional field you can use this field to sort the results; possible types of sorting: most_recent detailed_reviews")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response")
    postback_url: Optional[StrictStr] = Field(default=None, description="return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id=$id http://your-server.com/postbackscript?id=$id&tag=$tag Note: special symbols in postback_url will be urlencoded; i.a., the # symbol will be encoded into %23")
    pingback_url: Optional[StrictStr] = Field(default=None, description="notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id=$id http://your-server.com/pingscript?id=$id&tag=$tag Note: special symbols in pingback_url will be urlencoded; i.a., the # symbol will be encoded into %23")
    __properties: ClassVar[List[str]] = ["url_path", "keyword", "location_name", "location_code", "priority", "language_name", "language_code", "depth", "ratings", "visit_type", "months", "search_reviews_keyword", "sort_by", "tag", "postback_url", "pingback_url"]

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
        """Create an instance of BusinessDataTripadvisorReviewsTaskPostRequestInfo from a JSON string"""
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
        # set to None if url_path (nullable) is None
        # and model_fields_set contains the field
        if self.url_path is None and "url_path" in self.model_fields_set:
            _dict['url_path'] = None

        # set to None if keyword (nullable) is None
        # and model_fields_set contains the field
        if self.keyword is None and "keyword" in self.model_fields_set:
            _dict['keyword'] = None

        # set to None if location_name (nullable) is None
        # and model_fields_set contains the field
        if self.location_name is None and "location_name" in self.model_fields_set:
            _dict['location_name'] = None

        # set to None if location_code (nullable) is None
        # and model_fields_set contains the field
        if self.location_code is None and "location_code" in self.model_fields_set:
            _dict['location_code'] = None

        # set to None if priority (nullable) is None
        # and model_fields_set contains the field
        if self.priority is None and "priority" in self.model_fields_set:
            _dict['priority'] = None

        # set to None if language_name (nullable) is None
        # and model_fields_set contains the field
        if self.language_name is None and "language_name" in self.model_fields_set:
            _dict['language_name'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if depth (nullable) is None
        # and model_fields_set contains the field
        if self.depth is None and "depth" in self.model_fields_set:
            _dict['depth'] = None

        # set to None if ratings (nullable) is None
        # and model_fields_set contains the field
        if self.ratings is None and "ratings" in self.model_fields_set:
            _dict['ratings'] = None

        # set to None if visit_type (nullable) is None
        # and model_fields_set contains the field
        if self.visit_type is None and "visit_type" in self.model_fields_set:
            _dict['visit_type'] = None

        # set to None if months (nullable) is None
        # and model_fields_set contains the field
        if self.months is None and "months" in self.model_fields_set:
            _dict['months'] = None

        # set to None if search_reviews_keyword (nullable) is None
        # and model_fields_set contains the field
        if self.search_reviews_keyword is None and "search_reviews_keyword" in self.model_fields_set:
            _dict['search_reviews_keyword'] = None

        # set to None if sort_by (nullable) is None
        # and model_fields_set contains the field
        if self.sort_by is None and "sort_by" in self.model_fields_set:
            _dict['sort_by'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        # set to None if postback_url (nullable) is None
        # and model_fields_set contains the field
        if self.postback_url is None and "postback_url" in self.model_fields_set:
            _dict['postback_url'] = None

        # set to None if pingback_url (nullable) is None
        # and model_fields_set contains the field
        if self.pingback_url is None and "pingback_url" in self.model_fields_set:
            _dict['pingback_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BusinessDataTripadvisorReviewsTaskPostRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url_path": obj.get("url_path"),
            "keyword": obj.get("keyword"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "priority": obj.get("priority"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "depth": obj.get("depth"),
            "ratings": obj.get("ratings"),
            "visit_type": obj.get("visit_type"),
            "months": obj.get("months"),
            "search_reviews_keyword": obj.get("search_reviews_keyword"),
            "sort_by": obj.get("sort_by"),
            "tag": obj.get("tag"),
            "postback_url": obj.get("postback_url"),
            "pingback_url": obj.get("pingback_url")
        })
        return _obj

