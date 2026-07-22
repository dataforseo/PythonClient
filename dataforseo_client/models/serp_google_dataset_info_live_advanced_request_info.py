from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpGoogleDatasetInfoLiveAdvancedRequestInfo(BaseModel):
    """
    SerpGoogleDatasetInfoLiveAdvancedRequestInfo
    """ # noqa: E501
    dataset_id: Optional[StrictStr] = Field(default=None, description=r"ID of the datasetrequired fieldyou can find dataset ID in the dataset URL or dataset item of Google Dataset Search resultexample:L2cvMTFqbl85ZHN6MQ==")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search engine language codeoptional fieldif you use this field, you don't need to specify language_namepossible value:en")
    device: Optional[StrictStr] = Field(default=None, description=r"device typeoptional fieldreturn results for a specific device typepossible value: desktop")
    __properties: ClassVar[List[str]] = [
        "dataset_id", 
        "language_code", 
        "device", 
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

        _dict['dataset_id'] = self.dataset_id
        _dict['language_code'] = self.language_code
        _dict['device'] = self.device
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataset_id": obj.get("dataset_id"),
            "language_code": obj.get("language_code"),
            "device": obj.get("device"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj