from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class BacklinksInfo(BaseModel):
    """
    BacklinksInfo
    """ # noqa: E501
    referring_domains: Optional[StrictInt] = Field(default=None, description="number of referring domains")
    referring_main_domains: Optional[StrictInt] = Field(default=None, description="number of referring main domains")
    referring_pages: Optional[StrictInt] = Field(default=None, description="number of referring pages")
    dofollow: Optional[StrictInt] = Field(default=None, description="number of dofollow links")
    backlinks: Optional[StrictInt] = Field(default=None, description="total number of backlinks. the total number of backlinks, including dofollow and nofollow links")
    time_update: Optional[StrictStr] = Field(default=None, description="date and time when backlink data was updated. in the UTC format: 'yyyy-mm-dd hh-mm-ss +00:00'. example:. 2019-11-15 12:57:46 +00:00")
    __properties: ClassVar[List[str]] = [
        "referring_domains", 
        "referring_main_domains", 
        "referring_pages", 
        "dofollow", 
        "backlinks", 
        "time_update", 
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

        _dict['referring_domains'] = self.referring_domains
        _dict['referring_main_domains'] = self.referring_main_domains
        _dict['referring_pages'] = self.referring_pages
        _dict['dofollow'] = self.dofollow
        _dict['backlinks'] = self.backlinks
        _dict['time_update'] = self.time_update
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "referring_domains": obj.get("referring_domains"),
            "referring_main_domains": obj.get("referring_main_domains"),
            "referring_pages": obj.get("referring_pages"),
            "dofollow": obj.get("dofollow"),
            "backlinks": obj.get("backlinks"),
            "time_update": obj.get("time_update"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj