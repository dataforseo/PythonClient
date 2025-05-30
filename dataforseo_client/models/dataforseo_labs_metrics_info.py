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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class DataforseoLabsMetricsInfo(BaseModel):
    """
    DataforseoLabsMetricsInfo
    """ # noqa: E501
    pos_1: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="number of organic SERPs where the domain or subdomain ranks #1")
    pos_2_3: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="number of organic SERPs where the domain or subdomain ranks #2-3")
    pos_4_10: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="number of organic SERPs where the domain or subdomain ranks #4-10")
    pos_11_20: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="number of organic SERPs where the domain or subdomain ranks #11-20")
    pos_21_30: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="number of organic SERPs where the domain or subdomain ranks #21-30")
    pos_31_40: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="number of organic SERPs where the domain or subdomain ranks #31-40")
    pos_41_50: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="number of organic SERPs where the domain or subdomain ranks #41-50")
    pos_51_60: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="number of organic SERPs where the domain or subdomain ranks #51-60")
    pos_61_70: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="number of organic SERPs where the domain or subdomain ranks #61-70")
    pos_71_80: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="number of organic SERPs where the domain or subdomain ranks #71-80")
    pos_81_90: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="number of organic SERPs where the domain or subdomain ranks #81-90")
    pos_91_100: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="number of organic SERPs where the domain or subdomain ranks #91-100")
    etv: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="estimated traffic volume estimated organic monthly traffic to the domain or subdomain calculated as the product of CTR (click-through-rate) and search volume values of all keywords in the category that the domain or subdomain ranks for learn more about how the metric is calculated in this help center article")
    count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="total count of organic SERPs that contain the domain or subdomain")
    estimated_paid_traffic_cost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="estimated cost of converting organic search traffic into paid represents the estimated monthly cost (USD) of running ads for all keywords in the category that the domain or subdomain ranks for the metric is calculated as the product of organic etv and paid cpc values and indicates the cost of driving the estimated volume of monthly organic traffic through PPC advertising in Google Search learn more about how the metric is calculated in this help center article")
    is_new: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="number of new ranked elements indicates how many new ranked elements were found for the indicated target")
    is_up: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="rank went up indicates how many ranked elements of the indicated target went up")
    is_down: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="rank went down indicates how many ranked elements of the indicated target went down")
    is_lost: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="lost ranked elements indicates how many ranked elements of the indicated target were previously presented in SERPs, but weren’t found during the last check")
    clickstream_etv: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="estimated traffic volume based on clickstream data calculated as the product of click-through-rate and clickstream search volume values of all keywords the domain ranks for to retrieve results for this field, the parameter include_clickstream_data must be set to true learn more about how the metric is calculated in this help center article")
    clickstream_gender_distribution: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="distribution of estimated clickstream-based metrics by gender to retrieve results for this field, the parameter include_clickstream_data must be set to true learn more about how the metric is calculated in this help center article")
    clickstream_age_distribution: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="distribution of clickstream-based metrics by age to retrieve results for this field, the parameter include_clickstream_data must be set to true learn more about how the metric is calculated in this help center article")
    __properties: ClassVar[List[str]] = ["pos_1", "pos_2_3", "pos_4_10", "pos_11_20", "pos_21_30", "pos_31_40", "pos_41_50", "pos_51_60", "pos_61_70", "pos_71_80", "pos_81_90", "pos_91_100", "etv", "count", "estimated_paid_traffic_cost", "is_new", "is_up", "is_down", "is_lost", "clickstream_etv", "clickstream_gender_distribution", "clickstream_age_distribution"]

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
        """Create an instance of DataforseoLabsMetricsInfo from a JSON string"""
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
        # set to None if pos_1 (nullable) is None
        # and model_fields_set contains the field
        if self.pos_1 is None and "pos_1" in self.model_fields_set:
            _dict['pos_1'] = None

        # set to None if pos_2_3 (nullable) is None
        # and model_fields_set contains the field
        if self.pos_2_3 is None and "pos_2_3" in self.model_fields_set:
            _dict['pos_2_3'] = None

        # set to None if pos_4_10 (nullable) is None
        # and model_fields_set contains the field
        if self.pos_4_10 is None and "pos_4_10" in self.model_fields_set:
            _dict['pos_4_10'] = None

        # set to None if pos_11_20 (nullable) is None
        # and model_fields_set contains the field
        if self.pos_11_20 is None and "pos_11_20" in self.model_fields_set:
            _dict['pos_11_20'] = None

        # set to None if pos_21_30 (nullable) is None
        # and model_fields_set contains the field
        if self.pos_21_30 is None and "pos_21_30" in self.model_fields_set:
            _dict['pos_21_30'] = None

        # set to None if pos_31_40 (nullable) is None
        # and model_fields_set contains the field
        if self.pos_31_40 is None and "pos_31_40" in self.model_fields_set:
            _dict['pos_31_40'] = None

        # set to None if pos_41_50 (nullable) is None
        # and model_fields_set contains the field
        if self.pos_41_50 is None and "pos_41_50" in self.model_fields_set:
            _dict['pos_41_50'] = None

        # set to None if pos_51_60 (nullable) is None
        # and model_fields_set contains the field
        if self.pos_51_60 is None and "pos_51_60" in self.model_fields_set:
            _dict['pos_51_60'] = None

        # set to None if pos_61_70 (nullable) is None
        # and model_fields_set contains the field
        if self.pos_61_70 is None and "pos_61_70" in self.model_fields_set:
            _dict['pos_61_70'] = None

        # set to None if pos_71_80 (nullable) is None
        # and model_fields_set contains the field
        if self.pos_71_80 is None and "pos_71_80" in self.model_fields_set:
            _dict['pos_71_80'] = None

        # set to None if pos_81_90 (nullable) is None
        # and model_fields_set contains the field
        if self.pos_81_90 is None and "pos_81_90" in self.model_fields_set:
            _dict['pos_81_90'] = None

        # set to None if pos_91_100 (nullable) is None
        # and model_fields_set contains the field
        if self.pos_91_100 is None and "pos_91_100" in self.model_fields_set:
            _dict['pos_91_100'] = None

        # set to None if etv (nullable) is None
        # and model_fields_set contains the field
        if self.etv is None and "etv" in self.model_fields_set:
            _dict['etv'] = None

        # set to None if count (nullable) is None
        # and model_fields_set contains the field
        if self.count is None and "count" in self.model_fields_set:
            _dict['count'] = None

        # set to None if estimated_paid_traffic_cost (nullable) is None
        # and model_fields_set contains the field
        if self.estimated_paid_traffic_cost is None and "estimated_paid_traffic_cost" in self.model_fields_set:
            _dict['estimated_paid_traffic_cost'] = None

        # set to None if is_new (nullable) is None
        # and model_fields_set contains the field
        if self.is_new is None and "is_new" in self.model_fields_set:
            _dict['is_new'] = None

        # set to None if is_up (nullable) is None
        # and model_fields_set contains the field
        if self.is_up is None and "is_up" in self.model_fields_set:
            _dict['is_up'] = None

        # set to None if is_down (nullable) is None
        # and model_fields_set contains the field
        if self.is_down is None and "is_down" in self.model_fields_set:
            _dict['is_down'] = None

        # set to None if is_lost (nullable) is None
        # and model_fields_set contains the field
        if self.is_lost is None and "is_lost" in self.model_fields_set:
            _dict['is_lost'] = None

        # set to None if clickstream_etv (nullable) is None
        # and model_fields_set contains the field
        if self.clickstream_etv is None and "clickstream_etv" in self.model_fields_set:
            _dict['clickstream_etv'] = None

        # set to None if clickstream_gender_distribution (nullable) is None
        # and model_fields_set contains the field
        if self.clickstream_gender_distribution is None and "clickstream_gender_distribution" in self.model_fields_set:
            _dict['clickstream_gender_distribution'] = None

        # set to None if clickstream_age_distribution (nullable) is None
        # and model_fields_set contains the field
        if self.clickstream_age_distribution is None and "clickstream_age_distribution" in self.model_fields_set:
            _dict['clickstream_age_distribution'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataforseoLabsMetricsInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pos_1": obj.get("pos_1"),
            "pos_2_3": obj.get("pos_2_3"),
            "pos_4_10": obj.get("pos_4_10"),
            "pos_11_20": obj.get("pos_11_20"),
            "pos_21_30": obj.get("pos_21_30"),
            "pos_31_40": obj.get("pos_31_40"),
            "pos_41_50": obj.get("pos_41_50"),
            "pos_51_60": obj.get("pos_51_60"),
            "pos_61_70": obj.get("pos_61_70"),
            "pos_71_80": obj.get("pos_71_80"),
            "pos_81_90": obj.get("pos_81_90"),
            "pos_91_100": obj.get("pos_91_100"),
            "etv": obj.get("etv"),
            "count": obj.get("count"),
            "estimated_paid_traffic_cost": obj.get("estimated_paid_traffic_cost"),
            "is_new": obj.get("is_new"),
            "is_up": obj.get("is_up"),
            "is_down": obj.get("is_down"),
            "is_lost": obj.get("is_lost"),
            "clickstream_etv": obj.get("clickstream_etv"),
            "clickstream_gender_distribution": obj.get("clickstream_gender_distribution"),
            "clickstream_age_distribution": obj.get("clickstream_age_distribution")
        })
        return _obj


