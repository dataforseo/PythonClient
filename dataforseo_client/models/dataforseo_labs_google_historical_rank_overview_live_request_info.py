from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsGoogleHistoricalRankOverviewLiveRequestInfo(BaseModel):
    """
    DataforseoLabsGoogleHistoricalRankOverviewLiveRequestInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="domain. required field. the domain name of the target website. the domain should be specified without https:// and www.")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location. required field if you don’t specify location_code. Note: it is required to specify either location_name or location_code. you can receive the list of available locations with their location_name by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="location code. required field if you don’t specify location_name. Note: it is required to specify either location_name or location_code. you can receive the list of available locations with their location_code by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of the language. required field if you don’t specify language_code. Note: it is required to specify either language_name or language_code. you can receive the list of available locations with their language_name by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="language code. required field if you don’t specify language_name. Note: it is required to specify either language_name or language_code. you can receive the list of available locations with their language_code by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. en")
    date_from: Optional[StrictStr] = Field(default=None, description="starting date of the time range. optional field. if you don’t specify this field, the data will be provided for the previous 6 months. minimal possible value: 2020-10-01. date format: 'yyyy-mm-dd'")
    date_to: Optional[StrictStr] = Field(default=None, description="ending date of the time range. optional field. if you don’t specify this field, the today’s date will be used by default. date format: 'yyyy-mm-dd'. example:. '2021-04-01'")
    correlate: Optional[StrictBool] = Field(default=None, description="correlate data with previously obtained datasets. optional field. default value: true. if you use this parameter, our system will correlate data you obtain now with previously obtained datasets. this parameter is intended to mitigate any inconsistencies that may result from changes to our database. we recommend always setting correlate to true")
    ignore_synonyms: Optional[StrictBool] = Field(default=None, description="ignore highly similar keywords. optional field. if set to true, only data based on core keywords will be returned, data for all highly similar keywords will be excluded;. default value: false")
    include_clickstream_data: Optional[StrictBool] = Field(default=None, description="include or exclude data from clickstream-based metrics in the result. optional field. if the parameter is set to true, you will receive clickstream_etv, clickstream_gender_distribution, and clickstream_age_distribution fields with clickstream data in the response;. default value: false;. Note: historical clickstream data is available from 2024/05 (May, 2024);. with this parameter enabled, you will be charged double the price for the request;. learn more about how clickstream-based metrics are calculated in this help center article")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "target", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "date_from", 
        "date_to", 
        "correlate", 
        "ignore_synonyms", 
        "include_clickstream_data", 
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
        _dict['date_from'] = self.date_from
        _dict['date_to'] = self.date_to
        _dict['correlate'] = self.correlate
        _dict['ignore_synonyms'] = self.ignore_synonyms
        _dict['include_clickstream_data'] = self.include_clickstream_data
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
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "correlate": obj.get("correlate"),
            "ignore_synonyms": obj.get("ignore_synonyms"),
            "include_clickstream_data": obj.get("include_clickstream_data"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj