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

from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.about_this_result_element import AboutThisResultElement
from dataforseo_client.models.backlinks_info import BacklinksInfo
from dataforseo_client.models.base_dataforseo_labs_serp_element_item import BaseDataforseoLabsSerpElementItem
from dataforseo_client.models.rank_changes import RankChanges
from dataforseo_client.models.rank_info import RankInfo
from dataforseo_client.models.rating_info import RatingInfo
from typing import Optional, Set
from typing_extensions import Self

class OrganicDataforseoLabsSerpElementItem(BaseDataforseoLabsSerpElementItem):
    """
    OrganicDataforseoLabsSerpElementItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP can take the following values: left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    domain: Optional[StrictStr] = Field(default=None, description="subdomain in SERP")
    title: Optional[StrictStr] = Field(default=None, description="title of the result in SERP")
    url: Optional[StrictStr] = Field(default=None, description="relevant URL in SERP")
    breadcrumb: Optional[StrictStr] = Field(default=None, description="breadcrumb in SERP")
    website_name: Optional[StrictStr] = Field(default=None, description="relevant website name in SERP")
    is_image: Optional[StrictBool] = Field(default=None, description="indicates whether the element contains an image")
    is_video: Optional[StrictBool] = Field(default=None, description="indicates whether the element contains a video")
    is_featured_snippet: Optional[StrictBool] = Field(default=None, description="indicates whether the element is a featured_snippet")
    is_malicious: Optional[StrictBool] = Field(default=None, description="indicates whether the element is marked as malicious")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    pre_snippet: Optional[StrictStr] = Field(default=None, description="includes additional information appended before the result description in SERP")
    extended_snippet: Optional[StrictStr] = Field(default=None, description="includes additional information appended after the result description in SERP")
    amp_version: Optional[StrictBool] = Field(default=None, description="Accelerated Mobile Pages indicates whether an item has the Accelerated Mobile Page (AMP) version")
    rating: Optional[RatingInfo] = None
    highlighted: Optional[List[Optional[StrictStr]]] = Field(default=None, description="words highlighted in bold within the results description")
    links: Optional[Dict[str, Any]] = Field(default=None, description="sitelinks the links shown below some of Google’s search results if there are none, equals null")
    about_this_result: Optional[Dict[str, AboutThisResultElement]] = Field(default=None, description="contains information from the ‘About this result’ panel ‘About this result’ panel provides additional context about why Google returned this result for the given query; this feature appears after clicking on the three dots next to most results")
    main_domain: Optional[StrictStr] = Field(default=None, description="primary domain name in SERP")
    relative_url: Optional[StrictStr] = Field(default=None, description="URL in SERP that does not specify the HTTPs protocol and domain name")
    etv: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="estimated traffic volume estimated paid monthly traffic to the domain calculated as the product of CTR (click-through-rate) and search volume values of all keywords in the category that the domain ranks for learn more about how the metric is calculated in this help center article")
    impressions_etv: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="estimated traffic volume based on impressions estimated paid monthly traffic to the domain calculated as the product of CTR (click-through-rate) and impressions values of all keywords in the category that the domain ranks for learn more about how the metric is calculated in this help center article")
    estimated_paid_traffic_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="estimated cost of monthly search traffic represents the estimated cost of paid monthly traffic (USD) based on etv and cpc values of all keywords in the category that the domain ranks for learn more about how the metric is calculated in this help center article")
    clickstream_etv: Optional[StrictInt] = Field(default=None, description="estimated traffic volume based on clickstream data calculated as the product of click-through-rate and clickstream search volume values of all keywords the domain ranks for to retrieve results for this field, the parameter include_clickstream_data must be set to true learn more about how the metric is calculated in this help center article")
    rank_changes: Optional[RankChanges] = None
    backlinks_info: Optional[BacklinksInfo] = None
    rank_info: Optional[RankInfo] = None
    __properties: ClassVar[List[str]] = ["type", "se_type", "rank_group", "rank_absolute", "position", "xpath", "domain", "title", "url", "breadcrumb", "website_name", "is_image", "is_video", "is_featured_snippet", "is_malicious", "description", "pre_snippet", "extended_snippet", "amp_version", "rating", "highlighted", "links", "about_this_result", "main_domain", "relative_url", "etv", "impressions_etv", "estimated_paid_traffic_cost", "clickstream_etv", "rank_changes", "backlinks_info", "rank_info"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OrganicDataforseoLabsSerpElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rating
        if self.rating:
            _dict['rating'] = self.rating.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in about_this_result (dict)
        _field_dict = {}
        if self.about_this_result:
            for _key in self.about_this_result:
                if self.about_this_result[_key]:
                    _field_dict[_key] = self.about_this_result[_key].to_dict()
            _dict['about_this_result'] = _field_dict
        # override the default output from pydantic by calling `to_dict()` of rank_changes
        if self.rank_changes:
            _dict['rank_changes'] = self.rank_changes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of backlinks_info
        if self.backlinks_info:
            _dict['backlinks_info'] = self.backlinks_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rank_info
        if self.rank_info:
            _dict['rank_info'] = self.rank_info.to_dict()
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if se_type (nullable) is None
        # and model_fields_set contains the field
        if self.se_type is None and "se_type" in self.model_fields_set:
            _dict['se_type'] = None

        # set to None if rank_group (nullable) is None
        # and model_fields_set contains the field
        if self.rank_group is None and "rank_group" in self.model_fields_set:
            _dict['rank_group'] = None

        # set to None if rank_absolute (nullable) is None
        # and model_fields_set contains the field
        if self.rank_absolute is None and "rank_absolute" in self.model_fields_set:
            _dict['rank_absolute'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if xpath (nullable) is None
        # and model_fields_set contains the field
        if self.xpath is None and "xpath" in self.model_fields_set:
            _dict['xpath'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if breadcrumb (nullable) is None
        # and model_fields_set contains the field
        if self.breadcrumb is None and "breadcrumb" in self.model_fields_set:
            _dict['breadcrumb'] = None

        # set to None if website_name (nullable) is None
        # and model_fields_set contains the field
        if self.website_name is None and "website_name" in self.model_fields_set:
            _dict['website_name'] = None

        # set to None if is_image (nullable) is None
        # and model_fields_set contains the field
        if self.is_image is None and "is_image" in self.model_fields_set:
            _dict['is_image'] = None

        # set to None if is_video (nullable) is None
        # and model_fields_set contains the field
        if self.is_video is None and "is_video" in self.model_fields_set:
            _dict['is_video'] = None

        # set to None if is_featured_snippet (nullable) is None
        # and model_fields_set contains the field
        if self.is_featured_snippet is None and "is_featured_snippet" in self.model_fields_set:
            _dict['is_featured_snippet'] = None

        # set to None if is_malicious (nullable) is None
        # and model_fields_set contains the field
        if self.is_malicious is None and "is_malicious" in self.model_fields_set:
            _dict['is_malicious'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if pre_snippet (nullable) is None
        # and model_fields_set contains the field
        if self.pre_snippet is None and "pre_snippet" in self.model_fields_set:
            _dict['pre_snippet'] = None

        # set to None if extended_snippet (nullable) is None
        # and model_fields_set contains the field
        if self.extended_snippet is None and "extended_snippet" in self.model_fields_set:
            _dict['extended_snippet'] = None

        # set to None if amp_version (nullable) is None
        # and model_fields_set contains the field
        if self.amp_version is None and "amp_version" in self.model_fields_set:
            _dict['amp_version'] = None

        # set to None if highlighted (nullable) is None
        # and model_fields_set contains the field
        if self.highlighted is None and "highlighted" in self.model_fields_set:
            _dict['highlighted'] = None

        # set to None if links (nullable) is None
        # and model_fields_set contains the field
        if self.links is None and "links" in self.model_fields_set:
            _dict['links'] = None

        # set to None if about_this_result (nullable) is None
        # and model_fields_set contains the field
        if self.about_this_result is None and "about_this_result" in self.model_fields_set:
            _dict['about_this_result'] = None

        # set to None if main_domain (nullable) is None
        # and model_fields_set contains the field
        if self.main_domain is None and "main_domain" in self.model_fields_set:
            _dict['main_domain'] = None

        # set to None if relative_url (nullable) is None
        # and model_fields_set contains the field
        if self.relative_url is None and "relative_url" in self.model_fields_set:
            _dict['relative_url'] = None

        # set to None if etv (nullable) is None
        # and model_fields_set contains the field
        if self.etv is None and "etv" in self.model_fields_set:
            _dict['etv'] = None

        # set to None if impressions_etv (nullable) is None
        # and model_fields_set contains the field
        if self.impressions_etv is None and "impressions_etv" in self.model_fields_set:
            _dict['impressions_etv'] = None

        # set to None if estimated_paid_traffic_cost (nullable) is None
        # and model_fields_set contains the field
        if self.estimated_paid_traffic_cost is None and "estimated_paid_traffic_cost" in self.model_fields_set:
            _dict['estimated_paid_traffic_cost'] = None

        # set to None if clickstream_etv (nullable) is None
        # and model_fields_set contains the field
        if self.clickstream_etv is None and "clickstream_etv" in self.model_fields_set:
            _dict['clickstream_etv'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrganicDataforseoLabsSerpElementItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "se_type": obj.get("se_type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "domain": obj.get("domain"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "breadcrumb": obj.get("breadcrumb"),
            "website_name": obj.get("website_name"),
            "is_image": obj.get("is_image"),
            "is_video": obj.get("is_video"),
            "is_featured_snippet": obj.get("is_featured_snippet"),
            "is_malicious": obj.get("is_malicious"),
            "description": obj.get("description"),
            "pre_snippet": obj.get("pre_snippet"),
            "extended_snippet": obj.get("extended_snippet"),
            "amp_version": obj.get("amp_version"),
            "rating": RatingInfo.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "highlighted": obj.get("highlighted"),
            "links": obj.get("links"),
            "about_this_result": dict(
                (_k, AboutThisResultElement.from_dict(_v))
                for _k, _v in obj["about_this_result"].items()
            )
            if obj.get("about_this_result") is not None
            else None,
            "main_domain": obj.get("main_domain"),
            "relative_url": obj.get("relative_url"),
            "etv": obj.get("etv"),
            "impressions_etv": obj.get("impressions_etv"),
            "estimated_paid_traffic_cost": obj.get("estimated_paid_traffic_cost"),
            "clickstream_etv": obj.get("clickstream_etv"),
            "rank_changes": RankChanges.from_dict(obj["rank_changes"]) if obj.get("rank_changes") is not None else None,
            "backlinks_info": BacklinksInfo.from_dict(obj["backlinks_info"]) if obj.get("backlinks_info") is not None else None,
            "rank_info": RankInfo.from_dict(obj["rank_info"]) if obj.get("rank_info") is not None else None
        })
        return _obj


