from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ProductIdentifiers(BaseModel):
    """
    ProductIdentifiers
    """ # noqa: E501
    product_id: Optional[StrictStr] = Field(default=None, description=r"*unique product identifier on Google Shopping*. example:. `4485466949985702538`. learn more about the parameter in [this help center guide](https://dataforseo.com/help-center/product-id-google-shopping)")
    data_docid: Optional[StrictStr] = Field(default=None, description=r"*unique identifier of the SERP data element*. example:. `17363035694596624076`")
    gid: Optional[StrictStr] = Field(default=None, description=r"*global product identifier on Google Shopping*. example:. `4702526954592161872`. learn more about the parameter in [this help center guide](https://dataforseo.com/help-center/whats-a-gid-in-google-shopping-api)")
    __properties: ClassVar[List[str]] = [
        "product_id", 
        "data_docid", 
        "gid", 
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

        _dict['product_id'] = self.product_id
        _dict['data_docid'] = self.data_docid
        _dict['gid'] = self.gid
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "product_id": obj.get("product_id"),
            "data_docid": obj.get("data_docid"),
            "gid": obj.get("gid"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj