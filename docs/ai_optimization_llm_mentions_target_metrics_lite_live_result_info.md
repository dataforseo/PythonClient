# AiOptimizationLlmMentionsTargetMetricsLiteLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | <em>total amount of results relevant the request</em> |[optional]|
**offset** | **StrictInt** | <em>the number of mentions objects that are omitted in the <code>items</code> array</em> |[optional]|
**items_count** | **StrictInt** | <em>the number of results returned in the <code>items</code> array</em> |[optional]|
**aggregated_metrics** | **Any** | <em>aggregated mentions metrics</em><br>in this case, always returns <code>null</code> |[optional]|
**items** | **List[Optional[AiOptimizationLlmMentionsTargetMetricsLiteLiveItem]]** | <em>array of aggregated mentions metrics</em><br>contains objects with aggregated mention metrics for the specified target |[optional]|