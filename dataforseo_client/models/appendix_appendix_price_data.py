from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo



class AppendixAppendixPriceData(BaseModel):
    """
    AppendixAppendixPriceData
    """ # noqa: E501
    errors: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    user_data: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "errors", 
        "user_data", 
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

        _dict['errors'] = self.errors.to_dict() if self.errors else None
        _dict['user_data'] = self.user_data.to_dict() if self.user_data else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "errors": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["errors"]) if obj.get("errors") is not None else None,
            "user_data": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["user_data"]) if obj.get("user_data") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj