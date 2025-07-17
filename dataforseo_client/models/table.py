from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class Table(BaseModel):
    """
    Table
    """ # noqa: E501
    table_element: Optional[StrictStr] = Field(default=None, description="name assigned to the table element. possible values:. table_element")
    table_header: Optional[List[Optional[StrictStr]]] = Field(default=None, description="column names")
    table_content: Optional[List[Optional[List[Optional[StrictStr]]]]] = Field(default=None, description="the content of the table. one line of the table in this element of the array")
    __properties: ClassVar[List[str]] = [
        "table_element", 
        "table_header", 
        "table_content", 
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

        _dict['table_element'] = self.table_element
        _dict['table_header'] = self.table_header
        _dict['table_content'] = self.table_content
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "table_element": obj.get("table_element"),
            "table_header": obj.get("table_header"),
            "table_content": obj.get("table_content"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj