from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class OnPageAvailableFiltersResultInfo(BaseModel):
    """
    OnPageAvailableFiltersResultInfo
    """ # noqa: E501
    resources: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    pages: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    non_indexable: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    links: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    pages_by_resource: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    redirect_chains: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    keyword_density: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "resources", 
        "pages", 
        "non_indexable", 
        "links", 
        "pages_by_resource", 
        "redirect_chains", 
        "keyword_density", 
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

        _dict['resources'] = self.resources
        _dict['pages'] = self.pages
        _dict['non_indexable'] = self.non_indexable
        _dict['links'] = self.links
        _dict['pages_by_resource'] = self.pages_by_resource
        _dict['redirect_chains'] = self.redirect_chains
        _dict['keyword_density'] = self.keyword_density
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "resources": obj.get("resources"),
            "pages": obj.get("pages"),
            "non_indexable": obj.get("non_indexable"),
            "links": obj.get("links"),
            "pages_by_resource": obj.get("pages_by_resource"),
            "redirect_chains": obj.get("redirect_chains"),
            "keyword_density": obj.get("keyword_density"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj