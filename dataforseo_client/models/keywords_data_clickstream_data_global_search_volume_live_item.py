from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.country_distribution import CountryDistribution



class KeywordsDataClickstreamDataGlobalSearchVolumeLiveItem(BaseModel):
    """
    KeywordsDataClickstreamDataGlobalSearchVolumeLiveItem
    """ # noqa: E501
    keyword: Optional[StrictStr] = Field(default=None, description="keyword. keyword is returned with decoded %## (plus symbol ‘+’ will be decoded to a space character)")
    search_volume: Optional[StrictInt] = Field(default=None, description="clickstream-based average monthly search volume rate. represents the (approximate) number of searches for the given keyword idea based on clickstream. you can learn more about clickstream search volume in this Help Center article")
    country_distribution: Optional[List[Optional[CountryDistribution]]] = Field(default=None, description="distribution of clickstream by countries. represents clickstream-based search volume in available countries, as well as its respective percentage of global search volume")
    __properties: ClassVar[List[str]] = [
        "keyword", 
        "search_volume", 
        "country_distribution", 
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

        _dict['keyword'] = self.keyword
        _dict['search_volume'] = self.search_volume
        country_distribution_items = []
        if self.country_distribution:
            for _item in self.country_distribution:
                if _item:
                    country_distribution_items.append(_item.to_dict())
            _dict['country_distribution'] = country_distribution_items
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword": obj.get("keyword"),
            "search_volume": obj.get("search_volume"),
            "country_distribution": [CountryDistribution.from_dict(_item) for _item in obj["country_distribution"]] if obj.get("country_distribution") is not None else None,
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj