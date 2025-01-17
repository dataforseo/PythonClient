# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class BacklinksDomainIntersectionLiveRequestInfo(BaseModel):
    """
    BacklinksDomainIntersectionLiveRequestInfo
    """ # noqa: E501
    targets: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="domains, subdomains or webpages to get links for required field you can set up to 20 domains, subdomains or webpages a domain or a subdomain should be specified without https:// and www. a page should be specified with absolute URL (including http:// or https://) example: \"targets\": { \"1\": \"http://planet.postgresql.org/\", \"2\": \"http://gborg.postgresql.org/\" }")
    exclude_targets: Optional[List[StrictStr]] = Field(default=None, description="domains, subdomains or webpages you want to exclude optional field you can specify up to 10 domains, subdomains or webpages if you use this array, results will contain the referring domains that link to targets but don’t link to exclude_targets example: \"exclude_targets\": [ \"bbc.com\", \"https://www.apple.com/iphone/*\", \"https://dataforseo.com/apis/*\"]")
    filters: Optional[List[Optional[Dict[str, Any]]]] = Field(default=None, description="array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, =, <>, in, not_in, like, not_like, ilike, not_ilike you can use the % operator with like and not_like to match any string of zero or more characters example: [\"1.internal_links_count\",\">\",\"1\"] [[\"2.referring_pages\",\">\",\"2\"], \"and\", [\"1.backlinks\",\">\",\"10\"]] [[\"1.first_seen\",\">\",\"2017-10-23 11:31:45 +00:00\"], \"and\", [[\"2.target\",\"like\",\"%dataforseo.com%\"],\"or\",[\"1.referring_domains\",\">\",\"10\"]]] The full list of possible filters is available here.")
    order_by: Optional[List[StrictStr]] = Field(default=None, description="results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to set up a sorting type example: [\"backlinks,desc\"] note that you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\"backlinks,desc\",\"rank,asc\"]")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the array of returned results optional field default value: 0 if you specify the 10 value, the first ten backlinks in the results array will be omitted and the data will be provided for the successive backlinks")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned results optional field default value: 100 maximum value: 1000")
    internal_list_limit: Optional[StrictInt] = Field(default=None, description="maximum number of elements within internal arrays optional field you can use this field to limit the number of elements within the following arrays: referring_links_tld referring_links_types referring_links_attributes referring_links_platform_types referring_links_semantic_locations default value: 10 maximum value: 1000")
    backlinks_status_type: Optional[StrictStr] = Field(default=None, description="set what backlinks to return and count optional field you can use this field to choose what backlinks will be returned and used for aggregated metrics for your targets; possible values: all – all backlinks will be returned and counted; live – backlinks found during the last check will be returned and counted; lost – lost backlinks will be returned and counted; default value: live")
    backlinks_filters: Optional[List[Optional[Dict[str, Any]]]] = Field(default=None, description="filter the backlinks of your target optional field you can use this field to filter the initial backlinks that will be included in the dataset for aggregated metrics for your target you can filter the backlinks by all fields available in the response of this endpoint using this parameter, you can include only dofollow backlinks in the response and create a flexible backlinks dataset to calculate the metrics for example: \"backlinks_filters\": [[\"dofollow\", \"=\", true]]")
    include_subdomains: Optional[StrictBool] = Field(default=None, description="indicates if the subdomains of the target will be included in the search optional field if set to false, the subdomains will be ignored default value: true")
    include_indirect_links: Optional[StrictBool] = Field(default=None, description="indicates if indirect links to the targets will be included in the results optional field if set to true, the results will include data on indirect links pointing to a page that either redirects to a target, or points to a canonical page if set to false, indirect links will be ignored default value: true")
    exclude_internal_backlinks: Optional[StrictBool] = Field(default=None, description="indicates whether the backlinks from subdomains of the target are excluded optional field if set to false, the backlinks from subdomains of the target will be omitted and you won’t receive the same domain in the response; default value: true")
    intersection_mode: Optional[StrictStr] = Field(default=None, description="indicates whether to intersect backlinks optional field use this field to intersect or merge results for the specified domains possible values: all, partial all – results are based on all backlinks; partial – results are based on the intersecting backlinks only; default value: all")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = ["targets", "exclude_targets", "filters", "order_by", "offset", "limit", "internal_list_limit", "backlinks_status_type", "backlinks_filters", "include_subdomains", "include_indirect_links", "exclude_internal_backlinks", "intersection_mode", "tag"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of BacklinksDomainIntersectionLiveRequestInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if targets (nullable) is None
        # and model_fields_set contains the field
        if self.targets is None and "targets" in self.model_fields_set:
            _dict['targets'] = None

        # set to None if exclude_targets (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_targets is None and "exclude_targets" in self.model_fields_set:
            _dict['exclude_targets'] = None

        # set to None if filters (nullable) is None
        # and model_fields_set contains the field
        if self.filters is None and "filters" in self.model_fields_set:
            _dict['filters'] = None

        # set to None if order_by (nullable) is None
        # and model_fields_set contains the field
        if self.order_by is None and "order_by" in self.model_fields_set:
            _dict['order_by'] = None

        # set to None if offset (nullable) is None
        # and model_fields_set contains the field
        if self.offset is None and "offset" in self.model_fields_set:
            _dict['offset'] = None

        # set to None if limit (nullable) is None
        # and model_fields_set contains the field
        if self.limit is None and "limit" in self.model_fields_set:
            _dict['limit'] = None

        # set to None if internal_list_limit (nullable) is None
        # and model_fields_set contains the field
        if self.internal_list_limit is None and "internal_list_limit" in self.model_fields_set:
            _dict['internal_list_limit'] = None

        # set to None if backlinks_status_type (nullable) is None
        # and model_fields_set contains the field
        if self.backlinks_status_type is None and "backlinks_status_type" in self.model_fields_set:
            _dict['backlinks_status_type'] = None

        # set to None if backlinks_filters (nullable) is None
        # and model_fields_set contains the field
        if self.backlinks_filters is None and "backlinks_filters" in self.model_fields_set:
            _dict['backlinks_filters'] = None

        # set to None if include_subdomains (nullable) is None
        # and model_fields_set contains the field
        if self.include_subdomains is None and "include_subdomains" in self.model_fields_set:
            _dict['include_subdomains'] = None

        # set to None if include_indirect_links (nullable) is None
        # and model_fields_set contains the field
        if self.include_indirect_links is None and "include_indirect_links" in self.model_fields_set:
            _dict['include_indirect_links'] = None

        # set to None if exclude_internal_backlinks (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_internal_backlinks is None and "exclude_internal_backlinks" in self.model_fields_set:
            _dict['exclude_internal_backlinks'] = None

        # set to None if intersection_mode (nullable) is None
        # and model_fields_set contains the field
        if self.intersection_mode is None and "intersection_mode" in self.model_fields_set:
            _dict['intersection_mode'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BacklinksDomainIntersectionLiveRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "targets": obj.get("targets"),
            "exclude_targets": obj.get("exclude_targets"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "offset": obj.get("offset"),
            "limit": obj.get("limit"),
            "internal_list_limit": obj.get("internal_list_limit"),
            "backlinks_status_type": obj.get("backlinks_status_type"),
            "backlinks_filters": obj.get("backlinks_filters"),
            "include_subdomains": obj.get("include_subdomains"),
            "include_indirect_links": obj.get("include_indirect_links"),
            "exclude_internal_backlinks": obj.get("exclude_internal_backlinks"),
            "intersection_mode": obj.get("intersection_mode"),
            "tag": obj.get("tag")
        })
        return _obj


