# AiOptimizationLlmMentionsTargetMetricsLiteLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | total amount of results relevant the request |[optional]|
**offset** | **StrictInt** | the number of mentions objects that are omitted in the items array |[optional]|
**items_count** | **StrictInt** | the number of results returned in the items array |[optional]|
**aggregated_metrics** | **Any** | aggregated mentions metrics<br>in this case, always returns null |[optional]|
**items** | **List[Optional[AiOptimizationLlmMentionsTargetMetricsLiteLiveItem]]** | array of aggregated mentions metrics<br>contains objects with aggregated mention metrics for the specified target |[optional]|