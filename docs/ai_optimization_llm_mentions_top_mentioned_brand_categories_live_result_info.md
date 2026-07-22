# AiOptimizationLlmMentionsTopMentionedBrandCategoriesLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | total amount of results relevant the request |[optional]|
**offset** | **StrictInt** | the number of mentions objects that are omitted in the items array |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**aggregated_metrics** | **LlmMentionsAggregatedMetricsInfo** | aggregated mentions metrics<br>contains aggregated LLM mention metrics across all found brand categories, grouped by various dimensions |[optional]|
**items** | **List[Optional[AiOptimizationLlmMentionsTopMentionedBrandCategoriesLiveItem]]** | individual brand categories results<br>array containing detailed mention metrics for each of the found brand categories |[optional]|