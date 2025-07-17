from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SearchIntentInfo(BaseModel):
    """
    SearchIntentInfo
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type. possible values: google")
    main_intent: Optional[StrictStr] = Field(default=None, description="main search intent. possible values: informational, navigational, commercial, transactional")
    foreign_intent: Optional[List[Optional[StrictStr]]] = Field(default=None, description="supplementary search intents. possible values: informational, navigational, commercial, transactional")
    last_updated_time: Optional[StrictStr] = Field(default=None, description="date and time when the dataset was updated. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "main_intent", 
        "foreign_intent", 
        "last_updated_time", 
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

        _dict['se_type'] = self.se_type
        _dict['main_intent'] = self.main_intent
        _dict['foreign_intent'] = self.foreign_intent
        _dict['last_updated_time'] = self.last_updated_time
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "main_intent": obj.get("main_intent"),
            "foreign_intent": obj.get("foreign_intent"),
            "last_updated_time": obj.get("last_updated_time"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj