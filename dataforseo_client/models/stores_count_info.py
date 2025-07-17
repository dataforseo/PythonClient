from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class StoresCountInfo(BaseModel):
    """
    StoresCountInfo
    """ # noqa: E501
    count: Optional[StrictInt] = Field(default=None, description="number of stores that offer the product")
    displayed_text: Optional[StrictStr] = Field(default=None, description="text displayed on the Google Shopping page")
    count_from_text: Optional[StrictBool] = Field(default=None, description="whether the number of stores is taken from text. indicates whether the number of stores is taken from displayed_text;. if the API finds the exact number of stores in the HTML code of the Google Shopping page, this parameter is false;. if the API cannot find the number of stores in the HTML code of the page, it takes the number from the displayed_text;. in this case, the parameter is true")
    __properties: ClassVar[List[str]] = [
        "count", 
        "displayed_text", 
        "count_from_text", 
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

        _dict['count'] = self.count
        _dict['displayed_text'] = self.displayed_text
        _dict['count_from_text'] = self.count_from_text
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "count": obj.get("count"),
            "displayed_text": obj.get("displayed_text"),
            "count_from_text": obj.get("count_from_text"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj