# AiOptimizationLlmMentionsTopMentionedPagesLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | <em>total amount of results relevant the request</em> |[optional]|
**offset** | **StrictInt** | <em>the number of mentions objects that are omitted in the <code>items</code> array</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <code>items</code> array</em> |[optional]|
**aggregated_metrics** | **LlmMentionsAggregatedMetricsInfo** | <em>aggregated mentions metrics</em><br>contains aggregated LLM mention metrics across all found pages, grouped by various dimensions |[optional]|
**items** | **List[Optional[AiOptimizationLlmMentionsTopMentionedPagesLiveItem]]** | <em>individual page results</em><br>array containing detailed mention metrics for each of the found top mentioned pages |[optional]|