from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpGoogleAutocompleteTaskPostRequestInfo(BaseModel):
    """
    SerpGoogleAutocompleteTaskPostRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description=r"keyword. required field. you can specify up to 700 characters in the keyword field. all %## will be decoded (plus character ‘+’ will be decoded to a space character). if you need to use the “%” character for your keyword, please specify it as “%25”;. if you need to use the “+” character for your keyword, please specify it as “%2B”;. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_code: Optional[StrictInt] = Field(default=None, description=r"search engine location code. required field if you don't specify location_name;. you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/serp/google/locations. example:. 2840")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search engine language code. required field if you don't specify language_name. if you use this field, you don't need to specify language_name;. you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages. example:. en")
    cursor_pointer: Optional[StrictInt] = Field(default=None, description=r"search bar cursor pointer. optional field. the horizontal numerical position of the cursor pointer within the keyword in the search bar;. by modifying the position of the cursor pointer, you will obtain different autocomplete suggestions for the same seed keyword;. minimal value: 0. default value: the number of the last character of the specified keyword. example:. |which query are s - 'cursor_pointer': 0. which query is s| - 'cursor_pointer': 16. which que|ry is s - 'cursor_pointer': 9")
    priority: Optional[StrictInt] = Field(default=None, description=r"task priority. optional field. can take the following values:. 1 – normal execution priority (set by default);. 2 – high execution priority. You will be additionally charged for the tasks with high execution priority;. The cost can be calculated on the Pricing page")
    pingback_url: Optional[StrictStr] = Field(default=None, description=r"notification URL of a completed task. optional field. when a task is completed we will notify you by GET request sent to the URL you have specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.. example:. http://your-server.com/pingscript?id=$id. http://your-server.com/pingscript?id=$id&tag=$tag. Note: special characters in pingback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    postback_url: Optional[StrictStr] = Field(default=None, description=r"return URL for sending task results. optional field. once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example:. http://your-server.com/postbackscript?id=$id. http://your-server.com/postbackscript?id=$id&tag=$tag. Note: special characters in postback_url will be url-encoded;. i.e., the # character will be encoded into %23. learn more on our Help Center")
    postback_data: Optional[StrictStr] = Field(default=None, description=r"postback_url datatype. required field if you specify postback_url. corresponds to the datatype that will be sent to your server. possible values:. advanced")
    client: Optional[StrictStr] = Field(default=None, description=r"search client for autocomplete. optional field. autocomplete results may differ depending on the search client;. possible values:. chrome — used when google search is opened in google chrome;. chrome-omni — used in the address bar in chrome;. gws-wiz — used in google search home page;. gws-wiz-serp — used in google search engine results page;. safari — used when google search is opened in safari browser;. firefox — used when google search is opened in firefox browser;. psy-ab — may be used when google search is opened in google chrome browser;. toolbar — returns XML;. youtube — returns JSONP;. gws-wiz-local — used in google local;. img — used in google's image search;. products-cc — used in google shopping search")
    location_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine location. required field if you don't specify location_code. if you use this field, you don't need to specify location_code;. you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/serp/google/autocomplete/locations. example:. London,England,United Kingdom")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine language. required field if you don't specify language_code. if you use this field, you don't need to specify language_code;. you can receive the list of available languages of the search engine with their language_name by making a separate request to https://api.dataforseo.com/v3/serp/google/languages. example:. English")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_code", 
        "language_code", 
        "cursor_pointer", 
        "priority", 
        "pingback_url", 
        "postback_url", 
        "postback_data", 
        "client", 
        "location_name", 
        "language_name", 
        "tag", 
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
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['cursor_pointer'] = self.cursor_pointer
        _dict['priority'] = self.priority
        _dict['pingback_url'] = self.pingback_url
        _dict['postback_url'] = self.postback_url
        _dict['postback_data'] = self.postback_data
        _dict['client'] = self.client
        _dict['location_name'] = self.location_name
        _dict['language_name'] = self.language_name
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "cursor_pointer": obj.get("cursor_pointer"),
            "priority": obj.get("priority"),
            "pingback_url": obj.get("pingback_url"),
            "postback_url": obj.get("postback_url"),
            "postback_data": obj.get("postback_data"),
            "client": obj.get("client"),
            "location_name": obj.get("location_name"),
            "language_name": obj.get("language_name"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj