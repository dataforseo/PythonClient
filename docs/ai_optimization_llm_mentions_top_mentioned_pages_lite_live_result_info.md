# AiOptimizationLlmMentionsTopMentionedPagesLiteLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | total number of results |[optional]|
**offset** | **StrictInt** | offset in the results array of the returned mentions data<br>offset specified in the request |[optional]|
**items_count** | **StrictInt** | number of items in the results array |[optional]|
**aggregated_metrics** | **Any** | aggregated mentions metrics summary<br>contains overall aggregated LLM mention metrics across all found domains, grouped by various dimensionsin this case, the value will be null |[optional]|
**items** | **List[Optional[AiOptimizationLlmMentionsTopMentionedPagesLiteLiveItem]]** | contains relevant mentions data |[optional]|