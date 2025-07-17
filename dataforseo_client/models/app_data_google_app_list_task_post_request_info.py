from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AppDataGoogleAppListTaskPostRequestInfo(BaseModel):
    """
    AppDataGoogleAppListTaskPostRequestInfo
    """ # noqa: E501
    app_collection: Optional[StrictStr] = Field(default=None, description="app collection. required field. app collection on Google Play from which apps will be collected;. you can specify the following values:. featured, topselling_paid, topselling_free, topselling_new_free, topselling_new_paid, topgrossing, movers_shakers. Note: if featured is selected, the app_category parameter cannot be used")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location. required field if you don’t specify location_code. if you use this field, you don’t need to specify location_code. you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/app_data/google/locations. example:. West Los Angeles,California,United States")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code. required field if you don’t specify location_name. if you use this field, you don’t need to specify location_name. you can receive the list of available locations of the search engine with their location_code by making a separate request to https://api.dataforseo.com/v3/app_data/google/locations. example:. 9061121")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language. required field if language_code is not specified. if you use this field, you don’t need to specify language_code. you can receive the list of available languages with language_name by making a separate request to https://api.dataforseo.com/v3/app_data/google/languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code. required field if language_name is not specified. if you use this field, you don’t need to specify language_name. you can receive the list of available languages with their language_code by making a separate request to https://api.dataforseo.com/v3/app_data/google/languages. example:. en")
    priority: Optional[StrictInt] = Field(default=None, description="task priority. optional field. can take the following values:. 1 – normal execution priority (set by default). 2 – high execution priority. You will be additionally charged for the tasks with high execution priority.. The cost can be calculated on the Pricing page.")
    depth: Optional[StrictInt] = Field(default=None, description="parsing depth. optional field. number of apps to be returned in the API response;. we strongly recommend setting the parsing depth in the multiples of 100, because our system processes 100 results in a row;. default value: 100;. maximum value: 200")
    app_category: Optional[StrictStr] = Field(default=None, description="application category on Google Play. optional field. you can filter the results by app category;. example:. family;. you can receive the full list of available categories by making a separate request to https://api.dataforseo.com/v3/app_data/google/categories. Note: app_category cannot be used if app_collection parameter is set to featured")
    age_rating: Optional[StrictStr] = Field(default=None, description="filter results by age rating. optional field. you can use this field to filter the results by age rating;. possible types of filtering:. ages_up_to_5 — return apps approved for children up to 5 years old;. ages_6_8 — return apps approved for children from 6 to 8 years old;. ages_9_12 — return apps approved for children from 9 to 12 years old;. by default, the API returns apps for all ages;. Note: this filter works only in conjunction with the 'category': 'family' parameter")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    postback_url: Optional[StrictStr] = Field(default=None, description="return URL for sending task results. optional field. once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.. example:. http://your-server.com/postbackscript?id=$id. http://your-server.com/postbackscript?id=$id&tag=$tag. Note: special characters in postback_url will be urlencoded;. i.a., the # character will be encoded into %23")
    postback_data: Optional[StrictStr] = Field(default=None, description="postback_url datatype. required field if you specify postback_url. corresponds to the datatype that will be sent to your server. possible values:. advanced, html")
    pingback_url: Optional[StrictStr] = Field(default=None, description="notification URL of a completed task. optional field. when a task is completed we will notify you by GET request sent to the URL you have specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.. example:. http://your-server.com/pingscript?id=$id. http://your-server.com/pingscript?id=$id&tag=$tag. Note: special characters in pingback_url will be urlencoded;. i.a., the # character will be encoded into %23")
    __properties: ClassVar[List[str]] = [
        "app_collection", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "priority", 
        "depth", 
        "app_category", 
        "age_rating", 
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

        _dict['app_collection'] = self.app_collection
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['priority'] = self.priority
        _dict['depth'] = self.depth
        _dict['app_category'] = self.app_category
        _dict['age_rating'] = self.age_rating
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
            "app_collection": obj.get("app_collection"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "priority": obj.get("priority"),
            "depth": obj.get("depth"),
            "app_category": obj.get("app_category"),
            "age_rating": obj.get("age_rating"),
            "tag": obj.get("tag"),
            "postback_url": obj.get("postback_url"),
            "postback_data": obj.get("postback_data"),
            "pingback_url": obj.get("pingback_url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj