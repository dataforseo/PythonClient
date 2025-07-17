from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BacklinksAvailableFiltersResultInfo(BaseModel):
    """
    BacklinksAvailableFiltersResultInfo
    """ # noqa: E501
    content_duplicates: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    backlinks: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    domain_pages: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    anchors: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    referring_domains: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    domain_intersection: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    page_intersection: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    referring_networks: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    domain_pages_summary: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    competitors: Optional[Dict[str, Optional[StrictStr]]] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "content_duplicates", 
        "backlinks", 
        "domain_pages", 
        "anchors", 
        "referring_domains", 
        "domain_intersection", 
        "page_intersection", 
        "referring_networks", 
        "domain_pages_summary", 
        "competitors", 
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

        _dict['content_duplicates'] = self.content_duplicates
        _dict['backlinks'] = self.backlinks
        _dict['domain_pages'] = self.domain_pages
        _dict['anchors'] = self.anchors
        _dict['referring_domains'] = self.referring_domains
        _dict['domain_intersection'] = self.domain_intersection
        _dict['page_intersection'] = self.page_intersection
        _dict['referring_networks'] = self.referring_networks
        _dict['domain_pages_summary'] = self.domain_pages_summary
        _dict['competitors'] = self.competitors
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "content_duplicates": obj.get("content_duplicates"),
            "backlinks": obj.get("backlinks"),
            "domain_pages": obj.get("domain_pages"),
            "anchors": obj.get("anchors"),
            "referring_domains": obj.get("referring_domains"),
            "domain_intersection": obj.get("domain_intersection"),
            "page_intersection": obj.get("page_intersection"),
            "referring_networks": obj.get("referring_networks"),
            "domain_pages_summary": obj.get("domain_pages_summary"),
            "competitors": obj.get("competitors"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj