from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsCategoriesResultInfo(BaseModel):
    """
    DataforseoLabsCategoriesResultInfo
    """ # noqa: E501
    category_code: Optional[StrictInt] = Field(default=None, description="category code")
    category_name: Optional[StrictStr] = Field(default=None, description="full name of the category")
    category_code_parent: Optional[StrictInt] = Field(default=None, description="the code of the superordinate category. example:. 'category_code': 10178,. 'category_name': 'Apparel Accessories',. 'category_code_parent': 10021. where category_code_parent. corresponds to:. 'category_code': 10021,. 'category_name': 'Apparel'. 'category_code_parent': null")
    __properties: ClassVar[List[str]] = [
        "category_code", 
        "category_name", 
        "category_code_parent", 
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

        _dict['category_code'] = self.category_code
        _dict['category_name'] = self.category_name
        _dict['category_code_parent'] = self.category_code_parent
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "category_code": obj.get("category_code"),
            "category_name": obj.get("category_name"),
            "category_code_parent": obj.get("category_code_parent"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj