from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BacklinksBulkReferringDomainsLiveItem(BaseModel):
    """
    BacklinksBulkReferringDomainsLiveItem
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="domain, subdomain or webpage from a POST array")
    referring_domains: Optional[StrictInt] = Field(default=None, description="number of referring domains pointing to the target. note that we calculate main domains (root domains, like example.com) and their subdomains (e.g. blog.example.com) separately for this metric")
    referring_domains_nofollow: Optional[StrictInt] = Field(default=None, description="number of domains pointing at least one nofollow link to the target")
    referring_main_domains: Optional[StrictInt] = Field(default=None, description="number of referring main domains pointing to the target. the number of primary (root) domains referring to your target")
    referring_main_domains_nofollow: Optional[StrictInt] = Field(default=None, description="number of main domains pointing at least one nofollow link to the target")
    __properties: ClassVar[List[str]] = [
        "target", 
        "referring_domains", 
        "referring_domains_nofollow", 
        "referring_main_domains", 
        "referring_main_domains_nofollow", 
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

        _dict['target'] = self.target
        _dict['referring_domains'] = self.referring_domains
        _dict['referring_domains_nofollow'] = self.referring_domains_nofollow
        _dict['referring_main_domains'] = self.referring_main_domains
        _dict['referring_main_domains_nofollow'] = self.referring_main_domains_nofollow
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "target": obj.get("target"),
            "referring_domains": obj.get("referring_domains"),
            "referring_domains_nofollow": obj.get("referring_domains_nofollow"),
            "referring_main_domains": obj.get("referring_main_domains"),
            "referring_main_domains_nofollow": obj.get("referring_main_domains_nofollow"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj