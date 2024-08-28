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

from pydantic import Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.ad_link_element import AdLinkElement
from dataforseo_client.models.backlinks_info import BacklinksInfo
from dataforseo_client.models.base_dataforseo_labs_serp_element_item import BaseDataforseoLabsSerpElementItem
from dataforseo_client.models.rank_changes import RankChanges
from dataforseo_client.models.rank_info import RankInfo
from typing import Optional, Set
from typing_extensions import Self

class PaidDataforseoLabsSerpElementItem(BaseDataforseoLabsSerpElementItem):
    """
    PaidDataforseoLabsSerpElementItem
    """ # noqa: E501
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP can take the following values: left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    title: Optional[StrictStr] = Field(default=None, description="title of the item")
    domain: Optional[StrictStr] = Field(default=None, description="domain where a link points")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    breadcrumb: Optional[StrictStr] = Field(default=None, description="breadcrumb of the Ad element in SERP")
    url: Optional[StrictStr] = Field(default=None, description="URL link")
    highlighted: Optional[List[Optional[StrictStr]]] = Field(default=None, description="words highlighted in bold within the results description")
    extra: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="additional information about the result")
    description_rows: Optional[List[Optional[StrictStr]]] = Field(default=None, description="extended description if there is none, equals null")
    links: Optional[List[AdLinkElement]] = Field(default=None, description="link of the element")
    main_domain: Optional[StrictStr] = Field(default=None, description="primary domain name in SERP")
    relative_url: Optional[StrictStr] = Field(default=None, description="URL in SERP that does not specify the HTTPs protocol and domain name")
    etv: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="estimated traffic volume estimated organic monthly traffic to the domain calculated as the product of CTR (click-through-rate) and search volume values of the returned keyword learn more about how the metric is calculated in this help center article")
    impressions_etv: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="estimated traffic volume based on impressions estimated organic monthly traffic to the domain calculated as the product of CTR (click-through-rate) and impressions values of the returned keyword learn more about how the metric is calculated in this help center article")
    estimated_paid_traffic_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="estimated cost of converting organic search traffic into paid represents the estimated monthly cost of running ads for the returned keyword the metric is calculated as the product of organic etv and paid cpc values and indicates the cost of driving the estimated volume of monthly organic traffic through PPC advertising in Google Search learn more about how the metric is calculated in this help center article")
    rank_changes: Optional[RankChanges] = None
    clickstream_etv: Optional[StrictInt] = Field(default=None, description="estimated traffic volume based on clickstream data calculated as the product of click-through-rate and clickstream search volume values of all keywords the domain ranks for to retrieve results for this field, the parameter include_clickstream_data must be set to true learn more about how the metric is calculated in this help center article https://dataforseo.com/help-center/whats-clickstream-estimated-traffic-volume-and-how-is-it-calculated")
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    backlinks_info: Optional[BacklinksInfo] = None
    rank_info: Optional[RankInfo] = None
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "position", "xpath", "title", "domain", "description", "breadcrumb", "url", "highlighted", "extra", "description_rows", "links", "main_domain", "relative_url", "etv", "impressions_etv", "estimated_paid_traffic_cost", "rank_changes", "clickstream_etv", "se_type", "backlinks_info", "rank_info"]

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
        """Create an instance of PaidDataforseoLabsSerpElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
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

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if breadcrumb (nullable) is None
        # and model_fields_set contains the field
        if self.breadcrumb is None and "breadcrumb" in self.model_fields_set:
            _dict['breadcrumb'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if highlighted (nullable) is None
        # and model_fields_set contains the field
        if self.highlighted is None and "highlighted" in self.model_fields_set:
            _dict['highlighted'] = None

        # set to None if extra (nullable) is None
        # and model_fields_set contains the field
        if self.extra is None and "extra" in self.model_fields_set:
            _dict['extra'] = None

        # set to None if description_rows (nullable) is None
        # and model_fields_set contains the field
        if self.description_rows is None and "description_rows" in self.model_fields_set:
            _dict['description_rows'] = None

        # set to None if links (nullable) is None
        # and model_fields_set contains the field
        if self.links is None and "links" in self.model_fields_set:
            _dict['links'] = None

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

        # set to None if se_type (nullable) is None
        # and model_fields_set contains the field
        if self.se_type is None and "se_type" in self.model_fields_set:
            _dict['se_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaidDataforseoLabsSerpElementItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "title": obj.get("title"),
            "domain": obj.get("domain"),
            "description": obj.get("description"),
            "breadcrumb": obj.get("breadcrumb"),
            "url": obj.get("url"),
            "highlighted": obj.get("highlighted"),
            "extra": obj.get("extra"),
            "description_rows": obj.get("description_rows"),
            "links": [AdLinkElement.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None,
            "main_domain": obj.get("main_domain"),
            "relative_url": obj.get("relative_url"),
            "etv": obj.get("etv"),
            "impressions_etv": obj.get("impressions_etv"),
            "estimated_paid_traffic_cost": obj.get("estimated_paid_traffic_cost"),
            "rank_changes": RankChanges.from_dict(obj["rank_changes"]) if obj.get("rank_changes") is not None else None,
            "clickstream_etv": obj.get("clickstream_etv"),
            "se_type": obj.get("se_type"),
            "backlinks_info": BacklinksInfo.from_dict(obj["backlinks_info"]) if obj.get("backlinks_info") is not None else None,
            "rank_info": RankInfo.from_dict(obj["rank_info"]) if obj.get("rank_info") is not None else None
        })
        return _obj


