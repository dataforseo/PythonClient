from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.on_page_resource_issue_item_info import OnPageResourceIssueItemInfo



class OnPageResourceIssueInfo(BaseModel):
    """
    OnPageResourceIssueInfo
    """ # noqa: E501
    errors: Optional[List[Optional[OnPageResourceIssueItemInfo]]] = Field(default=None, description="resource errors")
    warnings: Optional[List[Optional[OnPageResourceIssueItemInfo]]] = Field(default=None, description="resource warnings")
    __properties: ClassVar[List[str]] = [
        "errors", 
        "warnings", 
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

        errors_items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    errors_items.append(_item.to_dict())
            _dict['errors'] = errors_items
        warnings_items = []
        if self.warnings:
            for _item in self.warnings:
                if _item:
                    warnings_items.append(_item.to_dict())
            _dict['warnings'] = warnings_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "errors": [OnPageResourceIssueItemInfo.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None,
            "warnings": [OnPageResourceIssueItemInfo.from_dict(_item) for _item in obj["warnings"]] if obj.get("warnings") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj