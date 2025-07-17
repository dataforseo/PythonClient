from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.social_metrics_info import SocialMetricsInfo
from dataforseo_client.models.content_rating_info import ContentRatingInfo



class AnalysisContentInfo(BaseModel):
    """
    AnalysisContentInfo
    """ # noqa: E501
    content_type: Optional[StrictStr] = Field(default=None, description="type of content. example:. page_content, comment")
    title: Optional[StrictStr] = Field(default=None, description="title of the result")
    main_title: Optional[StrictStr] = Field(default=None, description="page title")
    previous_title: Optional[StrictStr] = Field(default=None, description="title of the previous content block")
    level: Optional[StrictInt] = Field(default=None, description="title heading level. indicates h-tag level from 1 (top) to 6 (bottom)")
    author: Optional[StrictStr] = Field(default=None, description="author of the content")
    snippet: Optional[StrictStr] = Field(default=None, description="content snippet")
    snippet_length: Optional[StrictInt] = Field(default=None, description="character length of the snippet")
    social_metrics: Optional[List[Optional[SocialMetricsInfo]]] = Field(default=None, description="social media engagement metrics. data on social media interactions associated with the content based on website embeds developed and supported by social media platforms")
    highlighted_text: Optional[StrictStr] = Field(default=None, description="highlighted text from the snippet")
    language: Optional[StrictStr] = Field(default=None, description="content language. to obtain a full list of available languages, refer to the Languages endpoint")
    sentiment_connotations: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="sentiment connotations. contains sentiments (emotional reactions) related to the given citation and probability index per each sentiment. possible sentiment connotations: anger, happiness, love, sadness, share, fun")
    connotation_types: Optional[Dict[str, Optional[StrictInt]]] = Field(default=None, description="connotation types. contains types of sentiments (sentiment polarity) related to the given citation and probability index per each sentiment type. possible sentiment connotation types: positive, negative, neutral")
    text_category: Optional[List[Optional[StrictInt]]] = Field(default=None, description="text category. to obtain a full list of available categories, refer to the Categories endpoint")
    date_published: Optional[StrictStr] = Field(default=None, description="date and time when the content was published. in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2017-01-24 13:20:59 +00:00")
    content_quality_score: Optional[StrictInt] = Field(default=None, description="content quality score. this value is calculated based on the number of words, sentences and characters the content contains")
    semantic_location: Optional[StrictStr] = Field(default=None, description="semantic location. indicates semantic element in HTML where the target keyword citation is located. example:. article, header")
    rating: Optional[ContentRatingInfo] = Field(default=None, description="content rating. rating related to content_info")
    group_date: Optional[StrictStr] = Field(default=None, description="citation group date and time. indicates content publication date or date and time when our crawler visited the page for the first time;. this field can be used to group citations by date and display citation trends;. date and time are provided in the UTC format: “yyyy-mm-dd hh-mm-ss +00:00”. example:. 2017-01-24 13:20:59 +00:00")
    __properties: ClassVar[List[str]] = [
        "content_type", 
        "title", 
        "main_title", 
        "previous_title", 
        "level", 
        "author", 
        "snippet", 
        "snippet_length", 
        "social_metrics", 
        "highlighted_text", 
        "language", 
        "sentiment_connotations", 
        "connotation_types", 
        "text_category", 
        "date_published", 
        "content_quality_score", 
        "semantic_location", 
        "rating", 
        "group_date", 
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

        _dict['content_type'] = self.content_type
        _dict['title'] = self.title
        _dict['main_title'] = self.main_title
        _dict['previous_title'] = self.previous_title
        _dict['level'] = self.level
        _dict['author'] = self.author
        _dict['snippet'] = self.snippet
        _dict['snippet_length'] = self.snippet_length
        social_metrics_items = []
        if self.social_metrics:
            for _item in self.social_metrics:
                if _item:
                    social_metrics_items.append(_item.to_dict())
            _dict['social_metrics'] = social_metrics_items
        _dict['highlighted_text'] = self.highlighted_text
        _dict['language'] = self.language
        _dict['sentiment_connotations'] = self.sentiment_connotations
        _dict['connotation_types'] = self.connotation_types
        _dict['text_category'] = self.text_category
        _dict['date_published'] = self.date_published
        _dict['content_quality_score'] = self.content_quality_score
        _dict['semantic_location'] = self.semantic_location
        _dict['rating'] = self.rating.to_dict() if self.rating else None
        _dict['group_date'] = self.group_date
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "content_type": obj.get("content_type"),
            "title": obj.get("title"),
            "main_title": obj.get("main_title"),
            "previous_title": obj.get("previous_title"),
            "level": obj.get("level"),
            "author": obj.get("author"),
            "snippet": obj.get("snippet"),
            "snippet_length": obj.get("snippet_length"),
            "social_metrics": [SocialMetricsInfo.from_dict(_item) for _item in obj["social_metrics"]] if obj.get("social_metrics") is not None else None,
            "highlighted_text": obj.get("highlighted_text"),
            "language": obj.get("language"),
            "sentiment_connotations": obj.get("sentiment_connotations"),
            "connotation_types": obj.get("connotation_types"),
            "text_category": obj.get("text_category"),
            "date_published": obj.get("date_published"),
            "content_quality_score": obj.get("content_quality_score"),
            "semantic_location": obj.get("semantic_location"),
            "rating": ContentRatingInfo.from_dict(obj["rating"]) if obj.get("rating") is not None else None,
            "group_date": obj.get("group_date"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj