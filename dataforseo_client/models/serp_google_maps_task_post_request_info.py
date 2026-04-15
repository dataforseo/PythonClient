from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpGoogleMapsTaskPostRequestInfo(BaseModel):
    """
    SerpGoogleMapsTaskPostRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description=r"keywordrequired fieldyou can specify up to 700 characters  in the keyword fieldall %## will be decoded (plus character ‘+’ will be decoded to a space character)if you need to use the “%” character for your keyword, please specify it as “%25”;if you need to use the “+” character for your keyword, please specify it as “%2B”;if this field contains such parameters as ‘allinanchor:’, ‘allintext:’, ‘allintitle:’, ‘allinurl:’, ‘define:’, ‘filetype:’, ‘id:’, ‘inanchor:’, ‘info:’, ‘intext:’, ‘intitle:’, ‘inurl:’, ‘link:’, ‘related:’, ‘site:’, the charge per task will be multiplied by 5Note: queries containing the ‘cache:’ parameter are not supported and will return a validation errorlearn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_code: Optional[StrictInt] = Field(default=None, description=r"search engine location coderequired field if you don't specify location_name or location_coordinateif you use this field, you don't need to specify location_name or location_coordinateyou can receive the list of available locations of the search engines with their location_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/locationsexample:2840")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search engine language coderequired field if you don't specify language_nameif you use this field, you don't need to specify language_nameyou can receive the list of available languages of the search engine with their language_code by making a separate request to the https://api.dataforseo.com/v3/serp/google/languagesexample:en")
    depth: Optional[StrictInt] = Field(default=None, description=r"parsing depthoptional fieldnumber of results in SERPdefault value: 100max value: 700Your account will be billed per each SERP containing up to 100 results;Setting depth above 100 may result in additional charges if the search engine returns more than 100 results;The cost can be calculated on the Pricing page.")
    priority: Optional[StrictInt] = Field(default=None, description=r"task priorityoptional fieldcan take the following values:1 – normal execution priority (set by default)2 – high execution priorityYou will be additionally charged for the tasks with high execution priority.The cost can be calculated on the Pricing page.")
    device: Optional[StrictStr] = Field(default=None, description=r"device typeoptional fieldreturn results for a specific device typecan take the values:desktop, mobiledefault value: desktopnote: for mobile device, only 20 results are returned for every SERP")
    pingback_url: Optional[StrictStr] = Field(default=None, description=r"notification URL of a completed taskoptional fieldwhen a task is completed we will notify you by GET request sent to the URL you have specifiedyou can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.example:http://your-server.com/pingscript?id=$idhttp://your-server.com/pingscript?id=$id&tag=$tagNote: special characters in pingback_url will be urlencoded;i.a., the # character will be encoded into %23learn more on our Help Center")
    postback_url: Optional[StrictStr] = Field(default=None, description=r"URL for sending task resultsoptional fieldonce the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specifiedyou can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.example:http://your-server.com/postbackscript?id=$idhttp://your-server.com/postbackscript?id=$id&tag=$tagNote: special characters in postback_url will be urlencoded;i.a., the # character will be encoded into %23learn more on our Help Center")
    postback_data: Optional[StrictStr] = Field(default=None, description=r"postback_url datatyperequired field if you specify postback_urlcorresponds to the function you used for setting a taskpossible values:advanced")
    location_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine locationrequired field if you don't specify location_code or location_coordinateif you use this field, you don't need to specify location_code or location_coordinateyou can receive the list of available locations of the search engine with their location_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/locationsexample:London,England,United Kingdom")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of search engine languagerequired field if you don't specify language_codeif you use this field, you don't need to specify language_codeyou can receive the list of available languages of the search engine with their language_name by making a separate request to the https://api.dataforseo.com/v3/serp/google/languagesexample:English")
    os: Optional[StrictStr] = Field(default=None, description=r"device operating systemoptional fieldif you specify desktop in the device field, choose from the following values: windows, macosdefault value: windowsif you specify mobile in the device field, choose from the following values: android, iosdefault value: android")
    max_crawl_pages: Optional[StrictInt] = Field(default=None, description=r"page crawl limitoptional fieldnumber of search results pages to crawlmax value: 100Note: the max_crawl_pages and depth parameters complement each other;learn more at our help center")
    url: Optional[StrictStr] = Field(default=None, description=r"direct URL of the search queryoptional fieldyou can specify a direct URL and we will sort it out to the necessary fields. Note that this method is the most difficult for our API to process and also requires you to specify the exact language and location in the URL. In most cases, we wouldn’t recommend using this method.example:https://google.com/maps/search/pizza/@37.09024,-95.712891,4z")
    location_coordinate: Optional[StrictStr] = Field(default=None, description=r"GPS coordinates of a locationrequired field if you don't specify location_name or location_codeif you use this field, you don't need to specify location_name or location_codelocation_coordinate parameter should be specified in the 'latitude,longitude,zoom' formatif 'zoom' is not specified, 17z will be applied as a default valuethe maximum number of decimal digits for 'latitude' and 'longitude': 7the minimum value for 'zoom': 3zthe maximum value for 'zoom': 21zexample:52.6178549,-155.352142,20z")
    se_domain: Optional[StrictStr] = Field(default=None, description=r"search engine domainoptional fieldwe choose the relevant search engine domain automatically according to the location and language you specifyhowever, you can set a custom search engine domain in this fieldexample:google.co.uk")
    search_this_area: Optional[StrictBool] = Field(default=None, description=r"show results from the displayed areaoptional fieldcan take the values:true, falsedefault value: trueif set to false, the search_this_area mode will be turned offNote: if the search_this_area mode is turned off, Google Maps listings might contain results beyond the displayed area")
    search_places: Optional[StrictBool] = Field(default=None, description=r"search places modeoptional fieldthe search places mode allows to obtain Google Maps results on a certain place (e.g., Apple Store in New York)however, due to the pecularities of our data mining algorithm, this mode might interfere with some local-intent queries - and display results for a location that is different from that specified in the request;to prevent this interference and obtain correct results for keywords with local intent you may set this parameter to false;default value: trueNote: if the search_places mode is turned off and no results were found in the search area, the results array will be empty")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_code", 
        "language_code", 
        "depth", 
        "priority", 
        "device", 
        "pingback_url", 
        "postback_url", 
        "postback_data", 
        "location_name", 
        "language_name", 
        "os", 
        "max_crawl_pages", 
        "url", 
        "location_coordinate", 
        "se_domain", 
        "search_this_area", 
        "search_places", 
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
        _dict['depth'] = self.depth
        _dict['priority'] = self.priority
        _dict['device'] = self.device
        _dict['pingback_url'] = self.pingback_url
        _dict['postback_url'] = self.postback_url
        _dict['postback_data'] = self.postback_data
        _dict['location_name'] = self.location_name
        _dict['language_name'] = self.language_name
        _dict['os'] = self.os
        _dict['max_crawl_pages'] = self.max_crawl_pages
        _dict['url'] = self.url
        _dict['location_coordinate'] = self.location_coordinate
        _dict['se_domain'] = self.se_domain
        _dict['search_this_area'] = self.search_this_area
        _dict['search_places'] = self.search_places
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
            "depth": obj.get("depth"),
            "priority": obj.get("priority"),
            "device": obj.get("device"),
            "pingback_url": obj.get("pingback_url"),
            "postback_url": obj.get("postback_url"),
            "postback_data": obj.get("postback_data"),
            "location_name": obj.get("location_name"),
            "language_name": obj.get("language_name"),
            "os": obj.get("os"),
            "max_crawl_pages": obj.get("max_crawl_pages"),
            "url": obj.get("url"),
            "location_coordinate": obj.get("location_coordinate"),
            "se_domain": obj.get("se_domain"),
            "search_this_area": obj.get("search_this_area"),
            "search_places": obj.get("search_places"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj