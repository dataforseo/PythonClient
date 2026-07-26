# AiOptimizationLlmMentionsTopMentionedDomainsLiteLiveResultInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
**total_count** | **StrictInt** | <em>total number of results</em> |[optional]|
**offset** | **StrictInt** | <em>offset in the results array of the returned mentions data</em><br><code>offset</code> specified in the reqest |[optional]|
**items_count** | **StrictInt** | <em>number of items in the results array</em> |[optional]|
**aggregated_metrics** | **Any** | <em>aggregated mentions metrics summary</em><br>contains overall aggregated LLM mention metrics across all found domains, grouped by various dimensions</br>in this case, the value will be <code>null</code> |[optional]|
**items** | **List[Optional[AiOptimizationLlmMentionsTopMentionedDomainsLiteLiveItem]]** | <em>contains relevant mentions data</em> |[optional]|