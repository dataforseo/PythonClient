from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_mode_images_element_info import AiModeImagesElementInfo



class AiModeAiOverviewPaidElementInfo(BaseModel):
    """
    AiModeAiOverviewPaidElementInfo
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    title: Optional[StrictStr] = Field(default=None, description=r"*title of the element in SERP*")
    url: Optional[StrictStr] = Field(default=None, description=r"*reference page URL*")
    domain: Optional[StrictStr] = Field(default=None, description=r"*domain name of the reference*")
    ad_aclk: Optional[StrictStr] = Field(default=None, description=r"*unique ad click referral parameter*. using this parameter you can get a URL of the advertisement in [Google Shopping Sellers Ad URL](https://docs.dataforseo.com/v3/merchant/google/sellers/ad_url/)")
    website_name: Optional[StrictStr] = Field(default=None, description=r"*displayed name of the advertiser's website*")
    breadcrumb: Optional[StrictStr] = Field(default=None, description=r"*breadcrumb path displayed in the ad*")
    snippet: Optional[StrictStr] = Field(default=None, description=r"*description text of the ad*")
    images: Optional[List[Optional[AiModeImagesElementInfo]]] = Field(default=None, description=r"*images present in the ad*. if there are none, equals `null`")
    __properties: ClassVar[List[str]] = [
        "type", 
        "title", 
        "url", 
        "domain", 
        "ad_aclk", 
        "website_name", 
        "breadcrumb", 
        "snippet", 
        "images", 
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

        _dict['type'] = self.type
        _dict['title'] = self.title
        _dict['url'] = self.url
        _dict['domain'] = self.domain
        _dict['ad_aclk'] = self.ad_aclk
        _dict['website_name'] = self.website_name
        _dict['breadcrumb'] = self.breadcrumb
        _dict['snippet'] = self.snippet
        images_items = []
        if self.images:
            for _item in self.images:
                if _item:
                    images_items.append(_item.to_dict())
            _dict['images'] = images_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "url": obj.get("url"),
            "domain": obj.get("domain"),
            "ad_aclk": obj.get("ad_aclk"),
            "website_name": obj.get("website_name"),
            "breadcrumb": obj.get("breadcrumb"),
            "snippet": obj.get("snippet"),
            "images": [AiModeImagesElementInfo.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj