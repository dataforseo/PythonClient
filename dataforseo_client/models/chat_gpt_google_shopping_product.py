from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class ChatGptGoogleShoppingProduct(BaseModel):
    """
    ChatGptGoogleShoppingProduct
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    ei: Optional[StrictStr] = Field(default=None, description=r"event identifier. internal event identifier used by Google")
    product_id: Optional[StrictStr] = Field(default=None, description=r"product identifier. can be used as a data_docid in Google Shopping API endpoints")
    catalog_id: Optional[StrictStr] = Field(default=None, description=r"Google Shopping catalog identifier of the product. can be used as a product_id in Google Shopping API endpoints")
    gpcid: Optional[StrictStr] = Field(default=None, description=r"Google product cluster identifier. can be used as a gid in Google Shopping API endpoints")
    headline_offer_docid: Optional[StrictStr] = Field(default=None, description=r"document identifier of the main offer in the headline. can be used as a data_docid in Google Shopping API endpoints")
    image_docid: Optional[StrictStr] = Field(default=None, description=r"identifier for the displayed product’s image")
    rds: Optional[StrictStr] = Field(default=None, description=r"resource descriptor string . internal Google resource descriptor string that identifies the product within Google’s Shopping index")
    query: Optional[StrictStr] = Field(default=None, description=r"search query. search query used by ChatGPT to retrieve the product from Google Shopping")
    mid: Optional[StrictStr] = Field(default=None, description=r"merchant identifier. identifier of the seller or merchant account in Google Shopping")
    pvt: Optional[StrictStr] = Field(default=None, description=r"product view type. internal Google parameter that specifies the product view type used when rendering the product item")
    uule: Optional[StrictStr] = Field(default=None, description=r"encoded location parameter. indicates the location for a search")
    gl: Optional[StrictStr] = Field(default=None, description=r"country code. indicates the location for which search results are displayed")
    hl: Optional[StrictStr] = Field(default=None, description=r"host language code. indicates the language in which search results are displayed")
    __properties: ClassVar[List[str]] = [
        "type", 
        "ei", 
        "product_id", 
        "catalog_id", 
        "gpcid", 
        "headline_offer_docid", 
        "image_docid", 
        "rds", 
        "query", 
        "mid", 
        "pvt", 
        "uule", 
        "gl", 
        "hl", 
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
        _dict['ei'] = self.ei
        _dict['product_id'] = self.product_id
        _dict['catalog_id'] = self.catalog_id
        _dict['gpcid'] = self.gpcid
        _dict['headline_offer_docid'] = self.headline_offer_docid
        _dict['image_docid'] = self.image_docid
        _dict['rds'] = self.rds
        _dict['query'] = self.query
        _dict['mid'] = self.mid
        _dict['pvt'] = self.pvt
        _dict['uule'] = self.uule
        _dict['gl'] = self.gl
        _dict['hl'] = self.hl
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "ei": obj.get("ei"),
            "product_id": obj.get("product_id"),
            "catalog_id": obj.get("catalog_id"),
            "gpcid": obj.get("gpcid"),
            "headline_offer_docid": obj.get("headline_offer_docid"),
            "image_docid": obj.get("image_docid"),
            "rds": obj.get("rds"),
            "query": obj.get("query"),
            "mid": obj.get("mid"),
            "pvt": obj.get("pvt"),
            "uule": obj.get("uule"),
            "gl": obj.get("gl"),
            "hl": obj.get("hl"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj