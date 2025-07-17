from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AvgBacklinksInfo(BaseModel):
    """
    AvgBacklinksInfo
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    backlinks: Optional[StrictFloat] = Field(default=None, description="average number of backlinks")
    dofollow: Optional[StrictFloat] = Field(default=None, description="average number of dofollow links")
    referring_pages: Optional[StrictFloat] = Field(default=None, description="average number of referring pages")
    referring_domains: Optional[StrictFloat] = Field(default=None, description="average number of referring domains")
    referring_main_domains: Optional[StrictFloat] = Field(default=None, description="average number of referring main domains")
    rank: Optional[StrictFloat] = Field(default=None, description="average rank. learn more about the metric and its calculation formula in this help center article")
    main_domain_rank: Optional[StrictFloat] = Field(default=None, description="average main domain rank. learn more about the metric and its calculation formula in this help center article")
    last_updated_time: Optional[StrictStr] = Field(default=None, description="date and time when the dataset was updated. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "backlinks", 
        "dofollow", 
        "referring_pages", 
        "referring_domains", 
        "referring_main_domains", 
        "rank", 
        "main_domain_rank", 
        "last_updated_time", 
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
        _dict['backlinks'] = self.backlinks
        _dict['dofollow'] = self.dofollow
        _dict['referring_pages'] = self.referring_pages
        _dict['referring_domains'] = self.referring_domains
        _dict['referring_main_domains'] = self.referring_main_domains
        _dict['rank'] = self.rank
        _dict['main_domain_rank'] = self.main_domain_rank
        _dict['last_updated_time'] = self.last_updated_time
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "backlinks": obj.get("backlinks"),
            "dofollow": obj.get("dofollow"),
            "referring_pages": obj.get("referring_pages"),
            "referring_domains": obj.get("referring_domains"),
            "referring_main_domains": obj.get("referring_main_domains"),
            "rank": obj.get("rank"),
            "main_domain_rank": obj.get("main_domain_rank"),
            "last_updated_time": obj.get("last_updated_time"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj