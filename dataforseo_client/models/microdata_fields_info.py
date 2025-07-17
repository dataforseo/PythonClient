from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.message_info import MessageInfo



class MicrodataFieldsInfo(BaseModel):
    """
    MicrodataFieldsInfo
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="field name. name of the data field")
    types: Optional[List[Optional[StrictStr]]] = Field(default=None, description="list of microdata types")
    value: Optional[StrictStr] = Field(default=None, description="microdata value. microdata value specified on a target web page")
    test_results: Optional[MessageInfo] = Field(default=None, description="microdata validation test results. sub-type microdata test results that contain detected errors and related messages")
    fields: Optional[List[Optional[MicrodataFieldsInfo]]] = Field(default=None, description="microdata fields. an array of objects containing data fields related to the certain microdata type")
    __properties: ClassVar[List[str]] = [
        "name", 
        "types", 
        "value", 
        "test_results", 
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

        _dict['name'] = self.name
        _dict['types'] = self.types
        _dict['value'] = self.value
        _dict['test_results'] = self.test_results.to_dict() if self.test_results else None
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
            "name": obj.get("name"),
            "types": obj.get("types"),
            "value": obj.get("value"),
            "test_results": MessageInfo.from_dict(obj["test_results"]) if obj.get("test_results") is not None else None,
            "fields": [MicrodataFieldsInfo.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj