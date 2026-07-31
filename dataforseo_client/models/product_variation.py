from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ProductVariation(BaseModel):
    """
    ProductVariation
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    product_id: Optional[StrictStr] = Field(default=None, description=r"*product ID in a POST array*. learn more about the parameter in [this help center guide](https://dataforseo.com/help-center/product-id-google-shopping)")
    gid: Optional[StrictStr] = Field(default=None, description=r"*GID ID in a POST array*. learn more about the parameter in [this help center guide](https://dataforseo.com/help-center/whats-a-gid-in-google-shopping-api)")
    data_docid: Optional[StrictStr] = Field(default=None, description=r"*unique identifier of the SERP data element in the POST array*")
    pvf: Optional[StrictStr] = Field(default=None, description=r"*product variation filter*. used in the product variation URL as the identifier of the specific product variation")
    title: Optional[StrictStr] = Field(default=None, description=r"*name of the product seller*")
    url: Optional[StrictStr] = Field(default=None, description=r"*product variation URL on Google Shopping*")
    variation_category: Optional[StrictStr] = Field(default=None, description=r"*category of the product variation*. example: `'Storage Capacity'`")
    __properties: ClassVar[List[str]] = [
        "type", 
        "product_id", 
        "gid", 
        "data_docid", 
        "pvf", 
        "title", 
        "url", 
        "variation_category", 
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
        _dict['product_id'] = self.product_id
        _dict['gid'] = self.gid
        _dict['data_docid'] = self.data_docid
        _dict['pvf'] = self.pvf
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['variation_category'] = self.variation_category
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "product_id": obj.get("product_id"),
            "gid": obj.get("gid"),
            "data_docid": obj.get("data_docid"),
            "pvf": obj.get("pvf"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "variation_category": obj.get("variation_category"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj