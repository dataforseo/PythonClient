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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class SerpGoogleAdsSearchTaskPostRequestInfo(BaseModel):
    """
    SerpGoogleAdsSearchTaskPostRequestInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="domain name required field if advertiser_ids is not specified domain name associated with an advertiser account")
    advertiser_ids: Optional[List[StrictStr]] = Field(default=None, description="advertiser identifiers required field if target is not specified you can specify the maximum of 25 values in this array; advertiser_ids values for this parameter can be found in the Google Ads Advertisers endpoint;")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/ads_search/locations example: London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/ads_search/locations example: 2840")
    location_coordinate: Optional[StrictStr] = Field(default=None, description="GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code example: 52.6178549,-155.352142")
    platform: Optional[StrictStr] = Field(default=None, description="advertising platform optional field possible values: all, google_pay, google_maps, google_search, google_shopping, youtube default value: all")
    format: Optional[StrictStr] = Field(default=None, description="ad format optional field possible values: all, text, image, video")
    date_from: Optional[StrictStr] = Field(default=None, description="starting date of the time range optional field required field if date_to is specified;  date format: \"yyyy-mm-dd\" minimum value: 2018-05-31 maximum value: today’s date example: \"2020-01-01\"")
    date_to: Optional[StrictStr] = Field(default=None, description="ending date of the time range optional field required field if date_from is specified;  date format: \"yyyy-mm-dd\" minimum value: 2018-05-31 maximum value: today’s date example: \"2020-01-01\"")
    depth: Optional[StrictInt] = Field(default=None, description="parsing depth optional field number of results in SERP default value: 40 max value: 700 Note: your account will be billed per each SERP containing up to 40 results; thus, setting a depth above 40 may result in additional charges if the search engine returns more than 40 results; if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance")
    priority: Optional[StrictInt] = Field(default=None, description="task priority optional field can take the following values: 1 – normal execution priority (set by default) 2 – high execution priority You will be additionally charged for the tasks with high execution priority. The cost can be calculated on the Pricing page.")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response")
    postback_url: Optional[StrictStr] = Field(default=None, description="return URL for sending task results optional field once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/postbackscript?id=$id http://your-server.com/postbackscript?id=$id&tag=$tag Note: special characters in postback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center")
    postback_data: Optional[StrictStr] = Field(default=None, description="postback_url datatype required field if you specify postback_url corresponds to the function you used for setting a task possible values: advanced")
    pingback_url: Optional[StrictStr] = Field(default=None, description="notification URL of a completed task optional field when a task is completed we will notify you by GET request sent to the URL you have specified you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example: http://your-server.com/pingscript?id=$id http://your-server.com/pingscript?id=$id&tag=$tag Note: special characters in pingback_url will be urlencoded; i.a., the # character will be encoded into %23 learn more on our Help Center")
    __properties: ClassVar[List[str]] = ["target", "advertiser_ids", "location_name", "location_code", "location_coordinate", "platform", "format", "date_from", "date_to", "depth", "priority", "tag", "postback_url", "postback_data", "pingback_url"]

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
        """Create an instance of SerpGoogleAdsSearchTaskPostRequestInfo from a JSON string"""
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
        # set to None if target (nullable) is None
        # and model_fields_set contains the field
        if self.target is None and "target" in self.model_fields_set:
            _dict['target'] = None

        # set to None if advertiser_ids (nullable) is None
        # and model_fields_set contains the field
        if self.advertiser_ids is None and "advertiser_ids" in self.model_fields_set:
            _dict['advertiser_ids'] = None

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

        # set to None if platform (nullable) is None
        # and model_fields_set contains the field
        if self.platform is None and "platform" in self.model_fields_set:
            _dict['platform'] = None

        # set to None if format (nullable) is None
        # and model_fields_set contains the field
        if self.format is None and "format" in self.model_fields_set:
            _dict['format'] = None

        # set to None if date_from (nullable) is None
        # and model_fields_set contains the field
        if self.date_from is None and "date_from" in self.model_fields_set:
            _dict['date_from'] = None

        # set to None if date_to (nullable) is None
        # and model_fields_set contains the field
        if self.date_to is None and "date_to" in self.model_fields_set:
            _dict['date_to'] = None

        # set to None if depth (nullable) is None
        # and model_fields_set contains the field
        if self.depth is None and "depth" in self.model_fields_set:
            _dict['depth'] = None

        # set to None if priority (nullable) is None
        # and model_fields_set contains the field
        if self.priority is None and "priority" in self.model_fields_set:
            _dict['priority'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        # set to None if postback_url (nullable) is None
        # and model_fields_set contains the field
        if self.postback_url is None and "postback_url" in self.model_fields_set:
            _dict['postback_url'] = None

        # set to None if postback_data (nullable) is None
        # and model_fields_set contains the field
        if self.postback_data is None and "postback_data" in self.model_fields_set:
            _dict['postback_data'] = None

        # set to None if pingback_url (nullable) is None
        # and model_fields_set contains the field
        if self.pingback_url is None and "pingback_url" in self.model_fields_set:
            _dict['pingback_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SerpGoogleAdsSearchTaskPostRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "target": obj.get("target"),
            "advertiser_ids": obj.get("advertiser_ids"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "location_coordinate": obj.get("location_coordinate"),
            "platform": obj.get("platform"),
            "format": obj.get("format"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "depth": obj.get("depth"),
            "priority": obj.get("priority"),
            "tag": obj.get("tag"),
            "postback_url": obj.get("postback_url"),
            "postback_data": obj.get("postback_data"),
            "pingback_url": obj.get("pingback_url")
        })
        return _obj


