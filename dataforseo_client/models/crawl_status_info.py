from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class CrawlStatusInfo(BaseModel):
    """
    CrawlStatusInfo
    """ # noqa: E501
    max_crawl_pages: Optional[StrictInt] = Field(default=None, description="maximum number of pages to crawl.  indicates the max_crawl_pages limit you specified when setting a task")
    pages_in_queue: Optional[StrictInt] = Field(default=None, description="number of pages that are currently in the crawling queue")
    pages_crawled: Optional[StrictInt] = Field(default=None, description="number of crawled pages")
    __properties: ClassVar[List[str]] = [
        "max_crawl_pages", 
        "pages_in_queue", 
        "pages_crawled", 
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

        _dict['max_crawl_pages'] = self.max_crawl_pages
        _dict['pages_in_queue'] = self.pages_in_queue
        _dict['pages_crawled'] = self.pages_crawled
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "max_crawl_pages": obj.get("max_crawl_pages"),
            "pages_in_queue": obj.get("pages_in_queue"),
            "pages_crawled": obj.get("pages_crawled"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj