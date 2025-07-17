from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpGoogleAutocompleteLiveAdvancedRequestInfo(BaseModel):
    """
    SerpGoogleAutocompleteLiveAdvancedRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword. required field. you can specify up to 700 characters in the keyword field. all %## will be decoded (plus character ‘+’ will be decoded to a space character). if you need to use the “%” character for your keyword, please specify it as “%25”;. if you need to use the “+” character for your keyword, please specify it as “%2B”;. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location. required field if you don’t specify location_code. if you use this field, you don’t need to specify location_code;. you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/serp/google/autocomplete/locations. example:. London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code. required field if you don’t specify location_name;. you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/serp/google/locations. example:. 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language. required field if you don’t specify language_code. if you use this field, you don’t need to specify language_code;. you can receive the list of available languages of the search engine with their language_name by making a separate request to https://api.dataforseo.com/v3/serp/google/languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code. required field if you don’t specify language_name. if you use this field, you don’t need to specify language_name;. you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languages. example:. en")
    cursor_pointer: Optional[StrictInt] = Field(default=None, description="search bar cursor pointer. optional field. the horizontal numerical position of the cursor pointer within the keyword in the search bar;. by modifying the position of the cursor pointer, you will obtain different autocomplete suggestions for the same seed keyword;. minimal value: 0. default value: the number of the last character of the specified keyword. example:. |which query are s – 'cursor_pointer': 0. which query is s| – 'cursor_pointer': 16. which que|ry is s – 'cursor_pointer': 9")
    client: Optional[StrictStr] = Field(default=None, description="search client for autocomplete. optional field. autocomplete results may differ depending on the search client;. possible values:. chrome — used when google search is opened in google chrome;. chrome-omni — used in the address bar in chrome;. gws-wiz — used in google search home page;. gws-wiz-serp — used in google search engine results page;. safari — used when google search is opened in safari browser;. firefox — used when google search is opened in firefox browser;. psy-ab — may be used when google search is opened in google chrome browser;. toolbar — returns XML;. youtube — returns JSONP;. gws-wiz-local — used in google local;. img — used in google’s image search;. products-cc — used in google shopping search")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "cursor_pointer", 
        "client", 
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
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['cursor_pointer'] = self.cursor_pointer
        _dict['client'] = self.client
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
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "cursor_pointer": obj.get("cursor_pointer"),
            "client": obj.get("client"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj