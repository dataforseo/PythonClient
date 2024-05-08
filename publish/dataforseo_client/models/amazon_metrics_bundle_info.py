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

from pydantic import BaseModel
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.app_metrics_info import AppMetricsInfo
from typing import Optional, Set
from typing_extensions import Self

class AmazonMetricsBundleInfo(BaseModel):
    """
    AmazonMetricsBundleInfo
    """ # noqa: E501
    amazon_serp: Optional[AppMetricsInfo] = None
    amazon_paid: Optional[AppMetricsInfo] = None
    __properties: ClassVar[List[str]] = ["amazon_serp", "amazon_paid"]

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
        """Create an instance of AmazonMetricsBundleInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of amazon_serp
        if self.amazon_serp:
            _dict['amazon_serp'] = self.amazon_serp.to_dict()
        # override the default output from pydantic by calling `to_dict()` of amazon_paid
        if self.amazon_paid:
            _dict['amazon_paid'] = self.amazon_paid.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AmazonMetricsBundleInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amazon_serp": AppMetricsInfo.from_dict(obj["amazon_serp"]) if obj.get("amazon_serp") is not None else None,
            "amazon_paid": AppMetricsInfo.from_dict(obj["amazon_paid"]) if obj.get("amazon_paid") is not None else None
        })
        return _obj

