from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AboutThisResultElement(BaseModel):
    """
    AboutThisResultElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    url: Optional[StrictStr] = Field(default=None, description="result’s URL")
    source: Optional[StrictStr] = Field(default=None, description="source of additional information about the result")
    source_info: Optional[StrictStr] = Field(default=None, description="additional information about the result. description of the website from Wikipedia or another additional context")
    source_url: Optional[StrictStr] = Field(default=None, description="URL to full information from the 'source'")
    language: Optional[StrictStr] = Field(default=None, description="the language of the result")
    location: Optional[StrictStr] = Field(default=None, description="location for which the result is relevant")
    search_terms: Optional[List[Optional[StrictStr]]] = Field(default=None, description="matching search terms that appear in the result")
    related_terms: Optional[List[Optional[StrictStr]]] = Field(default=None, description="related search terms that appear in the result")
    __properties: ClassVar[List[str]] = [
        "type", 
        "url", 
        "source", 
        "source_info", 
        "source_url", 
        "language", 
        "location", 
        "search_terms", 
        "related_terms", 
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
        _dict['url'] = self.url
        _dict['source'] = self.source
        _dict['source_info'] = self.source_info
        _dict['source_url'] = self.source_url
        _dict['language'] = self.language
        _dict['location'] = self.location
        _dict['search_terms'] = self.search_terms
        _dict['related_terms'] = self.related_terms
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "url": obj.get("url"),
            "source": obj.get("source"),
            "source_info": obj.get("source_info"),
            "source_url": obj.get("source_url"),
            "language": obj.get("language"),
            "location": obj.get("location"),
            "search_terms": obj.get("search_terms"),
            "related_terms": obj.get("related_terms"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj