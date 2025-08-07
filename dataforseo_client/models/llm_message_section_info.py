from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.annotation_info import AnnotationInfo



class LlmMessageSectionInfo(BaseModel):
    """
    LlmMessageSectionInfo
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    text: Optional[StrictStr] = Field(default=None, description="AI-generated text content")
    annotations: Optional[List[Optional[AnnotationInfo]]] = Field(default=None, description="array of references used to generate the response. equals null if the web_search parameter is not set to true. Note: annotations may return empty even when web_search is true, as the AI will attempt to retrieve web information but may not find relevant results")
    __properties: ClassVar[List[str]] = [
        "type", 
        "text", 
        "annotations", 
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
        annotations_items = []
        if self.annotations:
            for _item in self.annotations:
                if _item:
                    annotations_items.append(_item.to_dict())
            _dict['annotations'] = annotations_items
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
            "annotations": [AnnotationInfo.from_dict(_item) for _item in obj["annotations"]] if obj.get("annotations") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj