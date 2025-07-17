from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BusinessDataGoogleQuestionsAndAnswersLiveRequestInfo(BaseModel):
    """
    BusinessDataGoogleQuestionsAndAnswersLiveRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword. required field. the keyword you specify should indicate the name of the local establishment. you can specify up to 700 characters in the keyword filed. all %## will be decoded (plus character ‘+’ will be decoded to a space character). if you need to use the “%” character for your keyword, please specify it as “%25”; . this field can also be used to pass the following parameters:. cid – a unique, google-defined id of the business entity;. place_id – an identifier of the business entity in Google Maps;. spp – a unique identifier of local services featured in the local_pack element of Google SERP. example:. cid:194604053573767737. place_id:GhIJQWDl0CIeQUARxks3icF8U8A. spp:CgsvZy8xdGN4cWRraBoUChIJPZDrEzLsZIgRoNrpodC5P30. learn more about the cid and place_id identifiers in this help center article. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location. required field if you don’t specify location_code or location_coordinate. if you use this field, you don’t need to specify location_code or location_coordinate. you can receive the list of available locations with location_name by making a separate request to https://api.dataforseo.com/v3/business_data/google/locations. example:. London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code. required field if you don’t specify location_name or location_coordinate. if you use this field, you don’t need to specify location_name or location_coordinate. you can receive the list of available locations with location_code by making a separate request to the https://api.dataforseo.com/v3/business_data/google/locations. example:. 2840")
    location_coordinate: Optional[StrictStr] = Field(default=None, description="GPS coordinates of a location. required field if you don’t specify location_name or location_code. if you use this field, you don’t need to specify location_name or location_code. location_coordinate parameter should be specified in the “latitude,longitude,radius” format. the maximum number of decimal digits for “latitude” and “longitude”: 7. the minimum value for “radius”: 199.9 (mm). the maximum value for “radius”: 199999 (mm). example:. 53.476225,-2.243572,200")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of search engine language. required field if you don’t specify language_code. if you use this field, you don’t need to specify language_code. you can receive the list of available languages with language_name by making a separate request to https://api.dataforseo.com/v3/business_data/google/languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="search engine language code. required field if you don’t specify language_name. if you use this field, you don’t need to specify language_name. you can receive the list of available languages with their language_code by making a separate request to https://api.dataforseo.com/v3/business_data/google/languages. example:. en")
    depth: Optional[StrictInt] = Field(default=None, description="parsing depth. optional field. number of results in SERP. default value: 20. max value: 100. Note: your account will be billed per each SERP containing up to 20 results;. thus, setting a depth above 20 may result in additional charges if the search engine returns more than 20 results;. if the specified depth is higher than the number of results in the response, the difference will be refunded automatically to your account balance")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_name", 
        "location_code", 
        "location_coordinate", 
        "language_name", 
        "language_code", 
        "depth", 
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
        _dict['location_coordinate'] = self.location_coordinate
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['depth'] = self.depth
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
            "location_coordinate": obj.get("location_coordinate"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "depth": obj.get("depth"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj