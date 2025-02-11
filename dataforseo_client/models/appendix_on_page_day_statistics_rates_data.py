# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from dataforseo_client.models.appendix_lighthouse_on_page_day_statistics_rates_data import AppendixLighthouseOnPageDayStatisticsRatesData
from typing import Optional, Set
from typing_extensions import Self

class AppendixOnPageDayStatisticsRatesData(BaseModel):
    """
    AppendixOnPageDayStatisticsRatesData
    """ # noqa: E501
    task_post: Optional[Union[StrictFloat, StrictInt]] = None
    tasks_ready: Optional[Union[StrictFloat, StrictInt]] = None
    summary: Optional[Union[StrictFloat, StrictInt]] = None
    resources: Optional[Union[StrictFloat, StrictInt]] = None
    pages: Optional[Union[StrictFloat, StrictInt]] = None
    non_indexable: Optional[Union[StrictFloat, StrictInt]] = None
    duplicate_tags: Optional[Union[StrictFloat, StrictInt]] = None
    links: Optional[Union[StrictFloat, StrictInt]] = None
    waterfall: Optional[Union[StrictFloat, StrictInt]] = None
    errors: Optional[Union[StrictFloat, StrictInt]] = None
    pages_by_resource: Optional[Union[StrictFloat, StrictInt]] = None
    duplicate_content: Optional[Union[StrictFloat, StrictInt]] = None
    raw_html: Optional[Union[StrictFloat, StrictInt]] = None
    instant_pages: Optional[Union[StrictFloat, StrictInt]] = None
    redirect_chains: Optional[Union[StrictFloat, StrictInt]] = None
    lighthouse: Optional[AppendixLighthouseOnPageDayStatisticsRatesData] = None
    keyword_density: Optional[Union[StrictFloat, StrictInt]] = None
    page_screenshot: Optional[Union[StrictFloat, StrictInt]] = None
    content_parsing: Optional[Union[StrictFloat, StrictInt]] = None
    content_parsing_live: Optional[Union[StrictFloat, StrictInt]] = None
    id_list: Optional[Union[StrictFloat, StrictInt]] = None
    force_stop: Optional[Union[StrictFloat, StrictInt]] = None
    available_filters: Optional[Union[StrictFloat, StrictInt]] = None
    microdata: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["task_post", "tasks_ready", "summary", "resources", "pages", "non_indexable", "duplicate_tags", "links", "waterfall", "errors", "pages_by_resource", "duplicate_content", "raw_html", "instant_pages", "redirect_chains", "lighthouse", "keyword_density", "page_screenshot", "content_parsing", "content_parsing_live", "id_list", "force_stop", "available_filters", "microdata"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AppendixOnPageDayStatisticsRatesData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of lighthouse
        if self.lighthouse:
            _dict['lighthouse'] = self.lighthouse.to_dict()
        # set to None if task_post (nullable) is None
        # and model_fields_set contains the field
        if self.task_post is None and "task_post" in self.model_fields_set:
            _dict['task_post'] = None

        # set to None if tasks_ready (nullable) is None
        # and model_fields_set contains the field
        if self.tasks_ready is None and "tasks_ready" in self.model_fields_set:
            _dict['tasks_ready'] = None

        # set to None if summary (nullable) is None
        # and model_fields_set contains the field
        if self.summary is None and "summary" in self.model_fields_set:
            _dict['summary'] = None

        # set to None if resources (nullable) is None
        # and model_fields_set contains the field
        if self.resources is None and "resources" in self.model_fields_set:
            _dict['resources'] = None

        # set to None if pages (nullable) is None
        # and model_fields_set contains the field
        if self.pages is None and "pages" in self.model_fields_set:
            _dict['pages'] = None

        # set to None if non_indexable (nullable) is None
        # and model_fields_set contains the field
        if self.non_indexable is None and "non_indexable" in self.model_fields_set:
            _dict['non_indexable'] = None

        # set to None if duplicate_tags (nullable) is None
        # and model_fields_set contains the field
        if self.duplicate_tags is None and "duplicate_tags" in self.model_fields_set:
            _dict['duplicate_tags'] = None

        # set to None if links (nullable) is None
        # and model_fields_set contains the field
        if self.links is None and "links" in self.model_fields_set:
            _dict['links'] = None

        # set to None if waterfall (nullable) is None
        # and model_fields_set contains the field
        if self.waterfall is None and "waterfall" in self.model_fields_set:
            _dict['waterfall'] = None

        # set to None if errors (nullable) is None
        # and model_fields_set contains the field
        if self.errors is None and "errors" in self.model_fields_set:
            _dict['errors'] = None

        # set to None if pages_by_resource (nullable) is None
        # and model_fields_set contains the field
        if self.pages_by_resource is None and "pages_by_resource" in self.model_fields_set:
            _dict['pages_by_resource'] = None

        # set to None if duplicate_content (nullable) is None
        # and model_fields_set contains the field
        if self.duplicate_content is None and "duplicate_content" in self.model_fields_set:
            _dict['duplicate_content'] = None

        # set to None if raw_html (nullable) is None
        # and model_fields_set contains the field
        if self.raw_html is None and "raw_html" in self.model_fields_set:
            _dict['raw_html'] = None

        # set to None if instant_pages (nullable) is None
        # and model_fields_set contains the field
        if self.instant_pages is None and "instant_pages" in self.model_fields_set:
            _dict['instant_pages'] = None

        # set to None if redirect_chains (nullable) is None
        # and model_fields_set contains the field
        if self.redirect_chains is None and "redirect_chains" in self.model_fields_set:
            _dict['redirect_chains'] = None

        # set to None if keyword_density (nullable) is None
        # and model_fields_set contains the field
        if self.keyword_density is None and "keyword_density" in self.model_fields_set:
            _dict['keyword_density'] = None

        # set to None if page_screenshot (nullable) is None
        # and model_fields_set contains the field
        if self.page_screenshot is None and "page_screenshot" in self.model_fields_set:
            _dict['page_screenshot'] = None

        # set to None if content_parsing (nullable) is None
        # and model_fields_set contains the field
        if self.content_parsing is None and "content_parsing" in self.model_fields_set:
            _dict['content_parsing'] = None

        # set to None if content_parsing_live (nullable) is None
        # and model_fields_set contains the field
        if self.content_parsing_live is None and "content_parsing_live" in self.model_fields_set:
            _dict['content_parsing_live'] = None

        # set to None if id_list (nullable) is None
        # and model_fields_set contains the field
        if self.id_list is None and "id_list" in self.model_fields_set:
            _dict['id_list'] = None

        # set to None if force_stop (nullable) is None
        # and model_fields_set contains the field
        if self.force_stop is None and "force_stop" in self.model_fields_set:
            _dict['force_stop'] = None

        # set to None if available_filters (nullable) is None
        # and model_fields_set contains the field
        if self.available_filters is None and "available_filters" in self.model_fields_set:
            _dict['available_filters'] = None

        # set to None if microdata (nullable) is None
        # and model_fields_set contains the field
        if self.microdata is None and "microdata" in self.model_fields_set:
            _dict['microdata'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppendixOnPageDayStatisticsRatesData from a dict"""
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
            "lighthouse": AppendixLighthouseOnPageDayStatisticsRatesData.from_dict(obj["lighthouse"]) if obj.get("lighthouse") is not None else None,
            "keyword_density": obj.get("keyword_density"),
            "page_screenshot": obj.get("page_screenshot"),
            "content_parsing": obj.get("content_parsing"),
            "content_parsing_live": obj.get("content_parsing_live"),
            "id_list": obj.get("id_list"),
            "force_stop": obj.get("force_stop"),
            "available_filters": obj.get("available_filters"),
            "microdata": obj.get("microdata")
        })
        return _obj


