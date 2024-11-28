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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.appendix_bing_keywords_data_price_data_info import AppendixBingKeywordsDataPriceDataInfo
from dataforseo_client.models.appendix_task_keywords_data_price_data_info import AppendixTaskKeywordsDataPriceDataInfo
from typing import Optional, Set
from typing_extensions import Self

class AppendixBacklinksPriceData(BaseModel):
    """
    AppendixBacklinksPriceData
    """ # noqa: E501
    anchors: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    backlinks: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    bulk_backlinks: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    bulk_new_lost_backlinks: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    bulk_new_lost_referring_domains: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    bulk_pages_summary: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    bulk_ranks: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    bulk_referring_domains: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    bulk_spam_score: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    competitors: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    content_duplicates: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    domain_intersection: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    domain_pages: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    domain_pages_summary: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    errors: Optional[AppendixTaskKeywordsDataPriceDataInfo] = None
    history: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    page_intersection: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    referring_domains: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    referring_networks: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    summary: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    timeseries_new_lost_summary: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    timeseries_summary: Optional[AppendixBingKeywordsDataPriceDataInfo] = None
    __properties: ClassVar[List[str]] = ["anchors", "backlinks", "bulk_backlinks", "bulk_new_lost_backlinks", "bulk_new_lost_referring_domains", "bulk_pages_summary", "bulk_ranks", "bulk_referring_domains", "bulk_spam_score", "competitors", "content_duplicates", "domain_intersection", "domain_pages", "domain_pages_summary", "errors", "history", "page_intersection", "referring_domains", "referring_networks", "summary", "timeseries_new_lost_summary", "timeseries_summary"]

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
        """Create an instance of AppendixBacklinksPriceData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of anchors
        if self.anchors:
            _dict['anchors'] = self.anchors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of backlinks
        if self.backlinks:
            _dict['backlinks'] = self.backlinks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_backlinks
        if self.bulk_backlinks:
            _dict['bulk_backlinks'] = self.bulk_backlinks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_new_lost_backlinks
        if self.bulk_new_lost_backlinks:
            _dict['bulk_new_lost_backlinks'] = self.bulk_new_lost_backlinks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_new_lost_referring_domains
        if self.bulk_new_lost_referring_domains:
            _dict['bulk_new_lost_referring_domains'] = self.bulk_new_lost_referring_domains.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_pages_summary
        if self.bulk_pages_summary:
            _dict['bulk_pages_summary'] = self.bulk_pages_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_ranks
        if self.bulk_ranks:
            _dict['bulk_ranks'] = self.bulk_ranks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_referring_domains
        if self.bulk_referring_domains:
            _dict['bulk_referring_domains'] = self.bulk_referring_domains.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bulk_spam_score
        if self.bulk_spam_score:
            _dict['bulk_spam_score'] = self.bulk_spam_score.to_dict()
        # override the default output from pydantic by calling `to_dict()` of competitors
        if self.competitors:
            _dict['competitors'] = self.competitors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of content_duplicates
        if self.content_duplicates:
            _dict['content_duplicates'] = self.content_duplicates.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_intersection
        if self.domain_intersection:
            _dict['domain_intersection'] = self.domain_intersection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_pages
        if self.domain_pages:
            _dict['domain_pages'] = self.domain_pages.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_pages_summary
        if self.domain_pages_summary:
            _dict['domain_pages_summary'] = self.domain_pages_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of errors
        if self.errors:
            _dict['errors'] = self.errors.to_dict()
        # override the default output from pydantic by calling `to_dict()` of history
        if self.history:
            _dict['history'] = self.history.to_dict()
        # override the default output from pydantic by calling `to_dict()` of page_intersection
        if self.page_intersection:
            _dict['page_intersection'] = self.page_intersection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of referring_domains
        if self.referring_domains:
            _dict['referring_domains'] = self.referring_domains.to_dict()
        # override the default output from pydantic by calling `to_dict()` of referring_networks
        if self.referring_networks:
            _dict['referring_networks'] = self.referring_networks.to_dict()
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of timeseries_new_lost_summary
        if self.timeseries_new_lost_summary:
            _dict['timeseries_new_lost_summary'] = self.timeseries_new_lost_summary.to_dict()
        # override the default output from pydantic by calling `to_dict()` of timeseries_summary
        if self.timeseries_summary:
            _dict['timeseries_summary'] = self.timeseries_summary.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AppendixBacklinksPriceData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "anchors": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["anchors"]) if obj.get("anchors") is not None else None,
            "backlinks": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["backlinks"]) if obj.get("backlinks") is not None else None,
            "bulk_backlinks": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["bulk_backlinks"]) if obj.get("bulk_backlinks") is not None else None,
            "bulk_new_lost_backlinks": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["bulk_new_lost_backlinks"]) if obj.get("bulk_new_lost_backlinks") is not None else None,
            "bulk_new_lost_referring_domains": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["bulk_new_lost_referring_domains"]) if obj.get("bulk_new_lost_referring_domains") is not None else None,
            "bulk_pages_summary": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["bulk_pages_summary"]) if obj.get("bulk_pages_summary") is not None else None,
            "bulk_ranks": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["bulk_ranks"]) if obj.get("bulk_ranks") is not None else None,
            "bulk_referring_domains": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["bulk_referring_domains"]) if obj.get("bulk_referring_domains") is not None else None,
            "bulk_spam_score": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["bulk_spam_score"]) if obj.get("bulk_spam_score") is not None else None,
            "competitors": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["competitors"]) if obj.get("competitors") is not None else None,
            "content_duplicates": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["content_duplicates"]) if obj.get("content_duplicates") is not None else None,
            "domain_intersection": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["domain_intersection"]) if obj.get("domain_intersection") is not None else None,
            "domain_pages": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["domain_pages"]) if obj.get("domain_pages") is not None else None,
            "domain_pages_summary": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["domain_pages_summary"]) if obj.get("domain_pages_summary") is not None else None,
            "errors": AppendixTaskKeywordsDataPriceDataInfo.from_dict(obj["errors"]) if obj.get("errors") is not None else None,
            "history": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["history"]) if obj.get("history") is not None else None,
            "page_intersection": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["page_intersection"]) if obj.get("page_intersection") is not None else None,
            "referring_domains": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["referring_domains"]) if obj.get("referring_domains") is not None else None,
            "referring_networks": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["referring_networks"]) if obj.get("referring_networks") is not None else None,
            "summary": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["summary"]) if obj.get("summary") is not None else None,
            "timeseries_new_lost_summary": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["timeseries_new_lost_summary"]) if obj.get("timeseries_new_lost_summary") is not None else None,
            "timeseries_summary": AppendixBingKeywordsDataPriceDataInfo.from_dict(obj["timeseries_summary"]) if obj.get("timeseries_summary") is not None else None
        })
        return _obj


