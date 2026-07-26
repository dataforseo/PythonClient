# AiOptimizationLlmMentionsMultiTargetMetricsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | <em>total number of results</em> |[optional]|
**offset** | **StrictInt** | <em>offset in the results array of the returned mentions data</em><br><code>offset</code> specified in the request |[optional]|
**items_count** | **StrictInt** | <em>number of items in the results array</em> |[optional]|
**aggregated_metrics** | **LlmMentionsAggregatedMetricsInfo** | <em>aggregated mentions metrics summary</em><br>contains overall aggregated LLM mention metrics across all LLM mentions that match at least one target specified in the request |[optional]|
**items** | **List[Optional[AiOptimizationLlmMentionsMultiTargetMetricsLiveItem]]** | <em>contains relevant mentions data</em> |[optional]|