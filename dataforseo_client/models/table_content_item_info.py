from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.row_cell_info import RowCellInfo



class TableContentItemInfo(BaseModel):
    """
    TableContentItemInfo
    """ # noqa: E501
    row_cells: Optional[List[Optional[RowCellInfo]]] = Field(default=None, description="content of the row cells of the header")
    __properties: ClassVar[List[str]] = [
        "row_cells", 
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

        row_cells_items = []
        if self.row_cells:
            for _item in self.row_cells:
                if _item:
                    row_cells_items.append(_item.to_dict())
            _dict['row_cells'] = row_cells_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "row_cells": [RowCellInfo.from_dict(_item) for _item in obj["row_cells"]] if obj.get("row_cells") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj