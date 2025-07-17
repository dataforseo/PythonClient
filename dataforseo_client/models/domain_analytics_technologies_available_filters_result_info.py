from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DomainAnalyticsTechnologiesAvailableFiltersResultInfo(BaseModel):
    """
    DomainAnalyticsTechnologiesAvailableFiltersResultInfo
    """ # noqa: E501
    domains_by_technology: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    aggregation_technologies: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    technologies_summary: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    domains_by_html_terms: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "domains_by_technology", 
        "aggregation_technologies", 
        "technologies_summary", 
        "domains_by_html_terms", 
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

        _dict['domains_by_technology'] = self.domains_by_technology
        _dict['aggregation_technologies'] = self.aggregation_technologies
        _dict['technologies_summary'] = self.technologies_summary
        _dict['domains_by_html_terms'] = self.domains_by_html_terms
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "domains_by_technology": obj.get("domains_by_technology"),
            "aggregation_technologies": obj.get("aggregation_technologies"),
            "technologies_summary": obj.get("technologies_summary"),
            "domains_by_html_terms": obj.get("domains_by_html_terms"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj