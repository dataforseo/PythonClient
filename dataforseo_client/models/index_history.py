from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class IndexHistory(BaseModel):
    """
    IndexHistory
    """ # noqa: E501
    date: Optional[StrictStr] = Field(default=None, description="date for which index volume data is provided. in the UTC format: “yyyy-mm-dd”. example:. 2021-10-01")
    total_backlinks: Optional[StrictInt] = Field(default=None, description="total number of backlinks our database contained on the given date")
    total_pages: Optional[StrictInt] = Field(default=None, description="total number of pages our database contained on the given date")
    __properties: ClassVar[List[str]] = [
        "date", 
        "total_backlinks", 
        "total_pages", 
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

        _dict['date'] = self.date
        _dict['total_backlinks'] = self.total_backlinks
        _dict['total_pages'] = self.total_pages
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "total_backlinks": obj.get("total_backlinks"),
            "total_pages": obj.get("total_pages"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj