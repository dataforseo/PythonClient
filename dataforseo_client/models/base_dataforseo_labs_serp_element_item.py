# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from importlib import import_module
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from dataforseo_client.models.q_answer_box_dataforseo_labs_serp_element_item import QAnswerBoxDataforseoLabsSerpElementItem
    from dataforseo_client.models.carousel_dataforseo_labs_serp_element_item import CarouselDataforseoLabsSerpElementItem
    from dataforseo_client.models.commercial_units_dataforseo_labs_serp_element_item import CommercialUnitsDataforseoLabsSerpElementItem
    from dataforseo_client.models.events_dataforseo_labs_serp_element_item import EventsDataforseoLabsSerpElementItem
    from dataforseo_client.models.featured_snippet_dataforseo_labs_serp_element_item import FeaturedSnippetDataforseoLabsSerpElementItem
    from dataforseo_client.models.find_results_on_dataforseo_labs_serp_element_item import FindResultsOnDataforseoLabsSerpElementItem
    from dataforseo_client.models.google_flights_dataforseo_labs_serp_element_item import GoogleFlightsDataforseoLabsSerpElementItem
    from dataforseo_client.models.google_hotels_dataforseo_labs_serp_element_item import GoogleHotelsDataforseoLabsSerpElementItem
    from dataforseo_client.models.google_posts_dataforseo_labs_serp_element_item import GooglePostsDataforseoLabsSerpElementItem
    from dataforseo_client.models.google_reviews_dataforseo_labs_serp_element_item import GoogleReviewsDataforseoLabsSerpElementItem
    from dataforseo_client.models.hotels_pack_dataforseo_labs_serp_element_item import HotelsPackDataforseoLabsSerpElementItem
    from dataforseo_client.models.images_dataforseo_labs_serp_element_item import ImagesDataforseoLabsSerpElementItem
    from dataforseo_client.models.jobs_dataforseo_labs_serp_element_item import JobsDataforseoLabsSerpElementItem
    from dataforseo_client.models.knowledge_graph_dataforseo_labs_serp_element_item import KnowledgeGraphDataforseoLabsSerpElementItem
    from dataforseo_client.models.knowledge_graph_carousel_item_dataforseo_labs_serp_element_item import KnowledgeGraphCarouselItemDataforseoLabsSerpElementItem
    from dataforseo_client.models.knowledge_graph_description_item_dataforseo_labs_serp_element_item import KnowledgeGraphDescriptionItemDataforseoLabsSerpElementItem
    from dataforseo_client.models.knowledge_graph_expanded_item_dataforseo_labs_serp_element_item import KnowledgeGraphExpandedItemDataforseoLabsSerpElementItem
    from dataforseo_client.models.knowledge_graph_images_item_dataforseo_labs_serp_element_item import KnowledgeGraphImagesItemDataforseoLabsSerpElementItem
    from dataforseo_client.models.knowledge_graph_list_item_dataforseo_labs_serp_element_item import KnowledgeGraphListItemDataforseoLabsSerpElementItem
    from dataforseo_client.models.knowledge_graph_part_item_dataforseo_labs_serp_element_item import KnowledgeGraphPartItemDataforseoLabsSerpElementItem
    from dataforseo_client.models.knowledge_graph_row_item_dataforseo_labs_serp_element_item import KnowledgeGraphRowItemDataforseoLabsSerpElementItem
    from dataforseo_client.models.knowledge_graph_shopping_item_dataforseo_labs_serp_element_item import KnowledgeGraphShoppingItemDataforseoLabsSerpElementItem
    from dataforseo_client.models.local_pack_dataforseo_labs_serp_element_item import LocalPackDataforseoLabsSerpElementItem
    from dataforseo_client.models.local_services_dataforseo_labs_serp_element_item import LocalServicesDataforseoLabsSerpElementItem
    from dataforseo_client.models.map_dataforseo_labs_serp_element_item import MapDataforseoLabsSerpElementItem
    from dataforseo_client.models.math_solver_dataforseo_labs_serp_element_item import MathSolverDataforseoLabsSerpElementItem
    from dataforseo_client.models.mention_carousel_dataforseo_labs_serp_element_item import MentionCarouselDataforseoLabsSerpElementItem
    from dataforseo_client.models.multi_carousel_dataforseo_labs_serp_element_item import MultiCarouselDataforseoLabsSerpElementItem
    from dataforseo_client.models.organic_dataforseo_labs_serp_element_item import OrganicDataforseoLabsSerpElementItem
    from dataforseo_client.models.paid_dataforseo_labs_serp_element_item import PaidDataforseoLabsSerpElementItem
    from dataforseo_client.models.people_also_ask_dataforseo_labs_serp_element_item import PeopleAlsoAskDataforseoLabsSerpElementItem
    from dataforseo_client.models.people_also_search_dataforseo_labs_serp_element_item import PeopleAlsoSearchDataforseoLabsSerpElementItem
    from dataforseo_client.models.podcasts_dataforseo_labs_serp_element_item import PodcastsDataforseoLabsSerpElementItem
    from dataforseo_client.models.popular_products_dataforseo_labs_serp_element_item import PopularProductsDataforseoLabsSerpElementItem
    from dataforseo_client.models.questions_and_answers_dataforseo_labs_serp_element_item import QuestionsAndAnswersDataforseoLabsSerpElementItem
    from dataforseo_client.models.recipes_dataforseo_labs_serp_element_item import RecipesDataforseoLabsSerpElementItem
    from dataforseo_client.models.related_searches_dataforseo_labs_serp_element_item import RelatedSearchesDataforseoLabsSerpElementItem
    from dataforseo_client.models.scholarly_articles_dataforseo_labs_serp_element_item import ScholarlyArticlesDataforseoLabsSerpElementItem
    from dataforseo_client.models.shopping_dataforseo_labs_serp_element_item import ShoppingDataforseoLabsSerpElementItem
    from dataforseo_client.models.stocks_box_dataforseo_labs_serp_element_item import StocksBoxDataforseoLabsSerpElementItem
    from dataforseo_client.models.top_sights_dataforseo_labs_serp_element_item import TopSightsDataforseoLabsSerpElementItem
    from dataforseo_client.models.top_stories_dataforseo_labs_serp_element_item import TopStoriesDataforseoLabsSerpElementItem
    from dataforseo_client.models.twitter_dataforseo_labs_serp_element_item import TwitterDataforseoLabsSerpElementItem
    from dataforseo_client.models.video_dataforseo_labs_serp_element_item import VideoDataforseoLabsSerpElementItem
    from dataforseo_client.models.visual_stories_dataforseo_labs_serp_element_item import VisualStoriesDataforseoLabsSerpElementItem

class BaseDataforseoLabsSerpElementItem(BaseModel):
    """
    BaseDataforseoLabsSerpElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP can take the following values: left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    __properties: ClassVar[List[str]] = ["type", "rank_group", "rank_absolute", "position", "xpath"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    # JSON field name that stores the object type
    __discriminator_property_name: ClassVar[str] = 'type'

    # discriminator mappings
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'answer_box': 'QAnswerBoxDataforseoLabsSerpElementItem','carousel': 'CarouselDataforseoLabsSerpElementItem','commercial_units': 'CommercialUnitsDataforseoLabsSerpElementItem','events': 'EventsDataforseoLabsSerpElementItem','featured_snippet': 'FeaturedSnippetDataforseoLabsSerpElementItem','find_results_on': 'FindResultsOnDataforseoLabsSerpElementItem','google_flights': 'GoogleFlightsDataforseoLabsSerpElementItem','google_hotels': 'GoogleHotelsDataforseoLabsSerpElementItem','google_posts': 'GooglePostsDataforseoLabsSerpElementItem','google_reviews': 'GoogleReviewsDataforseoLabsSerpElementItem','hotels_pack': 'HotelsPackDataforseoLabsSerpElementItem','images': 'ImagesDataforseoLabsSerpElementItem','jobs': 'JobsDataforseoLabsSerpElementItem','knowledge_graph': 'KnowledgeGraphDataforseoLabsSerpElementItem','knowledge_graph_carousel_item': 'KnowledgeGraphCarouselItemDataforseoLabsSerpElementItem','knowledge_graph_description_item': 'KnowledgeGraphDescriptionItemDataforseoLabsSerpElementItem','knowledge_graph_expanded_item': 'KnowledgeGraphExpandedItemDataforseoLabsSerpElementItem','knowledge_graph_images_item': 'KnowledgeGraphImagesItemDataforseoLabsSerpElementItem','knowledge_graph_list_item': 'KnowledgeGraphListItemDataforseoLabsSerpElementItem','knowledge_graph_part_item': 'KnowledgeGraphPartItemDataforseoLabsSerpElementItem','knowledge_graph_row_item': 'KnowledgeGraphRowItemDataforseoLabsSerpElementItem','knowledge_graph_shopping_item': 'KnowledgeGraphShoppingItemDataforseoLabsSerpElementItem','local_pack': 'LocalPackDataforseoLabsSerpElementItem','local_services': 'LocalServicesDataforseoLabsSerpElementItem','map': 'MapDataforseoLabsSerpElementItem','math_solver': 'MathSolverDataforseoLabsSerpElementItem','mention_carousel': 'MentionCarouselDataforseoLabsSerpElementItem','multi_carousel': 'MultiCarouselDataforseoLabsSerpElementItem','organic': 'OrganicDataforseoLabsSerpElementItem','paid': 'PaidDataforseoLabsSerpElementItem','people_also_ask': 'PeopleAlsoAskDataforseoLabsSerpElementItem','people_also_search': 'PeopleAlsoSearchDataforseoLabsSerpElementItem','podcasts': 'PodcastsDataforseoLabsSerpElementItem','popular_products': 'PopularProductsDataforseoLabsSerpElementItem','questions_and_answers': 'QuestionsAndAnswersDataforseoLabsSerpElementItem','recipes': 'RecipesDataforseoLabsSerpElementItem','related_searches': 'RelatedSearchesDataforseoLabsSerpElementItem','scholarly_articles': 'ScholarlyArticlesDataforseoLabsSerpElementItem','shopping': 'ShoppingDataforseoLabsSerpElementItem','stocks_box': 'StocksBoxDataforseoLabsSerpElementItem','top_sights': 'TopSightsDataforseoLabsSerpElementItem','top_stories': 'TopStoriesDataforseoLabsSerpElementItem','twitter': 'TwitterDataforseoLabsSerpElementItem','video': 'VideoDataforseoLabsSerpElementItem','visual_stories': 'VisualStoriesDataforseoLabsSerpElementItem'
    }

    @classmethod
    def get_discriminator_value(cls, obj: Dict[str, Any]) -> Optional[str]:
        """Returns the discriminator value (object type) of the data"""
        discriminator_value = obj[cls.__discriminator_property_name]
        if discriminator_value:
            return cls.__discriminator_value_class_map.get(discriminator_value)
        else:
            return None

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Union[QAnswerBoxDataforseoLabsSerpElementItem, CarouselDataforseoLabsSerpElementItem, CommercialUnitsDataforseoLabsSerpElementItem, EventsDataforseoLabsSerpElementItem, FeaturedSnippetDataforseoLabsSerpElementItem, FindResultsOnDataforseoLabsSerpElementItem, GoogleFlightsDataforseoLabsSerpElementItem, GoogleHotelsDataforseoLabsSerpElementItem, GooglePostsDataforseoLabsSerpElementItem, GoogleReviewsDataforseoLabsSerpElementItem, HotelsPackDataforseoLabsSerpElementItem, ImagesDataforseoLabsSerpElementItem, JobsDataforseoLabsSerpElementItem, KnowledgeGraphDataforseoLabsSerpElementItem, KnowledgeGraphCarouselItemDataforseoLabsSerpElementItem, KnowledgeGraphDescriptionItemDataforseoLabsSerpElementItem, KnowledgeGraphExpandedItemDataforseoLabsSerpElementItem, KnowledgeGraphImagesItemDataforseoLabsSerpElementItem, KnowledgeGraphListItemDataforseoLabsSerpElementItem, KnowledgeGraphPartItemDataforseoLabsSerpElementItem, KnowledgeGraphRowItemDataforseoLabsSerpElementItem, KnowledgeGraphShoppingItemDataforseoLabsSerpElementItem, LocalPackDataforseoLabsSerpElementItem, LocalServicesDataforseoLabsSerpElementItem, MapDataforseoLabsSerpElementItem, MathSolverDataforseoLabsSerpElementItem, MentionCarouselDataforseoLabsSerpElementItem, MultiCarouselDataforseoLabsSerpElementItem, OrganicDataforseoLabsSerpElementItem, PaidDataforseoLabsSerpElementItem, PeopleAlsoAskDataforseoLabsSerpElementItem, PeopleAlsoSearchDataforseoLabsSerpElementItem, PodcastsDataforseoLabsSerpElementItem, PopularProductsDataforseoLabsSerpElementItem, QuestionsAndAnswersDataforseoLabsSerpElementItem, RecipesDataforseoLabsSerpElementItem, RelatedSearchesDataforseoLabsSerpElementItem, ScholarlyArticlesDataforseoLabsSerpElementItem, ShoppingDataforseoLabsSerpElementItem, StocksBoxDataforseoLabsSerpElementItem, TopSightsDataforseoLabsSerpElementItem, TopStoriesDataforseoLabsSerpElementItem, TwitterDataforseoLabsSerpElementItem, VideoDataforseoLabsSerpElementItem, VisualStoriesDataforseoLabsSerpElementItem]]:
        """Create an instance of BaseDataforseoLabsSerpElementItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if rank_group (nullable) is None
        # and model_fields_set contains the field
        if self.rank_group is None and "rank_group" in self.model_fields_set:
            _dict['rank_group'] = None

        # set to None if rank_absolute (nullable) is None
        # and model_fields_set contains the field
        if self.rank_absolute is None and "rank_absolute" in self.model_fields_set:
            _dict['rank_absolute'] = None

        # set to None if position (nullable) is None
        # and model_fields_set contains the field
        if self.position is None and "position" in self.model_fields_set:
            _dict['position'] = None

        # set to None if xpath (nullable) is None
        # and model_fields_set contains the field
        if self.xpath is None and "xpath" in self.model_fields_set:
            _dict['xpath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict[str, Any]) -> Optional[Union[QAnswerBoxDataforseoLabsSerpElementItem, CarouselDataforseoLabsSerpElementItem, CommercialUnitsDataforseoLabsSerpElementItem, EventsDataforseoLabsSerpElementItem, FeaturedSnippetDataforseoLabsSerpElementItem, FindResultsOnDataforseoLabsSerpElementItem, GoogleFlightsDataforseoLabsSerpElementItem, GoogleHotelsDataforseoLabsSerpElementItem, GooglePostsDataforseoLabsSerpElementItem, GoogleReviewsDataforseoLabsSerpElementItem, HotelsPackDataforseoLabsSerpElementItem, ImagesDataforseoLabsSerpElementItem, JobsDataforseoLabsSerpElementItem, KnowledgeGraphDataforseoLabsSerpElementItem, KnowledgeGraphCarouselItemDataforseoLabsSerpElementItem, KnowledgeGraphDescriptionItemDataforseoLabsSerpElementItem, KnowledgeGraphExpandedItemDataforseoLabsSerpElementItem, KnowledgeGraphImagesItemDataforseoLabsSerpElementItem, KnowledgeGraphListItemDataforseoLabsSerpElementItem, KnowledgeGraphPartItemDataforseoLabsSerpElementItem, KnowledgeGraphRowItemDataforseoLabsSerpElementItem, KnowledgeGraphShoppingItemDataforseoLabsSerpElementItem, LocalPackDataforseoLabsSerpElementItem, LocalServicesDataforseoLabsSerpElementItem, MapDataforseoLabsSerpElementItem, MathSolverDataforseoLabsSerpElementItem, MentionCarouselDataforseoLabsSerpElementItem, MultiCarouselDataforseoLabsSerpElementItem, OrganicDataforseoLabsSerpElementItem, PaidDataforseoLabsSerpElementItem, PeopleAlsoAskDataforseoLabsSerpElementItem, PeopleAlsoSearchDataforseoLabsSerpElementItem, PodcastsDataforseoLabsSerpElementItem, PopularProductsDataforseoLabsSerpElementItem, QuestionsAndAnswersDataforseoLabsSerpElementItem, RecipesDataforseoLabsSerpElementItem, RelatedSearchesDataforseoLabsSerpElementItem, ScholarlyArticlesDataforseoLabsSerpElementItem, ShoppingDataforseoLabsSerpElementItem, StocksBoxDataforseoLabsSerpElementItem, TopSightsDataforseoLabsSerpElementItem, TopStoriesDataforseoLabsSerpElementItem, TwitterDataforseoLabsSerpElementItem, VideoDataforseoLabsSerpElementItem, VisualStoriesDataforseoLabsSerpElementItem]]:
        """Create an instance of BaseDataforseoLabsSerpElementItem from a dict"""
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        if object_type ==  'QAnswerBoxDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.q_answer_box_dataforseo_labs_serp_element_item").QAnswerBoxDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'CarouselDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.carousel_dataforseo_labs_serp_element_item").CarouselDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'CommercialUnitsDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.commercial_units_dataforseo_labs_serp_element_item").CommercialUnitsDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'EventsDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.events_dataforseo_labs_serp_element_item").EventsDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'FeaturedSnippetDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.featured_snippet_dataforseo_labs_serp_element_item").FeaturedSnippetDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'FindResultsOnDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.find_results_on_dataforseo_labs_serp_element_item").FindResultsOnDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'GoogleFlightsDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.google_flights_dataforseo_labs_serp_element_item").GoogleFlightsDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'GoogleHotelsDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.google_hotels_dataforseo_labs_serp_element_item").GoogleHotelsDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'GooglePostsDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.google_posts_dataforseo_labs_serp_element_item").GooglePostsDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'GoogleReviewsDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.google_reviews_dataforseo_labs_serp_element_item").GoogleReviewsDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'HotelsPackDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.hotels_pack_dataforseo_labs_serp_element_item").HotelsPackDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'ImagesDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.images_dataforseo_labs_serp_element_item").ImagesDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'JobsDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.jobs_dataforseo_labs_serp_element_item").JobsDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'KnowledgeGraphDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_dataforseo_labs_serp_element_item").KnowledgeGraphDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'KnowledgeGraphCarouselItemDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_carousel_item_dataforseo_labs_serp_element_item").KnowledgeGraphCarouselItemDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'KnowledgeGraphDescriptionItemDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_description_item_dataforseo_labs_serp_element_item").KnowledgeGraphDescriptionItemDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'KnowledgeGraphExpandedItemDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_expanded_item_dataforseo_labs_serp_element_item").KnowledgeGraphExpandedItemDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'KnowledgeGraphImagesItemDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_images_item_dataforseo_labs_serp_element_item").KnowledgeGraphImagesItemDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'KnowledgeGraphListItemDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_list_item_dataforseo_labs_serp_element_item").KnowledgeGraphListItemDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'KnowledgeGraphPartItemDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_part_item_dataforseo_labs_serp_element_item").KnowledgeGraphPartItemDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'KnowledgeGraphRowItemDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_row_item_dataforseo_labs_serp_element_item").KnowledgeGraphRowItemDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'KnowledgeGraphShoppingItemDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_shopping_item_dataforseo_labs_serp_element_item").KnowledgeGraphShoppingItemDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'LocalPackDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.local_pack_dataforseo_labs_serp_element_item").LocalPackDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'LocalServicesDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.local_services_dataforseo_labs_serp_element_item").LocalServicesDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'MapDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.map_dataforseo_labs_serp_element_item").MapDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'MathSolverDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.math_solver_dataforseo_labs_serp_element_item").MathSolverDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'MentionCarouselDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.mention_carousel_dataforseo_labs_serp_element_item").MentionCarouselDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'MultiCarouselDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.multi_carousel_dataforseo_labs_serp_element_item").MultiCarouselDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'OrganicDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.organic_dataforseo_labs_serp_element_item").OrganicDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'PaidDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.paid_dataforseo_labs_serp_element_item").PaidDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'PeopleAlsoAskDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.people_also_ask_dataforseo_labs_serp_element_item").PeopleAlsoAskDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'PeopleAlsoSearchDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.people_also_search_dataforseo_labs_serp_element_item").PeopleAlsoSearchDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'PodcastsDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.podcasts_dataforseo_labs_serp_element_item").PodcastsDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'PopularProductsDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.popular_products_dataforseo_labs_serp_element_item").PopularProductsDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'QuestionsAndAnswersDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.questions_and_answers_dataforseo_labs_serp_element_item").QuestionsAndAnswersDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'RecipesDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.recipes_dataforseo_labs_serp_element_item").RecipesDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'RelatedSearchesDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.related_searches_dataforseo_labs_serp_element_item").RelatedSearchesDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'ScholarlyArticlesDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.scholarly_articles_dataforseo_labs_serp_element_item").ScholarlyArticlesDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'ShoppingDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.shopping_dataforseo_labs_serp_element_item").ShoppingDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'StocksBoxDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.stocks_box_dataforseo_labs_serp_element_item").StocksBoxDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'TopSightsDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.top_sights_dataforseo_labs_serp_element_item").TopSightsDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'TopStoriesDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.top_stories_dataforseo_labs_serp_element_item").TopStoriesDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'TwitterDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.twitter_dataforseo_labs_serp_element_item").TwitterDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'VideoDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.video_dataforseo_labs_serp_element_item").VideoDataforseoLabsSerpElementItem.from_dict(obj)
        if object_type ==  'VisualStoriesDataforseoLabsSerpElementItem':
            return import_module("dataforseo_client.models.visual_stories_dataforseo_labs_serp_element_item").VisualStoriesDataforseoLabsSerpElementItem.from_dict(obj)

        raise ValueError("BaseDataforseoLabsSerpElementItem failed to lookup discriminator value from " +
                            json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                            ", mapping: " + json.dumps(cls.__discriminator_value_class_map))


