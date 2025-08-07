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
    from dataforseo_client.models.paid_serp_element_item import PaidSerpElementItem;
    from dataforseo_client.models.organic_serp_element_item import OrganicSerpElementItem;
    from dataforseo_client.models.featured_snippet_serp_element_item import FeaturedSnippetSerpElementItem;
    from dataforseo_client.models.knowledge_graph_serp_element_item import KnowledgeGraphSerpElementItem;
    from dataforseo_client.models.top_stories_serp_element_item import TopStoriesSerpElementItem;
    from dataforseo_client.models.people_also_ask_serp_element_item import PeopleAlsoAskSerpElementItem;
    from dataforseo_client.models.people_also_search_serp_element_item import PeopleAlsoSearchSerpElementItem;
    from dataforseo_client.models.images_serp_element_item import ImagesSerpElementItem;
    from dataforseo_client.models.twitter_serp_element_item import TwitterSerpElementItem;
    from dataforseo_client.models.google_reviews_serp_element_item import GoogleReviewsSerpElementItem;
    from dataforseo_client.models.jobs_serp_element_item import JobsSerpElementItem;
    from dataforseo_client.models.map_serp_element_item import MapSerpElementItem;
    from dataforseo_client.models.app_serp_element_item import AppSerpElementItem;
    from dataforseo_client.models.local_pack_serp_element_item import LocalPackSerpElementItem;
    from dataforseo_client.models.carousel_serp_element_item import CarouselSerpElementItem;
    from dataforseo_client.models.video_serp_element_item import VideoSerpElementItem;
    from dataforseo_client.models.answer_box_serp_element_item import AnswerBoxSerpElementItem;
    from dataforseo_client.models.shopping_serp_element_item import ShoppingSerpElementItem;
    from dataforseo_client.models.google_flights_serp_element_item import GoogleFlightsSerpElementItem;
    from dataforseo_client.models.mention_carousel_serp_element_item import MentionCarouselSerpElementItem;
    from dataforseo_client.models.events_serp_element_item import EventsSerpElementItem;
    from dataforseo_client.models.related_searches_serp_element_item import RelatedSearchesSerpElementItem;
    from dataforseo_client.models.multi_carousel_serp_element_item import MultiCarouselSerpElementItem;
    from dataforseo_client.models.recipes_serp_element_item import RecipesSerpElementItem;
    from dataforseo_client.models.top_sights_serp_element_item import TopSightsSerpElementItem;
    from dataforseo_client.models.scholarly_articles_serp_element_item import ScholarlyArticlesSerpElementItem;
    from dataforseo_client.models.popular_products_serp_element_item import PopularProductsSerpElementItem;
    from dataforseo_client.models.podcasts_serp_element_item import PodcastsSerpElementItem;
    from dataforseo_client.models.stocks_box_serp_element_item import StocksBoxSerpElementItem;
    from dataforseo_client.models.find_results_on_serp_element_item import FindResultsOnSerpElementItem;
    from dataforseo_client.models.questions_and_answers_serp_element_item import QuestionsAndAnswersSerpElementItem;
    from dataforseo_client.models.hotels_pack_serp_element_item import HotelsPackSerpElementItem;
    from dataforseo_client.models.visual_stories_serp_element_item import VisualStoriesSerpElementItem;
    from dataforseo_client.models.commercial_units_serp_element_item import CommercialUnitsSerpElementItem;
    from dataforseo_client.models.local_services_serp_element_item import LocalServicesSerpElementItem;
    from dataforseo_client.models.google_hotels_serp_element_item import GoogleHotelsSerpElementItem;
    from dataforseo_client.models.math_solver_serp_element_item import MathSolverSerpElementItem;
    from dataforseo_client.models.currency_box_serp_element_item import CurrencyBoxSerpElementItem;
    from dataforseo_client.models.google_posts_serp_element_item import GooglePostsSerpElementItem;
    from dataforseo_client.models.product_considerations_serp_element_item import ProductConsiderationsSerpElementItem;
    from dataforseo_client.models.found_on_web_serp_element_item import FoundOnWebSerpElementItem;
    from dataforseo_client.models.short_videos_serp_element_item import ShortVideosSerpElementItem;
    from dataforseo_client.models.refine_products_serp_element_item import RefineProductsSerpElementItem;
    from dataforseo_client.models.explore_brands_serp_element_item import ExploreBrandsSerpElementItem;
    from dataforseo_client.models.perspectives_serp_element_item import PerspectivesSerpElementItem;
    from dataforseo_client.models.discussions_and_forums_serp_element_item import DiscussionsAndForumsSerpElementItem;
    from dataforseo_client.models.compare_sites_serp_element_item import CompareSitesSerpElementItem;
    from dataforseo_client.models.courses_serp_element_item import CoursesSerpElementItem;
    from dataforseo_client.models.knowledge_graph_carousel_item_serp_element_item import KnowledgeGraphCarouselItemSerpElementItem;
    from dataforseo_client.models.knowledge_graph_description_item_serp_element_item import KnowledgeGraphDescriptionItemSerpElementItem;
    from dataforseo_client.models.knowledge_graph_images_item_serp_element_item import KnowledgeGraphImagesItemSerpElementItem;
    from dataforseo_client.models.knowledge_graph_list_item_serp_element_item import KnowledgeGraphListItemSerpElementItem;
    from dataforseo_client.models.knowledge_graph_row_item_serp_element_item import KnowledgeGraphRowItemSerpElementItem;
    from dataforseo_client.models.knowledge_graph_hotels_booking_item_serp_element_item import KnowledgeGraphHotelsBookingItemSerpElementItem;
    from dataforseo_client.models.knowledge_graph_expanded_item_serp_element_item import KnowledgeGraphExpandedItemSerpElementItem;
    from dataforseo_client.models.knowledge_graph_part_item_serp_element_item import KnowledgeGraphPartItemSerpElementItem;
    from dataforseo_client.models.knowledge_graph_shopping_item_serp_element_item import KnowledgeGraphShoppingItemSerpElementItem;
    from dataforseo_client.models.knowledge_graph_ai_overview_item_serp_element_item import KnowledgeGraphAiOverviewItemSerpElementItem;
    from dataforseo_client.models.ai_overview_serp_element_item import AiOverviewSerpElementItem;
    from dataforseo_client.models.third_party_reviews_serp_element_item import ThirdPartyReviewsSerpElementItem;
    from dataforseo_client.models.dictionary_serp_element_item import DictionarySerpElementItem;



class BaseSerpApiElementItem(BaseModel):
    """
    BaseSerpApiElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    rectangle: Optional[AiModeRectangleInfo] = Field(default=None, description="rectangle parameters. contains cartesian coordinates and pixel dimensions of the result’s snippet in SERP. equals null if calculate_rectangles in the POST request is not set to true")
    __properties: ClassVar[List[str]] = [
        "type", 
        "position", 
        "xpath", 
        "rectangle", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'paid': 'PaidSerpElementItem',
        'organic': 'OrganicSerpElementItem',
        'featured_snippet': 'FeaturedSnippetSerpElementItem',
        'knowledge_graph': 'KnowledgeGraphSerpElementItem',
        'top_stories': 'TopStoriesSerpElementItem',
        'people_also_ask': 'PeopleAlsoAskSerpElementItem',
        'people_also_search': 'PeopleAlsoSearchSerpElementItem',
        'images': 'ImagesSerpElementItem',
        'twitter': 'TwitterSerpElementItem',
        'google_reviews': 'GoogleReviewsSerpElementItem',
        'jobs': 'JobsSerpElementItem',
        'map': 'MapSerpElementItem',
        'app': 'AppSerpElementItem',
        'local_pack': 'LocalPackSerpElementItem',
        'carousel': 'CarouselSerpElementItem',
        'video': 'VideoSerpElementItem',
        'answer_box': 'AnswerBoxSerpElementItem',
        'shopping': 'ShoppingSerpElementItem',
        'google_flights': 'GoogleFlightsSerpElementItem',
        'mention_carousel': 'MentionCarouselSerpElementItem',
        'events': 'EventsSerpElementItem',
        'related_searches': 'RelatedSearchesSerpElementItem',
        'multi_carousel': 'MultiCarouselSerpElementItem',
        'recipes': 'RecipesSerpElementItem',
        'top_sights': 'TopSightsSerpElementItem',
        'scholarly_articles': 'ScholarlyArticlesSerpElementItem',
        'popular_products': 'PopularProductsSerpElementItem',
        'podcasts': 'PodcastsSerpElementItem',
        'stocks_box': 'StocksBoxSerpElementItem',
        'find_results_on': 'FindResultsOnSerpElementItem',
        'questions_and_answers': 'QuestionsAndAnswersSerpElementItem',
        'hotels_pack': 'HotelsPackSerpElementItem',
        'visual_stories': 'VisualStoriesSerpElementItem',
        'commercial_units': 'CommercialUnitsSerpElementItem',
        'local_services': 'LocalServicesSerpElementItem',
        'google_hotels': 'GoogleHotelsSerpElementItem',
        'math_solver': 'MathSolverSerpElementItem',
        'currency_box': 'CurrencyBoxSerpElementItem',
        'google_posts': 'GooglePostsSerpElementItem',
        'product_considerations': 'ProductConsiderationsSerpElementItem',
        'found_on_web': 'FoundOnWebSerpElementItem',
        'short_videos': 'ShortVideosSerpElementItem',
        'refine_products': 'RefineProductsSerpElementItem',
        'explore_brands': 'ExploreBrandsSerpElementItem',
        'perspectives': 'PerspectivesSerpElementItem',
        'discussions_and_forums': 'DiscussionsAndForumsSerpElementItem',
        'compare_sites': 'CompareSitesSerpElementItem',
        'courses': 'CoursesSerpElementItem',
        'knowledge_graph_carousel_item': 'KnowledgeGraphCarouselItemSerpElementItem',
        'knowledge_graph_description_item': 'KnowledgeGraphDescriptionItemSerpElementItem',
        'knowledge_graph_images_item': 'KnowledgeGraphImagesItemSerpElementItem',
        'knowledge_graph_list_item': 'KnowledgeGraphListItemSerpElementItem',
        'knowledge_graph_row_item': 'KnowledgeGraphRowItemSerpElementItem',
        'knowledge_graph_hotels_booking_item': 'KnowledgeGraphHotelsBookingItemSerpElementItem',
        'knowledge_graph_expanded_item': 'KnowledgeGraphExpandedItemSerpElementItem',
        'knowledge_graph_part_item': 'KnowledgeGraphPartItemSerpElementItem',
        'knowledge_graph_shopping_item': 'KnowledgeGraphShoppingItemSerpElementItem',
        'knowledge_graph_ai_overview_item': 'KnowledgeGraphAiOverviewItemSerpElementItem',
        'ai_overview': 'AiOverviewSerpElementItem',
        'third_party_reviews': 'ThirdPartyReviewsSerpElementItem',
        'dictionary': 'DictionarySerpElementItem',
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
        PaidSerpElementItem, 
        OrganicSerpElementItem, 
        FeaturedSnippetSerpElementItem, 
        KnowledgeGraphSerpElementItem, 
        TopStoriesSerpElementItem, 
        PeopleAlsoAskSerpElementItem, 
        PeopleAlsoSearchSerpElementItem, 
        ImagesSerpElementItem, 
        TwitterSerpElementItem, 
        GoogleReviewsSerpElementItem, 
        JobsSerpElementItem, 
        MapSerpElementItem, 
        AppSerpElementItem, 
        LocalPackSerpElementItem, 
        CarouselSerpElementItem, 
        VideoSerpElementItem, 
        AnswerBoxSerpElementItem, 
        ShoppingSerpElementItem, 
        GoogleFlightsSerpElementItem, 
        MentionCarouselSerpElementItem, 
        EventsSerpElementItem, 
        RelatedSearchesSerpElementItem, 
        MultiCarouselSerpElementItem, 
        RecipesSerpElementItem, 
        TopSightsSerpElementItem, 
        ScholarlyArticlesSerpElementItem, 
        PopularProductsSerpElementItem, 
        PodcastsSerpElementItem, 
        StocksBoxSerpElementItem, 
        FindResultsOnSerpElementItem, 
        QuestionsAndAnswersSerpElementItem, 
        HotelsPackSerpElementItem, 
        VisualStoriesSerpElementItem, 
        CommercialUnitsSerpElementItem, 
        LocalServicesSerpElementItem, 
        GoogleHotelsSerpElementItem, 
        MathSolverSerpElementItem, 
        CurrencyBoxSerpElementItem, 
        GooglePostsSerpElementItem, 
        ProductConsiderationsSerpElementItem, 
        FoundOnWebSerpElementItem, 
        ShortVideosSerpElementItem, 
        RefineProductsSerpElementItem, 
        ExploreBrandsSerpElementItem, 
        PerspectivesSerpElementItem, 
        DiscussionsAndForumsSerpElementItem, 
        CompareSitesSerpElementItem, 
        CoursesSerpElementItem, 
        KnowledgeGraphCarouselItemSerpElementItem, 
        KnowledgeGraphDescriptionItemSerpElementItem, 
        KnowledgeGraphImagesItemSerpElementItem, 
        KnowledgeGraphListItemSerpElementItem, 
        KnowledgeGraphRowItemSerpElementItem, 
        KnowledgeGraphHotelsBookingItemSerpElementItem, 
        KnowledgeGraphExpandedItemSerpElementItem, 
        KnowledgeGraphPartItemSerpElementItem, 
        KnowledgeGraphShoppingItemSerpElementItem, 
        KnowledgeGraphAiOverviewItemSerpElementItem, 
        AiOverviewSerpElementItem, 
        ThirdPartyReviewsSerpElementItem, 
        DictionarySerpElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'PaidSerpElementItem':
            return import_module("dataforseo_client.models.paid_serp_element_item").PaidSerpElementItem.from_dict(obj)
        if object_type == 'OrganicSerpElementItem':
            return import_module("dataforseo_client.models.organic_serp_element_item").OrganicSerpElementItem.from_dict(obj)
        if object_type == 'FeaturedSnippetSerpElementItem':
            return import_module("dataforseo_client.models.featured_snippet_serp_element_item").FeaturedSnippetSerpElementItem.from_dict(obj)
        if object_type == 'KnowledgeGraphSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_serp_element_item").KnowledgeGraphSerpElementItem.from_dict(obj)
        if object_type == 'TopStoriesSerpElementItem':
            return import_module("dataforseo_client.models.top_stories_serp_element_item").TopStoriesSerpElementItem.from_dict(obj)
        if object_type == 'PeopleAlsoAskSerpElementItem':
            return import_module("dataforseo_client.models.people_also_ask_serp_element_item").PeopleAlsoAskSerpElementItem.from_dict(obj)
        if object_type == 'PeopleAlsoSearchSerpElementItem':
            return import_module("dataforseo_client.models.people_also_search_serp_element_item").PeopleAlsoSearchSerpElementItem.from_dict(obj)
        if object_type == 'ImagesSerpElementItem':
            return import_module("dataforseo_client.models.images_serp_element_item").ImagesSerpElementItem.from_dict(obj)
        if object_type == 'TwitterSerpElementItem':
            return import_module("dataforseo_client.models.twitter_serp_element_item").TwitterSerpElementItem.from_dict(obj)
        if object_type == 'GoogleReviewsSerpElementItem':
            return import_module("dataforseo_client.models.google_reviews_serp_element_item").GoogleReviewsSerpElementItem.from_dict(obj)
        if object_type == 'JobsSerpElementItem':
            return import_module("dataforseo_client.models.jobs_serp_element_item").JobsSerpElementItem.from_dict(obj)
        if object_type == 'MapSerpElementItem':
            return import_module("dataforseo_client.models.map_serp_element_item").MapSerpElementItem.from_dict(obj)
        if object_type == 'AppSerpElementItem':
            return import_module("dataforseo_client.models.app_serp_element_item").AppSerpElementItem.from_dict(obj)
        if object_type == 'LocalPackSerpElementItem':
            return import_module("dataforseo_client.models.local_pack_serp_element_item").LocalPackSerpElementItem.from_dict(obj)
        if object_type == 'CarouselSerpElementItem':
            return import_module("dataforseo_client.models.carousel_serp_element_item").CarouselSerpElementItem.from_dict(obj)
        if object_type == 'VideoSerpElementItem':
            return import_module("dataforseo_client.models.video_serp_element_item").VideoSerpElementItem.from_dict(obj)
        if object_type == 'AnswerBoxSerpElementItem':
            return import_module("dataforseo_client.models.answer_box_serp_element_item").AnswerBoxSerpElementItem.from_dict(obj)
        if object_type == 'ShoppingSerpElementItem':
            return import_module("dataforseo_client.models.shopping_serp_element_item").ShoppingSerpElementItem.from_dict(obj)
        if object_type == 'GoogleFlightsSerpElementItem':
            return import_module("dataforseo_client.models.google_flights_serp_element_item").GoogleFlightsSerpElementItem.from_dict(obj)
        if object_type == 'MentionCarouselSerpElementItem':
            return import_module("dataforseo_client.models.mention_carousel_serp_element_item").MentionCarouselSerpElementItem.from_dict(obj)
        if object_type == 'EventsSerpElementItem':
            return import_module("dataforseo_client.models.events_serp_element_item").EventsSerpElementItem.from_dict(obj)
        if object_type == 'RelatedSearchesSerpElementItem':
            return import_module("dataforseo_client.models.related_searches_serp_element_item").RelatedSearchesSerpElementItem.from_dict(obj)
        if object_type == 'MultiCarouselSerpElementItem':
            return import_module("dataforseo_client.models.multi_carousel_serp_element_item").MultiCarouselSerpElementItem.from_dict(obj)
        if object_type == 'RecipesSerpElementItem':
            return import_module("dataforseo_client.models.recipes_serp_element_item").RecipesSerpElementItem.from_dict(obj)
        if object_type == 'TopSightsSerpElementItem':
            return import_module("dataforseo_client.models.top_sights_serp_element_item").TopSightsSerpElementItem.from_dict(obj)
        if object_type == 'ScholarlyArticlesSerpElementItem':
            return import_module("dataforseo_client.models.scholarly_articles_serp_element_item").ScholarlyArticlesSerpElementItem.from_dict(obj)
        if object_type == 'PopularProductsSerpElementItem':
            return import_module("dataforseo_client.models.popular_products_serp_element_item").PopularProductsSerpElementItem.from_dict(obj)
        if object_type == 'PodcastsSerpElementItem':
            return import_module("dataforseo_client.models.podcasts_serp_element_item").PodcastsSerpElementItem.from_dict(obj)
        if object_type == 'StocksBoxSerpElementItem':
            return import_module("dataforseo_client.models.stocks_box_serp_element_item").StocksBoxSerpElementItem.from_dict(obj)
        if object_type == 'FindResultsOnSerpElementItem':
            return import_module("dataforseo_client.models.find_results_on_serp_element_item").FindResultsOnSerpElementItem.from_dict(obj)
        if object_type == 'QuestionsAndAnswersSerpElementItem':
            return import_module("dataforseo_client.models.questions_and_answers_serp_element_item").QuestionsAndAnswersSerpElementItem.from_dict(obj)
        if object_type == 'HotelsPackSerpElementItem':
            return import_module("dataforseo_client.models.hotels_pack_serp_element_item").HotelsPackSerpElementItem.from_dict(obj)
        if object_type == 'VisualStoriesSerpElementItem':
            return import_module("dataforseo_client.models.visual_stories_serp_element_item").VisualStoriesSerpElementItem.from_dict(obj)
        if object_type == 'CommercialUnitsSerpElementItem':
            return import_module("dataforseo_client.models.commercial_units_serp_element_item").CommercialUnitsSerpElementItem.from_dict(obj)
        if object_type == 'LocalServicesSerpElementItem':
            return import_module("dataforseo_client.models.local_services_serp_element_item").LocalServicesSerpElementItem.from_dict(obj)
        if object_type == 'GoogleHotelsSerpElementItem':
            return import_module("dataforseo_client.models.google_hotels_serp_element_item").GoogleHotelsSerpElementItem.from_dict(obj)
        if object_type == 'MathSolverSerpElementItem':
            return import_module("dataforseo_client.models.math_solver_serp_element_item").MathSolverSerpElementItem.from_dict(obj)
        if object_type == 'CurrencyBoxSerpElementItem':
            return import_module("dataforseo_client.models.currency_box_serp_element_item").CurrencyBoxSerpElementItem.from_dict(obj)
        if object_type == 'GooglePostsSerpElementItem':
            return import_module("dataforseo_client.models.google_posts_serp_element_item").GooglePostsSerpElementItem.from_dict(obj)
        if object_type == 'ProductConsiderationsSerpElementItem':
            return import_module("dataforseo_client.models.product_considerations_serp_element_item").ProductConsiderationsSerpElementItem.from_dict(obj)
        if object_type == 'FoundOnWebSerpElementItem':
            return import_module("dataforseo_client.models.found_on_web_serp_element_item").FoundOnWebSerpElementItem.from_dict(obj)
        if object_type == 'ShortVideosSerpElementItem':
            return import_module("dataforseo_client.models.short_videos_serp_element_item").ShortVideosSerpElementItem.from_dict(obj)
        if object_type == 'RefineProductsSerpElementItem':
            return import_module("dataforseo_client.models.refine_products_serp_element_item").RefineProductsSerpElementItem.from_dict(obj)
        if object_type == 'ExploreBrandsSerpElementItem':
            return import_module("dataforseo_client.models.explore_brands_serp_element_item").ExploreBrandsSerpElementItem.from_dict(obj)
        if object_type == 'PerspectivesSerpElementItem':
            return import_module("dataforseo_client.models.perspectives_serp_element_item").PerspectivesSerpElementItem.from_dict(obj)
        if object_type == 'DiscussionsAndForumsSerpElementItem':
            return import_module("dataforseo_client.models.discussions_and_forums_serp_element_item").DiscussionsAndForumsSerpElementItem.from_dict(obj)
        if object_type == 'CompareSitesSerpElementItem':
            return import_module("dataforseo_client.models.compare_sites_serp_element_item").CompareSitesSerpElementItem.from_dict(obj)
        if object_type == 'CoursesSerpElementItem':
            return import_module("dataforseo_client.models.courses_serp_element_item").CoursesSerpElementItem.from_dict(obj)
        if object_type == 'KnowledgeGraphCarouselItemSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_carousel_item_serp_element_item").KnowledgeGraphCarouselItemSerpElementItem.from_dict(obj)
        if object_type == 'KnowledgeGraphDescriptionItemSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_description_item_serp_element_item").KnowledgeGraphDescriptionItemSerpElementItem.from_dict(obj)
        if object_type == 'KnowledgeGraphImagesItemSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_images_item_serp_element_item").KnowledgeGraphImagesItemSerpElementItem.from_dict(obj)
        if object_type == 'KnowledgeGraphListItemSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_list_item_serp_element_item").KnowledgeGraphListItemSerpElementItem.from_dict(obj)
        if object_type == 'KnowledgeGraphRowItemSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_row_item_serp_element_item").KnowledgeGraphRowItemSerpElementItem.from_dict(obj)
        if object_type == 'KnowledgeGraphHotelsBookingItemSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_hotels_booking_item_serp_element_item").KnowledgeGraphHotelsBookingItemSerpElementItem.from_dict(obj)
        if object_type == 'KnowledgeGraphExpandedItemSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_expanded_item_serp_element_item").KnowledgeGraphExpandedItemSerpElementItem.from_dict(obj)
        if object_type == 'KnowledgeGraphPartItemSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_part_item_serp_element_item").KnowledgeGraphPartItemSerpElementItem.from_dict(obj)
        if object_type == 'KnowledgeGraphShoppingItemSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_shopping_item_serp_element_item").KnowledgeGraphShoppingItemSerpElementItem.from_dict(obj)
        if object_type == 'KnowledgeGraphAiOverviewItemSerpElementItem':
            return import_module("dataforseo_client.models.knowledge_graph_ai_overview_item_serp_element_item").KnowledgeGraphAiOverviewItemSerpElementItem.from_dict(obj)
        if object_type == 'AiOverviewSerpElementItem':
            return import_module("dataforseo_client.models.ai_overview_serp_element_item").AiOverviewSerpElementItem.from_dict(obj)
        if object_type == 'ThirdPartyReviewsSerpElementItem':
            return import_module("dataforseo_client.models.third_party_reviews_serp_element_item").ThirdPartyReviewsSerpElementItem.from_dict(obj)
        if object_type == 'DictionarySerpElementItem':
            return import_module("dataforseo_client.models.dictionary_serp_element_item").DictionarySerpElementItem.from_dict(obj)

        raise ValueError("BaseSerpElementItem failed to lookup discriminator value from " +
                         json.dumps(obj) + ". Discriminator property name: " + cls.__discriminator_property_name +
                         ", mapping: " + json.dumps(cls.__discriminator_value_class_map))