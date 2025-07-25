from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsBingSubdomainsLiveRequestInfo(BaseModel):
    """
    DataforseoLabsBingSubdomainsLiveRequestInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="domain. required field. the domain name of the target website. the domain should be specified without https:// and www.")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location. optional field. if you use this field, you don’t need to specify location_code. you can receive the list of available locations with their location_name by making a separate request to. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available locations;. Note: this endpoint currently supports the US location only;. example:. United States")
    location_code: Optional[StrictInt] = Field(default=None, description="location code. optional field. if you use this field, you don’t need to specify location_name. you can receive the list of available locations with their location_code by making a separate request to. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;. ignore this field to get the results for all available locations;. Note: this endpoint currently supports the US location only;. example:. 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of the language. optional field. if you use this field, you don’t need to specify language_code. you can receive the list of available languages with their language_name by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="language code. optional field. if you use this field, you don’t need to specify language_name. you can receive the list of available languages with their language_code by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available languages. example:. en")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="display results by item type. optional field. indicates the type of search results included in the response. Note: if the item_types array contains item types that are different from organic, the results will be ordered by the first item type in the array; you will not be able to sort and filter results by the types of search results not included in the response;. possible values:. ['organic', 'paid', 'featured_snippet', 'local_pack']. default value:. ['organic', 'paid', 'featured_snippet', 'local_pack']")
    historical_serp_mode: Optional[StrictStr] = Field(default=None, description="data collection mode. optional field. you can use this field to filter the results;. possible types of filtering:. live — return metrics for SERPs in which the specified target currently has ranking results;. lost — return metrics for SERPs in which the specified target had previously had ranking results, but didn’t have them during the last check;. all — return metrics for both types of SERPs.. default value: live")
    ignore_synonyms: Optional[StrictBool] = Field(default=None, description="ignore highly similar keywords. optional field. if set to true, only core keywords will be returned, all highly similar keywords will be excluded;. default value: false")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, <, <=, >, >=, =, <>, in, not_in. example:. ['metrics.paid.count','>',0]. [['metrics.paid.count','>',0],'and',['metrics.paid.etv','>','50']]. [['metrics.organic.count','>','10'],. 'and',. [['metrics.organic.pos_1','<>',0],'or',['metrics.organic.pos_2_3','<>',0]]]. for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. you can use the same values as in the filters array to sort the results. possible sorting types:. asc – results will be sorted in the ascending order. desc – results will be sorted in the descending order. you should use a comma to specify a sorting type. example:. ['metrics.paid.etv,asc']. Note: you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['metrics.organic.etv,desc','metrics.paid.count,asc']. default rule:. ['metrics.organic.count,desc']. Note: if the item_types array contains item types that are different from organic, the results will be ordered by the first item type in the array")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned keywords. optional field. default value: 100. maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned keywords. optional field. default value: 0. if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "target", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "item_types", 
        "historical_serp_mode", 
        "ignore_synonyms", 
        "filters", 
        "order_by", 
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
        _dict['item_types'] = self.item_types
        _dict['historical_serp_mode'] = self.historical_serp_mode
        _dict['ignore_synonyms'] = self.ignore_synonyms
        _dict['filters'] = self.filters
        _dict['order_by'] = self.order_by
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
            "item_types": obj.get("item_types"),
            "historical_serp_mode": obj.get("historical_serp_mode"),
            "ignore_synonyms": obj.get("ignore_synonyms"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj