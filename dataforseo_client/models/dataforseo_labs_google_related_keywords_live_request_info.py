from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsGoogleRelatedKeywordsLiveRequestInfo(BaseModel):
    """
    DataforseoLabsGoogleRelatedKeywordsLiveRequestInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword. required field. UTF-8 encoding. the keywords will be converted to lowercase format. learn more about rules and limitations of keyword and keywords fields in DataForSEO APIs in this Help Center article")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location. required field if you don’t specify location_code. Note: it is required to specify either location_name or location_code. you can receive the list of available locations with their location_name by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="location code. required field if you don’t specify location_name. Note: it is required to specify either location_name or location_code. you can receive the list of available locations with their location_code by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of the language. required field if you don’t specify language_code. Note: it is required to specify either language_name or language_code. you can receive the list of available locations with their language_name by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="language code. required field if you don’t specify language_name. Note: it is required to specify either language_name or language_code. you can receive the list of available locations with their language_code by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. en")
    depth: Optional[StrictInt] = Field(default=None, description="keyword search depth. optional field. default value: 1. number of the returned results depends on the value you set in this field. you can specify a level from 0 to 4. estimated number of keywords for each level (maximum):. 0 – the keyword set in the keyword field. 1 – 8 keywords. 2 – 72 keywords. 3 – 584 keywords. 4 – 4680 keywords")
    include_seed_keyword: Optional[StrictBool] = Field(default=None, description="include data for the seed keyword. optional field. if set to true, data for the seed keyword specified in the keyword field will be provided in the seed_keyword_data array of the response. default value: false")
    include_serp_info: Optional[StrictBool] = Field(default=None, description="include data from SERP for each keyword. optional field. if set to true, we will return a serp_info array containing SERP data (number of search results, relevant URL, and SERP features) for every keyword in the response. default value: false")
    include_clickstream_data: Optional[StrictBool] = Field(default=None, description="include or exclude data from clickstream-based metrics in the result. optional field. if the parameter is set to true, you will receive clickstream_keyword_info, keyword_info_normalized_with_clickstream, and keyword_info_normalized_with_bing fields in the response. default value: false. with this parameter enabled, you will be charged double the price for the request. learn more about how clickstream-based metrics are calculated in this help center article")
    ignore_synonyms: Optional[StrictBool] = Field(default=None, description="ignore highly similar keywords. optional field. if set to true only core keywords will be returned, all highly similar keywords will be excluded;. default value: false")
    replace_with_core_keyword: Optional[StrictBool] = Field(default=None, description="return data for core keyword. optional field. if true, serp_info and related_keywords will be returned for the main keyword in the group that the specified keyword belongs to;. if false, serp_info and related_keywords will be returned for the specified keyword (if available);. refer to this help center article for more details;. default value: false")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, not_regex, <, <=, >, >=, =, <>, in, not_in, match, not_match, ilike, not_ilike, like,not_like. you can use the % operator with like and not_like, as well as ilike and not_ilike to match any string of zero or more characters. example:. ['keyword_data.keyword_info.search_volume','>',0]. [['keyword_info.search_volume','in',[0,1000]],. 'and',. ['keyword_data.keyword_info.competition_level','=','LOW']]. [['keyword_data.keyword_info.search_volume','>',100],. 'and',. [['keyword_data.keyword_info.cpc','<',0.5],. 'or',. ['keyword_info.high_top_of_page_bid','<=',0.5]]]. for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. you can use the same values as in the filters array to sort the results. possible sorting types:. asc – results will be sorted in the ascending order. desc – results will be sorted in the descending order. you should use a comma to set up a sorting type. example:. ['keyword_data.keyword_info.competition,desc']. default rule:. ['keyword_data.keyword_info.search_volume,desc']. note that you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['keyword_data.keyword_info.search_volume,desc','keyword_data.keyword_info.cpc,desc']")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned keywords. optional field. default value: 100. maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned keywords. optional field. default value: 0. if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "depth", 
        "include_seed_keyword", 
        "include_serp_info", 
        "include_clickstream_data", 
        "ignore_synonyms", 
        "replace_with_core_keyword", 
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

        _dict['keyword'] = self.keyword
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['depth'] = self.depth
        _dict['include_seed_keyword'] = self.include_seed_keyword
        _dict['include_serp_info'] = self.include_serp_info
        _dict['include_clickstream_data'] = self.include_clickstream_data
        _dict['ignore_synonyms'] = self.ignore_synonyms
        _dict['replace_with_core_keyword'] = self.replace_with_core_keyword
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
            "keyword": obj.get("keyword"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "depth": obj.get("depth"),
            "include_seed_keyword": obj.get("include_seed_keyword"),
            "include_serp_info": obj.get("include_serp_info"),
            "include_clickstream_data": obj.get("include_clickstream_data"),
            "ignore_synonyms": obj.get("ignore_synonyms"),
            "replace_with_core_keyword": obj.get("replace_with_core_keyword"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj