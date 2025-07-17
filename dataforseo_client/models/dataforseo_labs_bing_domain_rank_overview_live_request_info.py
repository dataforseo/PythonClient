from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsBingDomainRankOverviewLiveRequestInfo(BaseModel):
    """
    DataforseoLabsBingDomainRankOverviewLiveRequestInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="domain. required field. the domain name of the target website. the domain should be specified without https:// and www.")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location. optional field. if you use this field, you don’t need to specify location_code. you can receive the list of available locations with their location_name by making a separate request to. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;. ignore this field to get the results for all available locations;. Note: this endpoint currently supports the US location only;. example:. United States")
    location_code: Optional[StrictInt] = Field(default=None, description="location code. optional field. if you use this field, you don’t need to specify location_name. you can receive the list of available locations with their location_code by making a separate request to. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available locations;. Note: this endpoint currently supports the US location only;. example:. 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of the language. optional field. if you use this field, you don’t need to specify language_code. you can receive the list of available languages with their language_name by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="language code. optional field. if you use this field, you don’t need to specify language_name. you can receive the list of available languages with their language_code by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available languages. example:. en")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned results for domain. optional field. default value: 100. maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned items. optional field. default value: 0. if you specify the 10 value, the first ten items in the results array will be omitted and the data will be provided for the successive items")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "target", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "limit", 
        "offset", 
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

        _dict['target'] = self.target
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['limit'] = self.limit
        _dict['offset'] = self.offset
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "target": obj.get("target"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj