from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.microdata_fields_info import MicrodataFieldsInfo



class MicrodataInspectionInfo(BaseModel):
    """
    MicrodataInspectionInfo
    """ # noqa: E501
    types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="parent microdata types. for a full list of available types, please visit schema.org")
    fields: Optional[List[Optional[MicrodataFieldsInfo]]] = Field(default=None, description="microdata fields. an array of objects containing data fields related to the certain microdata type")
    __properties: ClassVar[List[str]] = [
        "types", 
        "fields", 
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

        _dict['types'] = self.types
        fields_items = []
        if self.fields:
            for _item in self.fields:
                if _item:
                    fields_items.append(_item.to_dict())
            _dict['fields'] = fields_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "types": obj.get("types"),
            "fields": [MicrodataFieldsInfo.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj