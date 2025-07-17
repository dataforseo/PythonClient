from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class KeywordsDataBingAudienceEstimationLiveRequestInfo(BaseModel):
    """
    KeywordsDataBingAudienceEstimationLiveRequestInfo
    """ # noqa: E501
    location_name: Optional[StrictStr] = Field(default=None, description="full name of search engine location. required field if you don’t specify location_code or location_coordinate. if you use this field, you don’t need to specify location_code or location_coordinate. you can receive the list of available locations of the search engine with their location_name by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/locations. example:. London,England,United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="search engine location code. required field if you don’t specify location_name or location_coordinate. if you use this field, you don’t need to specify location_name or location_coordinate. you can receive the list of available locations of the search engines with their location_code by making a separate request to https://api.dataforseo.com/v3/keywords_data/bing/locations. example:. 2840")
    location_coordinate: Optional[StrictStr] = Field(default=None, description="GPS coordinates of a location. required field if you don’t specify location_name or location_code. if you use this field, you don’t need to specify location_name or location_code. location_coordinate parameter should be specified in the “latitude,longitude,radius (in km)” format. the data will be provided for the country the specified coordinates belong to. example:. 29.6821525,-82.4098881,100")
    age: Optional[List[Optional[StrictStr]]] = Field(default=None, description="selection of age ranges for targeting. possible values: eighteen_to_twenty_four, fifty_to_sixty_four, sixty_five_and_above, thirteen_to_seventeen, thirty_five_to_forty_nine, twenty_five_to_thirty_four, unknown, zero_to_twelve")
    bid: Optional[StrictFloat] = Field(default=None, description="desired bid setting value in USD. maximum value: 1000")
    daily_budget: Optional[StrictFloat] = Field(default=None, description="daily campaign budget value in USD. maximum value: 10000")
    gender: Optional[List[Optional[StrictStr]]] = Field(default=None, description="gender to target. possible values: male, female, unknown")
    industry: Optional[List[Optional[StrictStr]]] = Field(default=None, description="industry of LinkedIn profile targeting. if you use this field, you can receive the list of available industry names  with industry_id by making a separate request to the https://api.dataforseo.com/v3/keywords_data/bing/audience_estimation/industries. example: 806301758")
    job_function: Optional[List[Optional[StrictStr]]] = Field(default=None, description="job function of LinkedIn profile targeting. if you use this field, you can receive the list of available job function names  with job_function_id by making a separate request to the https://api.dataforseo.com/v3/keywords_data/bing/audience_estimation/job_functions. example: 806300451")
    __properties: ClassVar[List[str]] = [
        "location_name", 
        "location_code", 
        "location_coordinate", 
        "age", 
        "bid", 
        "daily_budget", 
        "gender", 
        "industry", 
        "job_function", 
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

        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['location_coordinate'] = self.location_coordinate
        _dict['age'] = self.age
        _dict['bid'] = self.bid
        _dict['daily_budget'] = self.daily_budget
        _dict['gender'] = self.gender
        _dict['industry'] = self.industry
        _dict['job_function'] = self.job_function
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "location_coordinate": obj.get("location_coordinate"),
            "age": obj.get("age"),
            "bid": obj.get("bid"),
            "daily_budget": obj.get("daily_budget"),
            "gender": obj.get("gender"),
            "industry": obj.get("industry"),
            "job_function": obj.get("job_function"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj