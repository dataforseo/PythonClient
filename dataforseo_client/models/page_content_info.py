from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.page_section_content_info import PageSectionContentInfo
from dataforseo_client.models.topic_info import TopicInfo
from dataforseo_client.models.content_rating_info import ContentRatingInfo
from dataforseo_client.models.content_offer_info import ContentOfferInfo
from dataforseo_client.models.content_comment_info import ContentCommentInfo
from dataforseo_client.models.contacts import Contacts



class PageContentInfo(BaseModel):
    """
    PageContentInfo
    """ # noqa: E501
    header: Optional[PageSectionContentInfo] = Field(default=None, description="content of the header of the table")
    footer: Optional[PageSectionContentInfo] = Field(default=None, description="content of the footer of the table")
    main_topic: Optional[List[Optional[TopicInfo]]] = Field(default=None, description="main topic on the page. you can find more information about topic priority calculation in this help center article")
    secondary_topic: Optional[List[Optional[TopicInfo]]] = Field(default=None, description="secondary topic on the page. you can find more information about topic priority calculation in this help center article")
    ratings: Optional[List[Optional[ContentRatingInfo]]] = Field(default=None, description="contains objects with rating information for the products displayed on the page")
    offers: Optional[List[Optional[ContentOfferInfo]]] = Field(default=None, description="array of products displayed on the page. contains objects with information on products displayed on the page")
    comments: Optional[List[Optional[ContentCommentInfo]]] = Field(default=None, description="array of comments displayed on the page. contains objects with information on comments related to displayed products")
    contacts: Optional[Contacts] = Field(default=None, description="contact information. contains contact information displayed on the page")
    __properties: ClassVar[List[str]] = [
        "header", 
        "footer", 
        "main_topic", 
        "secondary_topic", 
        "ratings", 
        "offers", 
        "comments", 
        "contacts", 
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

        _dict['header'] = self.header.to_dict() if self.header else None
        _dict['footer'] = self.footer.to_dict() if self.footer else None
        main_topic_items = []
        if self.main_topic:
            for _item in self.main_topic:
                if _item:
                    main_topic_items.append(_item.to_dict())
            _dict['main_topic'] = main_topic_items
        secondary_topic_items = []
        if self.secondary_topic:
            for _item in self.secondary_topic:
                if _item:
                    secondary_topic_items.append(_item.to_dict())
            _dict['secondary_topic'] = secondary_topic_items
        ratings_items = []
        if self.ratings:
            for _item in self.ratings:
                if _item:
                    ratings_items.append(_item.to_dict())
            _dict['ratings'] = ratings_items
        offers_items = []
        if self.offers:
            for _item in self.offers:
                if _item:
                    offers_items.append(_item.to_dict())
            _dict['offers'] = offers_items
        comments_items = []
        if self.comments:
            for _item in self.comments:
                if _item:
                    comments_items.append(_item.to_dict())
            _dict['comments'] = comments_items
        _dict['contacts'] = self.contacts.to_dict() if self.contacts else None
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "header": PageSectionContentInfo.from_dict(obj["header"]) if obj.get("header") is not None else None,
            "footer": PageSectionContentInfo.from_dict(obj["footer"]) if obj.get("footer") is not None else None,
            "main_topic": [TopicInfo.from_dict(_item) for _item in obj["main_topic"]] if obj.get("main_topic") is not None else None,
            "secondary_topic": [TopicInfo.from_dict(_item) for _item in obj["secondary_topic"]] if obj.get("secondary_topic") is not None else None,
            "ratings": [ContentRatingInfo.from_dict(_item) for _item in obj["ratings"]] if obj.get("ratings") is not None else None,
            "offers": [ContentOfferInfo.from_dict(_item) for _item in obj["offers"]] if obj.get("offers") is not None else None,
            "comments": [ContentCommentInfo.from_dict(_item) for _item in obj["comments"]] if obj.get("comments") is not None else None,
            "contacts": Contacts.from_dict(obj["contacts"]) if obj.get("contacts") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj