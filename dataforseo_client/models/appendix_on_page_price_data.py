from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo
from dataforseo_client.models.appendix_google_business_data_price_data_info import AppendixGoogleBusinessDataPriceDataInfo



class AppendixOnPagePriceData(BaseModel):
    """
    AppendixOnPagePriceData
    """ # noqa: E501
    errors: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    lighthouse: Optional[AppendixGoogleBusinessDataPriceDataInfo] = Field(default=None, description="")
    content_parsing: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    content_parsing_live: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    duplicate_content: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    duplicate_tags: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    instant_pages: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    keyword_density: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    links: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    non_indexable: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    pages: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    pages_by_resource: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    page_screenshot: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    raw_html: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    redirect_chains: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    resources: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    summary: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    task_post: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    tasks_ready: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    waterfall: Optional[AppendixTaskKeywordsDataPriceDataInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "errors", 
        "lighthouse", 
        "content_parsing", 
        "content_parsing_live", 
        "duplicate_content", 
        "duplicate_tags", 
        "instant_pages", 
        "keyword_density", 
        "links", 
        "non_indexable", 
        "pages", 
        "pages_by_resource", 
        "page_screenshot", 
        "raw_html", 
        "redirect_chains", 
        "resources", 
        "summary", 
        "task_post", 
        "tasks_ready", 
        "waterfall", 
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

        _dict['errors'] = self.errors.to_dict() if self.errors else None
        _dict['lighthouse'] = self.lighthouse.to_dict() if self.lighthouse else None
        _dict['content_parsing'] = self.content_parsing.to_dict() if self.content_parsing else None
        _dict['content_parsing_live'] = self.content_parsing_live.to_dict() if self.content_parsing_live else None
        _dict['duplicate_content'] = self.duplicate_content.to_dict() if self.duplicate_content else None
        _dict['duplicate_tags'] = self.duplicate_tags.to_dict() if self.duplicate_tags else None
        _dict['instant_pages'] = self.instant_pages.to_dict() if self.instant_pages else None
        _dict['keyword_density'] = self.keyword_density.to_dict() if self.keyword_density else None
        _dict['links'] = self.links.to_dict() if self.links else None
        _dict['non_indexable'] = self.non_indexable.to_dict() if self.non_indexable else None
        _dict['pages'] = self.pages.to_dict() if self.pages else None
        _dict['pages_by_resource'] = self.pages_by_resource.to_dict() if self.pages_by_resource else None
        _dict['page_screenshot'] = self.page_screenshot.to_dict() if self.page_screenshot else None
        _dict['raw_html'] = self.raw_html.to_dict() if self.raw_html else None
        _dict['redirect_chains'] = self.redirect_chains.to_dict() if self.redirect_chains else None
        _dict['resources'] = self.resources.to_dict() if self.resources else None
        _dict['summary'] = self.summary.to_dict() if self.summary else None
        _dict['task_post'] = self.task_post.to_dict() if self.task_post else None
        _dict['tasks_ready'] = self.tasks_ready.to_dict() if self.tasks_ready else None
        _dict['waterfall'] = self.waterfall.to_dict() if self.waterfall else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "errors": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["errors"]) if obj.get("errors") is not None else None,
            "lighthouse": AppendixGoogleBusinessDataPriceDataInfo.from_dict(obj["lighthouse"]) if obj.get("lighthouse") is not None else None,
            "content_parsing": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["content_parsing"]) if obj.get("content_parsing") is not None else None,
            "content_parsing_live": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["content_parsing_live"]) if obj.get("content_parsing_live") is not None else None,
            "duplicate_content": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["duplicate_content"]) if obj.get("duplicate_content") is not None else None,
            "duplicate_tags": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["duplicate_tags"]) if obj.get("duplicate_tags") is not None else None,
            "instant_pages": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["instant_pages"]) if obj.get("instant_pages") is not None else None,
            "keyword_density": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["keyword_density"]) if obj.get("keyword_density") is not None else None,
            "links": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["links"]) if obj.get("links") is not None else None,
            "non_indexable": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["non_indexable"]) if obj.get("non_indexable") is not None else None,
            "pages": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["pages"]) if obj.get("pages") is not None else None,
            "pages_by_resource": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["pages_by_resource"]) if obj.get("pages_by_resource") is not None else None,
            "page_screenshot": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["page_screenshot"]) if obj.get("page_screenshot") is not None else None,
            "raw_html": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["raw_html"]) if obj.get("raw_html") is not None else None,
            "redirect_chains": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["redirect_chains"]) if obj.get("redirect_chains") is not None else None,
            "resources": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["resources"]) if obj.get("resources") is not None else None,
            "summary": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["summary"]) if obj.get("summary") is not None else None,
            "task_post": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["task_post"]) if obj.get("task_post") is not None else None,
            "tasks_ready": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["tasks_ready"]) if obj.get("tasks_ready") is not None else None,
            "waterfall": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["waterfall"]) if obj.get("waterfall") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj