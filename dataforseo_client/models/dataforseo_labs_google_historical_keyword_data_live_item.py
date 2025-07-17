from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.history import History



class DataforseoLabsGoogleHistoricalKeywordDataLiveItem(BaseModel):
    """
    DataforseoLabsGoogleHistoricalKeywordDataLiveItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    keyword: Optional[StrictStr] = Field(default=None, description="keyword. keyword is returned with decoded %## (plus character ‘+’ will be decoded to a space character)")
    location_code: Optional[StrictInt] = Field(default=None, description="location code in a POST array. if there is no data, then the value is null")
    language_code: Optional[StrictStr] = Field(default=None, description="language code in a POST array")
    history: Optional[List[Optional[History]]] = Field(default=None, description="array of objects with historical data for the keyword")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "keyword", 
        "location_code", 
        "language_code", 
        "history", 
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
        _dict['keyword'] = self.keyword
        _dict['location_code'] = self.location_code
        _dict['language_code'] = self.language_code
        history_items = []
        if self.history:
            for _item in self.history:
                if _item:
                    history_items.append(_item.to_dict())
            _dict['history'] = history_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "keyword": obj.get("keyword"),
            "location_code": obj.get("location_code"),
            "language_code": obj.get("language_code"),
            "history": [History.from_dict(_item) for _item in obj["history"]] if obj.get("history") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj