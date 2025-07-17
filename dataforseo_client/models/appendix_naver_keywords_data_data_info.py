from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_info import AppendixInfo



class AppendixNaverKeywordsDataDataInfo(BaseModel):
    """
    AppendixNaverKeywordsDataDataInfo
    """ # noqa: E501
    keywords_for_category: Optional[AppendixInfo] = Field(default=None, description="")
    search_volume: Optional[AppendixInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "keywords_for_category", 
        "search_volume", 
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

        _dict['keywords_for_category'] = self.keywords_for_category.to_dict() if self.keywords_for_category else None
        _dict['search_volume'] = self.search_volume.to_dict() if self.search_volume else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keywords_for_category": AppendixInfo.from_dict(obj["keywords_for_category"]) if obj.get("keywords_for_category") is not None else None,
            "search_volume": AppendixInfo.from_dict(obj["search_volume"]) if obj.get("search_volume") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj