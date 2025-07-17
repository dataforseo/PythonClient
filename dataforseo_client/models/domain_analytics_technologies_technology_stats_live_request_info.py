from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DomainAnalyticsTechnologiesTechnologyStatsLiveRequestInfo(BaseModel):
    """
    DomainAnalyticsTechnologiesTechnologyStatsLiveRequestInfo
    """ # noqa: E501
    technology: Optional[StrictStr] = Field(default=None, description="target technology. required field. you can find the full list of technologies you can specify here on this page. example:. 'Salesforce'")
    date_from: Optional[StrictStr] = Field(default=None, description="starting date of the time range. optional field. minimum value 2022-10-31. if you don’t specify this field, the minimum value will be used by default. date format: 'yyyy-mm-dd'. example:. '2023-06-01'")
    date_to: Optional[StrictStr] = Field(default=None, description="ending date of the time range. optional field. if you don’t specify this field, the today’s date will be used by default. date format: 'yyyy-mm-dd'. example:. '2023-01-15'")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "technology", 
        "date_from", 
        "date_to", 
        "tag", 
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

        _dict['technology'] = self.technology
        _dict['date_from'] = self.date_from
        _dict['date_to'] = self.date_to
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "technology": obj.get("technology"),
            "date_from": obj.get("date_from"),
            "date_to": obj.get("date_to"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj