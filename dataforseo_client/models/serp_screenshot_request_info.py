from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpScreenshotRequestInfo(BaseModel):
    """
    SerpScreenshotRequestInfo
    """ # noqa: E501
    task_id: Optional[StrictStr] = Field(default=None, description="task identifier. required field. unique identifier of the associated task in the UUID format. you will be able to use it within 7 days to request the results of the task at any time")
    browser_preset: Optional[StrictStr] = Field(default=None, description="browser resolution preset. optional field. browser preset associated with a certain device type. can take the following values: desktop, tablet, mobile. note: by default, browser preset corresponds to the device type specified in the POST request")
    browser_screen_width: Optional[StrictInt] = Field(default=None, description="width of the browser resolution. optional field. can be specified in the following range: 240-9999")
    browser_screen_height: Optional[StrictInt] = Field(default=None, description="height of the browser resolution. optional field. can be specified in the following range: 240-9999")
    browser_screen_scale_factor: Optional[StrictFloat] = Field(default=None, description="browser scale factor. optional field. can be specified in the following range: 0.5-3")
    page: Optional[StrictInt] = Field(default=None, description="number of SERP pages. optional field. if depth in the corresponding Task POST request exceeds 100 results (or 1 SERP page), specify the number of SERP pages to screenshot;. default value: 1")
    __properties: ClassVar[List[str]] = [
        "task_id", 
        "browser_preset", 
        "browser_screen_width", 
        "browser_screen_height", 
        "browser_screen_scale_factor", 
        "page", 
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

        _dict['task_id'] = self.task_id
        _dict['browser_preset'] = self.browser_preset
        _dict['browser_screen_width'] = self.browser_screen_width
        _dict['browser_screen_height'] = self.browser_screen_height
        _dict['browser_screen_scale_factor'] = self.browser_screen_scale_factor
        _dict['page'] = self.page
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "task_id": obj.get("task_id"),
            "browser_preset": obj.get("browser_preset"),
            "browser_screen_width": obj.get("browser_screen_width"),
            "browser_screen_height": obj.get("browser_screen_height"),
            "browser_screen_scale_factor": obj.get("browser_screen_scale_factor"),
            "page": obj.get("page"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj