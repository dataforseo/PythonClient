from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ShoppingSpecification(BaseModel):
    """
    ShoppingSpecification
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank on the product specification page. absolute position among all the elements found on the product specification page")
    position: Optional[StrictStr] = Field(default=None, description="alignment of the element on the product specification page. can take the following values:. right")
    xpath: Optional[StrictStr] = Field(default=None, description="XPath of the element")
    block_name: Optional[StrictStr] = Field(default=None, description="name of the block of product attributes. indicates the name of the product specification section in which the related element is listed")
    specification_name: Optional[StrictStr] = Field(default=None, description="product attribute. attribute name of the product data specification")
    specification_value: Optional[StrictStr] = Field(default=None, description="content of the specification")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "block_name", 
        "specification_name", 
        "specification_value", 
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

        _dict['type'] = self.type
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
        _dict['block_name'] = self.block_name
        _dict['specification_name'] = self.specification_name
        _dict['specification_value'] = self.specification_value
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "block_name": obj.get("block_name"),
            "specification_name": obj.get("specification_name"),
            "specification_value": obj.get("specification_value"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj