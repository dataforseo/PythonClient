from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.index_history import IndexHistory



class BacklinksIndexResultInfo(BaseModel):
    """
    BacklinksIndexResultInfo
    """ # noqa: E501
    total_backlinks: Optional[StrictInt] = Field(default=None, description="total number of backlinks our database contains for the moment of checking")
    total_pages: Optional[StrictInt] = Field(default=None, description="total number of pages our database contains for the moment of checking")
    index_history: Optional[List[Optional[IndexHistory]]] = Field(default=None, description="index volume data for the past 12 months")
    __properties: ClassVar[List[str]] = [
        "total_backlinks", 
        "total_pages", 
        "index_history", 
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

        _dict['total_backlinks'] = self.total_backlinks
        _dict['total_pages'] = self.total_pages
        index_history_items = []
        if self.index_history:
            for _item in self.index_history:
                if _item:
                    index_history_items.append(_item.to_dict())
            _dict['index_history'] = index_history_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "total_backlinks": obj.get("total_backlinks"),
            "total_pages": obj.get("total_pages"),
            "index_history": [IndexHistory.from_dict(_item) for _item in obj["index_history"]] if obj.get("index_history") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj