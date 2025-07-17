from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.appendix_info import AppendixInfo



class AppendixBacklinksLimitsRatesDataInfo(BaseModel):
    """
    AppendixBacklinksLimitsRatesDataInfo
    """ # noqa: E501
    summary: Optional[AppendixInfo] = Field(default=None, description="")
    history: Optional[AppendixInfo] = Field(default=None, description="")
    content_duplicates: Optional[AppendixInfo] = Field(default=None, description="")
    domain_intersection: Optional[AppendixInfo] = Field(default=None, description="")
    backlinks: Optional[AppendixInfo] = Field(default=None, description="")
    domain_pages: Optional[AppendixInfo] = Field(default=None, description="")
    anchors: Optional[AppendixInfo] = Field(default=None, description="")
    referring_domains: Optional[AppendixInfo] = Field(default=None, description="")
    page_intersection: Optional[AppendixInfo] = Field(default=None, description="")
    referring_networks: Optional[AppendixInfo] = Field(default=None, description="")
    bulk_ranks: Optional[AppendixInfo] = Field(default=None, description="")
    bulk_backlinks: Optional[AppendixInfo] = Field(default=None, description="")
    bulk_new_lost_backlinks: Optional[AppendixInfo] = Field(default=None, description="")
    bulk_new_lost_referring_domains: Optional[AppendixInfo] = Field(default=None, description="")
    bulk_referring_domains: Optional[AppendixInfo] = Field(default=None, description="")
    errors: Optional[StrictFloat] = Field(default=None, description="")
    domain_pages_summary: Optional[AppendixInfo] = Field(default=None, description="")
    timeseries_summary: Optional[AppendixInfo] = Field(default=None, description="")
    timeseries_new_lost_summary: Optional[AppendixInfo] = Field(default=None, description="")
    competitors: Optional[AppendixInfo] = Field(default=None, description="")
    bulk_spam_score: Optional[AppendixInfo] = Field(default=None, description="")
    bulk_pages_summary: Optional[AppendixInfo] = Field(default=None, description="")
    __properties: ClassVar[List[str]] = [
        "summary", 
        "history", 
        "content_duplicates", 
        "domain_intersection", 
        "backlinks", 
        "domain_pages", 
        "anchors", 
        "referring_domains", 
        "page_intersection", 
        "referring_networks", 
        "bulk_ranks", 
        "bulk_backlinks", 
        "bulk_new_lost_backlinks", 
        "bulk_new_lost_referring_domains", 
        "bulk_referring_domains", 
        "errors", 
        "domain_pages_summary", 
        "timeseries_summary", 
        "timeseries_new_lost_summary", 
        "competitors", 
        "bulk_spam_score", 
        "bulk_pages_summary", 
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

        _dict['summary'] = self.summary.to_dict() if self.summary else None
        _dict['history'] = self.history.to_dict() if self.history else None
        _dict['content_duplicates'] = self.content_duplicates.to_dict() if self.content_duplicates else None
        _dict['domain_intersection'] = self.domain_intersection.to_dict() if self.domain_intersection else None
        _dict['backlinks'] = self.backlinks.to_dict() if self.backlinks else None
        _dict['domain_pages'] = self.domain_pages.to_dict() if self.domain_pages else None
        _dict['anchors'] = self.anchors.to_dict() if self.anchors else None
        _dict['referring_domains'] = self.referring_domains.to_dict() if self.referring_domains else None
        _dict['page_intersection'] = self.page_intersection.to_dict() if self.page_intersection else None
        _dict['referring_networks'] = self.referring_networks.to_dict() if self.referring_networks else None
        _dict['bulk_ranks'] = self.bulk_ranks.to_dict() if self.bulk_ranks else None
        _dict['bulk_backlinks'] = self.bulk_backlinks.to_dict() if self.bulk_backlinks else None
        _dict['bulk_new_lost_backlinks'] = self.bulk_new_lost_backlinks.to_dict() if self.bulk_new_lost_backlinks else None
        _dict['bulk_new_lost_referring_domains'] = self.bulk_new_lost_referring_domains.to_dict() if self.bulk_new_lost_referring_domains else None
        _dict['bulk_referring_domains'] = self.bulk_referring_domains.to_dict() if self.bulk_referring_domains else None
        _dict['errors'] = self.errors
        _dict['domain_pages_summary'] = self.domain_pages_summary.to_dict() if self.domain_pages_summary else None
        _dict['timeseries_summary'] = self.timeseries_summary.to_dict() if self.timeseries_summary else None
        _dict['timeseries_new_lost_summary'] = self.timeseries_new_lost_summary.to_dict() if self.timeseries_new_lost_summary else None
        _dict['competitors'] = self.competitors.to_dict() if self.competitors else None
        _dict['bulk_spam_score'] = self.bulk_spam_score.to_dict() if self.bulk_spam_score else None
        _dict['bulk_pages_summary'] = self.bulk_pages_summary.to_dict() if self.bulk_pages_summary else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
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
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj