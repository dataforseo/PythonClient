# LlmMentionsAggregatedMetricsInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**location** | **List[Optional[AggregatedMetricsItemInfo]]** | location-based grouping<br>array of objects containing mention metrics segmented by geographical location |[optional]|
**language** | **List[Optional[AggregatedMetricsItemInfo]]** | language-based grouping<br>array of objects containing mention metrics segmented by content language |[optional]|
**platform** | **List[Optional[AggregatedMetricsItemInfo]]** | platform-based grouping<br>array of group elements containing mention metrics segmented by AI platform |[optional]|
**sources_domain** | **List[Optional[AggregatedMetricsItemInfo]]** | found top source domains relevant to the target<br>array of objects containing data on top domains that are cited as sources in LLM responses<br>learn more about the sources and how to retrieve LLM citation data at our Help Center |[optional]|
**search_results_domain** | **List[Optional[AggregatedMetricsItemInfo]]** | found top search results domains relevant to the target<br>array of objects containing data on top domains that appear in search results related to LLM queries |[optional]|
**brand_entities_title** | **List[Optional[AggregatedMetricsItemInfo]]** | data on brand entities relevant to the target<br>array of objects containing data on brand entity titles that appear in search results related to LLM queries |[optional]|
**brand_entities_category** | **List[Optional[AggregatedMetricsItemInfo]]** | data on brand entities relevant to the target<br>array of objects containing data on brand entity categories that appear in search results related to LLM queries |[optional]|
**total** | **AggregatedMetricsInfoTotalInfo** | aggregated mentions metrics summary<br>contains overall aggregated LLM mention metrics across all found domains |[optional]|