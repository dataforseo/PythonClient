# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.ai_overview_reference import AiOverviewReference
from dataforseo_client.models.images_element import ImagesElement
from typing import Optional, Set
from typing_extensions import Self

class AiOverviewElement(BaseModel):
    """
    AiOverviewElement
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    title: Optional[StrictStr] = Field(default=None, description="title of a given link element")
    text: Optional[StrictStr] = Field(default=None, description="reference text text snippet from the page that was used to generate the ai_overview_element")
    images: Optional[List[ImagesElement]] = Field(default=None, description="images of the element if there are none, equals null")
    references: Optional[List[AiOverviewReference]] = Field(default=None, description="references relevant to the element includes references to webpages that were used to generate the ai_overview_element")
    __properties: ClassVar[List[str]] = ["type", "title", "text", "images", "references"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AiOverviewElement from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item in self.images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in references (list)
        _items = []
        if self.references:
            for _item in self.references:
                if _item:
                    _items.append(_item.to_dict())
            _dict['references'] = _items
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if text (nullable) is None
        # and model_fields_set contains the field
        if self.text is None and "text" in self.model_fields_set:
            _dict['text'] = None

        # set to None if images (nullable) is None
        # and model_fields_set contains the field
        if self.images is None and "images" in self.model_fields_set:
            _dict['images'] = None

        # set to None if references (nullable) is None
        # and model_fields_set contains the field
        if self.references is None and "references" in self.model_fields_set:
            _dict['references'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AiOverviewElement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "text": obj.get("text"),
            "images": [ImagesElement.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "references": [AiOverviewReference.from_dict(_item) for _item in obj["references"]] if obj.get("references") is not None else None
        })
        return _obj

