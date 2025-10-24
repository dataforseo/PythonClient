from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.base_bing_serp_api_element_item import BaseBingSerpApiElementItem
from dataforseo_client.models.ai_mode_rectangle_info import AiModeRectangleInfo



class BingPeopleAlsoSearchSerpElementItem(BaseBingSerpApiElementItem):
    """
    BingPeopleAlsoSearchSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description=r"group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description=r"absolute rank in SERP. absolute position among all the elements in SERP")
    page: Optional[StrictInt] = Field(default=None, description=r"search results page number. indicates the number of the SERP page on which the element is located")
    position: Optional[StrictStr] = Field(default=None, description=r"the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description=r"the XPath of the element")
    rectangle: Optional[AiModeRectangleInfo] = Field(default=None, description=r"rectangle parameters. contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP. equals null if calculate_rectangles in the POST request is not set to true")
    title: Optional[StrictStr] = Field(default=None, description=r"title of the result in SERP")
    items: Optional[List[Optional[StrictStr]]] = Field(default=None, description=r"additional items present in the element. if there are none, equals null")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "page", 
        "position", 
        "xpath", 
        "rectangle", 
        "title", 
        "items", 
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
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['page'] = self.page
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
        _dict['rectangle'] = self.rectangle.to_dict() if self.rectangle else None
        _dict['title'] = self.title
        _dict['items'] = self.items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "page": obj.get("page"),
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "rectangle": AiModeRectangleInfo.from_dict(obj["rectangle"]) if obj.get("rectangle") is not None else None,
            "title": obj.get("title"),
            "items": obj.get("items"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj