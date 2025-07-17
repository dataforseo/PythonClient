from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BusinessDataTripadvisorReviewsTaskPostRequestInfo(BaseModel):
    """
    BusinessDataTripadvisorReviewsTaskPostRequestInfo
    """ # noqa: E501
    url_path: Optional[StrictStr] = Field(default=None, description="URL path of the business entity. required field if you do not specify keyword. URL path to the Tripadvisor page of the business entity;. examples:. Hotel_Review-g60763-d23462501-Reviews-Margaritaville_Times_Square-New_York_City_New_York.html. https://www.tripadvisor.com/Hotel_Review-g60763-d23462501-Reviews-Margaritaville_Times_Square-New_York_City_New_York.html")
    keyword: Optional[StrictStr] = Field(default=None, description="keyword. required field if you do not specify url_path. the keyword you specify should indicate a name of an existing business or prominent place on Tripadvisor;. you can specify up to 700 characters in the keyword filed;. all %## will be decoded (plus character ‘+’ will be decoded to a space character);. if you need to use the “%” character for your keyword, please specify it as “%25”")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location. required field if you don’t specify location_code or url_path. you can receive the list of available locations with location_name by making a separate request to the https://api.dataforseo.com/v3/business_data/tripadvisor/locations. example:. London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code. required field if you don’t specify location_name or url_path. you can receive the list of available locations with location_code by making a separate request to the https://api.dataforseo.com/v3/business_data/tripadvisor/locations. example:. 1003854")
    priority: Optional[StrictInt] = Field(default=None, description="task priority. optional field. can take the following values:. 1 – normal execution priority (set by default). 2 – high execution priority. You will be additionally charged for the tasks with high execution priority.. The cost can be calculated on the Pricing page.")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language. optional field. if you use this field, your account will be charged for one extra request. you can receive the list of available languages with language_name by making a separate request to the https://api.dataforseo.com/v3/business_data/tripadvisor/languages. example:. English. You will be additionally charged for setting a language parameter in this endpoint.. The cost can be calculated on the Pricing page.")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code. optional field. if you use this field, your account will be charged for one extra request. you can receive the list of available languages with language_code by making a separate request to the https://api.dataforseo.com/v3/business_data/tripadvisor/languages. example:. en. You will be additionally charged for setting a language parameter in this endpoint.. The cost can be calculated on the Pricing page.")
    depth: Optional[StrictInt] = Field(default=None, description="parsing depth. optional field. number of reviews in SERP;. we strongly recommend setting the parsing depth in the multiples of ten, because our systems processes ten reviews in a row;. default value: 10;. max value: 4490")
    ratings: Optional[List[Optional[StrictStr]]] = Field(default=None, description="Tripadvisor traveler rating for a place of interest. optional field. rating based on the written reviews by a traveler after they visited a place.. possible values: excellent, very_good, average, poor, terrible. you can specify several values at once")
    visit_type: Optional[List[Optional[StrictStr]]] = Field(default=None, description="filter by type of travelers who left a review. optional field. possible values: families, couples, solo, business, friends. you can specify several values at once")
    months: Optional[List[Optional[StrictStr]]] = Field(default=None, description="filter by months when a traveler made a visit. optional field. possible values: january, february, march, april, may, april, june, july, august, september, october, november, december. you can specify several values at once")
    search_reviews_keyword: Optional[StrictStr] = Field(default=None, description="search reviews containing a specified keyword. example:. dessert")
    sort_by: Optional[StrictStr] = Field(default=None, description="results sorting parameters. optional field. you can use this field to sort the results;. possible types of sorting:. most_recent. detailed_reviews")
    translate_reviews: Optional[StrictBool] = Field(default=None, description="translate reviews according to the URL path. optional field. if set to true, returned reviews will be translated to the language matching the specified url_path;. for example, if url_path contains tripadvisor.it and translate_reviews is true, reviews will be translated to the Italian language;. default value: true. you can learn more about how reviews are translated in this Help Center article")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    postback_url: Optional[StrictStr] = Field(default=None, description="return URL for sending task results. optional field. once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.. example:. http://your-server.com/postbackscript?id=$id. http://your-server.com/postbackscript?id=$id&tag=$tag. Note: special characters in postback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    pingback_url: Optional[StrictStr] = Field(default=None, description="notification URL of a completed task. optional field. when a task is completed we will notify you by GET request sent to the URL you have specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.. example:. http://your-server.com/pingscript?id=$id. http://your-server.com/pingscript?id=$id&tag=$tag. Note: special characters in pingback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    __properties: ClassVar[List[str]] = [
        "url_path", 
        "keyword", 
        "location_name", 
        "location_code", 
        "priority", 
        "language_name", 
        "language_code", 
        "depth", 
        "ratings", 
        "visit_type", 
        "months", 
        "search_reviews_keyword", 
        "sort_by", 
        "translate_reviews", 
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

        _dict['url_path'] = self.url_path
        _dict['keyword'] = self.keyword
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['priority'] = self.priority
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['depth'] = self.depth
        _dict['ratings'] = self.ratings
        _dict['visit_type'] = self.visit_type
        _dict['months'] = self.months
        _dict['search_reviews_keyword'] = self.search_reviews_keyword
        _dict['sort_by'] = self.sort_by
        _dict['translate_reviews'] = self.translate_reviews
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
            "translate_reviews": obj.get("translate_reviews"),
            "tag": obj.get("tag"),
            "postback_url": obj.get("postback_url"),
            "pingback_url": obj.get("pingback_url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj