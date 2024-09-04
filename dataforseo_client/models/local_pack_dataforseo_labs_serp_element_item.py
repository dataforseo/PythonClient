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
from dataforseo_client.models.base_dataforseo_labs_serp_element_item import BaseDataforseoLabsSerpElementItem
from dataforseo_client.models.rank_changes import RankChanges
from dataforseo_client.models.rating_info import RatingInfo
from typing import Optional, Set
from typing_extensions import Self

class LocalPackDataforseoLabsSerpElementItem(BaseDataforseoLabsSerpElementItem):
    """
    LocalPackDataforseoLabsSerpElementItem
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description="title of the result in SERP")
    description: Optional[StrictStr] = Field(default=None, description="description of the results element in SERP")
    domain: Optional[StrictStr] = Field(default=None, description="website domain")
    phone: Optional[StrictStr] = Field(default=None, description="phone number")
    url: Optional[StrictStr] = Field(default=None, description="relevant URL of the Ad element in SERP")
    is_paid: Optional[StrictBool] = Field(default=None, description="indicates whether the element is an ad")
    rating: Optional[RatingInfo] = None
    main_domain: Optional[StrictStr] = Field(default=None, description="primary domain name in SERP")
    relative_url: Optional[StrictStr] = Field(default=None, description="URL in SERP that does not specify the HTTPs protocol and domain name")
    etv: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="estimated traffic volume estimated organic monthly traffic to the domain calculated as the product of CTR (click-through-rate) and search volume values of the returned keyword learn more about how the metric is calculated in this help center article")
    impressions_etv: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="estimated traffic volume based on impressions estimated organic monthly traffic to the domain calculated as the product of CTR (click-through-rate) and impressions values of the returned keyword learn more about how the metric is calculated in this help center article")
    estimated_paid_traffic_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="estimated cost of converting organic search traffic into paid represents the estimated monthly cost of running ads for the returned keyword the metric is calculated as the product of organic etv and paid cpc values and indicates the cost of driving the estimated volume of monthly organic traffic through PPC advertising in Google Search learn more about how the metric is calculated in this help center article")
    rank_changes: Optional[RankChanges] = None
    clickstream_etv: Optional[StrictInt] = Field(default=None, description="estimated traffic volume based on clickstream data calculated as the product of click-through-rate and clickstream search volume values of all keywords the domain ranks for to retrieve results for this field, the parameter include_clickstream_data must be set to true learn more about how the metric is calculated in this help center article https://dataforseo.com/help-center/whats-clickstream-estimated-traffic-volume-and-how-is-it-calculated")
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "position", "xpath", "title", "description", "domain", "phone", "url", "is_paid", "rating", "main_domain", "relative_url", "etv", "impressions_etv", "estimated_paid_traffic_cost", "rank_changes", "clickstream_etv"]

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
        """Create an instance of LocalPackDataforseoLabsSerpElementItem from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of rank_changes
        if self.rank_changes:
            _dict['rank_changes'] = self.rank_changes.to_dict()
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

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if domain (nullable) is None
        # and model_fields_set contains the field
        if self.domain is None and "domain" in self.model_fields_set:
            _dict['domain'] = None

        # set to None if phone (nullable) is None
        # and model_fields_set contains the field
        if self.phone is None and "phone" in self.model_fields_set:
            _dict['phone'] = None

        # set to None if url (nullable) is None
        # and model_fields_set contains the field
        if self.url is None and "url" in self.model_fields_set:
            _dict['url'] = None

        # set to None if is_paid (nullable) is None
        # and model_fields_set contains the field
        if self.is_paid is None and "is_paid" in self.model_fields_set:
            _dict['is_paid'] = None

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
        """Create an instance of LocalPackDataforseoLabsSerpElementItem from a dict"""
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
            "description": obj.get("description"),
            "domain": obj.get("domain"),
            "phone": obj.get("phone"),
            "url": obj.get("url"),
            "is_paid": obj.get("is_paid"),
            "rating": RatingInfo.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "main_domain": obj.get("main_domain"),
            "relative_url": obj.get("relative_url"),
            "etv": obj.get("etv"),
            "impressions_etv": obj.get("impressions_etv"),
            "estimated_paid_traffic_cost": obj.get("estimated_paid_traffic_cost"),
            "rank_changes": RankChanges.from_dict(obj["rank_changes"]) if obj.get("rank_changes") is not None else None,
            "clickstream_etv": obj.get("clickstream_etv")
        })
        return _obj


