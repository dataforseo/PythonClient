from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BacklinksTimeseriesSummaryLiveItem(BaseModel):
    """
    BacklinksTimeseriesSummaryLiveItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    date: Optional[StrictStr] = Field(default=None, description="date and time when the data for the target was stored. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    rank: Optional[StrictInt] = Field(default=None, description="target rank for the given date. learn more about the metric and how it is calculated in this help center article")
    backlinks: Optional[StrictInt] = Field(default=None, description="number of backlinks for the given date")
    backlinks_nofollow: Optional[StrictInt] = Field(default=None, description="number of nofollow backlinks for the given date")
    referring_pages: Optional[StrictInt] = Field(default=None, description="number of pages pointing to target for the given date")
    referring_pages_nofollow: Optional[StrictInt] = Field(default=None, description="number of referring pages pointing at least one nofollow link to the target for the given date")
    referring_domains: Optional[StrictInt] = Field(default=None, description="number of referring domains for the given date. referring domains include subdomains that are counted as separate domains for this metric")
    referring_domains_nofollow: Optional[StrictInt] = Field(default=None, description="number of domains pointing at least one nofollow link to the target for the given date")
    referring_main_domains: Optional[StrictInt] = Field(default=None, description="number of referring main domains for the given date")
    referring_main_domains_nofollow: Optional[StrictInt] = Field(default=None, description="number of main domains pointing at least one nofollow link to the target for the given date")
    referring_ips: Optional[StrictInt] = Field(default=None, description="number of referring IP addresses for the given date. number of IP addresses pointing to this page")
    referring_subnets: Optional[StrictInt] = Field(default=None, description="number of referring subnetworks for the given date")
    __properties: ClassVar[List[str]] = [
        "type", 
        "date", 
        "rank", 
        "backlinks", 
        "backlinks_nofollow", 
        "referring_pages", 
        "referring_pages_nofollow", 
        "referring_domains", 
        "referring_domains_nofollow", 
        "referring_main_domains", 
        "referring_main_domains_nofollow", 
        "referring_ips", 
        "referring_subnets", 
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
        _dict['date'] = self.date
        _dict['rank'] = self.rank
        _dict['backlinks'] = self.backlinks
        _dict['backlinks_nofollow'] = self.backlinks_nofollow
        _dict['referring_pages'] = self.referring_pages
        _dict['referring_pages_nofollow'] = self.referring_pages_nofollow
        _dict['referring_domains'] = self.referring_domains
        _dict['referring_domains_nofollow'] = self.referring_domains_nofollow
        _dict['referring_main_domains'] = self.referring_main_domains
        _dict['referring_main_domains_nofollow'] = self.referring_main_domains_nofollow
        _dict['referring_ips'] = self.referring_ips
        _dict['referring_subnets'] = self.referring_subnets
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "date": obj.get("date"),
            "rank": obj.get("rank"),
            "backlinks": obj.get("backlinks"),
            "backlinks_nofollow": obj.get("backlinks_nofollow"),
            "referring_pages": obj.get("referring_pages"),
            "referring_pages_nofollow": obj.get("referring_pages_nofollow"),
            "referring_domains": obj.get("referring_domains"),
            "referring_domains_nofollow": obj.get("referring_domains_nofollow"),
            "referring_main_domains": obj.get("referring_main_domains"),
            "referring_main_domains_nofollow": obj.get("referring_main_domains_nofollow"),
            "referring_ips": obj.get("referring_ips"),
            "referring_subnets": obj.get("referring_subnets"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj