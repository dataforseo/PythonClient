from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class SerpGoogleDatasetInfoTaskPostRequestInfo(BaseModel):
    """
    SerpGoogleDatasetInfoTaskPostRequestInfo
    """ # noqa: E501
    dataset_id: Optional[StrictStr] = Field(default=None, description=r"ID of the datasetrequired fieldyou can find dataset ID in the dataset URL or dataset item of Google Dataset Search resultexample:L2cvMTFqbl85ZHN6MQ==")
    language_code: Optional[StrictStr] = Field(default=None, description=r"search engine language codeoptional fieldif you use this field, you don't need to specify language_namepossible value:en")
    priority: Optional[StrictInt] = Field(default=None, description=r"task priorityoptional fieldcan take the following values:1 – normal execution priority (set by default)2 – high execution priority. You will be additionally charged for the tasks with high execution priority.The cost can be calculated on the Pricing page.")
    device: Optional[StrictStr] = Field(default=None, description=r"device typeoptional fieldreturn results for a specific device typepossible value: desktop")
    pingback_url: Optional[StrictStr] = Field(default=None, description=r"notification URL of a completed taskoptional fieldwhen a task is completed we will notify you by GET request sent to the URL you have specifiedyou can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the request.example:http://your-server.com/pingscript?id=$idhttp://your-server.com/pingscript?id=$id&tag=$tagNote: special characters in pingback_url will be urlencoded;i.a., the # character will be encoded into %23. learn more on our Help Center")
    postback_url: Optional[StrictStr] = Field(default=None, description=r"URL for sending task resultsoptional fieldonce the task is completed, we will send a POST request with its results compressed in the gzip format to the postback_url you specifiedyou can use the ‘$id’ string as a $id variable and ‘$tag’ as urlencoded $tag variable. We will set the necessary values before sending the requestexample:http://your-server.com/postbackscript?id=$idhttp://your-server.com/postbackscript?id=$id&tag=$tagNote: special characters in postback_url will be urlencoded;i.a., the # character will be encoded into %23. learn more on our Help Center")
    postback_data: Optional[StrictStr] = Field(default=None, description=r"postback_url datatyperequired field if you specify postback_urlcorresponds to the datatype that will be sent to your serverpossible value: advanced")
    __properties: ClassVar[List[str]] = [
        "dataset_id", 
        "language_code", 
        "priority", 
        "device", 
        "pingback_url", 
        "postback_url", 
        "postback_data", 
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

        _dict['dataset_id'] = self.dataset_id
        _dict['language_code'] = self.language_code
        _dict['priority'] = self.priority
        _dict['device'] = self.device
        _dict['pingback_url'] = self.pingback_url
        _dict['postback_url'] = self.postback_url
        _dict['postback_data'] = self.postback_data
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataset_id": obj.get("dataset_id"),
            "language_code": obj.get("language_code"),
            "priority": obj.get("priority"),
            "device": obj.get("device"),
            "pingback_url": obj.get("pingback_url"),
            "postback_url": obj.get("postback_url"),
            "postback_data": obj.get("postback_data"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj