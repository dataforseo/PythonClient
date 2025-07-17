from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DomainAnalyticsTechnologiesTechnologiesSummaryLiveResultInfo(BaseModel):
    """
    DomainAnalyticsTechnologiesTechnologiesSummaryLiveResultInfo
    """ # noqa: E501
    countries: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="distribution of websites by country. contains country codes and number of websites per country")
    languages: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="distribution of websites by language. contains language codes and number of websites per language")
    content_languages: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="distribution of websites by content language. contains content language codes and number of websites per language")
    keywords: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="distribution of websites by keywords. contains keywords found in the websites’ titles, descriptions or meta keywords, and number of websites using each keyword")
    __properties: ClassVar[List[str]] = [
        "countries", 
        "languages", 
        "content_languages", 
        "keywords", 
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

        _dict['countries'] = self.countries
        _dict['languages'] = self.languages
        _dict['content_languages'] = self.content_languages
        _dict['keywords'] = self.keywords
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "countries": obj.get("countries"),
            "languages": obj.get("languages"),
            "content_languages": obj.get("content_languages"),
            "keywords": obj.get("keywords"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj