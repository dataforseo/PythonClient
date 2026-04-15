from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpGoogleFinanceQuoteLiveHtmlRequestInfo(BaseModel):
    """
    SerpGoogleFinanceQuoteLiveHtmlRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description=r"ticker or stock symbolrequired fieldin this field you can pass the ticker symbol of publicly traded shares of a particular stock or security on a particular stock exchange;you can specify up to 700 characters in the keyword field;all %## will be decoded (plus character ‘+’ will be decoded to a space character)if you need to use the “%” character for your keyword, please specify it as “%25”;if you need to use the “+” character for your keyword, please specify it as “%2B”;learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_code: Optional[StrictInt] = Field(default=None, description=r"search engine location coderequired field if you don't specify location_nameif you use this field, you don't need to specify location_nameyou can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/serp/google/locationsexample:2840")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search engine language coderequired field if you don't specify language_nameif you use this field, you don't need to specify language_nameyou can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languagesexample:en")
    device: Optional[StrictStr] = Field(default=None, description=r"device typeoptional fieldreturn results for a specific device typepossible value: desktop")
    location_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine locationrequired field if you don't specify location_codeif you use this field, you don't need to specify location_codeyou can receive the list of available locations of the search engine with their location_name by making a separate request to  https://api.dataforseo.com/v3/serp/google/locationsexample:London,England,United Kingdom")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine languagerequired field if you don't specify language_code if you use this field, you don't need to specify language_codeyou can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/languagesexample:English")
    os: Optional[StrictStr] = Field(default=None, description=r"device operating systemoptional fieldpossible values: windows")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response")
    window: Optional[StrictStr] = Field(default=None, description=r"time window for google_finance_quote graphoptional fieldpossible values: 1D, 5D, 1M, 6M, YTD, 1Y, 5Y, MAXdefault value: 1D")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_code", 
        "language_code", 
        "device", 
        "location_name", 
        "language_name", 
        "os", 
        "tag", 
        "window", 
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
        _dict['device'] = self.device
        _dict['location_name'] = self.location_name
        _dict['language_name'] = self.language_name
        _dict['os'] = self.os
        _dict['tag'] = self.tag
        _dict['window'] = self.window
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
            "device": obj.get("device"),
            "location_name": obj.get("location_name"),
            "language_name": obj.get("language_name"),
            "os": obj.get("os"),
            "tag": obj.get("tag"),
            "window": obj.get("window"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj