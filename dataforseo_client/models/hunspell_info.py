from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.hunspell_misspelled_info import HunspellMisspelledInfo



class HunspellInfo(BaseModel):
    """
    HunspellInfo
    """ # noqa: E501
    hunspell_language_code: Optional[StrictStr] = Field(default=None, description="spellcheck language code")
    misspelled: Optional[List[Optional[HunspellMisspelledInfo]]] = Field(default=None, description="array of misspelled words")
    __properties: ClassVar[List[str]] = [
        "hunspell_language_code", 
        "misspelled", 
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

        _dict['hunspell_language_code'] = self.hunspell_language_code
        misspelled_items = []
        if self.misspelled:
            for _item in self.misspelled:
                if _item:
                    misspelled_items.append(_item.to_dict())
            _dict['misspelled'] = misspelled_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hunspell_language_code": obj.get("hunspell_language_code"),
            "misspelled": [HunspellMisspelledInfo.from_dict(_item) for _item in obj["misspelled"]] if obj.get("misspelled") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj