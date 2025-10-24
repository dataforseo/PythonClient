from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, StrictBool
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set, Any, Dict, List
from typing_extensions import Self




class DataforseoLabsAvailableFiltersGoogleInfo(BaseModel):
    """
    DataforseoLabsAvailableFiltersGoogleInfo
    """ # noqa: E501
    keyword_data_keyword: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_last_updated_time: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_competition: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_competition_level: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_cpc: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_search_volume: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_low_top_of_page_bid: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_high_top_of_page_bid: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_categories: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_search_volume_trend_monthly: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_search_volume_trend_quarterly: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_search_volume_trend_yearly: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_clickstream_keyword_info_search_volume: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_clickstream_keyword_info_last_updated_time: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_clickstream_keyword_info_gender_distribution_female: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_clickstream_keyword_info_gender_distribution_male: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_clickstream_keyword_info_age_distribution_18_24: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_clickstream_keyword_info_age_distribution_25_34: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_clickstream_keyword_info_age_distribution_35_44: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_clickstream_keyword_info_age_distribution_45_54: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_clickstream_keyword_info_age_distribution_55_64: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_properties_core_keyword: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_properties_synonym_clustering_algorithm: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_properties_keyword_difficulty: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_properties_detected_language: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_properties_is_another_language: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_serp_info_check_url: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_serp_info_serp_item_types: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_serp_info_se_results_count: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_serp_info_last_updated_time: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_serp_info_previous_updated_time: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_avg_backlinks_info_backlinks: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_avg_backlinks_info_dofollow: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_avg_backlinks_info_referring_pages: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_avg_backlinks_info_referring_domains: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_avg_backlinks_info_referring_main_domains: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_avg_backlinks_info_rank: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_avg_backlinks_info_main_domain_rank: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_avg_backlinks_info_last_updated_time: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_search_intent_info_main_intent: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_search_intent_info_foreign_intent: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_search_intent_info_last_updated_time: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_normalized_with_bing_search_volume: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_normalized_with_bing_last_updated_time: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_normalized_with_bing_is_normalized: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_normalized_with_clickstream_search_volume: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_normalized_with_clickstream_last_updated_time: Optional[StrictStr] = Field(default=None, description=r"")
    keyword_data_keyword_info_normalized_with_clickstream_is_normalized: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_type: Optional[StrictStr] = Field(default=None, description=r"type of element")
    ranked_serp_element_serp_item_rank_group: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_rank_absolute: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_position: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_xpath: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_domain: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_title: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_url: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_breadcrumb: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_website_name: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_is_image: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_is_video: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_is_featured_snippet: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_is_malicious: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_description: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_pre_snippet: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_extended_snippet: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_amp_version: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_rating_rating_type: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_rating_value: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_rating_votes_count: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_rating_rating_max: Optional[StrictInt] = Field(default=None, description=r"the maximum value for a rating_type")
    ranked_serp_element_serp_item_about_this_result: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_main_domain: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_relative_url: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_etv: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_estimated_paid_traffic_cost: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_clickstream_etv: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_rank_changes_previous_rank_absolute: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_rank_changes_is_new: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_rank_changes_is_up: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_rank_changes_is_down: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_backlinks_info_referring_domains: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_backlinks_info_referring_main_domains: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_backlinks_info_referring_pages: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_backlinks_info_dofollow: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_backlinks_info_backlinks: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_backlinks_info_time_update: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_rank_info_page_rank: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_rank_info_main_domain_rank: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_check_url: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_types: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_se_results_count: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_keyword_difficulty: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_is_lost: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_last_updated_time: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_previous_updated_time: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_extra_ad_aclk: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_description_rows: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_phone: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_is_paid: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_featured_title: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_source: Optional[StrictStr] = Field(default=None, description=r"")
    ranked_serp_element_serp_item_text: Optional[StrictStr] = Field(default=None, description=r"")
    __properties: ClassVar[List[str]] = [
        "keyword_data.keyword", 
        "keyword_data.keyword_info.last_updated_time", 
        "keyword_data.keyword_info.competition", 
        "keyword_data.keyword_info.competition_level", 
        "keyword_data.keyword_info.cpc", 
        "keyword_data.keyword_info.search_volume", 
        "keyword_data.keyword_info.low_top_of_page_bid", 
        "keyword_data.keyword_info.high_top_of_page_bid", 
        "keyword_data.keyword_info.categories", 
        "keyword_data.keyword_info.search_volume_trend.monthly", 
        "keyword_data.keyword_info.search_volume_trend.quarterly", 
        "keyword_data.keyword_info.search_volume_trend.yearly", 
        "keyword_data.clickstream_keyword_info.search_volume", 
        "keyword_data.clickstream_keyword_info.last_updated_time", 
        "keyword_data.clickstream_keyword_info.gender_distribution.female", 
        "keyword_data.clickstream_keyword_info.gender_distribution.male", 
        "keyword_data.clickstream_keyword_info.age_distribution.18-24", 
        "keyword_data.clickstream_keyword_info.age_distribution.25-34", 
        "keyword_data.clickstream_keyword_info.age_distribution.35-44", 
        "keyword_data.clickstream_keyword_info.age_distribution.45-54", 
        "keyword_data.clickstream_keyword_info.age_distribution.55-64", 
        "keyword_data.keyword_properties.core_keyword", 
        "keyword_data.keyword_properties.synonym_clustering_algorithm", 
        "keyword_data.keyword_properties.keyword_difficulty", 
        "keyword_data.keyword_properties.detected_language", 
        "keyword_data.keyword_properties.is_another_language", 
        "keyword_data.serp_info.check_url", 
        "keyword_data.serp_info.serp_item_types", 
        "keyword_data.serp_info.se_results_count", 
        "keyword_data.serp_info.last_updated_time", 
        "keyword_data.serp_info.previous_updated_time", 
        "keyword_data.avg_backlinks_info.backlinks", 
        "keyword_data.avg_backlinks_info.dofollow", 
        "keyword_data.avg_backlinks_info.referring_pages", 
        "keyword_data.avg_backlinks_info.referring_domains", 
        "keyword_data.avg_backlinks_info.referring_main_domains", 
        "keyword_data.avg_backlinks_info.rank", 
        "keyword_data.avg_backlinks_info.main_domain_rank", 
        "keyword_data.avg_backlinks_info.last_updated_time", 
        "keyword_data.search_intent_info.main_intent", 
        "keyword_data.search_intent_info.foreign_intent", 
        "keyword_data.search_intent_info.last_updated_time", 
        "keyword_data.keyword_info_normalized_with_bing.search_volume", 
        "keyword_data.keyword_info_normalized_with_bing.last_updated_time", 
        "keyword_data.keyword_info_normalized_with_bing.is_normalized", 
        "keyword_data.keyword_info_normalized_with_clickstream.search_volume", 
        "keyword_data.keyword_info_normalized_with_clickstream.last_updated_time", 
        "keyword_data.keyword_info_normalized_with_clickstream.is_normalized", 
        "ranked_serp_element.serp_item.type", 
        "ranked_serp_element.serp_item.rank_group", 
        "ranked_serp_element.serp_item.rank_absolute", 
        "ranked_serp_element.serp_item.position", 
        "ranked_serp_element.serp_item.xpath", 
        "ranked_serp_element.serp_item.domain", 
        "ranked_serp_element.serp_item.title", 
        "ranked_serp_element.serp_item.url", 
        "ranked_serp_element.serp_item.breadcrumb", 
        "ranked_serp_element.serp_item.website_name", 
        "ranked_serp_element.serp_item.is_image", 
        "ranked_serp_element.serp_item.is_video", 
        "ranked_serp_element.serp_item.is_featured_snippet", 
        "ranked_serp_element.serp_item.is_malicious", 
        "ranked_serp_element.serp_item.description", 
        "ranked_serp_element.serp_item.pre_snippet", 
        "ranked_serp_element.serp_item.extended_snippet", 
        "ranked_serp_element.serp_item.amp_version", 
        "ranked_serp_element.serp_item.rating.rating_type", 
        "ranked_serp_element.serp_item.rating.value", 
        "ranked_serp_element.serp_item.rating.votes_count", 
        "ranked_serp_element.serp_item.rating.rating_max", 
        "ranked_serp_element.serp_item.about_this_result", 
        "ranked_serp_element.serp_item.main_domain", 
        "ranked_serp_element.serp_item.relative_url", 
        "ranked_serp_element.serp_item.etv", 
        "ranked_serp_element.serp_item.estimated_paid_traffic_cost", 
        "ranked_serp_element.serp_item.clickstream_etv", 
        "ranked_serp_element.serp_item.rank_changes.previous_rank_absolute", 
        "ranked_serp_element.serp_item.rank_changes.is_new", 
        "ranked_serp_element.serp_item.rank_changes.is_up", 
        "ranked_serp_element.serp_item.rank_changes.is_down", 
        "ranked_serp_element.serp_item.backlinks_info.referring_domains", 
        "ranked_serp_element.serp_item.backlinks_info.referring_main_domains", 
        "ranked_serp_element.serp_item.backlinks_info.referring_pages", 
        "ranked_serp_element.serp_item.backlinks_info.dofollow", 
        "ranked_serp_element.serp_item.backlinks_info.backlinks", 
        "ranked_serp_element.serp_item.backlinks_info.time_update", 
        "ranked_serp_element.serp_item.rank_info.page_rank", 
        "ranked_serp_element.serp_item.rank_info.main_domain_rank", 
        "ranked_serp_element.check_url", 
        "ranked_serp_element.serp_item_types", 
        "ranked_serp_element.se_results_count", 
        "ranked_serp_element.keyword_difficulty", 
        "ranked_serp_element.is_lost", 
        "ranked_serp_element.last_updated_time", 
        "ranked_serp_element.previous_updated_time", 
        "ranked_serp_element.serp_item.extra.ad_aclk", 
        "ranked_serp_element.serp_item.description_rows", 
        "ranked_serp_element.serp_item.phone", 
        "ranked_serp_element.serp_item.is_paid", 
        "ranked_serp_element.serp_item.featured_title", 
        "ranked_serp_element.serp_item.source", 
        "ranked_serp_element.serp_item.text", 
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

        _dict['keyword_data.keyword'] = self.keyword_data_keyword
        _dict['keyword_data.keyword_info.last_updated_time'] = self.keyword_data_keyword_info_last_updated_time
        _dict['keyword_data.keyword_info.competition'] = self.keyword_data_keyword_info_competition
        _dict['keyword_data.keyword_info.competition_level'] = self.keyword_data_keyword_info_competition_level
        _dict['keyword_data.keyword_info.cpc'] = self.keyword_data_keyword_info_cpc
        _dict['keyword_data.keyword_info.search_volume'] = self.keyword_data_keyword_info_search_volume
        _dict['keyword_data.keyword_info.low_top_of_page_bid'] = self.keyword_data_keyword_info_low_top_of_page_bid
        _dict['keyword_data.keyword_info.high_top_of_page_bid'] = self.keyword_data_keyword_info_high_top_of_page_bid
        _dict['keyword_data.keyword_info.categories'] = self.keyword_data_keyword_info_categories
        _dict['keyword_data.keyword_info.search_volume_trend.monthly'] = self.keyword_data_keyword_info_search_volume_trend_monthly
        _dict['keyword_data.keyword_info.search_volume_trend.quarterly'] = self.keyword_data_keyword_info_search_volume_trend_quarterly
        _dict['keyword_data.keyword_info.search_volume_trend.yearly'] = self.keyword_data_keyword_info_search_volume_trend_yearly
        _dict['keyword_data.clickstream_keyword_info.search_volume'] = self.keyword_data_clickstream_keyword_info_search_volume
        _dict['keyword_data.clickstream_keyword_info.last_updated_time'] = self.keyword_data_clickstream_keyword_info_last_updated_time
        _dict['keyword_data.clickstream_keyword_info.gender_distribution.female'] = self.keyword_data_clickstream_keyword_info_gender_distribution_female
        _dict['keyword_data.clickstream_keyword_info.gender_distribution.male'] = self.keyword_data_clickstream_keyword_info_gender_distribution_male
        _dict['keyword_data.clickstream_keyword_info.age_distribution.18-24'] = self.keyword_data_clickstream_keyword_info_age_distribution_18_24
        _dict['keyword_data.clickstream_keyword_info.age_distribution.25-34'] = self.keyword_data_clickstream_keyword_info_age_distribution_25_34
        _dict['keyword_data.clickstream_keyword_info.age_distribution.35-44'] = self.keyword_data_clickstream_keyword_info_age_distribution_35_44
        _dict['keyword_data.clickstream_keyword_info.age_distribution.45-54'] = self.keyword_data_clickstream_keyword_info_age_distribution_45_54
        _dict['keyword_data.clickstream_keyword_info.age_distribution.55-64'] = self.keyword_data_clickstream_keyword_info_age_distribution_55_64
        _dict['keyword_data.keyword_properties.core_keyword'] = self.keyword_data_keyword_properties_core_keyword
        _dict['keyword_data.keyword_properties.synonym_clustering_algorithm'] = self.keyword_data_keyword_properties_synonym_clustering_algorithm
        _dict['keyword_data.keyword_properties.keyword_difficulty'] = self.keyword_data_keyword_properties_keyword_difficulty
        _dict['keyword_data.keyword_properties.detected_language'] = self.keyword_data_keyword_properties_detected_language
        _dict['keyword_data.keyword_properties.is_another_language'] = self.keyword_data_keyword_properties_is_another_language
        _dict['keyword_data.serp_info.check_url'] = self.keyword_data_serp_info_check_url
        _dict['keyword_data.serp_info.serp_item_types'] = self.keyword_data_serp_info_serp_item_types
        _dict['keyword_data.serp_info.se_results_count'] = self.keyword_data_serp_info_se_results_count
        _dict['keyword_data.serp_info.last_updated_time'] = self.keyword_data_serp_info_last_updated_time
        _dict['keyword_data.serp_info.previous_updated_time'] = self.keyword_data_serp_info_previous_updated_time
        _dict['keyword_data.avg_backlinks_info.backlinks'] = self.keyword_data_avg_backlinks_info_backlinks
        _dict['keyword_data.avg_backlinks_info.dofollow'] = self.keyword_data_avg_backlinks_info_dofollow
        _dict['keyword_data.avg_backlinks_info.referring_pages'] = self.keyword_data_avg_backlinks_info_referring_pages
        _dict['keyword_data.avg_backlinks_info.referring_domains'] = self.keyword_data_avg_backlinks_info_referring_domains
        _dict['keyword_data.avg_backlinks_info.referring_main_domains'] = self.keyword_data_avg_backlinks_info_referring_main_domains
        _dict['keyword_data.avg_backlinks_info.rank'] = self.keyword_data_avg_backlinks_info_rank
        _dict['keyword_data.avg_backlinks_info.main_domain_rank'] = self.keyword_data_avg_backlinks_info_main_domain_rank
        _dict['keyword_data.avg_backlinks_info.last_updated_time'] = self.keyword_data_avg_backlinks_info_last_updated_time
        _dict['keyword_data.search_intent_info.main_intent'] = self.keyword_data_search_intent_info_main_intent
        _dict['keyword_data.search_intent_info.foreign_intent'] = self.keyword_data_search_intent_info_foreign_intent
        _dict['keyword_data.search_intent_info.last_updated_time'] = self.keyword_data_search_intent_info_last_updated_time
        _dict['keyword_data.keyword_info_normalized_with_bing.search_volume'] = self.keyword_data_keyword_info_normalized_with_bing_search_volume
        _dict['keyword_data.keyword_info_normalized_with_bing.last_updated_time'] = self.keyword_data_keyword_info_normalized_with_bing_last_updated_time
        _dict['keyword_data.keyword_info_normalized_with_bing.is_normalized'] = self.keyword_data_keyword_info_normalized_with_bing_is_normalized
        _dict['keyword_data.keyword_info_normalized_with_clickstream.search_volume'] = self.keyword_data_keyword_info_normalized_with_clickstream_search_volume
        _dict['keyword_data.keyword_info_normalized_with_clickstream.last_updated_time'] = self.keyword_data_keyword_info_normalized_with_clickstream_last_updated_time
        _dict['keyword_data.keyword_info_normalized_with_clickstream.is_normalized'] = self.keyword_data_keyword_info_normalized_with_clickstream_is_normalized
        _dict['ranked_serp_element.serp_item.type'] = self.ranked_serp_element_serp_item_type
        _dict['ranked_serp_element.serp_item.rank_group'] = self.ranked_serp_element_serp_item_rank_group
        _dict['ranked_serp_element.serp_item.rank_absolute'] = self.ranked_serp_element_serp_item_rank_absolute
        _dict['ranked_serp_element.serp_item.position'] = self.ranked_serp_element_serp_item_position
        _dict['ranked_serp_element.serp_item.xpath'] = self.ranked_serp_element_serp_item_xpath
        _dict['ranked_serp_element.serp_item.domain'] = self.ranked_serp_element_serp_item_domain
        _dict['ranked_serp_element.serp_item.title'] = self.ranked_serp_element_serp_item_title
        _dict['ranked_serp_element.serp_item.url'] = self.ranked_serp_element_serp_item_url
        _dict['ranked_serp_element.serp_item.breadcrumb'] = self.ranked_serp_element_serp_item_breadcrumb
        _dict['ranked_serp_element.serp_item.website_name'] = self.ranked_serp_element_serp_item_website_name
        _dict['ranked_serp_element.serp_item.is_image'] = self.ranked_serp_element_serp_item_is_image
        _dict['ranked_serp_element.serp_item.is_video'] = self.ranked_serp_element_serp_item_is_video
        _dict['ranked_serp_element.serp_item.is_featured_snippet'] = self.ranked_serp_element_serp_item_is_featured_snippet
        _dict['ranked_serp_element.serp_item.is_malicious'] = self.ranked_serp_element_serp_item_is_malicious
        _dict['ranked_serp_element.serp_item.description'] = self.ranked_serp_element_serp_item_description
        _dict['ranked_serp_element.serp_item.pre_snippet'] = self.ranked_serp_element_serp_item_pre_snippet
        _dict['ranked_serp_element.serp_item.extended_snippet'] = self.ranked_serp_element_serp_item_extended_snippet
        _dict['ranked_serp_element.serp_item.amp_version'] = self.ranked_serp_element_serp_item_amp_version
        _dict['ranked_serp_element.serp_item.rating.rating_type'] = self.ranked_serp_element_serp_item_rating_rating_type
        _dict['ranked_serp_element.serp_item.rating.value'] = self.ranked_serp_element_serp_item_rating_value
        _dict['ranked_serp_element.serp_item.rating.votes_count'] = self.ranked_serp_element_serp_item_rating_votes_count
        _dict['ranked_serp_element.serp_item.rating.rating_max'] = self.ranked_serp_element_serp_item_rating_rating_max
        _dict['ranked_serp_element.serp_item.about_this_result'] = self.ranked_serp_element_serp_item_about_this_result
        _dict['ranked_serp_element.serp_item.main_domain'] = self.ranked_serp_element_serp_item_main_domain
        _dict['ranked_serp_element.serp_item.relative_url'] = self.ranked_serp_element_serp_item_relative_url
        _dict['ranked_serp_element.serp_item.etv'] = self.ranked_serp_element_serp_item_etv
        _dict['ranked_serp_element.serp_item.estimated_paid_traffic_cost'] = self.ranked_serp_element_serp_item_estimated_paid_traffic_cost
        _dict['ranked_serp_element.serp_item.clickstream_etv'] = self.ranked_serp_element_serp_item_clickstream_etv
        _dict['ranked_serp_element.serp_item.rank_changes.previous_rank_absolute'] = self.ranked_serp_element_serp_item_rank_changes_previous_rank_absolute
        _dict['ranked_serp_element.serp_item.rank_changes.is_new'] = self.ranked_serp_element_serp_item_rank_changes_is_new
        _dict['ranked_serp_element.serp_item.rank_changes.is_up'] = self.ranked_serp_element_serp_item_rank_changes_is_up
        _dict['ranked_serp_element.serp_item.rank_changes.is_down'] = self.ranked_serp_element_serp_item_rank_changes_is_down
        _dict['ranked_serp_element.serp_item.backlinks_info.referring_domains'] = self.ranked_serp_element_serp_item_backlinks_info_referring_domains
        _dict['ranked_serp_element.serp_item.backlinks_info.referring_main_domains'] = self.ranked_serp_element_serp_item_backlinks_info_referring_main_domains
        _dict['ranked_serp_element.serp_item.backlinks_info.referring_pages'] = self.ranked_serp_element_serp_item_backlinks_info_referring_pages
        _dict['ranked_serp_element.serp_item.backlinks_info.dofollow'] = self.ranked_serp_element_serp_item_backlinks_info_dofollow
        _dict['ranked_serp_element.serp_item.backlinks_info.backlinks'] = self.ranked_serp_element_serp_item_backlinks_info_backlinks
        _dict['ranked_serp_element.serp_item.backlinks_info.time_update'] = self.ranked_serp_element_serp_item_backlinks_info_time_update
        _dict['ranked_serp_element.serp_item.rank_info.page_rank'] = self.ranked_serp_element_serp_item_rank_info_page_rank
        _dict['ranked_serp_element.serp_item.rank_info.main_domain_rank'] = self.ranked_serp_element_serp_item_rank_info_main_domain_rank
        _dict['ranked_serp_element.check_url'] = self.ranked_serp_element_check_url
        _dict['ranked_serp_element.serp_item_types'] = self.ranked_serp_element_serp_item_types
        _dict['ranked_serp_element.se_results_count'] = self.ranked_serp_element_se_results_count
        _dict['ranked_serp_element.keyword_difficulty'] = self.ranked_serp_element_keyword_difficulty
        _dict['ranked_serp_element.is_lost'] = self.ranked_serp_element_is_lost
        _dict['ranked_serp_element.last_updated_time'] = self.ranked_serp_element_last_updated_time
        _dict['ranked_serp_element.previous_updated_time'] = self.ranked_serp_element_previous_updated_time
        _dict['ranked_serp_element.serp_item.extra.ad_aclk'] = self.ranked_serp_element_serp_item_extra_ad_aclk
        _dict['ranked_serp_element.serp_item.description_rows'] = self.ranked_serp_element_serp_item_description_rows
        _dict['ranked_serp_element.serp_item.phone'] = self.ranked_serp_element_serp_item_phone
        _dict['ranked_serp_element.serp_item.is_paid'] = self.ranked_serp_element_serp_item_is_paid
        _dict['ranked_serp_element.serp_item.featured_title'] = self.ranked_serp_element_serp_item_featured_title
        _dict['ranked_serp_element.serp_item.source'] = self.ranked_serp_element_serp_item_source
        _dict['ranked_serp_element.serp_item.text'] = self.ranked_serp_element_serp_item_text
        return _dict


    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "keyword_data_keyword": obj.get("keyword_data.keyword"),
            "keyword_data_keyword_info_last_updated_time": obj.get("keyword_data.keyword_info.last_updated_time"),
            "keyword_data_keyword_info_competition": obj.get("keyword_data.keyword_info.competition"),
            "keyword_data_keyword_info_competition_level": obj.get("keyword_data.keyword_info.competition_level"),
            "keyword_data_keyword_info_cpc": obj.get("keyword_data.keyword_info.cpc"),
            "keyword_data_keyword_info_search_volume": obj.get("keyword_data.keyword_info.search_volume"),
            "keyword_data_keyword_info_low_top_of_page_bid": obj.get("keyword_data.keyword_info.low_top_of_page_bid"),
            "keyword_data_keyword_info_high_top_of_page_bid": obj.get("keyword_data.keyword_info.high_top_of_page_bid"),
            "keyword_data_keyword_info_categories": obj.get("keyword_data.keyword_info.categories"),
            "keyword_data_keyword_info_search_volume_trend_monthly": obj.get("keyword_data.keyword_info.search_volume_trend.monthly"),
            "keyword_data_keyword_info_search_volume_trend_quarterly": obj.get("keyword_data.keyword_info.search_volume_trend.quarterly"),
            "keyword_data_keyword_info_search_volume_trend_yearly": obj.get("keyword_data.keyword_info.search_volume_trend.yearly"),
            "keyword_data_clickstream_keyword_info_search_volume": obj.get("keyword_data.clickstream_keyword_info.search_volume"),
            "keyword_data_clickstream_keyword_info_last_updated_time": obj.get("keyword_data.clickstream_keyword_info.last_updated_time"),
            "keyword_data_clickstream_keyword_info_gender_distribution_female": obj.get("keyword_data.clickstream_keyword_info.gender_distribution.female"),
            "keyword_data_clickstream_keyword_info_gender_distribution_male": obj.get("keyword_data.clickstream_keyword_info.gender_distribution.male"),
            "keyword_data_clickstream_keyword_info_age_distribution_18_24": obj.get("keyword_data.clickstream_keyword_info.age_distribution.18-24"),
            "keyword_data_clickstream_keyword_info_age_distribution_25_34": obj.get("keyword_data.clickstream_keyword_info.age_distribution.25-34"),
            "keyword_data_clickstream_keyword_info_age_distribution_35_44": obj.get("keyword_data.clickstream_keyword_info.age_distribution.35-44"),
            "keyword_data_clickstream_keyword_info_age_distribution_45_54": obj.get("keyword_data.clickstream_keyword_info.age_distribution.45-54"),
            "keyword_data_clickstream_keyword_info_age_distribution_55_64": obj.get("keyword_data.clickstream_keyword_info.age_distribution.55-64"),
            "keyword_data_keyword_properties_core_keyword": obj.get("keyword_data.keyword_properties.core_keyword"),
            "keyword_data_keyword_properties_synonym_clustering_algorithm": obj.get("keyword_data.keyword_properties.synonym_clustering_algorithm"),
            "keyword_data_keyword_properties_keyword_difficulty": obj.get("keyword_data.keyword_properties.keyword_difficulty"),
            "keyword_data_keyword_properties_detected_language": obj.get("keyword_data.keyword_properties.detected_language"),
            "keyword_data_keyword_properties_is_another_language": obj.get("keyword_data.keyword_properties.is_another_language"),
            "keyword_data_serp_info_check_url": obj.get("keyword_data.serp_info.check_url"),
            "keyword_data_serp_info_serp_item_types": obj.get("keyword_data.serp_info.serp_item_types"),
            "keyword_data_serp_info_se_results_count": obj.get("keyword_data.serp_info.se_results_count"),
            "keyword_data_serp_info_last_updated_time": obj.get("keyword_data.serp_info.last_updated_time"),
            "keyword_data_serp_info_previous_updated_time": obj.get("keyword_data.serp_info.previous_updated_time"),
            "keyword_data_avg_backlinks_info_backlinks": obj.get("keyword_data.avg_backlinks_info.backlinks"),
            "keyword_data_avg_backlinks_info_dofollow": obj.get("keyword_data.avg_backlinks_info.dofollow"),
            "keyword_data_avg_backlinks_info_referring_pages": obj.get("keyword_data.avg_backlinks_info.referring_pages"),
            "keyword_data_avg_backlinks_info_referring_domains": obj.get("keyword_data.avg_backlinks_info.referring_domains"),
            "keyword_data_avg_backlinks_info_referring_main_domains": obj.get("keyword_data.avg_backlinks_info.referring_main_domains"),
            "keyword_data_avg_backlinks_info_rank": obj.get("keyword_data.avg_backlinks_info.rank"),
            "keyword_data_avg_backlinks_info_main_domain_rank": obj.get("keyword_data.avg_backlinks_info.main_domain_rank"),
            "keyword_data_avg_backlinks_info_last_updated_time": obj.get("keyword_data.avg_backlinks_info.last_updated_time"),
            "keyword_data_search_intent_info_main_intent": obj.get("keyword_data.search_intent_info.main_intent"),
            "keyword_data_search_intent_info_foreign_intent": obj.get("keyword_data.search_intent_info.foreign_intent"),
            "keyword_data_search_intent_info_last_updated_time": obj.get("keyword_data.search_intent_info.last_updated_time"),
            "keyword_data_keyword_info_normalized_with_bing_search_volume": obj.get("keyword_data.keyword_info_normalized_with_bing.search_volume"),
            "keyword_data_keyword_info_normalized_with_bing_last_updated_time": obj.get("keyword_data.keyword_info_normalized_with_bing.last_updated_time"),
            "keyword_data_keyword_info_normalized_with_bing_is_normalized": obj.get("keyword_data.keyword_info_normalized_with_bing.is_normalized"),
            "keyword_data_keyword_info_normalized_with_clickstream_search_volume": obj.get("keyword_data.keyword_info_normalized_with_clickstream.search_volume"),
            "keyword_data_keyword_info_normalized_with_clickstream_last_updated_time": obj.get("keyword_data.keyword_info_normalized_with_clickstream.last_updated_time"),
            "keyword_data_keyword_info_normalized_with_clickstream_is_normalized": obj.get("keyword_data.keyword_info_normalized_with_clickstream.is_normalized"),
            "ranked_serp_element_serp_item_type": obj.get("ranked_serp_element.serp_item.type"),
            "ranked_serp_element_serp_item_rank_group": obj.get("ranked_serp_element.serp_item.rank_group"),
            "ranked_serp_element_serp_item_rank_absolute": obj.get("ranked_serp_element.serp_item.rank_absolute"),
            "ranked_serp_element_serp_item_position": obj.get("ranked_serp_element.serp_item.position"),
            "ranked_serp_element_serp_item_xpath": obj.get("ranked_serp_element.serp_item.xpath"),
            "ranked_serp_element_serp_item_domain": obj.get("ranked_serp_element.serp_item.domain"),
            "ranked_serp_element_serp_item_title": obj.get("ranked_serp_element.serp_item.title"),
            "ranked_serp_element_serp_item_url": obj.get("ranked_serp_element.serp_item.url"),
            "ranked_serp_element_serp_item_breadcrumb": obj.get("ranked_serp_element.serp_item.breadcrumb"),
            "ranked_serp_element_serp_item_website_name": obj.get("ranked_serp_element.serp_item.website_name"),
            "ranked_serp_element_serp_item_is_image": obj.get("ranked_serp_element.serp_item.is_image"),
            "ranked_serp_element_serp_item_is_video": obj.get("ranked_serp_element.serp_item.is_video"),
            "ranked_serp_element_serp_item_is_featured_snippet": obj.get("ranked_serp_element.serp_item.is_featured_snippet"),
            "ranked_serp_element_serp_item_is_malicious": obj.get("ranked_serp_element.serp_item.is_malicious"),
            "ranked_serp_element_serp_item_description": obj.get("ranked_serp_element.serp_item.description"),
            "ranked_serp_element_serp_item_pre_snippet": obj.get("ranked_serp_element.serp_item.pre_snippet"),
            "ranked_serp_element_serp_item_extended_snippet": obj.get("ranked_serp_element.serp_item.extended_snippet"),
            "ranked_serp_element_serp_item_amp_version": obj.get("ranked_serp_element.serp_item.amp_version"),
            "ranked_serp_element_serp_item_rating_rating_type": obj.get("ranked_serp_element.serp_item.rating.rating_type"),
            "ranked_serp_element_serp_item_rating_value": obj.get("ranked_serp_element.serp_item.rating.value"),
            "ranked_serp_element_serp_item_rating_votes_count": obj.get("ranked_serp_element.serp_item.rating.votes_count"),
            "ranked_serp_element_serp_item_rating_rating_max": obj.get("ranked_serp_element.serp_item.rating.rating_max"),
            "ranked_serp_element_serp_item_about_this_result": obj.get("ranked_serp_element.serp_item.about_this_result"),
            "ranked_serp_element_serp_item_main_domain": obj.get("ranked_serp_element.serp_item.main_domain"),
            "ranked_serp_element_serp_item_relative_url": obj.get("ranked_serp_element.serp_item.relative_url"),
            "ranked_serp_element_serp_item_etv": obj.get("ranked_serp_element.serp_item.etv"),
            "ranked_serp_element_serp_item_estimated_paid_traffic_cost": obj.get("ranked_serp_element.serp_item.estimated_paid_traffic_cost"),
            "ranked_serp_element_serp_item_clickstream_etv": obj.get("ranked_serp_element.serp_item.clickstream_etv"),
            "ranked_serp_element_serp_item_rank_changes_previous_rank_absolute": obj.get("ranked_serp_element.serp_item.rank_changes.previous_rank_absolute"),
            "ranked_serp_element_serp_item_rank_changes_is_new": obj.get("ranked_serp_element.serp_item.rank_changes.is_new"),
            "ranked_serp_element_serp_item_rank_changes_is_up": obj.get("ranked_serp_element.serp_item.rank_changes.is_up"),
            "ranked_serp_element_serp_item_rank_changes_is_down": obj.get("ranked_serp_element.serp_item.rank_changes.is_down"),
            "ranked_serp_element_serp_item_backlinks_info_referring_domains": obj.get("ranked_serp_element.serp_item.backlinks_info.referring_domains"),
            "ranked_serp_element_serp_item_backlinks_info_referring_main_domains": obj.get("ranked_serp_element.serp_item.backlinks_info.referring_main_domains"),
            "ranked_serp_element_serp_item_backlinks_info_referring_pages": obj.get("ranked_serp_element.serp_item.backlinks_info.referring_pages"),
            "ranked_serp_element_serp_item_backlinks_info_dofollow": obj.get("ranked_serp_element.serp_item.backlinks_info.dofollow"),
            "ranked_serp_element_serp_item_backlinks_info_backlinks": obj.get("ranked_serp_element.serp_item.backlinks_info.backlinks"),
            "ranked_serp_element_serp_item_backlinks_info_time_update": obj.get("ranked_serp_element.serp_item.backlinks_info.time_update"),
            "ranked_serp_element_serp_item_rank_info_page_rank": obj.get("ranked_serp_element.serp_item.rank_info.page_rank"),
            "ranked_serp_element_serp_item_rank_info_main_domain_rank": obj.get("ranked_serp_element.serp_item.rank_info.main_domain_rank"),
            "ranked_serp_element_check_url": obj.get("ranked_serp_element.check_url"),
            "ranked_serp_element_serp_item_types": obj.get("ranked_serp_element.serp_item_types"),
            "ranked_serp_element_se_results_count": obj.get("ranked_serp_element.se_results_count"),
            "ranked_serp_element_keyword_difficulty": obj.get("ranked_serp_element.keyword_difficulty"),
            "ranked_serp_element_is_lost": obj.get("ranked_serp_element.is_lost"),
            "ranked_serp_element_last_updated_time": obj.get("ranked_serp_element.last_updated_time"),
            "ranked_serp_element_previous_updated_time": obj.get("ranked_serp_element.previous_updated_time"),
            "ranked_serp_element_serp_item_extra_ad_aclk": obj.get("ranked_serp_element.serp_item.extra.ad_aclk"),
            "ranked_serp_element_serp_item_description_rows": obj.get("ranked_serp_element.serp_item.description_rows"),
            "ranked_serp_element_serp_item_phone": obj.get("ranked_serp_element.serp_item.phone"),
            "ranked_serp_element_serp_item_is_paid": obj.get("ranked_serp_element.serp_item.is_paid"),
            "ranked_serp_element_serp_item_featured_title": obj.get("ranked_serp_element.serp_item.featured_title"),
            "ranked_serp_element_serp_item_source": obj.get("ranked_serp_element.serp_item.source"),
            "ranked_serp_element_serp_item_text": obj.get("ranked_serp_element.serp_item.text"),
        })

        additional_properties = {k: v for k, v in obj.items() if k not in cls.__properties}
        _obj.additional_properties = additional_properties
        return _obj