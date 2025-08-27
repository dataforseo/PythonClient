from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self


from importlib import import_module
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dataforseo_client.models.product_information_product_information_details_item import ProductInformationProductInformationDetailsItem;
    from dataforseo_client.models.product_information_product_information_text_item import ProductInformationProductInformationTextItem;
    from dataforseo_client.models.product_information_product_information_extended_item import ProductInformationProductInformationExtendedItem;



class BaseMerchantAmazonProductInformationElementItem(BaseModel):
    """
    BaseMerchantAmazonProductInformationElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    section_name: Optional[StrictStr] = Field(default=None, description="name of the section related to product information specified in the contents")
    __properties: ClassVar[List[str]] = [
        "type", 
        "section_name", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'product_information_details_item': 'ProductInformationProductInformationDetailsItem',
        'product_information_text_item': 'ProductInformationProductInformationTextItem',
        'product_information_extended_item': 'ProductInformationProductInformationExtendedItem',
    }

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
        return _dict


    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None
    
    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[
        ProductInformationProductInformationDetailsItem, 
        ProductInformationProductInformationTextItem, 
        ProductInformationProductInformationExtendedItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'ProductInformationProductInformationDetailsItem':
            return import_module("dataforseo_client.models.product_information_product_information_details_item").ProductInformationProductInformationDetailsItem.from_dict(obj)
        if object_type == 'ProductInformationProductInformationTextItem':
            return import_module("dataforseo_client.models.product_information_product_information_text_item").ProductInformationProductInformationTextItem.from_dict(obj)
        if object_type == 'ProductInformationProductInformationExtendedItem':
            return import_module("dataforseo_client.models.product_information_product_information_extended_item").ProductInformationProductInformationExtendedItem.from_dict(obj)

        return None