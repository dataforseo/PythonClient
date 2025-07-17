from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpAiSummaryRequestInfo(BaseModel):
    """
    SerpAiSummaryRequestInfo
    """ # noqa: E501
    task_id: Optional[StrictStr] = Field(default=None, description="task identifier. required field. unique identifier of the associated task in the UUID format. you will be able to use it within 30 days to request the results of the task at any time")
    prompt: Optional[StrictStr] = Field(default=None, description="AI prompt. optional field. additional task for AI summariser;. any form of text, question or information that communicates to AI what response you’re looking for;. max number of symbols or characters you can specify: 2000;. note: your prompt has to be relevant to the keyword specified in the POST request to SERP API")
    support_extra: Optional[StrictBool] = Field(default=None, description="support extra SERP features. optional field. if set to true, the AI model will consider the following extra SERP features, in addition to organic results: answer_box, knowledge_graph, featured_snippet;. default value: true")
    fetch_content: Optional[StrictBool] = Field(default=None, description="fetch content from pages in SERPs. optional field. if set to true, the API will fetch the content from pages featured in SERP results, and the AI model will consider this content when generating the summary in the result;. default value: false")
    include_links: Optional[StrictBool] = Field(default=None, description="include source links in the summary. optional field. if set to true, the summary field in the API response will contain links to sources of the generated summary;. default value: false")
    __properties: ClassVar[List[str]] = [
        "task_id", 
        "prompt", 
        "support_extra", 
        "fetch_content", 
        "include_links", 
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
        _dict['prompt'] = self.prompt
        _dict['support_extra'] = self.support_extra
        _dict['fetch_content'] = self.fetch_content
        _dict['include_links'] = self.include_links
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "task_id": obj.get("task_id"),
            "prompt": obj.get("prompt"),
            "support_extra": obj.get("support_extra"),
            "fetch_content": obj.get("fetch_content"),
            "include_links": obj.get("include_links"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj