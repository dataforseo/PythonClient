from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpGoogleAiModeTaskPostRequestInfo(BaseModel):
    """
    SerpGoogleAiModeTaskPostRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description=r"keywordrequired fieldyou can specify up to 700 characters in the keyword fieldall %## will be decoded (plus character ‘+’ will be decoded to a space character)if you need to use the “%” character for your keyword, please specify it as “%25”;if you need to use the “+” character for your keyword, please specify it as “%2B”learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_code: Optional[StrictInt] = Field(default=None, description=r"search engine location coderequired field if you don't specify location_name or location_coordinateif you use this field, you don't need to specify location_name or location_coordinateyou can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/locationsNote: check  Google Search Help for the list of countries where AI Mode is currently available")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search engine language coderequired field if you don't specify language_name;if you use this field, you don't need to specify language_name;you can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/ai_mode/languages")
    priority: Optional[StrictInt] = Field(default=None, description=r"task priorityoptional fieldcan take the following values:1 – normal execution priority (set by default)2 – high execution priorityYou will be additionally charged for the tasks with high execution priority.The cost can be calculated on the Pricing page.")
    device: Optional[StrictStr] = Field(default=None, description=r"device typeoptional fieldreturn results for a specific device typecan take the values:desktop, mobiledefault value: desktop")
    pingback_url: Optional[StrictStr] = Field(default=None, description=r"notification URL of a completed taskoptional fieldwhen a task is completed we will notify you by GET request sent to the URL you have specifiedyou can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.example:http://your-server.com/pingscript?id=$idhttp://your-server.com/pingscript?id=$id&tag=$tagNote: special characters in pingback_url will be urlencoded;i.a., the # character will be encoded into %23learn more on our Help Center")
    postback_url: Optional[StrictStr] = Field(default=None, description=r"URL for sending task resultsoptional fieldonce the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specifiedyou can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.example:http://your-server.com/postbackscript?id=$idhttp://your-server.com/postbackscript?id=$id&tag=$tagNote: special characters in postback_url will be urlencoded;i.a., the # character will be encoded into %23learn more on our Help Center")
    postback_data: Optional[StrictStr] = Field(default=None, description=r"postback_url datatyperequired field if you specify postback_urlcorresponds to the function you used for setting a taskpossible values:advanced, html")
    location_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine locationrequired field if you don't specify location_code or location_coordinateif you use this field, you don't need to specify location_code or location_coordinateyou can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/locationsNote: check  Google Search Help for the list of countries where AI Mode is currently available")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine languagerequired field if you don't specify language_code;if you use this field, you don't need to specify language_code;you can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/ai_mode/languages;")
    os: Optional[StrictStr] = Field(default=None, description=r"device operating systemoptional fieldif you specify desktop in the device field, choose from the following values: windows, macosdefault value: windowsif you specify mobile in the device field, choose from the following values: android, iosdefault value: android")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response")
    calculate_rectangles: Optional[StrictBool] = Field(default=None, description=r"calculate pixel rankings for SERP elements in advanced resultsoptional fieldpixel ranking refers to the distance between the result snippet and top left corner of the screen;Visit Help Center to learn more>>by default, the parameter is set to falseNote: if set to true, the charge per task will be multiplied by 2")
    browser_screen_width: Optional[StrictInt] = Field(default=None, description=r"browser screen widthoptional fieldyou can set a custom browser screen width to calculate pixel rankings for a particular device;can be specified within the following range: 240-9999;by default, the parameter is set to:1920 for desktop;360 for mobile on android;375 for mobile on iOS;Note: to use this parameter, set calculate_rectangles to true")
    browser_screen_height: Optional[StrictInt] = Field(default=None, description=r"browser screen heightoptional fieldyou can set a custom browser screen height to calculate pixel rankings for a particular device;can be specified within the following range: 240-9999;by default, the parameter is set to:1080 for desktop;640 for mobile on android;812 for mobile on iOS;Note: to use this parameter, set calculate_rectangles to true")
    browser_screen_resolution_ratio: Optional[StrictInt] = Field(default=None, description=r"browser screen resolution ratiooptional fieldyou can set a custom browser screen resolution ratio to calculate pixel rankings for a particular device;can be specified within the following range: 0.5-3;by default, the parameter is set to:1 for desktop;3 for mobile on android;3 for mobile on iOS;Note: to use this parameter, set calculate_rectangles to true")
    location_coordinate: Optional[StrictStr] = Field(default=None, description=r"GPS coordinates of a locationrequired field if you don't specify location_name or location_codeif you use this field, you don't need to specify location_name or location_codelocation_coordinate parameter should be specified in the 'latitude,longitude,zoom' formatif 'zoom' is not specified, 9z will be applied as a default valuethe maximum number of decimal digits for 'latitude' and 'longitude': 7the minimum value for 'zoom': 4zthe maximum value for 'zoom': 18zexample:52.6178549,-155.352142,18z")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_code", 
        "language_code", 
        "priority", 
        "device", 
        "pingback_url", 
        "postback_url", 
        "postback_data", 
        "location_name", 
        "language_name", 
        "os", 
        "tag", 
        "calculate_rectangles", 
        "browser_screen_width", 
        "browser_screen_height", 
        "browser_screen_resolution_ratio", 
        "location_coordinate", 
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
        _dict['priority'] = self.priority
        _dict['device'] = self.device
        _dict['pingback_url'] = self.pingback_url
        _dict['postback_url'] = self.postback_url
        _dict['postback_data'] = self.postback_data
        _dict['location_name'] = self.location_name
        _dict['language_name'] = self.language_name
        _dict['os'] = self.os
        _dict['tag'] = self.tag
        _dict['calculate_rectangles'] = self.calculate_rectangles
        _dict['browser_screen_width'] = self.browser_screen_width
        _dict['browser_screen_height'] = self.browser_screen_height
        _dict['browser_screen_resolution_ratio'] = self.browser_screen_resolution_ratio
        _dict['location_coordinate'] = self.location_coordinate
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
            "priority": obj.get("priority"),
            "device": obj.get("device"),
            "pingback_url": obj.get("pingback_url"),
            "postback_url": obj.get("postback_url"),
            "postback_data": obj.get("postback_data"),
            "location_name": obj.get("location_name"),
            "language_name": obj.get("language_name"),
            "os": obj.get("os"),
            "tag": obj.get("tag"),
            "calculate_rectangles": obj.get("calculate_rectangles"),
            "browser_screen_width": obj.get("browser_screen_width"),
            "browser_screen_height": obj.get("browser_screen_height"),
            "browser_screen_resolution_ratio": obj.get("browser_screen_resolution_ratio"),
            "location_coordinate": obj.get("location_coordinate"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj