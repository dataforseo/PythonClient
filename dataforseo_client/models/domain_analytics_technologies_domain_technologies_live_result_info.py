from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.technologies_info import TechnologiesInfo



class DomainAnalyticsTechnologiesDomainTechnologiesLiveResultInfo(BaseModel):
    """
    DomainAnalyticsTechnologiesDomainTechnologiesLiveResultInfo
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    domain: Optional[StrictStr] = Field(default=None, description="specified domain name")
    title: Optional[StrictStr] = Field(default=None, description="domain meta title")
    description: Optional[StrictStr] = Field(default=None, description="domain meta description")
    meta_keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="domain meta keywords")
    domain_rank: Optional[StrictInt] = Field(default=None, description="backlink rank of the target domain. learn more about the metric and how it is calculated in this help center article")
    last_visited: Optional[StrictStr] = Field(default=None, description="most recent date when our crawler visited the domain. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2022-10-10 12:57:46 +00:00")
    country_iso_code: Optional[StrictStr] = Field(default=None, description="domain ISO code. ISO code of the country that the target domain is determined to belong to")
    language_code: Optional[StrictStr] = Field(default=None, description="domain language. code of the language that the target domain is determined to be associated with")
    content_language_code: Optional[StrictStr] = Field(default=None, description="content language. code of the language that content on the target domain is written in")
    phone_numbers: Optional[List[Optional[StrictStr]]] = Field(default=None, description="phone numbers of the target. contact phone numbers indicated on the target website")
    emails: Optional[List[Optional[StrictStr]]] = Field(default=None, description="emails of the target. emails indicated on the target website")
    social_graph_urls: Optional[List[Optional[StrictStr]]] = Field(default=None, description="social media links and handles. social media URLs detected in the social graphs of the target website")
    technologies: Optional[TechnologiesInfo] = Field(default=None, description="technologies used by target domain. contains objects with the names of technologies used on the website. see the full list of available technologies structured by groups and categories")
    __properties: ClassVar[List[str]] = [
        "type", 
        "domain", 
        "title", 
        "description", 
        "meta_keywords", 
        "domain_rank", 
        "last_visited", 
        "country_iso_code", 
        "language_code", 
        "content_language_code", 
        "phone_numbers", 
        "emails", 
        "social_graph_urls", 
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

        _dict['type'] = self.type
        _dict['domain'] = self.domain
        _dict['title'] = self.title
        _dict['description'] = self.description
        _dict['meta_keywords'] = self.meta_keywords
        _dict['domain_rank'] = self.domain_rank
        _dict['last_visited'] = self.last_visited
        _dict['country_iso_code'] = self.country_iso_code
        _dict['language_code'] = self.language_code
        _dict['content_language_code'] = self.content_language_code
        _dict['phone_numbers'] = self.phone_numbers
        _dict['emails'] = self.emails
        _dict['social_graph_urls'] = self.social_graph_urls
        _dict['technologies'] = self.technologies.to_dict() if self.technologies else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "domain": obj.get("domain"),
            "title": obj.get("title"),
            "description": obj.get("description"),
            "meta_keywords": obj.get("meta_keywords"),
            "domain_rank": obj.get("domain_rank"),
            "last_visited": obj.get("last_visited"),
            "country_iso_code": obj.get("country_iso_code"),
            "language_code": obj.get("language_code"),
            "content_language_code": obj.get("content_language_code"),
            "phone_numbers": obj.get("phone_numbers"),
            "emails": obj.get("emails"),
            "social_graph_urls": obj.get("social_graph_urls"),
            "technologies": TechnologiesInfo.from_dict(obj["technologies"]) if obj.get("technologies") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj