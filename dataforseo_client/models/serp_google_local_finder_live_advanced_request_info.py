from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpGoogleLocalFinderLiveAdvancedRequestInfo(BaseModel):
    """
    SerpGoogleLocalFinderLiveAdvancedRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description=r"keywordrequired fieldyou can specify up to 700 characters in the keyword fieldall %## will be decoded (plus character ‘+’ will be decoded to a space character)if you need to use the “%” character for your keyword, please specify it as “%25”;if you need to use the “+” character for your keyword, please specify it as “%2B”learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_code: Optional[StrictInt] = Field(default=None, description=r"search engine location coderequired field if you don't specify location_name or location_coordinateif you use this field, you don't need to specify location_name or location_coordinateyou can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/locationsexample:2840")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search engine language coderequired field if you don't specify language_nameif you use this field, you don't need to specify language_nameyou can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languagesexample:en")
    depth: Optional[StrictInt] = Field(default=None, description=r"parsing depthoptional fieldnumber of results in SERPdefault value for desktop: 20max value for desktop: 100default value for mobile: 10max value for mobile: 100Your account will be billed per each SERP containing up to 20 results for desktop or up to 10 results for a mobile device;Setting depth above 20 for desktop or above 10 for mobile may result in additional charges if the search engine returns more than 20 or 10 results respectively;;If the specified depth is higher than the number of results in the response, the difference will be refunded to your account balance automaticallyThe cost can be calculated on the Pricing page.")
    device: Optional[StrictStr] = Field(default=None, description=r"device typeoptional fieldreturn results for a specific device typecan take the values:desktop, mobiledefault value: desktop")
    location_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine locationrequired field if you don't specify location_code or location_coordinateif you use this field, you don't need to specify location_code or location_coordinateyou can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/locationsexample:London,England,United Kingdom")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine languagerequired field if you don't specify language_codeif you use this field, you don't need to specify language_codeyou can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/languagesexample:English")
    os: Optional[StrictStr] = Field(default=None, description=r"device operating systemoptional fieldif you specify desktop in the device field, choose from the following values: windows, macosdefault value: windowsif you specify mobile in the device field, choose from the following values: android, iosdefault value: android")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response")
    priority: Optional[StrictInt] = Field(default=None, description=r"task priorityoptional fieldcan take the following values:1 – normal execution priority (set by default)2 – high execution priorityYou will be additionally charged for the tasks with high execution priority.The cost can be calculated on the Pricing page.")
    location_coordinate: Optional[StrictStr] = Field(default=None, description=r"GPS coordinates of a locationrequired field if you don't specify location_name or location_codeif you use this field, you don't need to specify location_name or location_codelocation_coordinate parameter should be specified in the 'latitude,longitude,zoom' formatif 'zoom' is not specified, 9z will be applied as a default valuethe maximum number of decimal digits for 'latitude' and 'longitude': 7the minimum value for 'zoom': 4zthe maximum value for 'zoom': 18zexample:52.6178549,-155.352142,20z")
    min_rating: Optional[StrictFloat] = Field(default=None, description=r"filter results by minimum ratingoptional fieldpossible values for desktop: 3.5, 4, 4.5;possible values for mobile: 2, 2.5, 3, 3.5, 4, 4.5")
    time_filter: Optional[StrictStr] = Field(default=None, description=r"filter results by open hoursoptional fieldusing this field, you can filter places in the results by the time a place is open for visitorsnote that Google may also provide results that do not match this filterpossible values: 'open_now', '24_hours', '$day_value', '$day_value;$time_value';instead of $day_value use one of these values: 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday';instead of $time_value use one of these values: '00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'example: 'tuesday;18'")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_code", 
        "language_code", 
        "depth", 
        "device", 
        "location_name", 
        "language_name", 
        "os", 
        "tag", 
        "priority", 
        "location_coordinate", 
        "min_rating", 
        "time_filter", 
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
        _dict['depth'] = self.depth
        _dict['device'] = self.device
        _dict['location_name'] = self.location_name
        _dict['language_name'] = self.language_name
        _dict['os'] = self.os
        _dict['tag'] = self.tag
        _dict['priority'] = self.priority
        _dict['location_coordinate'] = self.location_coordinate
        _dict['min_rating'] = self.min_rating
        _dict['time_filter'] = self.time_filter
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
            "depth": obj.get("depth"),
            "device": obj.get("device"),
            "location_name": obj.get("location_name"),
            "language_name": obj.get("language_name"),
            "os": obj.get("os"),
            "tag": obj.get("tag"),
            "priority": obj.get("priority"),
            "location_coordinate": obj.get("location_coordinate"),
            "min_rating": obj.get("min_rating"),
            "time_filter": obj.get("time_filter"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj