from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.dataforseo_labs_status_info import DataforseoLabsStatusInfo



class DataforseoLabsStatusResultInfo(BaseModel):
    """
    DataforseoLabsStatusResultInfo
    """ # noqa: E501
    google: Optional[DataforseoLabsStatusInfo] = Field(default=None, description="update information for the Google endpoints")
    bing: Optional[DataforseoLabsStatusInfo] = Field(default=None, description="update information for the Bing endpoints")
    amazon: Optional[DataforseoLabsStatusInfo] = Field(default=None, description="update information for the Amazon endpoints")
    __properties: ClassVar[List[str]] = [
        "google", 
        "bing", 
        "amazon", 
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

        _dict['google'] = self.google.to_dict() if self.google else None
        _dict['bing'] = self.bing.to_dict() if self.bing else None
        _dict['amazon'] = self.amazon.to_dict() if self.amazon else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "google": DataforseoLabsStatusInfo.from_dict(obj["google"]) if obj.get("google") is not None else None,
            "bing": DataforseoLabsStatusInfo.from_dict(obj["bing"]) if obj.get("bing") is not None else None,
            "amazon": DataforseoLabsStatusInfo.from_dict(obj["amazon"]) if obj.get("amazon") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj