# AiOptimizationLlmMentionsTargetMetricsLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | <em>total amount of results relevant to the request</em><br>in this case, always equals <code>0</code> |[optional]|
**offset** | **StrictInt** | <em>the number of mentions objects that are omitted in the <code>items</code> array</em><br>in this case, always equals <code>0</code> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <code>items</code> array</em><br>in this case, always equals <code>0</code> |[optional]|
**aggregated_metrics** | **LlmMentionsAggregatedMetricsInfo** | <em>aggregated mentions metrics</em><br>contains aggregated LLM mention metrics across all found domains, grouped by various dimensions |[optional]|
**items** | **List[Optional[Any]]** | <em>individual target results</em><br>in this case, equals <code>null</code> |[optional]|