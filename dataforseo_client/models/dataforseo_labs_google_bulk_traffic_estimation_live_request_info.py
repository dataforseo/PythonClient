from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsGoogleBulkTrafficEstimationLiveRequestInfo(BaseModel):
    """
    DataforseoLabsGoogleBulkTrafficEstimationLiveRequestInfo
    """ # noqa: E501
    targets: Optional[List[Optional[StrictStr]]] = Field(default=None, description="target domains, subdomains, and webpages. required field. you can specify domains, subdomains, and webpages in this field;. domains and subdomains should be specified without https:// and www.;. pages should be specified with absolute URL, including https:// and www.;. you can set up to 1000 domains, subdomains or webpages")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location. if you use this field, you don’t have to specify location_code. you can receive the list of available locations with their location_name by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available locations. example:. United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="location code. if you use this field, you don’t have to specify location_name. you can receive the list of available locations with their location_code by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available locations. example:. 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of the language. if you use this field, you don’t need to specify language_code. you can receive the list of available languages with their language_name by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="language code. if you use this field, you don’t need to specify language_name. you can receive the list of available languages with their language_code by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available languages. example:. en")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="display results by item type. optional field. indicates the type of search results included in the response. Note: if the item_types array contains item types that are different from organic, the results will be ordered by the first item type in the array. possible values:. ['organic', 'paid', 'featured_snippet', 'local_pack']. default value:. ['organic', 'paid']")
    ignore_synonyms: Optional[StrictBool] = Field(default=None, description="ignore highly similar keywords. optional field. if set to true, only core keywords will be returned, all highly similar keywords will be excluded;. default value: false")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "targets", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "item_types", 
        "ignore_synonyms", 
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
        _dict['item_types'] = self.item_types
        _dict['ignore_synonyms'] = self.ignore_synonyms
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
            "item_types": obj.get("item_types"),
            "ignore_synonyms": obj.get("ignore_synonyms"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj