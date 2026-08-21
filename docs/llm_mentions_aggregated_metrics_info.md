# LlmMentionsAggregatedMetricsInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**location** | **List[Optional[AggregatedMetricsItemInfo]]** | <em>location-based grouping</em><br>array of objects containing mention metrics segmented by geographical location |[optional]|
**language** | **List[Optional[AggregatedMetricsItemInfo]]** | <em>language-based grouping</em><br>array of objects containing mention metrics segmented by content language |[optional]|
**platform** | **List[Optional[AggregatedMetricsItemInfo]]** | <em>platform-based grouping</em><br>array of group elements containing mention metrics segmented by AI platform |[optional]|
**sources_domain** | **List[Optional[AggregatedMetricsItemInfo]]** | <em>found top source domains relevant to the target</em><br>array of objects containing data on top domains that are cited as sources in LLM responses<br>learn more about the sources and how to retrieve LLM citation data at our <a href='https://dataforseo.com/help-center/how-to-get-llm-citation-data-with-llm-mentions-api' target='_blank'>Help Center</a> |[optional]|
**search_results_domain** | **List[Optional[AggregatedMetricsItemInfo]]** | <em>found top search results domains relevant to the target</em><br>array of objects containing data on top domains that appear in search results related to LLM queries;<br><strong>Note:</strong> available only for <code>chat_gpt</code> |[optional]|
**brand_entities_title** | **List[Optional[AggregatedMetricsItemInfo]]** | <em>data on brand entities relevant to the target</em><br>array of objects containing data on brand entity titles that appear in search results related to LLM queries;<br><strong>Note:</strong> available only for <code>chat_gpt</code> |[optional]|
**brand_entities_category** | **List[Optional[AggregatedMetricsItemInfo]]** | <em>data on brand entities relevant to the target</em><br>array of objects containing data on brand entity categories that appear in search results related to LLM queries<br><strong>Note:</strong> available only for <code>chat_gpt</code> |[optional]|
**total** | **AggregatedMetricsInfoTotalInfo** | <em>aggregated mentions metrics summary</em><br>contains overall aggregated LLM mention metrics across all found domains |[optional]|