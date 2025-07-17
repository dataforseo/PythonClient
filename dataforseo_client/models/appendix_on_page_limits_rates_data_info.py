from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_info import AppendixInfo



class AppendixOnPageLimitsRatesDataInfo(BaseModel):
    """
    AppendixOnPageLimitsRatesDataInfo
    """ # noqa: E501
    task_post: Optional[StrictFloat] = Field(default=None, description="")
    tasks_ready: Optional[StrictFloat] = Field(default=None, description="")
    summary: Optional[StrictFloat] = Field(default=None, description="")
    resources: Optional[StrictFloat] = Field(default=None, description="")
    pages: Optional[StrictFloat] = Field(default=None, description="")
    non_indexable: Optional[StrictFloat] = Field(default=None, description="")
    duplicate_tags: Optional[StrictFloat] = Field(default=None, description="")
    links: Optional[StrictFloat] = Field(default=None, description="")
    waterfall: Optional[StrictFloat] = Field(default=None, description="")
    errors: Optional[StrictFloat] = Field(default=None, description="")
    pages_by_resource: Optional[StrictFloat] = Field(default=None, description="")
    duplicate_content: Optional[StrictFloat] = Field(default=None, description="")
    raw_html: Optional[StrictFloat] = Field(default=None, description="")
    instant_pages: Optional[StrictFloat] = Field(default=None, description="")
    redirect_chains: Optional[StrictFloat] = Field(default=None, description="")
    lighthouse: Optional[AppendixInfo] = Field(default=None, description="")
    keyword_density: Optional[StrictFloat] = Field(default=None, description="")
    page_screenshot: Optional[StrictFloat] = Field(default=None, description="")
    content_parsing: Optional[StrictFloat] = Field(default=None, description="")
    content_parsing_live: Optional[StrictFloat] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "task_post", 
        "tasks_ready", 
        "summary", 
        "resources", 
        "pages", 
        "non_indexable", 
        "duplicate_tags", 
        "links", 
        "waterfall", 
        "errors", 
        "pages_by_resource", 
        "duplicate_content", 
        "raw_html", 
        "instant_pages", 
        "redirect_chains", 
        "lighthouse", 
        "keyword_density", 
        "page_screenshot", 
        "content_parsing", 
        "content_parsing_live", 
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

        _dict['task_post'] = self.task_post
        _dict['tasks_ready'] = self.tasks_ready
        _dict['summary'] = self.summary
        _dict['resources'] = self.resources
        _dict['pages'] = self.pages
        _dict['non_indexable'] = self.non_indexable
        _dict['duplicate_tags'] = self.duplicate_tags
        _dict['links'] = self.links
        _dict['waterfall'] = self.waterfall
        _dict['errors'] = self.errors
        _dict['pages_by_resource'] = self.pages_by_resource
        _dict['duplicate_content'] = self.duplicate_content
        _dict['raw_html'] = self.raw_html
        _dict['instant_pages'] = self.instant_pages
        _dict['redirect_chains'] = self.redirect_chains
        _dict['lighthouse'] = self.lighthouse.to_dict() if self.lighthouse else None
        _dict['keyword_density'] = self.keyword_density
        _dict['page_screenshot'] = self.page_screenshot
        _dict['content_parsing'] = self.content_parsing
        _dict['content_parsing_live'] = self.content_parsing_live
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "task_post": obj.get("task_post"),
            "tasks_ready": obj.get("tasks_ready"),
            "summary": obj.get("summary"),
            "resources": obj.get("resources"),
            "pages": obj.get("pages"),
            "non_indexable": obj.get("non_indexable"),
            "duplicate_tags": obj.get("duplicate_tags"),
            "links": obj.get("links"),
            "waterfall": obj.get("waterfall"),
            "errors": obj.get("errors"),
            "pages_by_resource": obj.get("pages_by_resource"),
            "duplicate_content": obj.get("duplicate_content"),
            "raw_html": obj.get("raw_html"),
            "instant_pages": obj.get("instant_pages"),
            "redirect_chains": obj.get("redirect_chains"),
            "lighthouse": AppendixInfo.from_dict(obj["lighthouse"]) if obj.get("lighthouse") is not None else None,
            "keyword_density": obj.get("keyword_density"),
            "page_screenshot": obj.get("page_screenshot"),
            "content_parsing": obj.get("content_parsing"),
            "content_parsing_live": obj.get("content_parsing_live"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj