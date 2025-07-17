from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.local_business_delivery_service_info import LocalBusinessDeliveryServiceInfo
from dataforseo_client.models.base_local_business_link import BaseLocalBusinessLink



class LocalBusinessOrderLink(BaseLocalBusinessLink):
    """
    LocalBusinessOrderLink
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    delivery_services: Optional[List[Optional[LocalBusinessDeliveryServiceInfo]]] = Field(default=None, description="lists available delivery services")
    __properties: ClassVar[List[str]] = [
        "type", 
        "delivery_services", 
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
        delivery_services_items = []
        if self.delivery_services:
            for _item in self.delivery_services:
                if _item:
                    delivery_services_items.append(_item.to_dict())
            _dict['delivery_services'] = delivery_services_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "delivery_services": [LocalBusinessDeliveryServiceInfo.from_dict(_item) for _item in obj["delivery_services"]] if obj.get("delivery_services") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj