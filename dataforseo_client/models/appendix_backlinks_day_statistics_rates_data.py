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
from dataforseo_client.models.appendix_info import AppendixInfo
from typing import Optional, Set
from typing_extensions import Self

class AppendixBacklinksDayStatisticsRatesData(BaseModel):
    """
    AppendixBacklinksDayStatisticsRatesData
    """ # noqa: E501
    summary: Optional[AppendixInfo] = None
    history: Optional[AppendixInfo] = None
    content_duplicates: Optional[AppendixInfo] = None
    domain_intersection: Optional[AppendixInfo] = None
    backlinks: Optional[AppendixInfo] = None
    domain_pages: Optional[AppendixInfo] = None
    anchors: Optional[AppendixInfo] = None
    referring_domains: Optional[AppendixInfo] = None
    page_intersection: Optional[AppendixInfo] = None
    referring_networks: Optional[AppendixInfo] = None
    bulk_ranks: Optional[AppendixInfo] = None
    bulk_backlinks: Optional[AppendixInfo] = None
    bulk_new_lost_backlinks: Optional[AppendixInfo] = None
    bulk_new_lost_referring_domains: Optional[AppendixInfo] = None
    bulk_referring_domains: Optional[AppendixInfo] = None
    errors: Optional[Union[StrictFloat, StrictInt]] = None
    domain_pages_summary: Optional[AppendixInfo] = None
    timeseries_summary: Optional[AppendixInfo] = None
    timeseries_new_lost_summary: Optional[AppendixInfo] = None
    competitors: Optional[AppendixInfo] = None
    bulk_spam_score: Optional[AppendixInfo] = None
    bulk_pages_summary: Optional[AppendixInfo] = None
    historical_new_lost_summary: Optional[AppendixInfo] = None
    pages_summary_with_page_info: Optional[AppendixInfo] = None
    index: Optional[Union[StrictFloat, StrictInt]] = None
    id_list: Optional[Union[StrictFloat, StrictInt]] = None
    available_filters: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["summary", "history", "content_duplicates", "domain_intersection", "backlinks", "domain_pages", "anchors", "referring_domains", "page_intersection", "referring_networks", "bulk_ranks", "bulk_backlinks", "bulk_new_lost_backlinks", "bulk_new_lost_referring_domains", "bulk_referring_domains", "errors", "domain_pages_summary", "timeseries_summary", "timeseries_new_lost_summary", "competitors", "bulk_spam_score", "bulk_pages_summary", "historical_new_lost_summary", "pages_summary_with_page_info", "index", "id_list", "available_filters"]

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
        """Create an instance of AppendixBacklinksDayStatisticsRatesData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of history
        if self.history:
            _dict['history'] = self.history.to_dict()
        # override the default output from pydantic by calling `to_dict()` of content_duplicates
        if self.content_duplicates:
            _dict['content_duplicates'] = self.content_duplicates.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_intersection
        if self.domain_intersection:
            _dict['domain_intersection'] = self.domain_intersection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of backlinks
        if self.backlinks:
            _dict['backlinks'] = self.backlinks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_pages
        if self.domain_pages:
            _dict['domain_pages'] = self.domain_pages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of anchors
        if self.anchors:
            _dict['anchors'] = self.anchors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of referring_domains
        if self.referring_domains:
            _dict['referring_domains'] = self.referring_domains.to_dict()
        # override the default output from pydantic by calling `to_dict()` of page_intersection
        if self.page_intersection:
            _dict['page_intersection'] = self.page_intersection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of referring_networks
        if self.referring_networks:
            _dict['referring_networks'] = self.referring_networks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_ranks
        if self.bulk_ranks:
            _dict['bulk_ranks'] = self.bulk_ranks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_backlinks
        if self.bulk_backlinks:
            _dict['bulk_backlinks'] = self.bulk_backlinks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_new_lost_backlinks
        if self.bulk_new_lost_backlinks:
            _dict['bulk_new_lost_backlinks'] = self.bulk_new_lost_backlinks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_new_lost_referring_domains
        if self.bulk_new_lost_referring_domains:
            _dict['bulk_new_lost_referring_domains'] = self.bulk_new_lost_referring_domains.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_referring_domains
        if self.bulk_referring_domains:
            _dict['bulk_referring_domains'] = self.bulk_referring_domains.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_pages_summary
        if self.domain_pages_summary:
            _dict['domain_pages_summary'] = self.domain_pages_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of timeseries_summary
        if self.timeseries_summary:
            _dict['timeseries_summary'] = self.timeseries_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of timeseries_new_lost_summary
        if self.timeseries_new_lost_summary:
            _dict['timeseries_new_lost_summary'] = self.timeseries_new_lost_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of competitors
        if self.competitors:
            _dict['competitors'] = self.competitors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_spam_score
        if self.bulk_spam_score:
            _dict['bulk_spam_score'] = self.bulk_spam_score.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_pages_summary
        if self.bulk_pages_summary:
            _dict['bulk_pages_summary'] = self.bulk_pages_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of historical_new_lost_summary
        if self.historical_new_lost_summary:
            _dict['historical_new_lost_summary'] = self.historical_new_lost_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pages_summary_with_page_info
        if self.pages_summary_with_page_info:
            _dict['pages_summary_with_page_info'] = self.pages_summary_with_page_info.to_dict()
        # set to None if errors (nullable) is None
        # and model_fields_set contains the field
        if self.errors is None and "errors" in self.model_fields_set:
            _dict['errors'] = None

        # set to None if index (nullable) is None
        # and model_fields_set contains the field
        if self.index is None and "index" in self.model_fields_set:
            _dict['index'] = None

        # set to None if id_list (nullable) is None
        # and model_fields_set contains the field
        if self.id_list is None and "id_list" in self.model_fields_set:
            _dict['id_list'] = None

        # set to None if available_filters (nullable) is None
        # and model_fields_set contains the field
        if self.available_filters is None and "available_filters" in self.model_fields_set:
            _dict['available_filters'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppendixBacklinksDayStatisticsRatesData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "summary": AppendixInfo.from_dict(obj["summary"]) if obj.get("summary") is not None else None,
            "history": AppendixInfo.from_dict(obj["history"]) if obj.get("history") is not None else None,
            "content_duplicates": AppendixInfo.from_dict(obj["content_duplicates"]) if obj.get("content_duplicates") is not None else None,
            "domain_intersection": AppendixInfo.from_dict(obj["domain_intersection"]) if obj.get("domain_intersection") is not None else None,
            "backlinks": AppendixInfo.from_dict(obj["backlinks"]) if obj.get("backlinks") is not None else None,
            "domain_pages": AppendixInfo.from_dict(obj["domain_pages"]) if obj.get("domain_pages") is not None else None,
            "anchors": AppendixInfo.from_dict(obj["anchors"]) if obj.get("anchors") is not None else None,
            "referring_domains": AppendixInfo.from_dict(obj["referring_domains"]) if obj.get("referring_domains") is not None else None,
            "page_intersection": AppendixInfo.from_dict(obj["page_intersection"]) if obj.get("page_intersection") is not None else None,
            "referring_networks": AppendixInfo.from_dict(obj["referring_networks"]) if obj.get("referring_networks") is not None else None,
            "bulk_ranks": AppendixInfo.from_dict(obj["bulk_ranks"]) if obj.get("bulk_ranks") is not None else None,
            "bulk_backlinks": AppendixInfo.from_dict(obj["bulk_backlinks"]) if obj.get("bulk_backlinks") is not None else None,
            "bulk_new_lost_backlinks": AppendixInfo.from_dict(obj["bulk_new_lost_backlinks"]) if obj.get("bulk_new_lost_backlinks") is not None else None,
            "bulk_new_lost_referring_domains": AppendixInfo.from_dict(obj["bulk_new_lost_referring_domains"]) if obj.get("bulk_new_lost_referring_domains") is not None else None,
            "bulk_referring_domains": AppendixInfo.from_dict(obj["bulk_referring_domains"]) if obj.get("bulk_referring_domains") is not None else None,
            "errors": obj.get("errors"),
            "domain_pages_summary": AppendixInfo.from_dict(obj["domain_pages_summary"]) if obj.get("domain_pages_summary") is not None else None,
            "timeseries_summary": AppendixInfo.from_dict(obj["timeseries_summary"]) if obj.get("timeseries_summary") is not None else None,
            "timeseries_new_lost_summary": AppendixInfo.from_dict(obj["timeseries_new_lost_summary"]) if obj.get("timeseries_new_lost_summary") is not None else None,
            "competitors": AppendixInfo.from_dict(obj["competitors"]) if obj.get("competitors") is not None else None,
            "bulk_spam_score": AppendixInfo.from_dict(obj["bulk_spam_score"]) if obj.get("bulk_spam_score") is not None else None,
            "bulk_pages_summary": AppendixInfo.from_dict(obj["bulk_pages_summary"]) if obj.get("bulk_pages_summary") is not None else None,
            "historical_new_lost_summary": AppendixInfo.from_dict(obj["historical_new_lost_summary"]) if obj.get("historical_new_lost_summary") is not None else None,
            "pages_summary_with_page_info": AppendixInfo.from_dict(obj["pages_summary_with_page_info"]) if obj.get("pages_summary_with_page_info") is not None else None,
            "index": obj.get("index"),
            "id_list": obj.get("id_list"),
            "available_filters": obj.get("available_filters")
        })
        return _obj


