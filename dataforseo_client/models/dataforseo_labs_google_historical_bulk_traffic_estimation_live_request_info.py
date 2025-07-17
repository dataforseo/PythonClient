from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveRequestInfo(BaseModel):
    """
    DataforseoLabsGoogleHistoricalBulkTrafficEstimationLiveRequestInfo
    """ # noqa: E501
    targets: Optional[List[Optional[StrictStr]]] = Field(default=None, description="target domains and subdomains. required field. you can specify domains and subdomains in this field;. domains and subdomains should be specified without https:// and www.;. you can set up to 1000 domains or subdomains")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location. if you use this field, you don’t have to specify location_code. you can receive the list of available locations with their location_name by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available locations. example:. United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="location code. if you use this field, you don’t have to specify location_name. you can receive the list of available locations with their location_code by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available locations. example:. 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of the language. if you use this field, you don’t need to specify language_code. you can receive the list of available languages with their language_name by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="language code. if you use this field, you don’t need to specify language_name. you can receive the list of available languages with their language_code by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available languages. example:. en")
    date_from: Optional[StrictStr] = Field(default=None, description="starting date of the time range. optional field. if you don’t specify this field, the data will be provided for the previous 12 months. minimal possible value: 2020-10-01. date format: 'yyyy-mm-dd'")
    date_to: Optional[StrictStr] = Field(default=None, description="ending date of the time range. optional field. if you don’t specify this field, the today’s date will be used by default;. date format: 'yyyy-mm-dd'. example:. '2021-04-01'")
    ignore_synonyms: Optional[StrictBool] = Field(default=None, description="ignore highly similar keywords. optional field. if set to true, only core keywords will be returned, all highly similar keywords will be excluded;. default value: false")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="display results by item type. optional field. indicates the type of search results included in the response;. Note: if the item_types array contains item types that are different from organic, the results will be ordered by the first item type in the array;. possible values:. ['organic', 'paid', 'featured_snippet', 'local_pack']. default value:. ['organic', 'paid']")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "targets", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "date_from", 
        "date_to", 
        "ignore_synonyms", 
        "item_types", 
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

        _dict['targets'] = self.targets
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['date_from'] = self.date_from
        _dict['date_to'] = self.date_to
        _dict['ignore_synonyms'] = self.ignore_synonyms
        _dict['item_types'] = self.item_types
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "targets": obj.get("targets"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "ignore_synonyms": obj.get("ignore_synonyms"),
            "item_types": obj.get("item_types"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj