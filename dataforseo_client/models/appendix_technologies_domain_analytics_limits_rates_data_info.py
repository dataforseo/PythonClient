from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_info import AppendixInfo



class AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo(BaseModel):
    """
    AppendixTechnologiesDomainAnalyticsLimitsRatesDataInfo
    """ # noqa: E501
    domain_technologies: Optional[AppendixInfo] = Field(default=None, description="")
    domains_by_technology: Optional[AppendixInfo] = Field(default=None, description="")
    languages: Optional[StrictFloat] = Field(default=None, description="")
    locations: Optional[StrictFloat] = Field(default=None, description="")
    technologies: Optional[StrictFloat] = Field(default=None, description="")
    aggregation_technologies: Optional[AppendixInfo] = Field(default=None, description="")
    technologies_summary: Optional[AppendixInfo] = Field(default=None, description="")
    domains_by_html_terms: Optional[AppendixInfo] = Field(default=None, description="")
    technology_stats: Optional[AppendixInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "domain_technologies", 
        "domains_by_technology", 
        "languages", 
        "locations", 
        "technologies", 
        "aggregation_technologies", 
        "technologies_summary", 
        "domains_by_html_terms", 
        "technology_stats", 
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

        _dict['domain_technologies'] = self.domain_technologies.to_dict() if self.domain_technologies else None
        _dict['domains_by_technology'] = self.domains_by_technology.to_dict() if self.domains_by_technology else None
        _dict['languages'] = self.languages
        _dict['locations'] = self.locations
        _dict['technologies'] = self.technologies
        _dict['aggregation_technologies'] = self.aggregation_technologies.to_dict() if self.aggregation_technologies else None
        _dict['technologies_summary'] = self.technologies_summary.to_dict() if self.technologies_summary else None
        _dict['domains_by_html_terms'] = self.domains_by_html_terms.to_dict() if self.domains_by_html_terms else None
        _dict['technology_stats'] = self.technology_stats.to_dict() if self.technology_stats else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "domain_technologies": AppendixInfo.from_dict(obj["domain_technologies"]) if obj.get("domain_technologies") is not None else None,
            "domains_by_technology": AppendixInfo.from_dict(obj["domains_by_technology"]) if obj.get("domains_by_technology") is not None else None,
            "languages": obj.get("languages"),
            "locations": obj.get("locations"),
            "technologies": obj.get("technologies"),
            "aggregation_technologies": AppendixInfo.from_dict(obj["aggregation_technologies"]) if obj.get("aggregation_technologies") is not None else None,
            "technologies_summary": AppendixInfo.from_dict(obj["technologies_summary"]) if obj.get("technologies_summary") is not None else None,
            "domains_by_html_terms": AppendixInfo.from_dict(obj["domains_by_html_terms"]) if obj.get("domains_by_html_terms") is not None else None,
            "technology_stats": AppendixInfo.from_dict(obj["technology_stats"]) if obj.get("technology_stats") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj