# AiOptimizationLlmMentionsMultiTargetMetricsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | total number of results |[optional]|
**offset** | **StrictInt** | offset in the results array of the returned mentions data<br>offset specified in the request |[optional]|
**items_count** | **StrictInt** | number of items in the results array |[optional]|
**aggregated_metrics** | **LlmMentionsAggregatedMetricsInfo** | aggregated mentions metrics summary<br>contains overall aggregated LLM mention metrics across all LLM mentions that match at least one target specified in the request |[optional]|
**items** | **List[Optional[AiOptimizationLlmMentionsMultiTargetMetricsLiveItem]]** | contains relevant mentions data |[optional]|