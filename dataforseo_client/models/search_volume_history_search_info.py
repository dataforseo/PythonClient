from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.search_volume_history_item_info import SearchVolumeHistoryItemInfo



class SearchVolumeHistorySearchInfo(BaseModel):
    """
    SearchVolumeHistorySearchInfo
    """ # noqa: E501
    desktop: Optional[List[Optional[SearchVolumeHistoryItemInfo]]] = Field(default=None, description="device type = desktop. contains historical search volume data for searches made from desktop devices")
    non_smartphones: Optional[List[Optional[SearchVolumeHistoryItemInfo]]] = Field(default=None, description="device type = non-smartphones. contains historical search volume data for searches made from feature phones (non-smartphone mobile devices)")
    mobile: Optional[List[Optional[SearchVolumeHistoryItemInfo]]] = Field(default=None, description="device type = mobile. contains historical search volume data for searches made from mobile devices")
    tablet: Optional[List[Optional[SearchVolumeHistoryItemInfo]]] = Field(default=None, description="device type = tablet. contains historical search volume data for searches made from tablets")
    __properties: ClassVar[List[str]] = [
        "desktop", 
        "non_smartphones", 
        "mobile", 
        "tablet", 
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

        desktop_items = []
        if self.desktop:
            for _item in self.desktop:
                if _item:
                    desktop_items.append(_item.to_dict())
            _dict['desktop'] = desktop_items
        non_smartphones_items = []
        if self.non_smartphones:
            for _item in self.non_smartphones:
                if _item:
                    non_smartphones_items.append(_item.to_dict())
            _dict['non_smartphones'] = non_smartphones_items
        mobile_items = []
        if self.mobile:
            for _item in self.mobile:
                if _item:
                    mobile_items.append(_item.to_dict())
            _dict['mobile'] = mobile_items
        tablet_items = []
        if self.tablet:
            for _item in self.tablet:
                if _item:
                    tablet_items.append(_item.to_dict())
            _dict['tablet'] = tablet_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "desktop": [SearchVolumeHistoryItemInfo.from_dict(_item) for _item in obj["desktop"]] if obj.get("desktop") is not None else None,
            "non_smartphones": [SearchVolumeHistoryItemInfo.from_dict(_item) for _item in obj["non_smartphones"]] if obj.get("non_smartphones") is not None else None,
            "mobile": [SearchVolumeHistoryItemInfo.from_dict(_item) for _item in obj["mobile"]] if obj.get("mobile") is not None else None,
            "tablet": [SearchVolumeHistoryItemInfo.from_dict(_item) for _item in obj["tablet"]] if obj.get("tablet") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj