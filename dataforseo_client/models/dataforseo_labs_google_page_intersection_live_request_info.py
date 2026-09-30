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
    pages: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description=r"target URLs of pagesrequired fieldyou can set up to 20 pages in this objectthe pages should be specified with absolute URLs (including http:// or https://)example:'pages': {'1':'https://www.apple.com/mac/*','2':'https://dataforseo.com/*','3':'https://support.microsoft.com/'}if you specify a single page here, we will return results only for this page;you can also use a wildcard ('') character to specify the search patternexample:'example.com'search for the exact URL'example.com/eng/'search for the example.com page and all its related URLs which start with '/eng/', such as 'example.com/eng/index.html' and 'example.com/eng/help/', etc.note: a wilcard should be placed after the slash ('/') character in the end of the URL, it is not possible to place it after the domain in the following way:https://dataforseo.comuse https://dataforseo.com/ insteadNote: this endpoint will not provide results if the number of intersecting keywords exceeds 10 million")
    exclude_pages: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"URLs of pages you want to excludeoptional fieldyou can set up to 10 pages in this arrayif you use this array, results will contain the keywords for which URLs from the pages object rank, but URLs from exclude_pages array do not;note that if you specify this field, the results will be based on the keywords any URL from pages ranks for regardless of intersections between them. However, you can set intersection_mode to intersect and results will contain the keywords all URLs from pages rank for in the same SERP and URLs from exclude_pages do not. use a wildcard ('*') character to specify the search patternexample:'exclude_pages':['https://www.apple.com/iphone/*','https://dataforseo.com/apis/*','https://www.microsoft.com/en-us/industry/services/']")
    location_name: Optional[StrictStr] = Field(default=None, description=r"full name of the locationrequired field if you don't specify location_codeNote: it is required to specify either location_name or location_codeyou can receive the list of available locations with their location_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languagesexample:United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description=r"location coderequired field if you don't specify location_nameNote: it is required to specify either location_name or location_codeyou can receive the list of available locations with their location_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languagesexample:2840")
    language_name: Optional[StrictStr] = Field(default=None, description=r"full name of the languagerequired field if you don't specify language_codeNote: it is required to specify either language_name or language_codeyou can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languagesexample:English")
    language_code: Optional[StrictStr] = Field(default=None, description=r"language coderequired field if you don't specify language_nameNote: it is required to specify either language_name or language_codeyou can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languagesexample:en")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"search results typeindicates type of search results included in the responseoptional fieldpossible values: ['organic', 'paid', 'featured_snippet', 'local_pack']default value: ['organic', 'paid']")
    limit: Optional[StrictInt] = Field(default=None, description=r"the maximum number of returned keywordsoptional fielddefault value: 100maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description=r"offset in the items array of returned keywordsoptional fielddefault value: 0if you specify 10 here, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords")
    include_subdomains: Optional[StrictBool] = Field(default=None, description=r"indicates if the subdomains will be included in the searchoptional fieldif set to false, the subdomains will be ignoreddefault value: true")
    intersection_mode: Optional[StrictStr] = Field(default=None, description=r"indicates whether to intersect keywordsoptional fielduse this field to intersect or merge results for the specified URLspossible values: union, intersectunion - results are based on all keywords any URL from pages rank for;intersect - results are based on the keywords all URLs from pages rank for in the same SERP:by default, results are based on the intersect mode if you specify only pages array. If you specify exclude_pages as well, results are based on the union mode")
    include_serp_info: Optional[StrictBool] = Field(default=None, description=r"include data from SERP for each keywordoptional fieldif set to true, we will return a serp_info array containing SERP data (number of search results, relevant URL, and SERP features) for every keyword in the responsedefault value: false")
    include_clickstream_data: Optional[StrictBool] = Field(default=None, description=r"include or exclude data from clickstream-based metrics in the resultoptional fieldif the parameter is set to true, you will receive clickstream_keyword_info, clickstream_etv, keyword_info_normalized_with_clickstream, and keyword_info_normalized_with_bing fields in the responsedefault value: falsewith this parameter enabled, you will be charged double the price for the requestlearn more about how clickstream-based metrics are calculated in this help center article")
    ignore_synonyms: Optional[StrictBool] = Field(default=None, description=r"ignore highly similar keywordsoptional fieldif set to true only core keywords will be returned, all highly similar keywords will be excluded;  default value: false")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description=r"array of results filtering parametersoptional fieldyou can add several filters at once (8 filters maximum)you should set a logical operator and, or between the conditionsthe following operators are supported:regex, not_regex, , >=, =, <>, in, not_in, ilike, not_ilike, like, not_like, match, not_matchyou can use the % operator with like and not_like, as well as ilike and not_ilike to match any string of zero or more charactersnote that if you want to filter by any field in the intersection_result array you need to specify the number of corresponding pagefor instance, if you want to filter results by the ranking of the first specified URL, you should set the following filter:[intersection_result.1.rank_absolute,'=',1]if you want to filter results and receive only organic listings for the third specified URL, you should set the following filter:[intersection_result.3.type,'=','organic'] , etc.example:['keyword_data.keyword_info.search_volume','in',[100,1000]][['intersection_result.1.etv','>',0],'and',['intersection_result.1.description','like','%goat%']][['keyword_data.keyword_info.search_volume','>',100],'and',[['intersection_result.2.description','like','%goat%'],'or',['intersection_result.2.type','=','organic']]]for more information about filters, please refer to Dataforseo Labs - Filters or this help center guide")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"results sorting rulesoptional fieldyou can use the same values as in the filters array to sort the resultspossible sorting types:asc - results will be sorted in the ascending orderdesc - results will be sorted in the descending orderyou should use a comma to set up a sorting parameterexample:['keyword_data.keyword_info.competition,desc']default rule:['keyword_data.keyword_info.search_volume,desc']note that you can set no more than three sorting rules in a single requestyou should use a comma to separate several sorting rulesexample:['intersection_result.1.rank_group,asc','intersection_result.2.rank_absolute,asc']")
    tag: Optional[StrictStr] = Field(default=None, description=r"user-defined task identifieroptional fieldthe character limit is 255you can use this parameter to identify the task and match it with the resultyou will find the specified tag value in the data object of the response")
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