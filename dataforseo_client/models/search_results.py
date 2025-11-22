from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SearchResults(BaseModel):
    """
    SearchResults
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description=r"result description")
    breadcrumb: Optional[StrictStr] = Field(default=None, description=r"breadcrumb")
    position: Optional[StrictInt] = Field(default=None, description=r"position in the results")
    title: Optional[StrictStr] = Field(default=None, description=r"result title")
    domain: Optional[StrictStr] = Field(default=None, description=r"result domain")
    url: Optional[StrictStr] = Field(default=None, description=r"result URL")
    publication_date: Optional[StrictStr] = Field(default=None, description=r"date and time when the result was published. in the format: “year-month-date:minutes:UTC_difference_hours:UTC_difference_minutes”. example:. 2019-11-15 12:57:46 +00:00")
    __properties: ClassVar[List[str]] = [
        "description", 
        "breadcrumb", 
        "position", 
        "title", 
        "domain", 
        "url", 
        "publication_date", 
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

        _dict['description'] = self.description
        _dict['breadcrumb'] = self.breadcrumb
        _dict['position'] = self.position
        _dict['title'] = self.title
        _dict['domain'] = self.domain
        _dict['url'] = self.url
        _dict['publication_date'] = self.publication_date
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "breadcrumb": obj.get("breadcrumb"),
            "position": obj.get("position"),
            "title": obj.get("title"),
            "domain": obj.get("domain"),
            "url": obj.get("url"),
            "publication_date": obj.get("publication_date"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj