from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.backlinks_info import BacklinksInfo
from dataforseo_client.models.dataforseo_labs_metrics_info import DataforseoLabsMetricsInfo



class DataforseoLabsGoogleDomainWhoisOverviewLiveItem(BaseModel):
    """
    DataforseoLabsGoogleDomainWhoisOverviewLiveItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    domain: Optional[StrictStr] = Field(default=None, description="domain name")
    created_datetime: Optional[StrictStr] = Field(default=None, description="date and time of registration. date and time (in the ISO 8601 format) when the domain was first registered. example:. '1997-03-29 03:00:00 +00:00'")
    changed_datetime: Optional[StrictStr] = Field(default=None, description="date and time when the domain entry was changed. date and time (in the ISO 8601 format) when the domain entry was last modified. example:. '2021-01-14 08:36:28 +00:00'")
    expiration_datetime: Optional[StrictStr] = Field(default=None, description="date and time when the domain will expire. date and time (in the ISO 8601 format) when the domain is due to expire. example:. '2022-11-26 17:21:23 +00:00'")
    updated_datetime: Optional[StrictStr] = Field(default=None, description="date and time when the domain was updated. date and time (in the ISO 8601 format) when the domain was last updated. example:. '2021-01-29 13:59:38 +00:00'")
    first_seen: Optional[StrictStr] = Field(default=None, description="date and time when our crawler found the domain for the first time. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. '2019-11-15 12:57:46 +00:00'")
    epp_status_codes: Optional[List[Optional[StrictStr]]] = Field(default=None, description="extensive provisioning protocol status codes. the status of a domain name registration as defined by ICANN")
    tld: Optional[StrictStr] = Field(default=None, description="top-level domain. top-level domain in the DNS root zone")
    registered: Optional[StrictBool] = Field(default=None, description="domain registration status. if false, the domain name registration has expired. Note: expired domains will remain in the database for only a short period of time")
    registrar: Optional[StrictStr] = Field(default=None, description="domain registrar. if null, the domain registrar is unknown. example:. NameCheap, Inc.")
    metrics: Optional[Dict[str, Optional[DataforseoLabsMetricsInfo]]] = Field(default=None, description="ranking data relevant to the specified domain")
    backlinks_info: Optional[BacklinksInfo] = Field(default=None, description="backlink data for the returned domain")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "domain", 
        "created_datetime", 
        "changed_datetime", 
        "expiration_datetime", 
        "updated_datetime", 
        "first_seen", 
        "epp_status_codes", 
        "tld", 
        "registered", 
        "registrar", 
        "metrics", 
        "backlinks_info", 
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

        _dict['se_type'] = self.se_type
        _dict['domain'] = self.domain
        _dict['created_datetime'] = self.created_datetime
        _dict['changed_datetime'] = self.changed_datetime
        _dict['expiration_datetime'] = self.expiration_datetime
        _dict['updated_datetime'] = self.updated_datetime
        _dict['first_seen'] = self.first_seen
        _dict['epp_status_codes'] = self.epp_status_codes
        _dict['tld'] = self.tld
        _dict['registered'] = self.registered
        _dict['registrar'] = self.registrar
        _dict['metrics'] = self.metrics
        _dict['backlinks_info'] = self.backlinks_info.to_dict() if self.backlinks_info else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "domain": obj.get("domain"),
            "created_datetime": obj.get("created_datetime"),
            "changed_datetime": obj.get("changed_datetime"),
            "expiration_datetime": obj.get("expiration_datetime"),
            "updated_datetime": obj.get("updated_datetime"),
            "first_seen": obj.get("first_seen"),
            "epp_status_codes": obj.get("epp_status_codes"),
            "tld": obj.get("tld"),
            "registered": obj.get("registered"),
            "registrar": obj.get("registrar"),
            "metrics": obj.get("metrics"),
            "backlinks_info": BacklinksInfo.from_dict(obj["backlinks_info"]) if obj.get("backlinks_info") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj