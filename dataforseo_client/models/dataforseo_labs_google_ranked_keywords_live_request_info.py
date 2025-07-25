from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsGoogleRankedKeywordsLiveRequestInfo(BaseModel):
    """
    DataforseoLabsGoogleRankedKeywordsLiveRequestInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="domain name or page url. required field. the domain name of the target website or URL of the target webpage;. the domain name must be specified without https:// or www.;. the webpage URL must be specified with https:// or www.. Note: if you specify the webpage URL without https:// or www., the result will be returned for the entire domain rather than the specific page")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location. optional field. if you use this field, you don’t need to specify location_code. you can receive the list of available locations with their location_name by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available locations. example:. United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="location code. optional field. if you use this field, you don’t need to specify location_name. you can receive the list of available locations with their location_code by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available locations. example:. 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of the language. optional field. if you use this field, you don’t need to specify language_code. you can receive the list of available languages with their language_name by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="language code. optional field. if you use this field, you don’t need to specify language_name. you can receive the list of available languages with their language_code by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. ignore this field to get the results for all available languages. example:. en")
    ignore_synonyms: Optional[StrictBool] = Field(default=None, description="ignore highly similar keywords. optional field. if set to true only core keywords will be returned, all highly similar keywords will be excluded;. default value: false")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="display results by item type. optional field. indicates the type of search results included in the response. Note: if the item_types array contains item types that are different from organic, the results will be ordered by the first item type in the array; you will not be able to sort and filter results by the types of search results not included in the response;. possible values:. ['organic', 'paid', 'featured_snippet', 'local_pack', 'ai_overview_reference']. default value:. ['organic', 'paid']")
    include_clickstream_data: Optional[StrictBool] = Field(default=None, description="include or exclude data from clickstream-based metrics in the result. optional field. if the parameter is set to true, you will receive clickstream_keyword_info, clickstream_etv, clickstream_gender_distribution, clickstream_age_distribution, keyword_info_normalized_with_clickstream, and keyword_info_normalized_with_bing fields in the response. default value: false. with this parameter enabled, you will be charged double the price for the request. learn more about how clickstream-based metrics are calculated in this help center article")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned keywords. optional field. default value: 100. maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned keywords. optional field. default value: 0. if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords")
    load_rank_absolute: Optional[StrictBool] = Field(default=None, description="return rankings distribution by rank_absolute. optional field. default value: false. if set to true, we will return the field metrics_absolute containing rankings distribution by the rank_absolute parameter that indicates the result’s position among all SERP elements")
    historical_serp_mode: Optional[StrictStr] = Field(default=None, description="data collection mode. optional field. you can use this field to filter the results;. possible types of filtering:. live — return keywords for which the specified target currently has ranking results in SERP;. lost — return keywords for which the specified target had previously had ranking results in SERP, but didn’t have them during the last check;. all — return both types of keywords.. default value: live")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, not_regex, <, <=, >, >=, =, <>, in, not_in, match, not_match, ilike, not_ilike, like, not_like. you can use the % operator with like and not_like, as well as ilike and not_ilike to match any string of zero or more characters. example:. ['ranked_serp_element.serp_item.rank_group','<=',10]. [['ranked_serp_element.serp_item.rank_group','<=',10],. 'and',. ['ranked_serp_element.serp_item.type','<>','paid']]. [['keyword_data.keyword_info.search_volume','<>',0],. 'and',. [['ranked_serp_element.serp_item.type','<>','paid'],'or',['ranked_serp_element.serp_item.is_malicious','=',false]]]. if you want to get the keywords a particular webpage ranks for, you can use a target field or filter by the ranked_serp_element.serp_item.relative_url parameter. example:. ['ranked_serp_element.serp_item.relative_url', '=', '/apis/rank-tracker-api']. for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. you can use the same values as in the filters array to sort the results. possible sorting types:. asc – results will be sorted in the ascending order. desc – results will be sorted in the descending order. you should use a comma to set up a sorting type. example:. ['keyword_data.keyword_info.competition,desc']. default rule:. ['ranked_serp_element.serp_item.rank_group,asc']. note that you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['keyword_data.keyword_info.search_volume,desc','keyword_data.keyword_info.cpc,desc']")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "target", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "ignore_synonyms", 
        "item_types", 
        "include_clickstream_data", 
        "limit", 
        "offset", 
        "load_rank_absolute", 
        "historical_serp_mode", 
        "filters", 
        "order_by", 
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
        _dict['ignore_synonyms'] = self.ignore_synonyms
        _dict['item_types'] = self.item_types
        _dict['include_clickstream_data'] = self.include_clickstream_data
        _dict['limit'] = self.limit
        _dict['offset'] = self.offset
        _dict['load_rank_absolute'] = self.load_rank_absolute
        _dict['historical_serp_mode'] = self.historical_serp_mode
        _dict['filters'] = self.filters
        _dict['order_by'] = self.order_by
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
            "ignore_synonyms": obj.get("ignore_synonyms"),
            "item_types": obj.get("item_types"),
            "include_clickstream_data": obj.get("include_clickstream_data"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "load_rank_absolute": obj.get("load_rank_absolute"),
            "historical_serp_mode": obj.get("historical_serp_mode"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj