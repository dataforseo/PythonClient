from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.app_store_info_organic import AppStoreInfoOrganic



class AppDataAppleAppListingsSearchLiveItem(BaseModel):
    """
    AppDataAppleAppListingsSearchLiveItem
    """ # noqa: E501
    app_id: Optional[StrictStr] = Field(default=None, description="ID of the returned app")
    se_domain: Optional[StrictStr] = Field(default=None, description="search engine domain in a POST array")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    check_url: Optional[StrictStr] = Field(default=None, description="direct URL to search engine results. you can use it to make sure that we provided accurate results")
    time_update: Optional[StrictStr] = Field(default=None, description="date and time when SERP data was last updated. in the ISO 8601 format: “YYYY-MM-DDThh:mm:ss.sssssssZ”. example:. 2023-05-23 10:16:19 +00:00")
    item: Optional[AppStoreInfoOrganic] = Field(default=None, description="detailed information about the app")
    __properties: ClassVar[List[str]] = [
        "app_id", 
        "se_domain", 
        "location_code", 
        "language_code", 
        "check_url", 
        "time_update", 
        "item", 
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

        _dict['app_id'] = self.app_id
        _dict['se_domain'] = self.se_domain
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        _dict['check_url'] = self.check_url
        _dict['time_update'] = self.time_update
        _dict['item'] = self.item.to_dict() if self.item else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "app_id": obj.get("app_id"),
            "se_domain": obj.get("se_domain"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "check_url": obj.get("check_url"),
            "time_update": obj.get("time_update"),
            "item": AppStoreInfoOrganic.from_dict(obj["item"]) if obj.get("item") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj