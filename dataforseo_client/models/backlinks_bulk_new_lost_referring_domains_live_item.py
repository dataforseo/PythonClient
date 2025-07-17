from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BacklinksBulkNewLostReferringDomainsLiveItem(BaseModel):
    """
    BacklinksBulkNewLostReferringDomainsLiveItem
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="domain, subdomain or webpage from a POST array")
    new_referring_domains: Optional[StrictInt] = Field(default=None, description="number of new referring domains. number of new referring domains pointing to the target")
    lost_referring_domains: Optional[StrictInt] = Field(default=None, description="number of lost referring domains. number of lost referring domains of the target")
    new_referring_main_domains: Optional[StrictInt] = Field(default=None, description="number of new referring main domains pointing to the target")
    lost_referring_main_domains: Optional[StrictInt] = Field(default=None, description="number of lost referring main domains pointing to the target")
    __properties: ClassVar[List[str]] = [
        "target", 
        "new_referring_domains", 
        "lost_referring_domains", 
        "new_referring_main_domains", 
        "lost_referring_main_domains", 
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
        _dict['new_referring_domains'] = self.new_referring_domains
        _dict['lost_referring_domains'] = self.lost_referring_domains
        _dict['new_referring_main_domains'] = self.new_referring_main_domains
        _dict['lost_referring_main_domains'] = self.lost_referring_main_domains
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "target": obj.get("target"),
            "new_referring_domains": obj.get("new_referring_domains"),
            "lost_referring_domains": obj.get("lost_referring_domains"),
            "new_referring_main_domains": obj.get("new_referring_main_domains"),
            "lost_referring_main_domains": obj.get("lost_referring_main_domains"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj