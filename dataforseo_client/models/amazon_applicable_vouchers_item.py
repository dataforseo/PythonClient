from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class AmazonApplicableVouchersItem(BaseModel):
    """
    AmazonApplicableVouchersItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    text: Optional[StrictStr] = Field(default=None, description="text of the voucher")
    fixed_discount: Optional[StrictFloat] = Field(default=None, description="value of the fixed discount")
    fixed_discount_currency: Optional[StrictStr] = Field(default=None, description="currency code of the fixed discount")
    percentage_discount: Optional[StrictFloat] = Field(default=None, description="value of the percentage discount. if the discount is fixed, the value will be null")
    important_details: Optional[StrictStr] = Field(default=None, description="important details about the terms of discount vouchers")
    __properties: ClassVar[List[str]] = [
        "type", 
        "text", 
        "fixed_discount", 
        "fixed_discount_currency", 
        "percentage_discount", 
        "important_details", 
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
        _dict['text'] = self.text
        _dict['fixed_discount'] = self.fixed_discount
        _dict['fixed_discount_currency'] = self.fixed_discount_currency
        _dict['percentage_discount'] = self.percentage_discount
        _dict['important_details'] = self.important_details
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "text": obj.get("text"),
            "fixed_discount": obj.get("fixed_discount"),
            "fixed_discount_currency": obj.get("fixed_discount_currency"),
            "percentage_discount": obj.get("percentage_discount"),
            "important_details": obj.get("important_details"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj