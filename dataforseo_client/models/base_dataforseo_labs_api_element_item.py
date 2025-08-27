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
    from dataforseo_client.models.data_labs_local_pack_serp_element_item import DataLabsLocalPackSerpElementItem;
    from dataforseo_client.models.data_labs_paid_serp_element_item import DataLabsPaidSerpElementItem;
    from dataforseo_client.models.data_labs_featured_snippet_serp_element_item import DataLabsFeaturedSnippetSerpElementItem;
    from dataforseo_client.models.data_labs_answer_box_serp_element_item import DataLabsAnswerBoxSerpElementItem;
    from dataforseo_client.models.data_labs_carousel_serp_element_item import DataLabsCarouselSerpElementItem;
    from dataforseo_client.models.data_labs_multi_carousel_serp_element_item import DataLabsMultiCarouselSerpElementItem;
    from dataforseo_client.models.data_labs_google_flights_serp_element_item import DataLabsGoogleFlightsSerpElementItem;
    from dataforseo_client.models.data_labs_google_reviews_serp_element_item import DataLabsGoogleReviewsSerpElementItem;
    from dataforseo_client.models.data_labs_google_posts_serp_element_item import DataLabsGooglePostsSerpElementItem;
    from dataforseo_client.models.data_labs_images_serp_element_item import DataLabsImagesSerpElementItem;
    from dataforseo_client.models.data_labs_jobs_serp_element_item import DataLabsJobsSerpElementItem;
    from dataforseo_client.models.data_labs_knowledge_graph_serp_element_item import DataLabsKnowledgeGraphSerpElementItem;
    from dataforseo_client.models.data_labs_hotels_pack_serp_element_item import DataLabsHotelsPackSerpElementItem;
    from dataforseo_client.models.data_labs_map_serp_element_item import DataLabsMapSerpElementItem;
    from dataforseo_client.models.data_labs_organic_serp_element_item import DataLabsOrganicSerpElementItem;
    from dataforseo_client.models.data_labs_people_also_ask_serp_element_item import DataLabsPeopleAlsoAskSerpElementItem;
    from dataforseo_client.models.data_labs_related_searches_serp_element_item import DataLabsRelatedSearchesSerpElementItem;
    from dataforseo_client.models.data_labs_people_also_search_serp_element_item import DataLabsPeopleAlsoSearchSerpElementItem;
    from dataforseo_client.models.data_labs_shopping_serp_element_item import DataLabsShoppingSerpElementItem;
    from dataforseo_client.models.data_labs_top_stories_serp_element_item import DataLabsTopStoriesSerpElementItem;
    from dataforseo_client.models.data_labs_twitter_serp_element_item import DataLabsTwitterSerpElementItem;
    from dataforseo_client.models.data_labs_video_serp_element_item import DataLabsVideoSerpElementItem;
    from dataforseo_client.models.data_labs_events_serp_element_item import DataLabsEventsSerpElementItem;
    from dataforseo_client.models.data_labs_mention_carousel_serp_element_item import DataLabsMentionCarouselSerpElementItem;
    from dataforseo_client.models.data_labs_recipes_serp_element_item import DataLabsRecipesSerpElementItem;
    from dataforseo_client.models.data_labs_top_sights_serp_element_item import DataLabsTopSightsSerpElementItem;
    from dataforseo_client.models.data_labs_scholarly_articles_serp_element_item import DataLabsScholarlyArticlesSerpElementItem;
    from dataforseo_client.models.data_labs_popular_products_serp_element_item import DataLabsPopularProductsSerpElementItem;
    from dataforseo_client.models.data_labs_podcasts_serp_element_item import DataLabsPodcastsSerpElementItem;
    from dataforseo_client.models.data_labs_questions_and_answers_serp_element_item import DataLabsQuestionsAndAnswersSerpElementItem;
    from dataforseo_client.models.data_labs_find_results_on_serp_element_item import DataLabsFindResultsOnSerpElementItem;
    from dataforseo_client.models.data_labs_stocks_box_serp_element_item import DataLabsStocksBoxSerpElementItem;
    from dataforseo_client.models.data_labs_commercial_units_serp_element_item import DataLabsCommercialUnitsSerpElementItem;
    from dataforseo_client.models.data_labs_local_services_serp_element_item import DataLabsLocalServicesSerpElementItem;
    from dataforseo_client.models.data_labs_google_hotels_serp_element_item import DataLabsGoogleHotelsSerpElementItem;
    from dataforseo_client.models.data_labs_math_solver_serp_element_item import DataLabsMathSolverSerpElementItem;



class BaseDataforseoLabsApiElementItem(BaseModel):
    """
    BaseDataforseoLabsApiElementItem
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="type of element")
    se_type: Optional[StrictStr] = Field(default=None, description="search engine type")
    rank_group: Optional[StrictInt] = Field(default=None, description="position within a group of elements with identical type values. positions of elements with different type values are omitted from rank_group")
    rank_absolute: Optional[StrictInt] = Field(default=None, description="absolute rank in SERP. absolute position among all the elements in SERP")
    position: Optional[StrictStr] = Field(default=None, description="the alignment of the element in SERP. can take the following values:. left, right")
    xpath: Optional[StrictStr] = Field(default=None, description="the XPath of the element")
    __properties: ClassVar[List[str]] = [
        "type", 
        "se_type", 
        "rank_group", 
        "rank_absolute", 
        "position", 
        "xpath", 
        ]
    __discriminator_property_name: ClassVar[str] = 'type'
    __discriminator_value_class_map: ClassVar[Dict[str, str]] = {
        'local_pack': 'DataLabsLocalPackSerpElementItem',
        'paid': 'DataLabsPaidSerpElementItem',
        'featured_snippet': 'DataLabsFeaturedSnippetSerpElementItem',
        'answer_box': 'DataLabsAnswerBoxSerpElementItem',
        'carousel': 'DataLabsCarouselSerpElementItem',
        'multi_carousel': 'DataLabsMultiCarouselSerpElementItem',
        'google_flights': 'DataLabsGoogleFlightsSerpElementItem',
        'google_reviews': 'DataLabsGoogleReviewsSerpElementItem',
        'google_posts': 'DataLabsGooglePostsSerpElementItem',
        'images': 'DataLabsImagesSerpElementItem',
        'jobs': 'DataLabsJobsSerpElementItem',
        'knowledge_graph': 'DataLabsKnowledgeGraphSerpElementItem',
        'hotels_pack': 'DataLabsHotelsPackSerpElementItem',
        'map': 'DataLabsMapSerpElementItem',
        'organic': 'DataLabsOrganicSerpElementItem',
        'people_also_ask': 'DataLabsPeopleAlsoAskSerpElementItem',
        'related_searches': 'DataLabsRelatedSearchesSerpElementItem',
        'people_also_search': 'DataLabsPeopleAlsoSearchSerpElementItem',
        'shopping': 'DataLabsShoppingSerpElementItem',
        'top_stories': 'DataLabsTopStoriesSerpElementItem',
        'twitter': 'DataLabsTwitterSerpElementItem',
        'video': 'DataLabsVideoSerpElementItem',
        'events': 'DataLabsEventsSerpElementItem',
        'mention_carousel': 'DataLabsMentionCarouselSerpElementItem',
        'recipes': 'DataLabsRecipesSerpElementItem',
        'top_sights': 'DataLabsTopSightsSerpElementItem',
        'scholarly_articles': 'DataLabsScholarlyArticlesSerpElementItem',
        'popular_products': 'DataLabsPopularProductsSerpElementItem',
        'podcasts': 'DataLabsPodcastsSerpElementItem',
        'questions_and_answers': 'DataLabsQuestionsAndAnswersSerpElementItem',
        'find_results_on': 'DataLabsFindResultsOnSerpElementItem',
        'stocks_box': 'DataLabsStocksBoxSerpElementItem',
        'commercial_units': 'DataLabsCommercialUnitsSerpElementItem',
        'local_services': 'DataLabsLocalServicesSerpElementItem',
        'google_hotels': 'DataLabsGoogleHotelsSerpElementItem',
        'math_solver': 'DataLabsMathSolverSerpElementItem',
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
        _dict['se_type'] = self.se_type
        _dict['rank_group'] = self.rank_group
        _dict['rank_absolute'] = self.rank_absolute
        _dict['position'] = self.position
        _dict['xpath'] = self.xpath
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
        DataLabsLocalPackSerpElementItem, 
        DataLabsPaidSerpElementItem, 
        DataLabsFeaturedSnippetSerpElementItem, 
        DataLabsAnswerBoxSerpElementItem, 
        DataLabsCarouselSerpElementItem, 
        DataLabsMultiCarouselSerpElementItem, 
        DataLabsGoogleFlightsSerpElementItem, 
        DataLabsGoogleReviewsSerpElementItem, 
        DataLabsGooglePostsSerpElementItem, 
        DataLabsImagesSerpElementItem, 
        DataLabsJobsSerpElementItem, 
        DataLabsKnowledgeGraphSerpElementItem, 
        DataLabsHotelsPackSerpElementItem, 
        DataLabsMapSerpElementItem, 
        DataLabsOrganicSerpElementItem, 
        DataLabsPeopleAlsoAskSerpElementItem, 
        DataLabsRelatedSearchesSerpElementItem, 
        DataLabsPeopleAlsoSearchSerpElementItem, 
        DataLabsShoppingSerpElementItem, 
        DataLabsTopStoriesSerpElementItem, 
        DataLabsTwitterSerpElementItem, 
        DataLabsVideoSerpElementItem, 
        DataLabsEventsSerpElementItem, 
        DataLabsMentionCarouselSerpElementItem, 
        DataLabsRecipesSerpElementItem, 
        DataLabsTopSightsSerpElementItem, 
        DataLabsScholarlyArticlesSerpElementItem, 
        DataLabsPopularProductsSerpElementItem, 
        DataLabsPodcastsSerpElementItem, 
        DataLabsQuestionsAndAnswersSerpElementItem, 
        DataLabsFindResultsOnSerpElementItem, 
        DataLabsStocksBoxSerpElementItem, 
        DataLabsCommercialUnitsSerpElementItem, 
        DataLabsLocalServicesSerpElementItem, 
        DataLabsGoogleHotelsSerpElementItem, 
        DataLabsMathSolverSerpElementItem
    ]]:
        # look up the object type based on discriminator mapping
        object_type = cls.get_discriminator_value(obj)
        
        if object_type == 'DataLabsLocalPackSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_local_pack_serp_element_item").DataLabsLocalPackSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsPaidSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_paid_serp_element_item").DataLabsPaidSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsFeaturedSnippetSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_featured_snippet_serp_element_item").DataLabsFeaturedSnippetSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsAnswerBoxSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_answer_box_serp_element_item").DataLabsAnswerBoxSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsCarouselSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_carousel_serp_element_item").DataLabsCarouselSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsMultiCarouselSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_multi_carousel_serp_element_item").DataLabsMultiCarouselSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsGoogleFlightsSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_google_flights_serp_element_item").DataLabsGoogleFlightsSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsGoogleReviewsSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_google_reviews_serp_element_item").DataLabsGoogleReviewsSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsGooglePostsSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_google_posts_serp_element_item").DataLabsGooglePostsSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsImagesSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_images_serp_element_item").DataLabsImagesSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsJobsSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_jobs_serp_element_item").DataLabsJobsSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsKnowledgeGraphSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_knowledge_graph_serp_element_item").DataLabsKnowledgeGraphSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsHotelsPackSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_hotels_pack_serp_element_item").DataLabsHotelsPackSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsMapSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_map_serp_element_item").DataLabsMapSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsOrganicSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_organic_serp_element_item").DataLabsOrganicSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsPeopleAlsoAskSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_people_also_ask_serp_element_item").DataLabsPeopleAlsoAskSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsRelatedSearchesSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_related_searches_serp_element_item").DataLabsRelatedSearchesSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsPeopleAlsoSearchSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_people_also_search_serp_element_item").DataLabsPeopleAlsoSearchSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsShoppingSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_shopping_serp_element_item").DataLabsShoppingSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsTopStoriesSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_top_stories_serp_element_item").DataLabsTopStoriesSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsTwitterSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_twitter_serp_element_item").DataLabsTwitterSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsVideoSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_video_serp_element_item").DataLabsVideoSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsEventsSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_events_serp_element_item").DataLabsEventsSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsMentionCarouselSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_mention_carousel_serp_element_item").DataLabsMentionCarouselSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsRecipesSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_recipes_serp_element_item").DataLabsRecipesSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsTopSightsSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_top_sights_serp_element_item").DataLabsTopSightsSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsScholarlyArticlesSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_scholarly_articles_serp_element_item").DataLabsScholarlyArticlesSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsPopularProductsSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_popular_products_serp_element_item").DataLabsPopularProductsSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsPodcastsSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_podcasts_serp_element_item").DataLabsPodcastsSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsQuestionsAndAnswersSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_questions_and_answers_serp_element_item").DataLabsQuestionsAndAnswersSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsFindResultsOnSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_find_results_on_serp_element_item").DataLabsFindResultsOnSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsStocksBoxSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_stocks_box_serp_element_item").DataLabsStocksBoxSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsCommercialUnitsSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_commercial_units_serp_element_item").DataLabsCommercialUnitsSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsLocalServicesSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_local_services_serp_element_item").DataLabsLocalServicesSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsGoogleHotelsSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_google_hotels_serp_element_item").DataLabsGoogleHotelsSerpElementItem.from_dict(obj)
        if object_type == 'DataLabsMathSolverSerpElementItem':
            return import_module("dataforseo_client.models.data_labs_math_solver_serp_element_item").DataLabsMathSolverSerpElementItem.from_dict(obj)

        return None