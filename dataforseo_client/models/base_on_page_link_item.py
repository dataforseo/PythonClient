from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self


from importlib import import_module
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dataforseo_client.models.on_page_anchor_link_item import OnPageAnchorLinkItem;
    from dataforseo_client.models.on_page_image_link_item import OnPageImageLinkItem;
    from dataforseo_client.models.on_page_canonical_link_item import OnPageCanonicalLinkItem;
    from dataforseo_client.models.on_page_alternate_link_item import OnPageAlternateLinkItem;
    from dataforseo_client.models.on_page_link_link_item import OnPageLinkLinkItem;
    from dataforseo_client.models.on_page_redirect_link_item import OnPageRedirectLinkItem;
    from dataforseo_client.models.on_page_meta_link_item import OnPageMetaLinkItem;



class BaseOnPageLinkItem(BaseModel):
    """
    BaseOnPageLinkItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    domain_from: Optional[StrictStr] = Field(default=None, description="referring domain. the link was found on this domain")
    domain_to: Optional[StrictStr] = Field(default=None, description="referenced domain. the link is pointing to this domain")
    page_from: Optional[StrictStr] = Field(default=None, description="referring page. relative URL of the page on which the link was found")
    page_to: Optional[StrictStr] = Field(default=None, description="referenced page. relative URL of the page to which the link is pointing")
    link_from: Optional[StrictStr] = Field(default=None, description="referring page. absolute URL of the page on which the link was found")
    link_to: Optional[StrictStr] = Field(default=None, description="referenced page. absolute URL of the page to which the link is pointing")
    dofollow: Optional[StrictBool] = Field(default=None, description="indicates whether the link is dofollow. if the value is true, the link doesn’t have a rel='nofollow' attribute")
    page_from_scheme: Optional[StrictStr] = Field(default=None, description="url scheme of the referring page")
    page_to_scheme: Optional[StrictStr] = Field(default=None, description="url scheme of the referenced page")
    direction: Optional[StrictStr] = Field(default=None, description="direction of the link. possible values: internal, external")
    is_broken: Optional[StrictBool] = Field(default=None, description="link is broken. indicates whether a link is directing to a broken page or resource")
    is_link_relation_conflict: Optional[StrictBool] = Field(default=None, description="indicates that the link may have a conflict with another link. if true, at least one link pointing to link_to has a rel='nofollow' attribute and at least one is dofollow")
    page_to_status_code: Optional[StrictInt] = Field(default=None, description="status code of the referenced page. status code of the page to which the link is pointing")
    __properties: ClassVar[List[str]] = [
        "type", 
        "domain_from", 
        "domain_to", 
        "page_from", 
        "page_to", 
        "link_from", 
        "link_to", 
        "dofollow", 
        "page_from_scheme", 
        "page_to_scheme", 
        "direction", 
        "is_broken", 
        "is_link_relation_conflict", 
        "page_to_status_code", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'anchor': 'OnPageAnchorLinkItem',
        'image': 'OnPageImageLinkItem',
        'canonical': 'OnPageCanonicalLinkItem',
        'alternate': 'OnPageAlternateLinkItem',
        'link': 'OnPageLinkLinkItem',
        'redirect': 'OnPageRedirectLinkItem',
        'meta': 'OnPageMetaLinkItem',
    }

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
        _dict['domain_from'] = self.domain_from
        _dict['domain_to'] = self.domain_to
        _dict['page_from'] = self.page_from
        _dict['page_to'] = self.page_to
        _dict['link_from'] = self.link_from
        _dict['link_to'] = self.link_to
        _dict['dofollow'] = self.dofollow
        _dict['page_from_scheme'] = self.page_from_scheme
        _dict['page_to_scheme'] = self.page_to_scheme
        _dict['direction'] = self.direction
        _dict['is_broken'] = self.is_broken
        _dict['is_link_relation_conflict'] = self.is_link_relation_conflict
        _dict['page_to_status_code'] = self.page_to_status_code
        return _dict


    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None
    
    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[
        OnPageAnchorLinkItem, 
        OnPageImageLinkItem, 
        OnPageCanonicalLinkItem, 
        OnPageAlternateLinkItem, 
        OnPageLinkLinkItem, 
        OnPageRedirectLinkItem, 
        OnPageMetaLinkItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'OnPageAnchorLinkItem':
            return import_module("dataforseo_client.models.on_page_anchor_link_item").OnPageAnchorLinkItem.from_dict(obj)
        if object_type == 'OnPageImageLinkItem':
            return import_module("dataforseo_client.models.on_page_image_link_item").OnPageImageLinkItem.from_dict(obj)
        if object_type == 'OnPageCanonicalLinkItem':
            return import_module("dataforseo_client.models.on_page_canonical_link_item").OnPageCanonicalLinkItem.from_dict(obj)
        if object_type == 'OnPageAlternateLinkItem':
            return import_module("dataforseo_client.models.on_page_alternate_link_item").OnPageAlternateLinkItem.from_dict(obj)
        if object_type == 'OnPageLinkLinkItem':
            return import_module("dataforseo_client.models.on_page_link_link_item").OnPageLinkLinkItem.from_dict(obj)
        if object_type == 'OnPageRedirectLinkItem':
            return import_module("dataforseo_client.models.on_page_redirect_link_item").OnPageRedirectLinkItem.from_dict(obj)
        if object_type == 'OnPageMetaLinkItem':
            return import_module("dataforseo_client.models.on_page_meta_link_item").OnPageMetaLinkItem.from_dict(obj)

        raise ValueError("BaseSerpElementItem failed to lookup discriminator value from " +
                         json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                         ", mapping: " + json.dumps(cls.__discriminator_value_class_map))