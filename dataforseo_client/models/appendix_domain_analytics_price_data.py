from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_whois_domain_analytics_price_data import AppendixWhoisDomainAnalyticsPriceData
from dataforseo_client.models.appendix_technologies_domain_analytics_price_data import AppendixTechnologiesDomainAnalyticsPriceData
from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo



class AppendixDomainAnalyticsPriceData(BaseModel):
    """
    AppendixDomainAnalyticsPriceData
    """ # noqa: E501
    whois: Optional[AppendixWhoisDomainAnalyticsPriceData] = Field(default=None, description="")
    technologies: Optional[AppendixTechnologiesDomainAnalyticsPriceData] = Field(default=None, description="")
    errors: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    tasks_ready: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "whois", 
        "technologies", 
        "errors", 
        "tasks_ready", 
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

        _dict['whois'] = self.whois.to_dict() if self.whois else None
        _dict['technologies'] = self.technologies.to_dict() if self.technologies else None
        _dict['errors'] = self.errors.to_dict() if self.errors else None
        _dict['tasks_ready'] = self.tasks_ready.to_dict() if self.tasks_ready else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "whois": AppendixWhoisDomainAnalyticsPriceData.from_dict(obj["whois"]) if obj.get("whois") is not None else None,
            "technologies": AppendixTechnologiesDomainAnalyticsPriceData.from_dict(obj["technologies"]) if obj.get("technologies") is not None else None,
            "errors": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["errors"]) if obj.get("errors") is not None else None,
            "tasks_ready": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["tasks_ready"]) if obj.get("tasks_ready") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj