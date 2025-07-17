from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class Autocomplete(BaseModel):
    """
    Autocomplete
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    relevance: Optional[StrictInt] = Field(default=None, description="relevance of suggested keyword. represents the relevant of the autocomplete suggestion to the target keyword. can take values from 500 to 2000. the higher the value, the more relevant is the suggestion. Note: only available for the following client:. chrome/chrome-omni")
    suggestion: Optional[StrictStr] = Field(default=None, description="google autocomplete keyword suggestion")
    suggestion_type: Optional[StrictStr] = Field(default=None, description="google autocomplete suggestion type. Note: only available for the following client:. chrome/chrome-omni")
    search_query_url: Optional[StrictStr] = Field(default=None, description="url to search results. url to search results relevant to the google autocomplete suggestion")
    thumbnail_url: Optional[StrictStr] = Field(default=None, description="url of the thumbnail image. url of the thumbnail image of the google autocomplete suggestion. Note: only available for the following client:. gws-wiz. gws-wiz-serp")
    highlighted: Optional[List[Optional[StrictStr]]] = Field(default=None, description="keywords highlighted in autocomplete. contains a list of google autocomplete suggestions that are highlighted in the search bar;. Note: array is only available for the following client:. gws-wiz. psy-ab. gws-wiz-local")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "relevance", 
        "suggestion", 
        "suggestion_type", 
        "search_query_url", 
        "thumbnail_url", 
        "highlighted", 
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
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['relevance'] = self.relevance
        _dict['suggestion'] = self.suggestion
        _dict['suggestion_type'] = self.suggestion_type
        _dict['search_query_url'] = self.search_query_url
        _dict['thumbnail_url'] = self.thumbnail_url
        _dict['highlighted'] = self.highlighted
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "rank_group": obj.get("rank_group"),
            "rank_absolute": obj.get("rank_absolute"),
            "relevance": obj.get("relevance"),
            "suggestion": obj.get("suggestion"),
            "suggestion_type": obj.get("suggestion_type"),
            "search_query_url": obj.get("search_query_url"),
            "thumbnail_url": obj.get("thumbnail_url"),
            "highlighted": obj.get("highlighted"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj