from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SslInfo(BaseModel):
    """
    SslInfo
    """ # noqa: E501
    valid_certificate: Optional[StrictBool] = Field(default=None, description="ssl certificate validity. indicates whether the ssl certificate detected on a website is not expired, suspended, revoked or invalid")
    certificate_issuer: Optional[StrictStr] = Field(default=None, description="ssl certificate authority. the entity that issued the detected ssl certificate")
    certificate_subject: Optional[StrictStr] = Field(default=None, description="ssl certificate subject. the entity associated with the public key")
    certificate_version: Optional[StrictInt] = Field(default=None, description="ssl certificate version. indicates the version of X.509 used by an ssl certificate")
    certificate_hash: Optional[StrictStr] = Field(default=None, description="ssl certificate hash. the version of the ssl certificate’s hash function")
    certificate_expiration_date: Optional[StrictStr] = Field(default=None, description="ssl certificate expiration date. the date and time when the ssl certificate expires. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    __properties: ClassVar[List[str]] = [
        "valid_certificate", 
        "certificate_issuer", 
        "certificate_subject", 
        "certificate_version", 
        "certificate_hash", 
        "certificate_expiration_date", 
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

        _dict['valid_certificate'] = self.valid_certificate
        _dict['certificate_issuer'] = self.certificate_issuer
        _dict['certificate_subject'] = self.certificate_subject
        _dict['certificate_version'] = self.certificate_version
        _dict['certificate_hash'] = self.certificate_hash
        _dict['certificate_expiration_date'] = self.certificate_expiration_date
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "valid_certificate": obj.get("valid_certificate"),
            "certificate_issuer": obj.get("certificate_issuer"),
            "certificate_subject": obj.get("certificate_subject"),
            "certificate_version": obj.get("certificate_version"),
            "certificate_hash": obj.get("certificate_hash"),
            "certificate_expiration_date": obj.get("certificate_expiration_date"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj