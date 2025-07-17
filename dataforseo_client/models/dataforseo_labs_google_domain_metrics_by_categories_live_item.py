from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.dataforseo_labs_metrics_info import DataforseoLabsMetricsInfo



class DataforseoLabsGoogleDomainMetricsByCategoriesLiveItem(BaseModel):
    """
    DataforseoLabsGoogleDomainMetricsByCategoriesLiveItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    top_categories: Optional[List[Optional[StrictInt]]] = Field(default=None, description="categories for which domains are collected")
    organic_etv: Optional[StrictFloat] = Field(default=None, description="current organic ETV of the domain")
    organic_count: Optional[StrictInt] = Field(default=None, description="current total count of organic SERPs that contain the domain")
    organic_is_lost: Optional[StrictInt] = Field(default=None, description="current number of lost ranked elements. indicates how many ranked elements of the domain were previously presented in SERPs, but weren’t found during the last check")
    organic_is_new: Optional[StrictInt] = Field(default=None, description="current number of new ranked elements. indicates how many new ranked elements were found for the domain")
    domain: Optional[StrictStr] = Field(default=None, description="domain found for the specified category")
    main_domain: Optional[StrictStr] = Field(default=None, description="primary domain")
    metrics_history: Optional[Dict[str, Optional[Dict[str, Optional[DataforseoLabsMetricsInfo]]]]] = Field(default=None, description="historical ranking and traffic data of the domain")
    metrics_difference: Optional[Dict[str, Optional[DataforseoLabsMetricsInfo]]] = Field(default=None, description="metrics difference between first_date and second_date. calculated by subtracting domain metrics as of the greater date from domain metrics as of the smaller date")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "top_categories", 
        "organic_etv", 
        "organic_count", 
        "organic_is_lost", 
        "organic_is_new", 
        "domain", 
        "main_domain", 
        "metrics_history", 
        "metrics_difference", 
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

        _dict['se_type'] = self.se_type
        _dict['top_categories'] = self.top_categories
        _dict['organic_etv'] = self.organic_etv
        _dict['organic_count'] = self.organic_count
        _dict['organic_is_lost'] = self.organic_is_lost
        _dict['organic_is_new'] = self.organic_is_new
        _dict['domain'] = self.domain
        _dict['main_domain'] = self.main_domain
        _dict['metrics_history'] = self.metrics_history
        _dict['metrics_difference'] = self.metrics_difference
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "top_categories": obj.get("top_categories"),
            "organic_etv": obj.get("organic_etv"),
            "organic_count": obj.get("organic_count"),
            "organic_is_lost": obj.get("organic_is_lost"),
            "organic_is_new": obj.get("organic_is_new"),
            "domain": obj.get("domain"),
            "main_domain": obj.get("main_domain"),
            "metrics_history": obj.get("metrics_history"),
            "metrics_difference": obj.get("metrics_difference"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj