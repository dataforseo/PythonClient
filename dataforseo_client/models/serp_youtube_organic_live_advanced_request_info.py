from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpYoutubeOrganicLiveAdvancedRequestInfo(BaseModel):
    """
    SerpYoutubeOrganicLiveAdvancedRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description=r"keyword. required field. you can specify up to 700 characters in the keyword field. all %## will be decoded (plus character ‘+’ will be decoded to a space character). if you need to use the “%” character for your keyword, please specify it as “%25”;. if you need to use the “+” character for your keyword, please specify it as “%2B”;. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_code: Optional[StrictInt] = Field(default=None, description=r"search engine location code. required field if you don't specify location_name . if you use this field, you don't need to specify location_name. you can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/locations. example:. 2840")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search engine language code. required field if you don't specify language_name. if you use this field, you don't need to specify language_name. you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/languages. example:. en")
    device: Optional[StrictStr] = Field(default=None, description=r"device type. optional field. return results for a specific device type. available values: desktop, mobile")
    block_depth: Optional[StrictInt] = Field(default=None, description=r"parsing depth. optional field. number of blocks of results in SERP. default value: 20. max value: 700. Note: your account will be billed per each SERP containing up to 20 results;. thus, setting a block depth above 20 may result in additional charges if the search engine returns more than 20 results;. if the specified block depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance")
    location_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine location. required field if you don't specify location_code. if you use this field, you don't need to specify location_code. you can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/locations. example:. United States")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine language. required field if you don't specify language_code. if you use this field, you don't need to specify language_code. you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/youtube/languages. example:. English")
    os: Optional[StrictStr] = Field(default=None, description=r"device operating system. optional field. if you specify desktop in the device field, choose from the following values: windows, macos. default value: windows. if you specify mobile in the device field, choose from the following values: android, ios. default value: android")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    search_param: Optional[StrictStr] = Field(default=None, description=r"additional parameters of the search query. optional field. example:. sp=EgIQAg%253D%253D")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_code", 
        "language_code", 
        "device", 
        "block_depth", 
        "location_name", 
        "language_name", 
        "os", 
        "tag", 
        "search_param", 
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
        _dict['block_depth'] = self.block_depth
        _dict['location_name'] = self.location_name
        _dict['language_name'] = self.language_name
        _dict['os'] = self.os
        _dict['tag'] = self.tag
        _dict['search_param'] = self.search_param
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
            "block_depth": obj.get("block_depth"),
            "location_name": obj.get("location_name"),
            "language_name": obj.get("language_name"),
            "os": obj.get("os"),
            "tag": obj.get("tag"),
            "search_param": obj.get("search_param"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj