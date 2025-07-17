from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class OnPageResourceIssueItemInfo(BaseModel):
    """
    OnPageResourceIssueItemInfo
    """ # noqa: E501
    line: Optional[StrictInt] = Field(default=None, description="line where the error was found")
    column: Optional[StrictInt] = Field(default=None, description="column where the error was found")
    message: Optional[StrictStr] = Field(default=None, description="text message of the error. the full list of possible HTML errors can be found here")
    status_code: Optional[StrictInt] = Field(default=None, description="status code of the error. possible values:. 0 — Unidentified Error;. 501 — Html Parse Error;. 1501 — JS Parse Error;. 2501 — CSS Parse Error;. 3501 — Image Parse Error;. 3502 — Image Scale Is Zero;. 3503 — Image Size Is Zero;. 3504 — Image Format Invalid")
    __properties: ClassVar[List[str]] = [
        "line", 
        "column", 
        "message", 
        "status_code", 
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

        _dict['line'] = self.line
        _dict['column'] = self.column
        _dict['message'] = self.message
        _dict['status_code'] = self.status_code
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "line": obj.get("line"),
            "column": obj.get("column"),
            "message": obj.get("message"),
            "status_code": obj.get("status_code"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj