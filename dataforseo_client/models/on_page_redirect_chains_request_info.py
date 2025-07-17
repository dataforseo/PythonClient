from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class OnPageRedirectChainsRequestInfo(BaseModel):
    """
    OnPageRedirectChainsRequestInfo
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="ID of the task. required field. you can get this ID in the response of the Task POST endpoint. example:. “07131248-1535-0216-1000-17384017ad04”")
    url: Optional[StrictStr] = Field(default=None, description="page URL. optional field. absolute URL of the target page. if you use this field, the API response will return only redirect chains which contain the specified URL")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned redirect chains. optional field. default value: 100. maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned redirect chains. optional field. default value: 0. if you specify the 10 value, the first ten redirect chains in the results array will be omitted and the data will be provided for the successive redirect chains")
    filters: Optional[List[Optional[Any]]] = Field(default=None, description="array of results filtering parameters. optional field. you can use only one filtering parameter with this endpoint. the following filtering parameter is supported:. is_redirect_loop. the following operators are supported:. regex, not_regex, =, <>. examples:. ['is_redirect_loop','=','true']. ['is_redirect_loop','<>','false']")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier. optional field. the character limit is 255. you can use this parameter to identify the task and match it with the result. you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = [
        "id", 
        "url", 
        "limit", 
        "offset", 
        "filters", 
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

        _dict['id'] = self.id
        _dict['url'] = self.url
        _dict['limit'] = self.limit
        _dict['offset'] = self.offset
        _dict['filters'] = self.filters
        _dict['tag'] = self.tag
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "url": obj.get("url"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "filters": obj.get("filters"),
            "tag": obj.get("tag"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj