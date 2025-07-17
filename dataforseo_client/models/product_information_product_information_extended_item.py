from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.product_information_rows import ProductInformationRows
from dataforseo_client.models.base_merchant_amazon_product_information_element_item import BaseMerchantAmazonProductInformationElementItem



class ProductInformationProductInformationExtendedItem(BaseMerchantAmazonProductInformationElementItem):
    """
    ProductInformationProductInformationExtendedItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    section_name: Optional[StrictStr] = Field(default=None, description="name of the section related to product information specified in the contents")
    contents: Optional[List[Optional[ProductInformationRows]]] = Field(default=None, description="contains information specified about the product within the section_name")
    __properties: ClassVar[List[str]] = [
        "type", 
        "section_name", 
        "contents", 
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
        _dict['section_name'] = self.section_name
        contents_items = []
        if self.contents:
            for _item in self.contents:
                if _item:
                    contents_items.append(_item.to_dict())
            _dict['contents'] = contents_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "section_name": obj.get("section_name"),
            "contents": [ProductInformationRows.from_dict(_item) for _item in obj["contents"]] if obj.get("contents") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj