from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BusinessDataGoogleHotelInfoTaskPostRequestInfo(BaseModel):
    """
    BusinessDataGoogleHotelInfoTaskPostRequestInfo
    """ # noqa: E501
    hotel_identifier: Optional[StrictStr] = Field(default=None, description="unique hotel identifier. required field if you don’t specify keyword. if you use this field, you don’t need to specify keyword. unique identifier of a hotel entity in Google search;. you can obtain the value by making a request to Advanced Google SERP API (enclosed in the hotels_pack element of the response), or the Hotel Searches endpoint of Business Data API. example:. ChYIq6SB--i6p6cpGgovbS8wN2s5ODZfEAE")
    keyword: Optional[StrictStr] = Field(default=None, description="keyword. required field if you don’t specify hotel_identifier. if you use this field, you don’t need to specify hotel_identifier. the keyword you specify should indicate the name of the hotel entity. you can specify up to 700 characters in the keyword filed. all %## will be decoded (plus character ‘+’ will be decoded to a space character). if you need to use the “%” character for your keyword, please specify it as “%25”")
    priority: Optional[StrictInt] = Field(default=None, description="task priority. optional field. can take the following values:. 1 – normal execution priority (set by default). 2 – high execution priority. You will be additionally charged for the tasks with high execution priority.. The cost can be calculated on the Pricing page.")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location. required field if you don’t specify location_code or location_coordinate. if you use this field, you don’t need to specify location_code or location_coordinate. you can receive the list of available locations with location_name by making a separate request to https://api.dataforseo.com/v3/business_data/google/locations. example:. London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code. required field if you don’t specify location_name or location_coordinate. if you use this field, you don’t need to specify location_name or location_coordinate. you can receive the list of available locations with location_code by making a separate request to the https://api.dataforseo.com/v3/business_data/google/locations. example:. 2840")
    location_coordinate: Optional[StrictStr] = Field(default=None, description="GPS coordinates of a location. required field if you don’t specify location_name or location_code. if you use this field, you don’t need to specify location_name or location_code. location_coordinate parameter should be specified in the “latitude,longitude” format. the maximum number of decimal digits for “latitude” and “longitude”: 7. Note: if the coordinates are used to set a location, the search will occur in the nearest settlement;. example:. 53.476225,-2.243572")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language. required field if you don’t specify language_code. if you use this field, you don’t need to specify language_code. you can receive the list of available languages with language_name by making a separate request to https://api.dataforseo.com/v3/business_data/google/languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code. required field if you don’t specify language_name. if you use this field, you don’t need to specify language_name. you can receive the list of available languages with their language_code by making a separate request to https://api.dataforseo.com/v3/business_data/google/languages. example:. en")
    check_in: Optional[StrictStr] = Field(default=None, description="check-in date. optional field. if you don’t specify this field, tomorrow’s date will be used by default;. the value must not be earlier than today’s date. date format: 'yyyy-mm-dd'. example:. '2019-01-15'")
    check_out: Optional[StrictStr] = Field(default=None, description="check-out date. optional field. if you don’t specify this field, our system will apply the date of two days from now by default;. Note: the value cannot be less than or equal to check_in;. the range between check_in and check_out values cannot exceed 30 days. date format: 'yyyy-mm-dd'. example:. '2019-01-15'")
    currency: Optional[StrictStr] = Field(default=None, description="currency. optional field. example:. 'USD'")
    adults: Optional[StrictInt] = Field(default=None, description="number of adults. optional field. if you don’t specify this field, two adults will be used by default. example:. 1")
    children: Optional[List[Optional[StrictStr]]] = Field(default=None, description="number and age of children. optional field. if you don’t specify this field, no children will be included in the search;. set the following value if you want to include one 14-years-old child:. [14]. set the following value if you want to include one 13-years-old child and one 8-years-old child:. [13,8]")
    load_prices_by_dates: Optional[StrictBool] = Field(default=None, description="load hotel stay prices by dates. optional field. if you specify this parameter with true, the response will include the prices_by_dates array with hotel stay prices divided by dates. if you use this parameter, you will be charged double the base price for a request")
    prices_start_date: Optional[StrictStr] = Field(default=None, description="start date to load prices by dates. optional field. to use this parameter, you must specify load_prices_by_dates with true. if this parameter is not specified, the start date is set to check_in date. date format: yyyy-mm-dd. example:. 2025-05-20")
    prices_end_date: Optional[StrictStr] = Field(default=None, description="end date to load prices by dates. optional field. to use this parameter, you must specify load_prices_by_dates with true. if this parameter is not specified, you will get prices by date for the month. date format: yyyy-mm-dd. example:. 2025-05-21")
    prices_date_range: Optional[StrictStr] = Field(default=None, description="predefined period for retrieving daily price data. optional field. to use this parameter, you must specify load_prices_by_dates with true. if the prices_start_date is not specified, the start date is set to check_in date. possible values: month, three_months, six_months, year. default value: month")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255;. you can use this parameter to identify the task and match it with the result;. you will find the specified tag value in the data object of the response")
    postback_url: Optional[StrictStr] = Field(default=None, description="return URL for sending task results. optional field. once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified;. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request;. example:. http://your-server.com/postbackscript?id=$id. http://your-server.com/postbackscript?id=$id&tag=$tag. Note: special characters in postback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    postback_data: Optional[StrictStr] = Field(default=None, description="postback_url datatype. required field if you specify postback_url. corresponds to the datatype that will be sent to your server. possible values:. advanced, html")
    pingback_url: Optional[StrictStr] = Field(default=None, description="notification URL of a completed task. optional field. when a task is completed we will notify you by GET request sent to the URL you have specified;. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable;. we will set the necessary values before sending the request;. example:. http://your-server.com/pingscript?id=$id. http://your-server.com/pingscript?id=$id&tag=$tag. Note: special characters in pingback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    __properties: ClassVar[List[str]] = [
        "hotel_identifier", 
        "keyword", 
        "priority", 
        "location_name", 
        "location_code", 
        "location_coordinate", 
        "language_name", 
        "language_code", 
        "check_in", 
        "check_out", 
        "currency", 
        "adults", 
        "children", 
        "load_prices_by_dates", 
        "prices_start_date", 
        "prices_end_date", 
        "prices_date_range", 
        "tag", 
        "postback_url", 
        "postback_data", 
        "pingback_url", 
        ]

    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )

    def to_str(self) -> str:
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        excluded_fields: Set[str] = set([
        ])

        _dict = {}

        _dict['hotel_identifier'] = self.hotel_identifier
        _dict['keyword'] = self.keyword
        _dict['priority'] = self.priority
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['location_coordinate'] = self.location_coordinate
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['check_in'] = self.check_in
        _dict['check_out'] = self.check_out
        _dict['currency'] = self.currency
        _dict['adults'] = self.adults
        _dict['children'] = self.children
        _dict['load_prices_by_dates'] = self.load_prices_by_dates
        _dict['prices_start_date'] = self.prices_start_date
        _dict['prices_end_date'] = self.prices_end_date
        _dict['prices_date_range'] = self.prices_date_range
        _dict['tag'] = self.tag
        _dict['postback_url'] = self.postback_url
        _dict['postback_data'] = self.postback_data
        _dict['pingback_url'] = self.pingback_url
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hotel_identifier": obj.get("hotel_identifier"),
            "keyword": obj.get("keyword"),
            "priority": obj.get("priority"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "location_coordinate": obj.get("location_coordinate"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "check_in": obj.get("check_in"),
            "check_out": obj.get("check_out"),
            "currency": obj.get("currency"),
            "adults": obj.get("adults"),
            "children": obj.get("children"),
            "load_prices_by_dates": obj.get("load_prices_by_dates"),
            "prices_start_date": obj.get("prices_start_date"),
            "prices_end_date": obj.get("prices_end_date"),
            "prices_date_range": obj.get("prices_date_range"),
            "tag": obj.get("tag"),
            "postback_url": obj.get("postback_url"),
            "postback_data": obj.get("postback_data"),
            "pingback_url": obj.get("pingback_url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj