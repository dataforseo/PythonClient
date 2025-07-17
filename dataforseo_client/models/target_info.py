from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class TargetInfo(BaseModel):
    """
    TargetInfo
    """ # noqa: E501
    server: Optional[StrictStr] = Field(default=None, description="server")
    cms: Optional[StrictStr] = Field(default=None, description="content management system")
    platform_type: Optional[List[Optional[StrictStr]]] = Field(default=None, description="platform type")
    ip_address: Optional[StrictStr] = Field(default=None, description="IP address of the target")
    country: Optional[StrictStr] = Field(default=None, description="country code that the target domain is determined to belong to")
    is_ip: Optional[StrictBool] = Field(default=None, description="indicates if the target is IP. if true, the domain, subdomain or webpage functions as an IP address and does not have a domain name")
    target_spam_score: Optional[StrictInt] = Field(default=None, description="spam score of the target. if the target is a domain/subdomain, this fields indicates the average spam score of all pages of that domain/subdomain;. learn more about how the metric is calculated on this help center page")
    __properties: ClassVar[List[str]] = [
        "server", 
        "cms", 
        "platform_type", 
        "ip_address", 
        "country", 
        "is_ip", 
        "target_spam_score", 
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

        _dict['server'] = self.server
        _dict['cms'] = self.cms
        _dict['platform_type'] = self.platform_type
        _dict['ip_address'] = self.ip_address
        _dict['country'] = self.country
        _dict['is_ip'] = self.is_ip
        _dict['target_spam_score'] = self.target_spam_score
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "server": obj.get("server"),
            "cms": obj.get("cms"),
            "platform_type": obj.get("platform_type"),
            "ip_address": obj.get("ip_address"),
            "country": obj.get("country"),
            "is_ip": obj.get("is_ip"),
            "target_spam_score": obj.get("target_spam_score"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj