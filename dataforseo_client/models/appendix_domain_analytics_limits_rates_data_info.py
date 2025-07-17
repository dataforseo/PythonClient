from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_whois_domain_analytics_limits_rates_data_info import AppendixWhoisDomainAnalyticsLimitsRatesDataInfo
from dataforseo_client.models.appendix_technologies_domain_analytics_limits_rates_data_info import AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo



class AppendixDomainAnalyticsLimitsRatesDataInfo(BaseModel):
    """
    AppendixDomainAnalyticsLimitsRatesDataInfo
    """ # noqa: E501
    tasks_ready: Optional[StrictFloat] = Field(default=None, description="")
    errors: Optional[StrictFloat] = Field(default=None, description="")
    whois: Optional[AppendixWhoisDomainAnalyticsLimitsRatesDataInfo] = Field(default=None, description="")
    technologies: Optional[AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "tasks_ready", 
        "errors", 
        "whois", 
        "technologies", 
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

        _dict['tasks_ready'] = self.tasks_ready
        _dict['errors'] = self.errors
        _dict['whois'] = self.whois.to_dict() if self.whois else None
        _dict['technologies'] = self.technologies.to_dict() if self.technologies else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tasks_ready": obj.get("tasks_ready"),
            "errors": obj.get("errors"),
            "whois": AppendixWhoisDomainAnalyticsLimitsRatesDataInfo.from_dict(obj["whois"]) if obj.get("whois") is not None else None,
            "technologies": AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo.from_dict(obj["technologies"]) if obj.get("technologies") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj