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

class DataforseoLabsGoogleKeywordSuggestionsLiveRequestInfo(BaseModel):
    """
    DataforseoLabsGoogleKeywordSuggestionsLiveRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword required field UTF-8 encoding the keywords will be converted to lowercase format; learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location optional field if you use this field, you don’t need to specify location_code you can receive the list of available locations with their location_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available locations example: United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="location code optional field if you use this field, you don’t need to specify location_name you can receive the list of available locations with their location_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages ignore this field to get the results for all available locations example: 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of the language optional field if you use this field, you don’t need to specify language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: English Note: if omitted, results default to the language with the most keyword records in the specified location; refer to the available_languages.keywords field of the Locations and Languages endpoint to determine the default language")
    language_code: Optional[StrictStr] = Field(default=None, description="language code optional field if you use this field, you don’t need to specify language_name you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: en Note: if omitted, results default to the language with the most keyword records in the specified location; refer to the available_languages.keywords field of the Locations and Languages endpoint to determine the default language")
    include_seed_keyword: Optional[StrictBool] = Field(default=None, description="include data for the seed keyword optional field if set to true, data for the seed keyword specified in the keyword field will be provided in the seed_keyword_data array of the response default value: false")
    include_serp_info: Optional[StrictBool] = Field(default=None, description="include data from SERP for each keyword optional field if set to true, we will return a serp_info array containing SERP data (number of search results, relevant URL, and SERP features) for every keyword in the response default value: false")
    include_clickstream_data: Optional[StrictBool] = Field(default=None, description="include or exclude data from clickstream-based metrics in the result optional field if the parameter is set to true, you will receive clickstream_keyword_info, keyword_info_normalized_with_clickstream, and keyword_info_normalized_with_bing fields in the response default value: false with this parameter enabled, you will be charged double the price for the request learn more about how clickstream-based metrics are calculated in this help center article")
    exact_match: Optional[StrictBool] = Field(default=None, description="search for the exact phrase optional field if set to true, the returned keywords will include the exact keyword phrase you specified, with potentially other words before or after that phrase default value: false")
    ignore_synonyms: Optional[StrictBool] = Field(default=None, description="ignore highly similar keywords optional field if set to true only core keywords will be returned, all highly similar keywords will be excluded; default value: false")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, <, <=, >, >=, =, <>, in, not_in, match, not_match, ilike, not_ilike, like, not_like you can use the % operator with like and not_like, as well as ilike and not_ilike to match any string of zero or more characters example: [\"keyword_info.search_volume\",\">\",0] [[\"keyword_info.search_volume\",\"in\",[0,1000]], \"and\", [\"keyword_info.competition_level\",\"=\",\"LOW\"]][[\"keyword_info.search_volume\",\">\",100], \"and\", [[\"keyword_info.cpc\",\"<\",0.5], \"or\", [\"keyword_info.high_top_of_page_bid\",\"<=\",0.5]]] for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide")
    order_by: Optional[List[StrictStr]] = Field(default=None, description="results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order a comma is used as a separator example: [\"keyword_info.competition,desc\"] default rule: [\"keyword_info.search_volume,desc\"] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\"keyword_info.search_volume,desc\",\"keyword_info.cpc,desc\"]")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned keywords optional field default value: 100 maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned keywords optional field default value: 0 if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords")
    offset_token: Optional[StrictStr] = Field(default=None, description="offset token for subsequent requests optional field provided in the identical filed of the response to each request; use this parameter to avoid timeouts while trying to obtain over 10,000 results in a single request; by specifying the unique offset_token value from the response array, you will get the subsequent results of the initial task; offset_token values are unique for each subsequent task Note: if the offset_token is specified in the request, all other parameters except limit will not be taken into account when processing a task.")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = ["keyword", "location_name", "location_code", "language_name", "language_code", "include_seed_keyword", "include_serp_info", "include_clickstream_data", "exact_match", "ignore_synonyms", "filters", "order_by", "limit", "offset", "offset_token", "tag"]

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
        """Create an instance of DataforseoLabsGoogleKeywordSuggestionsLiveRequestInfo from a JSON string"""
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

        # set to None if include_seed_keyword (nullable) is None
        # and model_fields_set contains the field
        if self.include_seed_keyword is None and "include_seed_keyword" in self.model_fields_set:
            _dict['include_seed_keyword'] = None

        # set to None if include_serp_info (nullable) is None
        # and model_fields_set contains the field
        if self.include_serp_info is None and "include_serp_info" in self.model_fields_set:
            _dict['include_serp_info'] = None

        # set to None if include_clickstream_data (nullable) is None
        # and model_fields_set contains the field
        if self.include_clickstream_data is None and "include_clickstream_data" in self.model_fields_set:
            _dict['include_clickstream_data'] = None

        # set to None if exact_match (nullable) is None
        # and model_fields_set contains the field
        if self.exact_match is None and "exact_match" in self.model_fields_set:
            _dict['exact_match'] = None

        # set to None if ignore_synonyms (nullable) is None
        # and model_fields_set contains the field
        if self.ignore_synonyms is None and "ignore_synonyms" in self.model_fields_set:
            _dict['ignore_synonyms'] = None

        # set to None if filters (nullable) is None
        # and model_fields_set contains the field
        if self.filters is None and "filters" in self.model_fields_set:
            _dict['filters'] = None

        # set to None if order_by (nullable) is None
        # and model_fields_set contains the field
        if self.order_by is None and "order_by" in self.model_fields_set:
            _dict['order_by'] = None

        # set to None if limit (nullable) is None
        # and model_fields_set contains the field
        if self.limit is None and "limit" in self.model_fields_set:
            _dict['limit'] = None

        # set to None if offset (nullable) is None
        # and model_fields_set contains the field
        if self.offset is None and "offset" in self.model_fields_set:
            _dict['offset'] = None

        # set to None if offset_token (nullable) is None
        # and model_fields_set contains the field
        if self.offset_token is None and "offset_token" in self.model_fields_set:
            _dict['offset_token'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataforseoLabsGoogleKeywordSuggestionsLiveRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "include_seed_keyword": obj.get("include_seed_keyword"),
            "include_serp_info": obj.get("include_serp_info"),
            "include_clickstream_data": obj.get("include_clickstream_data"),
            "exact_match": obj.get("exact_match"),
            "ignore_synonyms": obj.get("ignore_synonyms"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "offset_token": obj.get("offset_token"),
            "tag": obj.get("tag")
        })
        return _obj


