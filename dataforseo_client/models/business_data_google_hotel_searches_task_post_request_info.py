from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BusinessDataGoogleHotelSearchesTaskPostRequestInfo(BaseModel):
    """
    BusinessDataGoogleHotelSearchesTaskPostRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword. optional field. the keyword you specify is used to search for the list of hotels;. if you don’t use this field, we will return the list of hotels found in a specified location;. you can specify up to 700 characters in the keyword filed. all %## will be decoded (plus character ‘+’ will be decoded to a space character). if you need to use the “%” character for your keyword, please specify it as “%25”;. Note: in order to obtain accurate search results, the location name is appended to the keyword automatically. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    priority: Optional[StrictInt] = Field(default=None, description="task priority. optional field. can take the following values:. 1 – normal execution priority (set by default). 2 – high execution priority. You will be additionally charged for the tasks with high execution priority.. The cost can be calculated on the Pricing page.")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location. required field if you don’t specify location_code or location_coordinate. if you use this field, you don’t need to specify location_code or location_coordinate. you can receive the list of available locations with location_name by making a separate request to https://api.dataforseo.com/v3/business_data/google/locations. example:. London,England,United Kingdom. Note: in order to obtain accurate search results, the location_name you specify will be automatically appended to the keyword")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code. required field if you don’t specify location_name or location_coordinate. if you use this field, you don’t need to specify location_name or location_coordinate. you can receive the list of available locations with location_code by making a separate request to the https://api.dataforseo.com/v3/business_data/google/locations. example:. 2840")
    location_coordinate: Optional[StrictStr] = Field(default=None, description="GPS coordinates of a location. required field if you don’t specify location_name or location_code. if you use this field, you don’t need to specify location_name or location_code. location_coordinate parameter should be specified in the “latitude,longitude” format. the maximum number of decimal digits for “latitude” and “longitude”: 7. Note: if the coordinates are used to set a location, the search will occur in the nearest settlement;. example:. 53.476225,-2.243572")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language. required field if you don’t specify language_code. if you use this field, you don’t need to specify language_code. you can receive the list of available languages with language_name by making a separate request to https://api.dataforseo.com/v3/business_data/google/languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code. required field if you don’t specify language_name. if you use this field, you don’t need to specify language_name. you can receive the list of available languages with their language_code by making a separate request to https://api.dataforseo.com/v3/business_data/google/languages. example:. en")
    depth: Optional[StrictInt] = Field(default=None, description="parsing depth. optional field. number of results in Google Hotels. default value: 20 organic results. max value: 140. Note: your account will be billed per each 20 organic results regardless of paid listings in the response;. thus, setting a depth above 20 may result in additional charges if Google Hotels return more than 20 results;. if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance")
    check_in: Optional[StrictStr] = Field(default=None, description="check-in date. optional field. if you don’t specify this field, tomorrow’s date will be used by default;. date format: 'yyyy-mm-dd'. example:. '2019-01-15'. Note: the value cannot precede the today’s date")
    check_out: Optional[StrictStr] = Field(default=None, description="check-out date. optional field. if you don’t specify this field, our system will apply the date of two days from now by default;. date format: 'yyyy-mm-dd'. example:. '2019-01-15'. Note: the value cannot be less than or equal to check_in;. the range between check_in and check_out values cannot exceed 30 days")
    currency: Optional[StrictStr] = Field(default=None, description="currency. optional field. example:. 'USD'")
    adults: Optional[StrictInt] = Field(default=None, description="number of adults. optional field. if you don’t specify this field, the default value of 2 will be applied;. note that you can specify up to 6 persons including both adults and children. example:. 1")
    children: Optional[List[Optional[StrictStr]]] = Field(default=None, description="number and age of children. optional field. if you don’t specify this field, no children will be included in the search;. age of child can be from 0 to 17;. note that you can specify up to 6 persons including both adults and children. set the following value if you want to include one 14-year-old child:. [14]. set the following value if you want to include one 13-year-old child and one 8-year-old child:. [13,8]")
    stars: Optional[List[Optional[StrictStr]]] = Field(default=None, description="hotel stars. optional field. set this field to [5] if you want to get the list of 5-star hotels only. example:. [3,4,5]")
    min_rating: Optional[StrictFloat] = Field(default=None, description="minimum rating. optional field. you can use this field to specify guest rating higher than a certain value. example:. 2.5")
    sort_by: Optional[StrictStr] = Field(default=None, description="results sorting parameters. optional field. you can use this field to sort the results. possible types of sorting:. relevance – sort by most relevant. lowest_price – sort by the lowest price. highest_rating – sort by highest rating. most_reviewed – sort by most reviewed. default value: relevance")
    min_price: Optional[StrictInt] = Field(default=None, description="minimum price per night. optional field. the currency of this value depends on the currency field. example:. 100")
    max_price: Optional[StrictInt] = Field(default=None, description="maximum price per night. optional field. the currency of this value depends on the currency field. example:. 600")
    free_cancellation: Optional[StrictBool] = Field(default=None, description="hotels with a free cancellation. optional field. set this field to true if you want to get the list of hotels with free cancellation of reservations. default value: false")
    is_vacation_rentals: Optional[StrictBool] = Field(default=None, description="search for vacation rentals. optional field. set this field to true if you want to get the list of vacation rentals instead of hotels. default value: false")
    amenities: Optional[List[Optional[StrictStr]]] = Field(default=None, description="hotel amenities. optional field. you can use this field to specify different hotel amenities. example:.   [.             'free_parking',.             'pets_allowed'.         ]. . possible values:. 'air_conditioning',. 'all_inclusive_available',. 'bar',. 'free_breakfast',. 'fitness_center',. 'kid_friendly',. 'free_parking',. 'pets_allowed',. 'pool',. 'restaurant',. 'room_service',. 'spa',. 'free_wifi',. 'parking',. 'indoor_pool',. 'outdoor_pool',. 'wheelchair_accessible',. 'beach_access'")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    postback_url: Optional[StrictStr] = Field(default=None, description="return URL for sending task results. optional field. once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.. example:. http://your-server.com/postbackscript?id=$id. http://your-server.com/postbackscript?id=$id&tag=$tag. Note: special characters in postback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    pingback_url: Optional[StrictStr] = Field(default=None, description="notification URL of a completed task. optional field. when a task is completed we will notify you by GET request sent to the URL you have specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.. example:. http://your-server.com/pingscript?id=$id. http://your-server.com/pingscript?id=$id&tag=$tag. Note: special characters in pingback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "priority", 
        "location_name", 
        "location_code", 
        "location_coordinate", 
        "language_name", 
        "language_code", 
        "depth", 
        "check_in", 
        "check_out", 
        "currency", 
        "adults", 
        "children", 
        "stars", 
        "min_rating", 
        "sort_by", 
        "min_price", 
        "max_price", 
        "free_cancellation", 
        "is_vacation_rentals", 
        "amenities", 
        "tag", 
        "postback_url", 
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

        _dict['keyword'] = self.keyword
        _dict['priority'] = self.priority
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['location_coordinate'] = self.location_coordinate
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['depth'] = self.depth
        _dict['check_in'] = self.check_in
        _dict['check_out'] = self.check_out
        _dict['currency'] = self.currency
        _dict['adults'] = self.adults
        _dict['children'] = self.children
        _dict['stars'] = self.stars
        _dict['min_rating'] = self.min_rating
        _dict['sort_by'] = self.sort_by
        _dict['min_price'] = self.min_price
        _dict['max_price'] = self.max_price
        _dict['free_cancellation'] = self.free_cancellation
        _dict['is_vacation_rentals'] = self.is_vacation_rentals
        _dict['amenities'] = self.amenities
        _dict['tag'] = self.tag
        _dict['postback_url'] = self.postback_url
        _dict['pingback_url'] = self.pingback_url
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "priority": obj.get("priority"),
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
            "tag": obj.get("tag"),
            "postback_url": obj.get("postback_url"),
            "pingback_url": obj.get("pingback_url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj