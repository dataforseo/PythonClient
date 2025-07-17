from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsGooglePageIntersectionLiveRequestInfo(BaseModel):
    """
    DataforseoLabsGooglePageIntersectionLiveRequestInfo
    """ # noqa: E501
    pages: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="target URLs of pages. required field. you can set up to 20 pages in this object. the pages should be specified with absolute URLs (including http:// or https://). example:. 'pages': {. '1':'https://www.apple.com/mac/*',. '2':'https://dataforseo.com/*',. '3':'https://support.microsoft.com/'. }if you specify a single page here, we will return results only for this page;. you can also use a wildcard (‘*’) character to specify the search pattern. example:. 'example.com'. search for the exact URL. 'example.com/eng/*'. search for the example.com page and all its related URLs which start with ‘/eng/’, such as “example.com/eng/index.html” and “example.com/eng/help/”, etc.. note: a wilcard should be placed after the slash (‘/’) character in the end of the URL, it is not possible to place it after the domain in the following way:. https://dataforseo.com*. use https://dataforseo.com/* instead. Note: this endpoint will not provide results if the number of intersecting keywords exceeds 10 million")
    exclude_pages: Optional[List[Optional[StrictStr]]] = Field(default=None, description="URLs of pages you want to exclude. optional field. you can set up to 10 pages in this array. if you use this array, results will contain the keywords for which URLs from the pages object rank, but URLs from exclude_pages array do not;. note that if you specify this field, the results will be based on the keywords any URL from pages ranks for regardless of intersections between them. However, you can set intersection_mode to intersect and results will contain the keywords all URLs from pages rank for in the same SERP and URLs from exclude_pages do not.. use a wildcard (‘*’) character to specify the search pattern. example:. 'exclude_pages': [. 'https://www.apple.com/iphone/*',. 'https://dataforseo.com/apis/*',. 'https://www.microsoft.com/en-us/industry/services/'. ]")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location. required field if you don’t specify location_code. Note: it is required to specify either location_name or location_code. you can receive the list of available locations with their location_name by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="location code. required field if you don’t specify location_name. Note: it is required to specify either location_name or location_code. you can receive the list of available locations with their location_code by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of the language. required field if you don’t specify language_code. Note: it is required to specify either language_name or language_code. you can receive the list of available languages with their language_name by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="language code. required field if you don’t specify language_name. Note: it is required to specify either language_name or language_code. you can receive the list of available languages with their language_code by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. en")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="search results type. indicates type of search results included in the response. optional field. possible values:. ['organic', 'paid', 'featured_snippet', 'local_pack']. default value:. ['organic', 'paid']")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned keywords. optional field. default value: 100. maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the items array of returned keywords. optional field. default value: 0. if you specify 10 here, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords")
    include_subdomains: Optional[StrictBool] = Field(default=None, description="indicates if the subdomains will be included in the search. optional field. if set to false, the subdomains will be ignored. default value: true")
    intersection_mode: Optional[StrictStr] = Field(default=None, description="indicates whether to intersect keywords. optional field. use this field to intersect or merge results for the specified URLs. possible values: union, intersect. union – results are based on all keywords any URL from pages rank for;. intersect – results are based on the keywords all URLs from pages rank for in the same SERP:. by default, results are based on the intersect mode if you specify only pages array. If you specify exclude_pages as well, results are based on the union mode")
    include_serp_info: Optional[StrictBool] = Field(default=None, description="include data from SERP for each keyword. optional field. if set to true, we will return a serp_info array containing SERP data (number of search results, relevant URL, and SERP features) for every keyword in the response. default value: false")
    include_clickstream_data: Optional[StrictBool] = Field(default=None, description="include or exclude data from clickstream-based metrics in the result. optional field. if the parameter is set to true, you will receive clickstream_keyword_info, clickstream_etv, keyword_info_normalized_with_clickstream, and keyword_info_normalized_with_bing fields in the response. default value: false. with this parameter enabled, you will be charged double the price for the request. learn more about how clickstream-based metrics are calculated in this help center article")
    ignore_synonyms: Optional[StrictBool] = Field(default=None, description="ignore highly similar keywords. optional field. if set to true only core keywords will be returned, all highly similar keywords will be excluded;. default value: false")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, not_regex, <, <=, >, >=, =, <>, in, not_in, ilike, not_ilike, like, not_like, match, not_match. you can use the % operator with like and not_like, as well as ilike and not_ilike to match any string of zero or more characters. note that if you want to filter by any field in the intersection_result array you need to specify the number of corresponding page. for instance, if you want to filter results by the ranking of the first specified URL, you should set the following filter:. [intersection_result.1.rank_absolute,'=',1]. if you want to filter results and receive only organic listings for the third specified URL, you should set the following filter:. [intersection_result.3.type,'=','organic'] , etc.example:. ['keyword_data.keyword_info.search_volume','in',[100,1000]]. [['intersection_result.1.etv','>',0],'and',['intersection_result.1.description','like','%goat%']][['keyword_data.keyword_info.search_volume','>',100],. 'and',. [['intersection_result.2.description','like','%goat%'],. 'or',. ['intersection_result.2.type','=','organic']]]. for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. you can use the same values as in the filters array to sort the results. possible sorting types:. asc – results will be sorted in the ascending order. desc – results will be sorted in the descending order. you should use a comma to set up a sorting parameter. example:. ['keyword_data.keyword_info.competition,desc']. default rule:. ['keyword_data.keyword_info.search_volume,desc']. note that you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['intersection_result.1.rank_group,asc','intersection_result.2.rank_absolute,asc']")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "pages", 
        "exclude_pages", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "item_types", 
        "limit", 
        "offset", 
        "include_subdomains", 
        "intersection_mode", 
        "include_serp_info", 
        "include_clickstream_data", 
        "ignore_synonyms", 
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

        _dict['pages'] = self.pages
        _dict['exclude_pages'] = self.exclude_pages
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['item_types'] = self.item_types
        _dict['limit'] = self.limit
        _dict['offset'] = self.offset
        _dict['include_subdomains'] = self.include_subdomains
        _dict['intersection_mode'] = self.intersection_mode
        _dict['include_serp_info'] = self.include_serp_info
        _dict['include_clickstream_data'] = self.include_clickstream_data
        _dict['ignore_synonyms'] = self.ignore_synonyms
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
            "pages": obj.get("pages"),
            "exclude_pages": obj.get("exclude_pages"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "item_types": obj.get("item_types"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "include_subdomains": obj.get("include_subdomains"),
            "intersection_mode": obj.get("intersection_mode"),
            "include_serp_info": obj.get("include_serp_info"),
            "include_clickstream_data": obj.get("include_clickstream_data"),
            "ignore_synonyms": obj.get("ignore_synonyms"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj