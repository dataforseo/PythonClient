from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_mode_rectangle_info import AiModeRectangleInfo



class GoogleJobsItem(BaseModel):
    """
    GoogleJobsItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    job_id: Optional[StrictStr] = Field(default=None, description="ID of the job on Google Jobs")
    title: Optional[StrictStr] = Field(default=None, description="title of the element")
    employer_name: Optional[StrictStr] = Field(default=None, description="name of the employer")
    employer_url: Optional[StrictStr] = Field(default=None, description="URL to the employer’s website")
    employer_image_url: Optional[StrictStr] = Field(default=None, description="URL to the image used in the job posting")
    location: Optional[StrictStr] = Field(default=None, description="location for which the job vacancy is posted")
    source_name: Optional[StrictStr] = Field(default=None, description="original source of the job vacancy")
    source_url: Optional[StrictStr] = Field(default=None, description="URL to the original source of the job vacancy")
    salary: Optional[StrictStr] = Field(default=None, description="the salary indicated in the job vacancy. if the salary isn’t indicated, this field will equal null")
    contract_type: Optional[StrictStr] = Field(default=None, description="employment contract type")
    timestamp: Optional[StrictStr] = Field(default=None, description="date and time when the result was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2019-11-15 12:57:46 +00:00")
    time_ago: Optional[StrictStr] = Field(default=None, description="indicates how long ago the job vacancy was posted")
    rectangle: Optional[AiModeRectangleInfo] = Field(default=None, description="rectangle parameters. contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP;. in this case, will equal null")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        "job_id", 
        "title", 
        "employer_name", 
        "employer_url", 
        "employer_image_url", 
        "location", 
        "source_name", 
        "source_url", 
        "salary", 
        "contract_type", 
        "timestamp", 
        "time_ago", 
        "rectangle", 
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
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
        _dict['job_id'] = self.job_id
        _dict['title'] = self.title
        _dict['employer_name'] = self.employer_name
        _dict['employer_url'] = self.employer_url
        _dict['employer_image_url'] = self.employer_image_url
        _dict['location'] = self.location
        _dict['source_name'] = self.source_name
        _dict['source_url'] = self.source_url
        _dict['salary'] = self.salary
        _dict['contract_type'] = self.contract_type
        _dict['timestamp'] = self.timestamp
        _dict['time_ago'] = self.time_ago
        _dict['rectangle'] = self.rectangle.to_dict() if self.rectangle else None
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
            "position": obj.get("position"),
            "xpath": obj.get("xpath"),
            "job_id": obj.get("job_id"),
            "title": obj.get("title"),
            "employer_name": obj.get("employer_name"),
            "employer_url": obj.get("employer_url"),
            "employer_image_url": obj.get("employer_image_url"),
            "location": obj.get("location"),
            "source_name": obj.get("source_name"),
            "source_url": obj.get("source_url"),
            "salary": obj.get("salary"),
            "contract_type": obj.get("contract_type"),
            "timestamp": obj.get("timestamp"),
            "time_ago": obj.get("time_ago"),
            "rectangle": AiModeRectangleInfo.from_dict(obj["rectangle"]) if obj.get("rectangle") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj