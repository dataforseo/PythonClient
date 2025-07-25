from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsBingCompetitorsDomainLiveRequestInfo(BaseModel):
    """
    DataforseoLabsBingCompetitorsDomainLiveRequestInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="domain. required field. the domain name of the target website. the domain should be specified without https:// and www.")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location. required field if you don’t specify location_code. Note: it is required to specify either location_name or location_code. you can receive the list of available locations with their location_name by making a separate request to. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;. Note: this endpoint currently supports the US location only;. example:. United States")
    location_code: Optional[StrictInt] = Field(default=None, description="location code. required field if you don’t specify location_name. Note: it is required to specify either location_name or location_code. you can receive the list of available locations with their location_code by making a separate request to. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages;. Note: this endpoint currently supports the US location only;. example:. 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of the language. required field if you don’t specify language_code. Note: it is required to specify either language_name or language_code. you can receive the list of available languages with their language_name by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. English")
    language_code: Optional[StrictStr] = Field(default=None, description="language code. required field if you don’t specify language_name. Note: it is required to specify either language_name or language_code. you can receive the list of available languages with their language_code by making a separate request to the. https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages. example:. en")
    item_types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="display results by item type. optional field. indicates the type of search results included in the response. Note: if the item_types array contains item types that are different from organic, the results will be ordered by the first item type in the array; you will not be able to sort and filter results by the types of search results not included in the response;. possible values:. ['organic', 'paid', 'featured_snippet', 'local_pack']. default value:. ['organic', 'paid', 'featured_snippet', 'local_pack']")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can add several filters at once (8 filters maximum). you should set a logical operator and, or between the conditions. the following operators are supported:. regex, not_regex, <, <=, >, >=, =, <>, in, not_in. example:. ['metrics.organic.count','>',50]. [['metrics.organic.pos_1','<>',0],'and',['metrics.organic.etv','>=','10']]. [[['metrics.organic.count','>=',50],'and',['metrics.organic.pos_1','in',[1,5]]],. 'or',. ['metrics.organic.etv','>=','100']]. for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide")
    order_by: Optional[List[Optional[StrictStr]]] = Field(default=None, description="results sorting rules. optional field. you can use the same values as in the filters array to sort the results. possible sorting types:. asc – results will be sorted in the ascending order. desc – results will be sorted in the descending order. you should use a comma to specify a sorting type. example:. ['metrics.paid.etv,asc']. Note: you can set no more than three sorting rules in a single request. you should use a comma to separate several sorting rules. example:. ['metrics.organic.etv,desc','metrics.paid.count,asc']. default rule:. ['metrics.organic.count,desc']. Note: if the item_types array contains item types that are different from organic, the results will be ordered by the first item type in the array")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned domains. optional field. default value: 100. maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned domains. optional field. default value: 0. if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords")
    max_rank_group: Optional[StrictInt] = Field(default=None, description="maximum rank up to which competitors will be considered. optional field. default value: 100. if you specify 10 here, we will extract competitors from the top 10 Bing search results only")
    exclude_top_domains: Optional[StrictBool] = Field(default=None, description="indicates whether to exclude world’s largest websites. optional field. default value: false. set to true if you want to get highly-relevant competitors excluding the websites listed below:. wikipedia.org. pinterest.com. amazon.com. google.com. facebook.com. wordpress.com. medium.com. quora.com. reddit.com. youtube.com. ebay.com. uol.com.br. instagram.com. olx.com. twitter.com. linkedin.com. slideshare.net")
    intersecting_domains: Optional[List[Optional[StrictStr]]] = Field(default=None, description="additional domains for improving results accuracy. optional field. to improve the accuracy of the result, you can specify domains that are known to intersect with the target in SERPs;. if you use this array, metrics in the result will be based on SERPs where both target website and intersecting_domains appear;. Note: you can specify up to 20 domains in this array")
    ignore_synonyms: Optional[StrictBool] = Field(default=None, description="ignore highly similar keywords. optional field. if set to true, only core keywords will be returned, all highly similar keywords will be excluded;. default value: false")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "target", 
        "location_name", 
        "location_code", 
        "language_name", 
        "language_code", 
        "item_types", 
        "filters", 
        "order_by", 
        "limit", 
        "offset", 
        "max_rank_group", 
        "exclude_top_domains", 
        "intersecting_domains", 
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

        _dict['target'] = self.target
        _dict['location_name'] = self.location_name
        _dict['location_code'] = self.location_code
        _dict['language_name'] = self.language_name
        _dict['language_code'] = self.language_code
        _dict['item_types'] = self.item_types
        _dict['filters'] = self.filters
        _dict['order_by'] = self.order_by
        _dict['limit'] = self.limit
        _dict['offset'] = self.offset
        _dict['max_rank_group'] = self.max_rank_group
        _dict['exclude_top_domains'] = self.exclude_top_domains
        _dict['intersecting_domains'] = self.intersecting_domains
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
            "target": obj.get("target"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "item_types": obj.get("item_types"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "max_rank_group": obj.get("max_rank_group"),
            "exclude_top_domains": obj.get("exclude_top_domains"),
            "intersecting_domains": obj.get("intersecting_domains"),
            "ignore_synonyms": obj.get("ignore_synonyms"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj