from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpGoogleDatasetSearchTaskPostRequestInfo(BaseModel):
    """
    SerpGoogleDatasetSearchTaskPostRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword. required field. you can specify up to 700 characters in the keyword field. all %## will be decoded (plus character ‘+’ will be decoded to a space character). if you need to use the “%” character for your keyword, please specify it as “%25”;. if you need to use the “+” character for your keyword, please specify it as “%2B”.. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    priority: Optional[StrictInt] = Field(default=None, description="task priority. optional field. can take the following values:. 1 – normal execution priority (set by default). 2 – high execution priority. You will be additionally charged for the tasks with high execution priority.. The cost can be calculated on the Pricing page.")
    depth: Optional[StrictInt] = Field(default=None, description="parsing depth. optional field. number of results in SERP. default value: 20. max value: 700. Note: your account will be billed per each SERP containing up to 20 results;. thus, setting a depth above 20 may result in additional charges if the search engine returns more than 20 results;. if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language. optional field. if you use this field, you don’t need to specify language_code. possible value:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code. optional field. possible value:. en")
    device: Optional[StrictStr] = Field(default=None, description="device type. optional field. possible value: desktop")
    os: Optional[StrictStr] = Field(default=None, description="device operating system. optional field. possible values: windows, macos. default value: windows")
    last_updated: Optional[StrictStr] = Field(default=None, description="last time the dataset was updated. optional field. possible values: 1m, 1y, 3y")
    file_formats: Optional[List[Optional[StrictStr]]] = Field(default=None, description="file formats of the dataset. optional field. possible values: other, archive, text, image, document, tabular")
    usage_rights: Optional[StrictStr] = Field(default=None, description="usage rights of the dataset. optional field. possible values: commercial, noncommercial")
    is_free: Optional[StrictBool] = Field(default=None, description="indicates whether displayed datasets are free. optional field. possible values: true, false")
    topics: Optional[List[Optional[StrictStr]]] = Field(default=None, description="dataset topics. optional field. possible values: humanities, social_sciences, life_sciences, agriculture, natural_sciences, geo, computer, architecture_and_urban_planning, engineering")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    postback_url: Optional[StrictStr] = Field(default=None, description="return URL for sending task results. optional field. once the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request. example:. http://your-server.com/postbackscript?id=$id. http://your-server.com/postbackscript?id=$id&tag=$tag. Note: special characters in postback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    postback_data: Optional[StrictStr] = Field(default=None, description="postback_url datatype. required field if you specify postback_url. corresponds to the datatype that will be sent to your server. only value: advanced")
    pingback_url: Optional[StrictStr] = Field(default=None, description="notification URL of a completed task. optional field. when a task is completed we will notify you by GET request sent to the URL you have specified. you can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.. example:. http://your-server.com/pingscript?id=$id. http://your-server.com/pingscript?id=$id&tag=$tag. Note: special characters in pingback_url will be urlencoded;. i.a., the # character will be encoded into %23. learn more on our Help Center")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "priority", 
        "depth", 
        "language_name", 
        "language_code", 
        "device", 
        "os", 
        "last_updated", 
        "file_formats", 
        "usage_rights", 
        "is_free", 
        "topics", 
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

        _dict['keyword'] = self.keyword
        _dict['priority'] = self.priority
        _dict['depth'] = self.depth
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['device'] = self.device
        _dict['os'] = self.os
        _dict['last_updated'] = self.last_updated
        _dict['file_formats'] = self.file_formats
        _dict['usage_rights'] = self.usage_rights
        _dict['is_free'] = self.is_free
        _dict['topics'] = self.topics
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
            "keyword": obj.get("keyword"),
            "priority": obj.get("priority"),
            "depth": obj.get("depth"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "device": obj.get("device"),
            "os": obj.get("os"),
            "last_updated": obj.get("last_updated"),
            "file_formats": obj.get("file_formats"),
            "usage_rights": obj.get("usage_rights"),
            "is_free": obj.get("is_free"),
            "topics": obj.get("topics"),
            "tag": obj.get("tag"),
            "postback_url": obj.get("postback_url"),
            "postback_data": obj.get("postback_data"),
            "pingback_url": obj.get("pingback_url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj