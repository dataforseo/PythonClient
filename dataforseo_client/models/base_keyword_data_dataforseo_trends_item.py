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
    from dataforseo_client.models.dataforseo_trends_dataforseo_trends_graph_element_item import DataforseoTrendsDataforseoTrendsGraphElementItem;
    from dataforseo_client.models.dataforseo_trends_subregion_interests_element_item import DataforseoTrendsSubregionInterestsElementItem;
    from dataforseo_client.models.dataforseo_trends_demography_element_item import DataforseoTrendsDemographyElementItem;



class BaseKeywordDataDataforseoTrendsItem(BaseModel):
    """
    BaseKeywordDataDataforseoTrendsItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictInt] = Field(default=None, description="the alignment of the element. can take the following values: 1, 2, 3, 4, etc.")
    keywords: Optional[List[Optional[StrictStr]]] = Field(default=None, description="relevant keywords. the data included in the dataforseo_trends_graph element is based on the keywords listed in this array")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "keywords", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'dataforseo_trends_graph': 'DataforseoTrendsDataforseoTrendsGraphElementItem',
        'subregion_interests': 'DataforseoTrendsSubregionInterestsElementItem',
        'demography': 'DataforseoTrendsDemographyElementItem',
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
        _dict['position'] = self.position
        _dict['keywords'] = self.keywords
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
        DataforseoTrendsDataforseoTrendsGraphElementItem, 
        DataforseoTrendsSubregionInterestsElementItem, 
        DataforseoTrendsDemographyElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'DataforseoTrendsDataforseoTrendsGraphElementItem':
            return import_module("dataforseo_client.models.dataforseo_trends_dataforseo_trends_graph_element_item").DataforseoTrendsDataforseoTrendsGraphElementItem.from_dict(obj)
        if object_type == 'DataforseoTrendsSubregionInterestsElementItem':
            return import_module("dataforseo_client.models.dataforseo_trends_subregion_interests_element_item").DataforseoTrendsSubregionInterestsElementItem.from_dict(obj)
        if object_type == 'DataforseoTrendsDemographyElementItem':
            return import_module("dataforseo_client.models.dataforseo_trends_demography_element_item").DataforseoTrendsDemographyElementItem.from_dict(obj)

        return None