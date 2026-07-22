# AiOptimizationLlmMentionsTargetMetricsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | total amount of results relevant to the request<br>in this case, always equals 0 |[optional]|
**offset** | **StrictInt** | the number of mentions objects that are omitted in the items array<br>in this case, always equals 0 |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array<br>in this case, always equals 0 |[optional]|
**aggregated_metrics** | **LlmMentionsAggregatedMetricsInfo** | aggregated mentions metrics<br>contains aggregated LLM mention metrics across all found domains, grouped by various dimensions |[optional]|
**items** | **List[Optional[Any]]** | individual target results<br>in this case, equals null |[optional]|