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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class BusinessDataGoogleHotelSearchesLiveRequestInfo(BaseModel):
    """
    BusinessDataGoogleHotelSearchesLiveRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword optional field the keyword you specify is used to search for the list of hotels; if you don’t use this field, we will return the list of hotels found in a specified location; you can specify up to 700 characters in the keyword filed all %## will be decoded (plus character ‘+’ will be decoded to a space character) if you need to use the “%” character for your keyword, please specify it as “%25”; Note: in order to obtain accurate search results, the location name is appended to the keyword automatically learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location required field if you don’t specify location_code or location_coordinate if you use this field, you don’t need to specify location_code or location_coordinate you can receive the list of available locations with location_name by making a separate request to https://api.dataforseo.com/v3/business_data/google/locations example: London,England,United Kingdom Note: in order to obtain accurate search results, the location_name you specify will be automatically appended to the keyword")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code required field if you don’t specify location_name or location_coordinate if you use this field, you don’t need to specify location_name or location_coordinate you can receive the list of available locations with location_code by making a separate request to the https://api.dataforseo.com/v3/business_data/google/locations example: 2840")
    location_coordinate: Optional[StrictStr] = Field(default=None, description="GPS coordinates of a location required field if you don’t specify location_name or location_code if you use this field, you don’t need to specify location_name or location_code location_coordinate parameter should be specified in the “latitude,longitude” format the maximum number of decimal digits for “latitude” and “longitude”: 7 Note: if the coordinates are used to set a location, the search will occur in the nearest settlement example: 53.476225,-2.243572")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language required field if you don’t specify language_code if you use this field, you don’t need to specify language_code you can receive the list of available languages with language_name by making a separate request to https://api.dataforseo.com/v3/business_data/google/languages example: English")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code required field if you don’t specify language_name if you use this field, you don’t need to specify language_name you can receive the list of available languages with their language_code by making a separate request to https://api.dataforseo.com/v3/business_data/google/languages example: en")
    depth: Optional[StrictInt] = Field(default=None, description="parsing depth optional field number of results in Google Hotels default value: 20 organic results max value: 140 Note: your account will be billed per each 20 organic results regardless of paid listings in the response; thus, setting a depth above 20 may result in additional charges if Google Hotels return more than 20 results; if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance")
    check_in: Optional[StrictStr] = Field(default=None, description="check-in date optional field if you don’t specify this field, tomorrow’s date will be used by default; date format: \"yyyy-mm-dd\" example: \"2019-01-15\" Note: the value cannot precede the today’s date")
    check_out: Optional[StrictStr] = Field(default=None, description="check-out date optional field if you don’t specify this field, our system will apply the date of two days from now by default; date format: \"yyyy-mm-dd\" example: \"2019-01-15\" Note: the value cannot be less than or equal to check_in; the range between check_in and check_out values cannot exceed 30 days")
    currency: Optional[StrictStr] = Field(default=None, description="currency optional field example: \"USD\"")
    adults: Optional[StrictInt] = Field(default=None, description="number of adults optional field if you don’t specify this field, the default value of 2 will be applied; note that you can specify up to 6 persons including both adults and children example: 1")
    children: Optional[List[StrictStr]] = Field(default=None, description="number and age of children optional field if you don’t specify this field, no children will be included in the search; age of child can be from 0 to 17; note that you can specify up to 6 persons including both adults and children set the following value if you want to include one 14-year-old child: [14] set the following value if you want to include one 13-year-old child and one 8-year-old child: [13,8]")
    stars: Optional[List[StrictStr]] = Field(default=None, description="hotel stars optional field set this field to [5] if you want to get the list of 5-star hotels only example: [3,4,5]")
    min_rating: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="minimum rating optional field you can use this field to specify guest rating higher than a certain value example: 2.5")
    sort_by: Optional[StrictStr] = Field(default=None, description="results sorting parameters optional field you can use this field to sort the results possible types of sorting: relevance – sort by most relevant lowest_price – sort by the lowest price highest_rating – sort by highest rating most_reviewed – sort by most reviewed default value: relevance")
    min_price: Optional[StrictInt] = Field(default=None, description="minimum price per night optional field the currency of this value depends on the currency field example: 100")
    max_price: Optional[StrictInt] = Field(default=None, description="maximum price per night optional field the currency of this value depends on the currency field example: 600")
    free_cancellation: Optional[StrictBool] = Field(default=None, description="hotels with a free cancellation optional field set this field to true if you want to get the list of hotels with free cancellation of reservations default value: false")
    is_vacation_rentals: Optional[StrictBool] = Field(default=None, description="search for vacation rentals optional field set this field to true if you want to get the list of vacation rentals instead of hotels default value: false")
    amenities: Optional[List[StrictStr]] = Field(default=None, description="hotel amenities optional field you can use this field to specify different hotel amenities example:   [             \"free_parking\",             \"pets_allowed\"         ]  possible values: \"air_conditioning\", \"all_inclusive_available\", \"bar\", \"free_breakfast\", \"fitness_center\", \"kid_friendly\", \"free_parking\", \"pets_allowed\", \"pool\", \"restaurant\", \"room_service\", \"spa\", \"free_wifi\", \"parking\", \"indoor_pool\", \"outdoor_pool\", \"wheelchair_accessible\", \"beach_access\"")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = ["keyword", "location_name", "location_code", "location_coordinate", "language_name", "language_code", "depth", "check_in", "check_out", "currency", "adults", "children", "stars", "min_rating", "sort_by", "min_price", "max_price", "free_cancellation", "is_vacation_rentals", "amenities", "tag"]

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
        """Create an instance of BusinessDataGoogleHotelSearchesLiveRequestInfo from a JSON string"""
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

        # set to None if depth (nullable) is None
        # and model_fields_set contains the field
        if self.depth is None and "depth" in self.model_fields_set:
            _dict['depth'] = None

        # set to None if check_in (nullable) is None
        # and model_fields_set contains the field
        if self.check_in is None and "check_in" in self.model_fields_set:
            _dict['check_in'] = None

        # set to None if check_out (nullable) is None
        # and model_fields_set contains the field
        if self.check_out is None and "check_out" in self.model_fields_set:
            _dict['check_out'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if adults (nullable) is None
        # and model_fields_set contains the field
        if self.adults is None and "adults" in self.model_fields_set:
            _dict['adults'] = None

        # set to None if children (nullable) is None
        # and model_fields_set contains the field
        if self.children is None and "children" in self.model_fields_set:
            _dict['children'] = None

        # set to None if stars (nullable) is None
        # and model_fields_set contains the field
        if self.stars is None and "stars" in self.model_fields_set:
            _dict['stars'] = None

        # set to None if min_rating (nullable) is None
        # and model_fields_set contains the field
        if self.min_rating is None and "min_rating" in self.model_fields_set:
            _dict['min_rating'] = None

        # set to None if sort_by (nullable) is None
        # and model_fields_set contains the field
        if self.sort_by is None and "sort_by" in self.model_fields_set:
            _dict['sort_by'] = None

        # set to None if min_price (nullable) is None
        # and model_fields_set contains the field
        if self.min_price is None and "min_price" in self.model_fields_set:
            _dict['min_price'] = None

        # set to None if max_price (nullable) is None
        # and model_fields_set contains the field
        if self.max_price is None and "max_price" in self.model_fields_set:
            _dict['max_price'] = None

        # set to None if free_cancellation (nullable) is None
        # and model_fields_set contains the field
        if self.free_cancellation is None and "free_cancellation" in self.model_fields_set:
            _dict['free_cancellation'] = None

        # set to None if is_vacation_rentals (nullable) is None
        # and model_fields_set contains the field
        if self.is_vacation_rentals is None and "is_vacation_rentals" in self.model_fields_set:
            _dict['is_vacation_rentals'] = None

        # set to None if amenities (nullable) is None
        # and model_fields_set contains the field
        if self.amenities is None and "amenities" in self.model_fields_set:
            _dict['amenities'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BusinessDataGoogleHotelSearchesLiveRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "location_coordinate": obj.get("location_coordinate"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "depth": obj.get("depth"),
            "check_in": obj.get("check_in"),
            "check_out": obj.get("check_out"),
            "currency": obj.get("currency"),
            "adults": obj.get("adults"),
            "children": obj.get("children"),
            "stars": obj.get("stars"),
            "min_rating": obj.get("min_rating"),
            "sort_by": obj.get("sort_by"),
            "min_price": obj.get("min_price"),
            "max_price": obj.get("max_price"),
            "free_cancellation": obj.get("free_cancellation"),
            "is_vacation_rentals": obj.get("is_vacation_rentals"),
            "amenities": obj.get("amenities"),
            "tag": obj.get("tag")
        })
        return _obj


