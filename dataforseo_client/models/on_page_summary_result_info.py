from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.crawl_status_info import CrawlStatusInfo
from dataforseo_client.models.domain_info import DomainInfo
from dataforseo_client.models.page_metrics import PageMetrics



class OnPageSummaryResultInfo(BaseModel):
    """
    OnPageSummaryResultInfo
    """ # noqa: E501
    crawl_progress: Optional[StrictStr] = Field(default=None, description="status of the crawling session. possible values: in_progress, finished")
    crawl_status: Optional[CrawlStatusInfo] = Field(default=None, description="details of the crawling session")
    crawl_gateway_address: Optional[StrictStr] = Field(default=None, description="crawler ip address. displays the IP address used by the crawler to initiate the current crawling session. you can find the full list of IPs used by our crawler in the Overview section")
    crawl_stop_reason: Optional[StrictStr] = Field(default=None, description="reason why the crawling stopped. information about the reason why the crawling process stopped;. possible values:. limit_exceeded – the limit set in the max_crawl_pages was exceeded;. empty_queue – all URLs in the queue were crawled;. force_stopped – the crawling process was halted using the On Page API Force Stop function;. unexpected_exception – an internal error was encountered while crawling the target, contact support for more info")
    domain_info: Optional[DomainInfo] = Field(default=None, description="domain-wide info. on-page information about the target domain and crawling process")
    page_metrics: Optional[PageMetrics] = Field(default=None, description="page-specific info. metrics information on the target website pages")
    __properties: ClassVar[List[str]] = [
        "crawl_progress", 
        "crawl_status", 
        "crawl_gateway_address", 
        "crawl_stop_reason", 
        "domain_info", 
        "page_metrics", 
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

        _dict['crawl_progress'] = self.crawl_progress
        _dict['crawl_status'] = self.crawl_status.to_dict() if self.crawl_status else None
        _dict['crawl_gateway_address'] = self.crawl_gateway_address
        _dict['crawl_stop_reason'] = self.crawl_stop_reason
        _dict['domain_info'] = self.domain_info.to_dict() if self.domain_info else None
        _dict['page_metrics'] = self.page_metrics.to_dict() if self.page_metrics else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "crawl_progress": obj.get("crawl_progress"),
            "crawl_status": CrawlStatusInfo.from_dict(obj["crawl_status"]) if obj.get("crawl_status") is not None else None,
            "crawl_gateway_address": obj.get("crawl_gateway_address"),
            "crawl_stop_reason": obj.get("crawl_stop_reason"),
            "domain_info": DomainInfo.from_dict(obj["domain_info"]) if obj.get("domain_info") is not None else None,
            "page_metrics": PageMetrics.from_dict(obj["page_metrics"]) if obj.get("page_metrics") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj