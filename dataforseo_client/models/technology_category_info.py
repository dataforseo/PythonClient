from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class TechnologyCategoryInfo(BaseModel):
    """
    TechnologyCategoryInfo
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="id of the technology category. example:. crm, cart_abandonment")
    path: Optional[StrictStr] = Field(default=None, description="path to the technology category. example:. user_generated_content.content_curation")
    title: Optional[StrictStr] = Field(default=None, description="title of the technology category")
    technologies: Optional[List[Optional[StrictStr]]] = Field(default=None, description="list of technologies in this category. example:. 'Salesforce', 'CareCart'")
    __properties: ClassVar[List[str]] = [
        "id", 
        "path", 
        "title", 
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

        _dict['id'] = self.id
        _dict['path'] = self.path
        _dict['title'] = self.title
        _dict['technologies'] = self.technologies
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "path": obj.get("path"),
            "title": obj.get("title"),
            "technologies": obj.get("technologies"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj