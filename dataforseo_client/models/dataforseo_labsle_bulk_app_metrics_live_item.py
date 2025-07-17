from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.app_metrics_info import AppMetricsInfo



class DataforseoLabsleBulkAppMetricsLiveItem(BaseModel):
    """
    DataforseoLabsleBulkAppMetricsLiveItem
    """ # noqa: E501
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    app_id: Optional[StrictStr] = Field(default=None, description="id of the app in a POST array")
    metrics: Optional[Dict[str, Optional[AppMetricsInfo]]] = Field(default=None, description="metrics for the ranking keywords of the app. ranking data relevant to the keywords that the provided application ranks for on Google Play")
    __properties: ClassVar[List[str]] = [
        "se_type", 
        "app_id", 
        "metrics", 
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

        _dict['se_type'] = self.se_type
        _dict['app_id'] = self.app_id
        _dict['metrics'] = self.metrics
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "se_type": obj.get("se_type"),
            "app_id": obj.get("app_id"),
            "metrics": obj.get("metrics"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj