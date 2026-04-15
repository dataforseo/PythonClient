from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AiOptimizationGeminiLlmScraperTaskPostRequestInfo(BaseModel):
    """
    AiOptimizationGeminiLlmScraperTaskPostRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description=r"keywordrequired fieldyou can specify up to 2000 characters in the keyword fieldall %## will be decoded (plus character ‘+’ will be decoded to a space character)if you need to use the “%” character for your keyword, please specify it as “%25”;if you need to use the “+” character for your keyword, please specify it as “%2B”learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    priority: Optional[StrictInt] = Field(default=None, description=r"task priorityoptional fieldcan take the following values:1 – normal execution priority (set by default)2 – high execution priorityYou will be additionally charged for the tasks with high execution priority.The cost can be calculated on the Pricing page.")
    location_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine locationrequired field if you don't specify location_codeif you use this field, you don't need to specify location_codeyou can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/gemini/llm_scraper/locationsexample:United States")
    location_code: Optional[StrictInt] = Field(default=None, description=r"search engine location coderequired field if you don't specify location_nameif you use this field, you don't need to specify location_nameyou can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/gemini/llm_scraper/locationsexample:2840")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine languagerequired field if you don't specify language_code;if you use this field, you don't need to specify language_code;you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/gemini/llm_scraper/languagesexample:English")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search engine language coderequired field if you don't specify language_name;if you use this field, you don't need to specify language_name;you can receive the list of available languages of the search engine with their language_code_by making a separate request to the https://api.dataforseo.com/v3/ai_optimization/gemini/llm_scraper/languagesexample:enn")
    expand_citations: Optional[StrictBool] = Field(default=None, description=r"return expanded citation bar in HTML resultsoptional fieldwhen enabled, the HTML endpoint will return data from the expanded citation bar;default value: false")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response")
    postback_url: Optional[StrictStr] = Field(default=None, description=r"URL for sending task resultsoptional fieldonce the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specifiedyou can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.example:http://your-server.com/postbackscript?id=$idhttp://your-server.com/postbackscript?id=$id&tag=$tagNote: special characters in postback_url will be urlencoded;i.a., the # character will be encoded into %23learn more on our Help Center")
    postback_data: Optional[StrictStr] = Field(default=None, description=r"postback_url datatyperequired field if you specify postback_urlcorresponds to the function you used for setting a taskpossible values:advanced, html")
    pingback_url: Optional[StrictStr] = Field(default=None, description=r"notification URL of a completed taskoptional fieldwhen a task is completed we will notify you by GET request sent to the URL you have specifiedyou can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.example:http://your-server.com/pingscript?id=$idhttp://your-server.com/pingscript?id=$id&tag=$tagNote: special characters in pingback_url will be urlencoded;i.a., the # character will be encoded into %23learn more on our Help Center")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "priority", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "expand_citations", 
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
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['expand_citations'] = self.expand_citations
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
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "expand_citations": obj.get("expand_citations"),
            "tag": obj.get("tag"),
            "postback_url": obj.get("postback_url"),
            "postback_data": obj.get("postback_data"),
            "pingback_url": obj.get("pingback_url"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj