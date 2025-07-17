from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.trustpilot_search_organic import TrustpilotSearchOrganic



class BusinessDataTrustpilotSearchTaskGetResultInfo(BaseModel):
    """
    BusinessDataTrustpilotSearchTaskGetResultInfo
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword in a POST array")
    se_domain: Optional[StrictStr] = Field(default=None, description="search engine domain in a POST array")
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to search engine results. you can use it to make sure that we provided accurate results")
    datetime: Optional[StrictStr] = Field(default=None, description="date and time when the result was received. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    items_count: Optional[StrictInt] = Field(default=None, description="the number of items in the results array. you can get more results by using the depth parameter when setting a task")
    items: Optional[List[Optional[TrustpilotSearchOrganic]]] = Field(default=None, description="found reviews. you can get more results by using the depth parameter when setting a task")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "se_domain", 
        "check_url", 
        "datetime", 
        "items_count", 
        "items", 
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

        _dict['keyword'] = self.keyword
        _dict['se_domain'] = self.se_domain
        _dict['check_url'] = self.check_url
        _dict['datetime'] = self.datetime
        _dict['items_count'] = self.items_count
        items_items = []
        if self.items:
            for _item in self.items:
                if _item:
                    items_items.append(_item.to_dict())
            _dict['items'] = items_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "se_domain": obj.get("se_domain"),
            "check_url": obj.get("check_url"),
            "datetime": obj.get("datetime"),
            "items_count": obj.get("items_count"),
            "items": [TrustpilotSearchOrganic.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj