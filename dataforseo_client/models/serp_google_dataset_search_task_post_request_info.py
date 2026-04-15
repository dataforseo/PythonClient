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
    keyword: Optional[StrictStr] = Field(default=None, description=r"keywordrequired fieldyou can specify up to 700 characters in the keyword fieldall %## will be decoded (plus character ‘+’ will be decoded to a space character)if you need to use the “%” character for your keyword, please specify it as “%25”;if you need to use the “+” character for your keyword, please specify it as “%2B”.learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search engine language codeoptional fieldpossible value:en")
    depth: Optional[StrictInt] = Field(default=None, description=r"parsing depthoptional fieldnumber of results in SERPdefault value: 20max value: 700Your account will be billed per each SERP containing up to 20 results;Setting depth above 20 may result in additional charges if the search engine returns more than 20 results;If the specified depth is higher than the number of results in the response, the difference will be refunded to your account balance automatically;")
    priority: Optional[StrictInt] = Field(default=None, description=r"task priorityoptional fieldcan take the following values:1 – normal execution priority (set by default)2 – high execution priorityYou will be additionally charged for the tasks with high execution priority.The cost can be calculated on the Pricing page.")
    device: Optional[StrictStr] = Field(default=None, description=r"device typeoptional fieldreturn results for a specific device typepossible value: desktop")
    pingback_url: Optional[StrictStr] = Field(default=None, description=r"notification URL of a completed taskoptional fieldwhen a task is completed we will notify you by GET request sent to the URL you have specifiedyou can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.example:http://your-server.com/pingscript?id=$idhttp://your-server.com/pingscript?id=$id&tag=$tagNote: special characters in pingback_url will be urlencoded;i.a., the # character will be encoded into %23learn more on our Help Center")
    postback_url: Optional[StrictStr] = Field(default=None, description=r"URL for sending task resultsoptional fieldonce the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specifiedyou can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the requestexample:http://your-server.com/postbackscript?id=$idhttp://your-server.com/postbackscript?id=$id&tag=$tagNote: special characters in postback_url will be urlencoded;i.a., the # character will be encoded into %23learn more on our Help Center")
    postback_data: Optional[StrictStr] = Field(default=None, description=r"postback_url datatyperequired field if you specify postback_urlcorresponds to the datatype that will be sent to your serveronly value: advanced")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine languageoptional fieldif you use this field, you don't need to specify language_codepossible value:English")
    os: Optional[StrictStr] = Field(default=None, description=r"device operating systemoptional fieldpossible values: windows, macosdefault value: windows")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response")
    last_updated: Optional[StrictStr] = Field(default=None, description=r"last time the dataset was updatedoptional fieldpossible values: 1m, 1y, 3y")
    file_formats: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"file formats of the datasetoptional fieldpossible values: other, archive, text, image, document, tabular")
    usage_rights: Optional[StrictStr] = Field(default=None, description=r"usage rights of the datasetoptional fieldpossible values: commercial, noncommercial")
    is_free: Optional[StrictBool] = Field(default=None, description=r"indicates whether displayed datasets are freeoptional fieldpossible values: true, false")
    topics: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"dataset topicsoptional fieldpossible values: humanities, social_sciences, life_sciences, agriculture, natural_sciences, geo, computer, architecture_and_urban_planning, engineering")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "language_code", 
        "depth", 
        "priority", 
        "device", 
        "pingback_url", 
        "postback_url", 
        "postback_data", 
        "language_name", 
        "os", 
        "tag", 
        "last_updated", 
        "file_formats", 
        "usage_rights", 
        "is_free", 
        "topics", 
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
        _dict['language_code'] = self.language_code
        _dict['depth'] = self.depth
        _dict['priority'] = self.priority
        _dict['device'] = self.device
        _dict['pingback_url'] = self.pingback_url
        _dict['postback_url'] = self.postback_url
        _dict['postback_data'] = self.postback_data
        _dict['language_name'] = self.language_name
        _dict['os'] = self.os
        _dict['tag'] = self.tag
        _dict['last_updated'] = self.last_updated
        _dict['file_formats'] = self.file_formats
        _dict['usage_rights'] = self.usage_rights
        _dict['is_free'] = self.is_free
        _dict['topics'] = self.topics
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "language_code": obj.get("language_code"),
            "depth": obj.get("depth"),
            "priority": obj.get("priority"),
            "device": obj.get("device"),
            "pingback_url": obj.get("pingback_url"),
            "postback_url": obj.get("postback_url"),
            "postback_data": obj.get("postback_data"),
            "language_name": obj.get("language_name"),
            "os": obj.get("os"),
            "tag": obj.get("tag"),
            "last_updated": obj.get("last_updated"),
            "file_formats": obj.get("file_formats"),
            "usage_rights": obj.get("usage_rights"),
            "is_free": obj.get("is_free"),
            "topics": obj.get("topics"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj