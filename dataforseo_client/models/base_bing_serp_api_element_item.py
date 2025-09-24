from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self

from dataforseo_client.models.ai_mode_rectangle_info import AiModeRectangleInfo

from importlib import import_module
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dataforseo_client.models.bing_organic_serp_element_item import BingOrganicSerpElementItem;
    from dataforseo_client.models.bing_paid_serp_element_item import BingPaidSerpElementItem;
    from dataforseo_client.models.bing_featured_snippet_serp_element_item import BingFeaturedSnippetSerpElementItem;
    from dataforseo_client.models.bing_related_searches_serp_element_item import BingRelatedSearchesSerpElementItem;
    from dataforseo_client.models.bing_ai_overview_serp_element_item import BingAiOverviewSerpElementItem;
    from dataforseo_client.models.bing_images_serp_element_item import BingImagesSerpElementItem;
    from dataforseo_client.models.bing_video_serp_element_item import BingVideoSerpElementItem;
    from dataforseo_client.models.bing_shopping_serp_element_item import BingShoppingSerpElementItem;
    from dataforseo_client.models.bing_answer_box_serp_element_item import BingAnswerBoxSerpElementItem;
    from dataforseo_client.models.bing_local_pack_serp_element_item import BingLocalPackSerpElementItem;
    from dataforseo_client.models.bing_questions_and_answers_serp_element_item import BingQuestionsAndAnswersSerpElementItem;
    from dataforseo_client.models.bing_hotels_pack_serp_element_item import BingHotelsPackSerpElementItem;
    from dataforseo_client.models.bing_jobs_serp_element_item import BingJobsSerpElementItem;
    from dataforseo_client.models.bing_top_stories_serp_element_item import BingTopStoriesSerpElementItem;
    from dataforseo_client.models.bing_carousel_serp_element_item import BingCarouselSerpElementItem;
    from dataforseo_client.models.bing_map_serp_element_item import BingMapSerpElementItem;
    from dataforseo_client.models.bing_events_serp_element_item import BingEventsSerpElementItem;
    from dataforseo_client.models.bing_recipes_serp_element_item import BingRecipesSerpElementItem;
    from dataforseo_client.models.bing_people_also_ask_serp_element_item import BingPeopleAlsoAskSerpElementItem;
    from dataforseo_client.models.bing_people_also_search_serp_element_item import BingPeopleAlsoSearchSerpElementItem;



class BaseBingSerpApiElementItem(BaseModel):
    """
    BaseBingSerpApiElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description=r"group rank in SERP. position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description=r"absolute rank in SERP. absolute position among all the elements in SERP")
    page: Optional[StrictInt] = Field(default=None, description=r"search results page number. indicates the number of the SERP page on which the element is located")
    position: Optional[StrictStr] = Field(default=None, description=r"the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description=r"the XPath of the element")
    rectangle: Optional[AiModeRectangleInfo] = Field(default=None, description=r"rectangle parameters. contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP. equals null if calculate_rectangles in the POST request is not set to true")
    __properties: ClassVar[List[str]] = [
        "type", 
        "rank_group", 
        "rank_absolute", 
        "page", 
        "position", 
        "xpath", 
        "rectangle", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'organic': 'BingOrganicSerpElementItem',
        'paid': 'BingPaidSerpElementItem',
        'featured_snippet': 'BingFeaturedSnippetSerpElementItem',
        'related_searches': 'BingRelatedSearchesSerpElementItem',
        'ai_overview': 'BingAiOverviewSerpElementItem',
        'images': 'BingImagesSerpElementItem',
        'video': 'BingVideoSerpElementItem',
        'shopping': 'BingShoppingSerpElementItem',
        'answer_box': 'BingAnswerBoxSerpElementItem',
        'local_pack': 'BingLocalPackSerpElementItem',
        'questions_and_answers': 'BingQuestionsAndAnswersSerpElementItem',
        'hotels_pack': 'BingHotelsPackSerpElementItem',
        'jobs': 'BingJobsSerpElementItem',
        'top_stories': 'BingTopStoriesSerpElementItem',
        'carousel': 'BingCarouselSerpElementItem',
        'map': 'BingMapSerpElementItem',
        'events': 'BingEventsSerpElementItem',
        'recipes': 'BingRecipesSerpElementItem',
        'people_also_ask': 'BingPeopleAlsoAskSerpElementItem',
        'people_also_search': 'BingPeopleAlsoSearchSerpElementItem',
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
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['page'] = self.page
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
        _dict['rectangle'] = self.rectangle.to_dict() if self.rectangle else None
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
        BingOrganicSerpElementItem, 
        BingPaidSerpElementItem, 
        BingFeaturedSnippetSerpElementItem, 
        BingRelatedSearchesSerpElementItem, 
        BingAiOverviewSerpElementItem, 
        BingImagesSerpElementItem, 
        BingVideoSerpElementItem, 
        BingShoppingSerpElementItem, 
        BingAnswerBoxSerpElementItem, 
        BingLocalPackSerpElementItem, 
        BingQuestionsAndAnswersSerpElementItem, 
        BingHotelsPackSerpElementItem, 
        BingJobsSerpElementItem, 
        BingTopStoriesSerpElementItem, 
        BingCarouselSerpElementItem, 
        BingMapSerpElementItem, 
        BingEventsSerpElementItem, 
        BingRecipesSerpElementItem, 
        BingPeopleAlsoAskSerpElementItem, 
        BingPeopleAlsoSearchSerpElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'BingOrganicSerpElementItem':
            return import_module("dataforseo_client.models.bing_organic_serp_element_item").BingOrganicSerpElementItem.from_dict(obj)
        if object_type == 'BingPaidSerpElementItem':
            return import_module("dataforseo_client.models.bing_paid_serp_element_item").BingPaidSerpElementItem.from_dict(obj)
        if object_type == 'BingFeaturedSnippetSerpElementItem':
            return import_module("dataforseo_client.models.bing_featured_snippet_serp_element_item").BingFeaturedSnippetSerpElementItem.from_dict(obj)
        if object_type == 'BingRelatedSearchesSerpElementItem':
            return import_module("dataforseo_client.models.bing_related_searches_serp_element_item").BingRelatedSearchesSerpElementItem.from_dict(obj)
        if object_type == 'BingAiOverviewSerpElementItem':
            return import_module("dataforseo_client.models.bing_ai_overview_serp_element_item").BingAiOverviewSerpElementItem.from_dict(obj)
        if object_type == 'BingImagesSerpElementItem':
            return import_module("dataforseo_client.models.bing_images_serp_element_item").BingImagesSerpElementItem.from_dict(obj)
        if object_type == 'BingVideoSerpElementItem':
            return import_module("dataforseo_client.models.bing_video_serp_element_item").BingVideoSerpElementItem.from_dict(obj)
        if object_type == 'BingShoppingSerpElementItem':
            return import_module("dataforseo_client.models.bing_shopping_serp_element_item").BingShoppingSerpElementItem.from_dict(obj)
        if object_type == 'BingAnswerBoxSerpElementItem':
            return import_module("dataforseo_client.models.bing_answer_box_serp_element_item").BingAnswerBoxSerpElementItem.from_dict(obj)
        if object_type == 'BingLocalPackSerpElementItem':
            return import_module("dataforseo_client.models.bing_local_pack_serp_element_item").BingLocalPackSerpElementItem.from_dict(obj)
        if object_type == 'BingQuestionsAndAnswersSerpElementItem':
            return import_module("dataforseo_client.models.bing_questions_and_answers_serp_element_item").BingQuestionsAndAnswersSerpElementItem.from_dict(obj)
        if object_type == 'BingHotelsPackSerpElementItem':
            return import_module("dataforseo_client.models.bing_hotels_pack_serp_element_item").BingHotelsPackSerpElementItem.from_dict(obj)
        if object_type == 'BingJobsSerpElementItem':
            return import_module("dataforseo_client.models.bing_jobs_serp_element_item").BingJobsSerpElementItem.from_dict(obj)
        if object_type == 'BingTopStoriesSerpElementItem':
            return import_module("dataforseo_client.models.bing_top_stories_serp_element_item").BingTopStoriesSerpElementItem.from_dict(obj)
        if object_type == 'BingCarouselSerpElementItem':
            return import_module("dataforseo_client.models.bing_carousel_serp_element_item").BingCarouselSerpElementItem.from_dict(obj)
        if object_type == 'BingMapSerpElementItem':
            return import_module("dataforseo_client.models.bing_map_serp_element_item").BingMapSerpElementItem.from_dict(obj)
        if object_type == 'BingEventsSerpElementItem':
            return import_module("dataforseo_client.models.bing_events_serp_element_item").BingEventsSerpElementItem.from_dict(obj)
        if object_type == 'BingRecipesSerpElementItem':
            return import_module("dataforseo_client.models.bing_recipes_serp_element_item").BingRecipesSerpElementItem.from_dict(obj)
        if object_type == 'BingPeopleAlsoAskSerpElementItem':
            return import_module("dataforseo_client.models.bing_people_also_ask_serp_element_item").BingPeopleAlsoAskSerpElementItem.from_dict(obj)
        if object_type == 'BingPeopleAlsoSearchSerpElementItem':
            return import_module("dataforseo_client.models.bing_people_also_search_serp_element_item").BingPeopleAlsoSearchSerpElementItem.from_dict(obj)

        return None