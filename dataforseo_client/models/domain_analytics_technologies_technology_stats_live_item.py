from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DomainAnalyticsTechnologiesTechnologyStatsLiveItem(BaseModel):
    """
    DomainAnalyticsTechnologiesTechnologyStatsLiveItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    date: Optional[StrictStr] = Field(default=None, description="date for which the data is provided")
    domains_count: Optional[StrictInt] = Field(default=None, description="number of domains that use the specified technology")
    countries: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="distribution of websites by country. contains country codes and number of websites per country")
    languages: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="distribution of websites by language. contains language codes and number of websites per language")
    domains_rank: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="distribution of websites by backlink rank. contains domain rank ranges and number of websites per range. learn more about rank and how it is calculated in this help center article")
    __properties: ClassVar[List[str]] = [
        "type", 
        "date", 
        "domains_count", 
        "countries", 
        "languages", 
        "domains_rank", 
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

        _dict['type'] = self.type
        _dict['date'] = self.date
        _dict['domains_count'] = self.domains_count
        _dict['countries'] = self.countries
        _dict['languages'] = self.languages
        _dict['domains_rank'] = self.domains_rank
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "date": obj.get("date"),
            "domains_count": obj.get("domains_count"),
            "countries": obj.get("countries"),
            "languages": obj.get("languages"),
            "domains_rank": obj.get("domains_rank"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj