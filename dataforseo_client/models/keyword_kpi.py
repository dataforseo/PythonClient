from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.keyword_kpi_item_info import KeywordKpiItemInfo



class KeywordKpi(BaseModel):
    """
    KeywordKpi
    """ # noqa: E501
    desktop: Optional[List[Optional[KeywordKpiItemInfo]]] = Field(default=None, description="keyword data aggregated for desktop devices. if there is no data, then the value is null")
    mobile: Optional[List[Optional[KeywordKpiItemInfo]]] = Field(default=None, description="keyword data aggregated for mobile devices. if there is no data, then the value is null")
    tablet: Optional[List[Optional[KeywordKpiItemInfo]]] = Field(default=None, description="keyword data aggregated for tablet devices. if there is no data, then the value is null")
    __properties: ClassVar[List[str]] = [
        "desktop", 
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
            "desktop": [KeywordKpiItemInfo.from_dict(_item) for _item in obj["desktop"]] if obj.get("desktop") is not None else None,
            "mobile": [KeywordKpiItemInfo.from_dict(_item) for _item in obj["mobile"]] if obj.get("mobile") is not None else None,
            "tablet": [KeywordKpiItemInfo.from_dict(_item) for _item in obj["tablet"]] if obj.get("tablet") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj