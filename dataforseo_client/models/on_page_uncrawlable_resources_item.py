from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.uncrawlable_resources_meta import UncrawlableResourcesMeta



class OnPageUncrawlableResourcesItem(BaseModel):
    """
    OnPageUncrawlableResourcesItem
    """ # noqa: E501
    url: Optional[StrictStr] = Field(default=None, description=r"*URL of the uncrawlable resource*")
    reason: Optional[StrictStr] = Field(default=None, description=r"*reason the resource is uncrawlable*. can take the following values: `content_type_inconsistency`")
    status_code: Optional[StrictInt] = Field(default=None, description=r"*general status code*. you can find the full list of the response codes [here](/v3/appendix/errors). **Note:** we strongly recommend designing a necessary system for handling related exceptional or error conditions")
    fetch_time: Optional[StrictStr] = Field(default=None, description=r"*date and time when the resource was fetched*. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. `2026-03-09 18:20:32 +00:00`")
    meta: Optional[UncrawlableResourcesMeta] = Field(default=None, description=r"*metadata of the uncrawlable resource*")
    __properties: ClassVar[List[str]] = [
        "url", 
        "reason", 
        "status_code", 
        "fetch_time", 
        "meta", 
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

        _dict['url'] = self.url
        _dict['reason'] = self.reason
        _dict['status_code'] = self.status_code
        _dict['fetch_time'] = self.fetch_time
        _dict['meta'] = self.meta.to_dict() if self.meta else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "reason": obj.get("reason"),
            "status_code": obj.get("status_code"),
            "fetch_time": obj.get("fetch_time"),
            "meta": UncrawlableResourcesMeta.from_dict(obj["meta"]) if obj.get("meta") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj